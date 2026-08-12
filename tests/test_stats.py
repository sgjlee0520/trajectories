import os
import subprocess
import sys
import tempfile
import unittest

from src import stats


class TestBootstrap(unittest.TestCase):
    def test_ci_brackets_the_median(self):
        values = [8, 9, 10, 11, 12, 13, 10, 11, 9, 10]
        lo, med, hi = stats.bootstrap_median_ci(values, iters=2000, seed=1)
        self.assertLessEqual(lo, med)
        self.assertLessEqual(med, hi)

    def test_deterministic_given_seed(self):
        values = [3, 7, 11, 4, 9, 12, 6]
        first = stats.bootstrap_median_ci(values, iters=1000, seed=42)
        second = stats.bootstrap_median_ci(values, iters=1000, seed=42)
        self.assertEqual(first, second)

    def test_ci_narrows_as_n_grows(self):
        small_lo, _, small_hi = stats.bootstrap_median_ci(
            [5, 10, 15] * 4, iters=2000, seed=3)
        large_lo, _, large_hi = stats.bootstrap_median_ci(
            [5, 10, 15] * 60, iters=2000, seed=3)
        self.assertLess(stats.half_width(large_lo, large_hi),
                        stats.half_width(small_lo, small_hi))

    def test_too_few_values_raises(self):
        with self.assertRaises(ValueError):
            stats.bootstrap_median_ci([7], iters=100, seed=0)


class TestStoppingRule(unittest.TestCase):
    def test_below_n_floor_never_stops(self):
        result = stats.check_stopping_rule([10.0, 10.1, 10.2], n=29,
                                           ci_half_width=0.2)
        self.assertFalse(result["stop"])
        self.assertIn("N floor", result["reason"])

    def test_needs_three_wave_medians(self):
        result = stats.check_stopping_rule([10.0, 10.1], n=100,
                                           ci_half_width=0.2)
        self.assertFalse(result["stop"])
        self.assertIn("three wave medians", result["reason"])

    def test_wide_ci_blocks_stop(self):
        result = stats.check_stopping_rule([10.0, 10.1, 10.2], n=100,
                                           ci_half_width=2.5)
        self.assertFalse(result["stop"])
        self.assertIn("CI half-width", result["reason"])

    def test_drifting_median_blocks_stop(self):
        result = stats.check_stopping_rule([10.0, 12.0, 13.5], n=100,
                                           ci_half_width=0.5)
        self.assertFalse(result["stop"])
        self.assertIn("drift", result["reason"])

    def test_one_settled_delta_is_not_enough(self):
        # Second-to-last delta is 2.0, only the last one settled.
        result = stats.check_stopping_rule([10.0, 12.0, 12.1], n=100,
                                           ci_half_width=0.5)
        self.assertFalse(result["stop"])

    def test_stops_when_all_conditions_met(self):
        result = stats.check_stopping_rule([11.8, 12.0, 12.2], n=210,
                                           ci_half_width=0.9)
        self.assertTrue(result["stop"])

    def test_drift_exactly_at_threshold_blocks(self):
        # Spec: drift must be strictly under 0.5 yr, so 0.5 does not qualify.
        result = stats.check_stopping_rule([10.0, 10.5, 11.0], n=100,
                                           ci_half_width=0.5)
        self.assertFalse(result["stop"])
        self.assertIn("drift", result["reason"])

    def test_half_width_exactly_at_threshold_passes(self):
        # Spec: CI half-width of exactly 1.0 yr satisfies the rule.
        result = stats.check_stopping_rule([11.8, 12.0, 12.2], n=210,
                                           ci_half_width=1.0)
        self.assertTrue(result["stop"])


class TestRevenueStrictValues(unittest.TestCase):
    def rows(self):
        def row(basis, clock, excluded="false"):
            return {"hit_basis": basis, "clock_education": clock,
                    "excluded": excluded}
        return [
            row("primary", 11),
            row("primary", 9),
            row("fallback", 40),
            row("equivalent", 50),
            row("primary", None),
        ]

    def test_drops_excluded_rows_even_when_dated(self):
        """An excluded row with its dates intact must not reach the median.

        Excluded rows used to fall out only because an undatable hit left the
        clock None. A row excluded for any other reason would have counted.
        """
        rows = self.rows() + [{"hit_basis": "primary", "clock_education": 99,
                               "excluded": "true"}]
        self.assertEqual(stats.revenue_strict_values(rows), [11, 9])

    def test_keeps_only_primary_basis(self):
        self.assertEqual(stats.revenue_strict_values(self.rows()), [11, 9])

    def test_excludes_fallback_and_equivalent(self):
        values = stats.revenue_strict_values(self.rows())
        self.assertNotIn(40, values)
        self.assertNotIn(50, values)

    def test_drops_none_clock_values(self):
        self.assertNotIn(None, stats.revenue_strict_values(self.rows()))

    def test_honours_the_clock_argument(self):
        rows = [{"hit_basis": "primary", "clock_venture": 3,
                 "clock_education": 11, "excluded": "false"}]
        self.assertEqual(
            stats.revenue_strict_values(rows, clock="clock_venture"), [3])

    def test_empty_when_no_primary_rows(self):
        rows = [{"hit_basis": "fallback", "clock_education": 7,
                 "excluded": "false"}]
        self.assertEqual(stats.revenue_strict_values(rows), [])


