import csv
import os
import tempfile
import unittest

from src import clocks
from tests.test_schema import valid_row


class TestEra(unittest.TestCase):
    def test_1994_is_pre1995(self):
        self.assertEqual(clocks.era_of(1994), "pre1995")

    def test_1995_is_post1995(self):
        self.assertEqual(clocks.era_of(1995), "post1995")

    def test_unknown_hit_year_gives_empty_era(self):
        self.assertEqual(clocks.era_of(None), "")


class TestComputeClocks(unittest.TestCase):
    def test_bezos_shaped_row(self):
        # born 1964, education ends 1986, own venture 1994, hit 1997
        result = clocks.compute_clocks(valid_row())
        self.assertEqual(result["clock_education"], 11)
        self.assertEqual(result["clock_age18"], 15)
        self.assertEqual(result["clock_venture"], 3)
        self.assertEqual(result["age_at_first_hit"], 33)

    def test_carries_slice_keys(self):
        result = clocks.compute_clocks(valid_row())
        self.assertEqual(result["bucket"], "software_internet")
        self.assertEqual(result["hit_basis"], "primary")
        self.assertEqual(result["country_primary"], "US")
        self.assertEqual(result["era"], "post1995")

    def test_unknown_education_gives_none_for_that_clock_only(self):
        row = valid_row(
            a2_education_end_conf="none",
            a2_education_end_date="unknown",
            a2_education_end_src="",
        )
        result = clocks.compute_clocks(row)
        self.assertIsNone(result["clock_education"])
        self.assertEqual(result["clock_venture"], 3)

    def test_unknown_birth_nulls_only_the_birth_derived_clocks(self):
        # birth + 18 is arithmetic on a possibly-None value. If the guard is
        # ever refactored away, this is the test that catches it.
        row = valid_row(
            a1_birth_conf="none",
            a1_birth_date="unknown",
            a1_birth_src="",
        )
        result = clocks.compute_clocks(row)
        self.assertIsNone(result["clock_age18"])
        self.assertIsNone(result["age_at_first_hit"])
        self.assertEqual(result["clock_education"], 11)
        self.assertEqual(result["clock_venture"], 3)

    def test_excluded_row_yields_all_none_clocks(self):
        row = valid_row(
            a5_first_hit_conf="none",
            a5_first_hit_date="unknown",
            a5_first_hit_src="",
            excluded="true",
            exclusion_reason="no disclosed revenue",
            hit_criterion="",
            hit_basis="",
        )
        result = clocks.compute_clocks(row)
        self.assertIsNone(result["clock_education"])
        self.assertIsNone(result["clock_age18"])
        self.assertIsNone(result["clock_venture"])
        self.assertIsNone(result["age_at_first_hit"])


class TestWriteClocks(unittest.TestCase):
    def test_roundtrip(self):
        rows = [clocks.compute_clocks(valid_row())]
        handle, path = tempfile.mkstemp(suffix=".csv")
        os.close(handle)
        try:
            clocks.write_clocks(rows, path)
            with open(path, newline="", encoding="utf-8") as f:
                out = list(csv.DictReader(f))
            self.assertEqual(len(out), 1)
            self.assertEqual(out[0]["clock_education"], "11.0")
        finally:
            os.remove(path)

    def test_none_written_as_empty_string(self):
        row = valid_row(
            a4_first_venture_conf="none",
            a4_first_venture_date="unknown",
            a4_first_venture_src="",
        )
        handle, path = tempfile.mkstemp(suffix=".csv")
        os.close(handle)
        try:
            clocks.write_clocks([clocks.compute_clocks(row)], path)
            with open(path, newline="", encoding="utf-8") as f:
                out = list(csv.DictReader(f))
            self.assertEqual(out[0]["clock_venture"], "")
        finally:
            os.remove(path)

    def test_load_clocks_roundtrips_none(self):
        row = valid_row(
            a4_first_venture_conf="none",
            a4_first_venture_date="unknown",
            a4_first_venture_src="",
        )
        handle, path = tempfile.mkstemp(suffix=".csv")
        os.close(handle)
        try:
            clocks.write_clocks([clocks.compute_clocks(row)], path)
            loaded = clocks.load_clocks(path)
            self.assertEqual(len(loaded), 1)
            self.assertIsNone(loaded[0]["clock_venture"])
            self.assertEqual(loaded[0]["clock_education"], 11)
        finally:
            os.remove(path)

    def test_load_clocks_treats_whitespace_cell_as_unknown(self):
        handle, path = tempfile.mkstemp(suffix=".csv")
        os.close(handle)
        try:
            with open(path, "w", newline="", encoding="utf-8") as f:
                f.write(",".join(clocks.CLOCK_COLUMNS) + "\n")
                f.write("p001,software_internet,primary,US,f,post1995,"
                        "11,15,   ,33,,,,\n")
            loaded = clocks.load_clocks(path)
            self.assertIsNone(loaded[0]["clock_venture"])
            self.assertEqual(loaded[0]["clock_age18"], 15)
        finally:
            os.remove(path)


class TestMidpoint(unittest.TestCase):
    def test_degenerate_span(self):
        self.assertEqual(clocks.midpoint((1994, 1994)), 1994.0)

    def test_two_year_span(self):
        self.assertEqual(clocks.midpoint((1960, 1961)), 1960.5)

    def test_empty_span(self):
        self.assertIsNone(clocks.midpoint((None, None)))


