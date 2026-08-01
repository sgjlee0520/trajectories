import unittest

from src import report


def clock_row(person_id, bucket, basis, education, country="US",
              era="post1995", gender="f"):
    return {
        "person_id": person_id,
        "bucket": bucket,
        "hit_basis": basis,
        "country_primary": country,
        "gender": gender,
        "era": era,
        "clock_education": education,
        "clock_age18": None if education is None else education + 4,
        "clock_venture": None,
        "age_at_first_hit": None if education is None else education + 22,
    }


def sample_rows():
    rows = []
    for i in range(12):
        rows.append(clock_row("p%02d" % i, "software_internet", "primary",
                              8 + (i % 5)))
    for i in range(6):
        rows.append(clock_row("f%02d" % i, "hardware_deeptech", "fallback",
                              12 + (i % 3)))
    for i in range(5):
        rows.append(clock_row("s%02d" % i, "science_research", "equivalent",
                              18 + (i % 4), country="DE", era="pre1995"))
    return rows


class TestSummarise(unittest.TestCase):
    def test_reports_n_and_median(self):
        result = report.summarise([10, 12, 14])
        self.assertEqual(result["n"], 3)
        self.assertEqual(result["median"], 12)

    def test_single_value_has_no_ci(self):
        result = report.summarise([10])
        self.assertEqual(result["n"], 1)
        self.assertIsNone(result["median"])

    def test_empty_has_no_ci(self):
        result = report.summarise([])
        self.assertEqual(result["n"], 0)
        self.assertIsNone(result["median"])


class TestStrictnessRuns(unittest.TestCase):
    def test_three_levels_have_increasing_n(self):
        runs = report.strictness_runs(sample_rows(), "clock_education")
        self.assertEqual(runs["revenue_strict"]["n"], 12)
        self.assertEqual(runs["all_commercial"]["n"], 18)
        self.assertEqual(runs["pooled"]["n"], 23)

    def test_revenue_strict_excludes_fallback(self):
        # Two primary rows so a median exists; the fallback row's 50 would
        # drag it far off if the filter leaked.
        rows = [clock_row("a", "software_internet", "primary", 5),
                clock_row("b", "software_internet", "primary", 7),
                clock_row("c", "software_internet", "fallback", 50)]
        runs = report.strictness_runs(rows, "clock_education")
        self.assertEqual(runs["revenue_strict"]["n"], 2)
        self.assertEqual(runs["revenue_strict"]["median"], 6)
        self.assertEqual(runs["all_commercial"]["n"], 3)


class TestSliceBy(unittest.TestCase):
    def test_slices_by_bucket(self):
        result = report.slice_by(sample_rows(), "bucket", "clock_education")
        self.assertEqual(result["software_internet"]["n"], 12)
        self.assertEqual(result["science_research"]["n"], 5)

    def test_slices_by_era(self):
        result = report.slice_by(sample_rows(), "era", "clock_education")
        self.assertEqual(result["pre1995"]["n"], 5)


class TestBuildReport(unittest.TestCase):
    def test_contains_survivorship_caveat(self):
        text = report.build_report(sample_rows())
        self.assertIn("survivorship", text.lower())

    def test_contains_all_three_strictness_levels(self):
        text = report.build_report(sample_rows())
        self.assertIn("Revenue-strict", text)
        self.assertIn("All commercial", text)
        self.assertIn("Pooled", text)

    def test_small_slices_are_flagged(self):
        text = report.build_report(sample_rows())
        # science_research has n=5, far below the 30 needed to mean anything.
        self.assertIn("too small to read", text)

    def test_reports_stopping_rule_verdict(self):
        text = report.build_report(sample_rows())
        self.assertIn("Stopping rule", text)


if __name__ == "__main__":
    unittest.main()