class TestAudit(unittest.TestCase):
    def test_samples_fifteen_percent(self):
        ids = ["p%03d" % i for i in range(100)]
        sample = stats.audit_sample(ids, fraction=0.15, seed=0)
        self.assertEqual(len(sample), 15)

    def test_always_samples_at_least_one(self):
        sample = stats.audit_sample(["p001", "p002"], fraction=0.15, seed=0)
        self.assertEqual(len(sample), 1)

    def test_deterministic_given_seed(self):
        ids = ["p%03d" % i for i in range(50)]
        self.assertEqual(stats.audit_sample(ids, seed=7),
                         stats.audit_sample(ids, seed=7))

    def test_different_waves_audit_different_positions(self):
        """The audit must not hit the same slots in the roster forever.

        With a constant seed, sample() returns the same indices for every
        population of the same size, and the runbook has researchers append
        names in bucket-allocation order -- so the same three buckets got
        audited every wave and the rest never once.
        """
        waves = [["p%03d" % i for i in range(start, start + 25)]
                 for start in (0, 25, 50)]
        chosen = {self.positions(wave) for wave in waves}
        self.assertEqual(len(chosen), 3)

    def positions(self, ids):
        ordered = sorted(ids)
        return tuple(ordered.index(i) for i in stats.audit_sample(ids))

    def test_same_ids_select_the_same_rows(self):
        ids = ["p%03d" % i for i in range(25)]
        self.assertEqual(stats.audit_sample(ids), stats.audit_sample(ids))

    def test_selection_survives_a_fresh_interpreter(self):
        """Reproducibility is the whole reason the seed exists.

        The builtin hash() is salted per process, so a seed derived from it
        would pick different rows on every run.
        """
        code = ("from src import stats;"
                "print(stats.audit_sample(['p%03d' % i for i in range(25)]))")
        root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        runs = []
        for hash_seed in ("0", "12345"):
            env = dict(os.environ, PYTHONHASHSEED=hash_seed)
            runs.append(subprocess.check_output(
                [sys.executable, "-c", code], cwd=root, env=env))
        self.assertEqual(runs[0], runs[1])

    def test_agreement_within_one_year_is_not_disagreement(self):
        pairs = [(1997, 1997), (2001, 2002), (1985, 1984)]
        self.assertEqual(stats.audit_disagreement(pairs), 0.0)

    def test_two_year_gap_counts_as_disagreement(self):
        pairs = [(1997, 1999), (2001, 2001), (1985, 1985), (1990, 1990)]
        self.assertAlmostEqual(stats.audit_disagreement(pairs), 0.25)

    def test_one_pass_unknown_counts_as_disagreement(self):
        pairs = [(1997, None), (2001, 2001)]
        self.assertAlmostEqual(stats.audit_disagreement(pairs), 0.5)

    def test_both_unknown_agree(self):
        pairs = [(None, None), (2001, 2001)]
        self.assertEqual(stats.audit_disagreement(pairs), 0.0)

    def test_empty_pairs_is_zero(self):
        self.assertEqual(stats.audit_disagreement([]), 0.0)


class TestHistory(unittest.TestCase):
    def make_file(self, content=""):
        handle, path = tempfile.mkstemp(suffix=".txt")
        os.close(handle)
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        return path

    def test_read_history_skips_comments_and_blanks(self):
        path = self.make_file(
            "# header comment\n"
            "10.1\n"
            "\n"
            "   \n"
            "10.3\n"
            "# last-n: 50\n"
        )
        try:
            self.assertEqual(stats.read_history(path), [10.1, 10.3])
        finally:
            os.remove(path)

    def test_read_history_all_comments_is_empty(self):
        path = self.make_file("# just a header\n# last-n: 25\n")
        try:
            self.assertEqual(stats.read_history(path), [])
        finally:
            os.remove(path)

    def test_append_history_writes_and_returns_true_on_fresh_file(self):
        path = self.make_file("")
        try:
            result = stats.append_history(path, 10.3, 25)
            self.assertTrue(result)
            self.assertEqual(stats.read_history(path), [10.3])
        finally:
            os.remove(path)

    def test_append_history_same_n_twice_is_a_noop(self):
        path = self.make_file("")
        try:
            stats.append_history(path, 10.3, 25)
            with open(path, encoding="utf-8") as f:
                before = f.read()
            result = stats.append_history(path, 99.9, 25)
            with open(path, encoding="utf-8") as f:
                after = f.read()
            self.assertFalse(result)
            self.assertEqual(before, after)
        finally:
            os.remove(path)

    def test_append_history_different_n_appends(self):
        path = self.make_file("")
        try:
            stats.append_history(path, 10.3, 25)
            result = stats.append_history(path, 10.5, 50)
            self.assertTrue(result)
            self.assertEqual(stats.read_history(path), [10.3, 10.5])
        finally:
            os.remove(path)

    def test_round_trip_two_waves_no_marker_pollution(self):
        path = self.make_file("")
        try:
            stats.append_history(path, 10.3, 25)
            stats.append_history(path, 10.5, 50)
            self.assertEqual(stats.read_history(path), [10.3, 10.5])
        finally:
            os.remove(path)


class TestReadAuditPairs(unittest.TestCase):
    def test_converts_blank_and_unknown_to_none(self):
        handle, path = tempfile.mkstemp(suffix=".csv")
        os.close(handle)
        try:
            with open(path, "w", encoding="utf-8") as f:
                f.write("person_id,first_pass,second_pass\n")
                f.write("p001,1997,1998\n")
                f.write("p002,2001,unknown\n")
                f.write("p003,,2005\n")
            self.assertEqual(
                stats.read_audit_pairs(path),
                [(1997, 1998), (2001, None), (None, 2005)])
        finally:
            os.remove(path)


if __name__ == "__main__":
    unittest.main()