class TestWeakestConf(unittest.TestCase):
    def test_picks_the_weakest(self):
        self.assertEqual(clocks.weakest_conf("high", "medium"), "medium")
        self.assertEqual(clocks.weakest_conf("low", "high"), "low")
        self.assertEqual(clocks.weakest_conf("high", "high"), "high")

    def test_none_is_weakest_of_all(self):
        self.assertEqual(clocks.weakest_conf("high", "none"), "none")


class TestBoundedClocks(unittest.TestCase):
    def moore_row(self):
        # Education 1954, venture 1957, hit bracketed to 1960-1961.
        return valid_row(
            a1_birth_date="1929",
            a2_education_end_date="1954",
            a3_first_domain_job_date="1954",
            a4_first_venture_date="1957",
            a5_first_hit_date="1960-1961",
            a6_scale_hit_date="1968",
        )

    def test_midpoint_clock(self):
        result = clocks.compute_clocks(self.moore_row())
        self.assertEqual(result["clock_education"], 6.5)

    def test_envelope(self):
        result = clocks.compute_clocks(self.moore_row())
        self.assertEqual(result["clock_education_min"], 6)
        self.assertEqual(result["clock_education_max"], 7)

    def test_bounded_flag_set(self):
        self.assertEqual(clocks.compute_clocks(self.moore_row())["bounded"],
                         "true")

    def test_unbounded_row_has_equal_envelope_and_false_flag(self):
        result = clocks.compute_clocks(valid_row())
        self.assertEqual(result["clock_education"], 11)
        self.assertEqual(result["clock_education_min"], 11)
        self.assertEqual(result["clock_education_max"], 11)
        self.assertEqual(result["bounded"], "false")

    def test_conf_min_takes_the_weaker_of_the_two_feeding_anchors(self):
        row = valid_row(a2_education_end_conf="medium")
        self.assertEqual(clocks.compute_clocks(row)["conf_min"], "medium")

    def test_conf_min_high_when_both_high(self):
        self.assertEqual(clocks.compute_clocks(valid_row())["conf_min"], "high")

    def test_excluded_row_has_empty_envelope(self):
        row = valid_row(
            a5_first_hit_conf="none",
            a5_first_hit_date="unknown",
            a5_first_hit_src="",
            excluded="true",
            exclusion_reason="crossing_undatable",
            hit_criterion="",
            hit_basis="",
        )
        result = clocks.compute_clocks(row)
        self.assertIsNone(result["clock_education"])
        self.assertIsNone(result["clock_education_min"])
        self.assertIsNone(result["clock_education_max"])


if __name__ == "__main__":
    unittest.main()


class TestRank1VentureClock(unittest.TestCase):
    def test_rank1_has_no_venture_clock(self):
        """A ranking is not a venture; 0.0 would read as a short gap."""
        row = valid_row()
        row["hit_criterion"] = "rank1"
        row["a4_first_venture_date"] = row["a5_first_hit_date"]
        self.assertIsNone(clocks.compute_clocks(row)["clock_venture"])

    def test_other_criteria_keep_the_venture_clock(self):
        row = valid_row()
        self.assertIsNotNone(clocks.compute_clocks(row)["clock_venture"])


class TestHitClampedToEarlierAnchor(unittest.TestCase):
    """A bounded hit cannot start before an anchor it must follow.

    The schema's ordering rule already asserts the hit is not before the
    education end, so the part of the bracket below that anchor is not a
    possible hit year. Averaging over it understates every clock, always in
    the same direction.
    """

    def bracket_row(self, **overrides):
        # Hit bracketed 1995-2005, education ends 2003: the hit can only be
        # 2003-2005, so the midpoint is 2004 and the clock is 1.
        row = valid_row(a2_education_end_date="2003",
                        a5_first_hit_date="1995-2005")
        row.update(overrides)
        return row

    def test_midpoint_uses_only_the_possible_part_of_the_bracket(self):
        result = clocks.compute_clocks(self.bracket_row())
        self.assertEqual(result["clock_education"], 1.0)

    def test_envelope_is_clamped_too(self):
        result = clocks.compute_clocks(self.bracket_row())
        self.assertEqual(result["clock_education_min"], 0)
        self.assertEqual(result["clock_education_max"], 2)

    def test_venture_clock_clamped_by_the_venture_anchor(self):
        row = self.bracket_row(a4_first_venture_date="2003")
        self.assertEqual(clocks.compute_clocks(row)["clock_venture"], 1.0)

    def test_clamp_past_the_end_of_the_bracket_gives_none(self):
        # The certain violation schema.validate_row rejects: a negative
        # number here would be worse than no number.
        row = valid_row(a2_education_end_date="2006",
                        a5_first_hit_date="2000-2005")
        result = clocks.compute_clocks(row)
        self.assertIsNone(result["clock_education"])
        self.assertIsNone(result["clock_education_min"])
        self.assertIsNone(result["clock_education_max"])

    def test_no_clock_is_ever_negative(self):
        # clock_age18 is excluded on purpose: a hit before 18 is a real
        # outlier, not a data error, and its clock is legitimately negative.
        keys = ("clock_education", "clock_venture",
                "clock_education_min", "clock_education_max")
        cases = [
            self.bracket_row(),
            valid_row(a2_education_end_date="1996-2000",
                      a5_first_hit_date="1997"),
            valid_row(a4_first_venture_date="1994-2000",
                      a5_first_hit_date="1996-1999"),
            valid_row(a2_education_end_date="1997",
                      a4_first_venture_date="1997",
                      a5_first_hit_date="1997"),
        ]
        for row in cases:
            result = clocks.compute_clocks(row)
            for key in keys:
                value = result[key]
                if value is not None:
                    self.assertGreaterEqual(value, 0,
                                            "%s went negative: %r"
                                            % (key, result))
