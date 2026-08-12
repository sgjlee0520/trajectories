import unittest

from src import report


def clock_row(person_id, bucket, basis, education, country="US",
              era="post1995", gender="f", bounded="false", conf_min="high"):
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
        "clock_education_min": education,
        "clock_education_max": education,
        "bounded": bounded,
        "conf_min": conf_min,
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

    def test_flag_is_attached_to_the_undersized_row_only(self):
        rows = [clock_row("big%02d" % i, "software_internet", "primary",
                          8 + (i % 7)) for i in range(35)]
        rows += [clock_row("s%02d" % i, "science_research", "equivalent",
                           18 + (i % 4)) for i in range(5)]
        text = report.build_report(rows)
        small = [l for l in text.splitlines()
                 if l.startswith("| science_research")]
        large = [l for l in text.splitlines()
                 if l.startswith("| software_internet")]
        self.assertEqual(len(small), 1)
        self.assertEqual(len(large), 1)
        self.assertIn("too small to read", small[0])
        self.assertNotIn("too small to read", large[0])

    def test_single_row_slice_is_flagged(self):
        # n=1 has no median at all, which makes it the most misreadable
        # slice, not an exempt one.
        rows = [clock_row("a", "software_internet", "primary", 5),
                clock_row("b", "science_research", "equivalent", 20)]
        text = report.build_report(rows)
        line = [l for l in text.splitlines()
                if l.startswith("| science_research")][0]
        self.assertIn("n=1", line)
        self.assertIn("too small to read", line)

    def test_reports_stopping_rule_numbers(self):
        text = report.build_report(sample_rows())
        self.assertIn("Stopping rule", text)
        # 12 of the 23 sample rows are hit_basis == "primary".
        self.assertIn("Revenue-strict n = 12", text)
        self.assertIn("threshold 1.00", text)


class TestConfidenceRuns(unittest.TestCase):
    def rows(self):
        return ([clock_row("h%02d" % i, "software_internet", "primary", 8)
                 for i in range(5)]
                + [clock_row("m%02d" % i, "software_internet", "primary", 20,
                             conf_min="medium") for i in range(5)])

    def test_high_only_excludes_weaker_rows(self):
        runs = report.confidence_runs(self.rows())
        self.assertEqual(runs["high_only"]["n"], 5)
        self.assertEqual(runs["high_only"]["median"], 8)

    def test_all_rows_includes_everything(self):
        runs = report.confidence_runs(self.rows())
        self.assertEqual(runs["all_rows"]["n"], 10)

    def test_divergence_is_visible(self):
        runs = report.confidence_runs(self.rows())
        self.assertNotEqual(runs["high_only"]["median"],
                            runs["all_rows"]["median"])


class TestBoundedRuns(unittest.TestCase):
    def rows(self):
        rows = [clock_row("u%02d" % i, "software_internet", "primary", 10)
                for i in range(4)]
        for i in range(2):
            row = clock_row("b%02d" % i, "software_internet", "primary", 6.5,
                            bounded="true")
            row["clock_education_min"] = 6
            row["clock_education_max"] = 7
            rows.append(row)
        return rows

    def test_unbounded_only_drops_bounded_rows(self):
        runs = report.bounded_runs(self.rows())
        self.assertEqual(runs["unbounded_only"]["n"], 4)

    def test_midpoint_all_keeps_everything(self):
        runs = report.bounded_runs(self.rows())
        self.assertEqual(runs["midpoint_all"]["n"], 6)

    def test_envelope_brackets_the_midpoint(self):
        runs = report.bounded_runs(self.rows())
        self.assertLessEqual(runs["envelope_min"]["median"],
                             runs["midpoint_all"]["median"])
        self.assertGreaterEqual(runs["envelope_max"]["median"],
                                runs["midpoint_all"]["median"])


class TestNewReportSections(unittest.TestCase):
    def test_report_contains_confidence_section(self):
        text = report.build_report(sample_rows())
        self.assertIn("Confidence sensitivity", text)
        self.assertIn("high-confidence rows only", text)

    def test_report_contains_bounded_section(self):
        text = report.build_report(sample_rows())
        self.assertIn("Bounded-date sensitivity", text)


if __name__ == "__main__":
    unittest.main()
