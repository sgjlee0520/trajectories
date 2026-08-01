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
            self.assertEqual(out[0]["clock_education"], "11")
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


if __name__ == "__main__":
    unittest.main()
