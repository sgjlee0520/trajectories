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


if __name__ == "__main__":
    unittest.main()
