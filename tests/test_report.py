import unittest

from src import report


def clock_row(person_id, bucket, basis, education, country="US",
              era="post1995", gender="f", bounded="false", conf_min="high",
              excluded="false", exclusion_reason=""):
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
        "excluded": excluded,
        "exclusion_reason": exclusion_reason,
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


def conf_rows(high=8, weak=20):
    """Five high-confidence rows and five weaker ones, medians apart."""
    return ([clock_row("h%02d" % i, "software_internet", "primary", high)
             for i in range(5)]
            + [clock_row("m%02d" % i, "software_internet", "primary", weak,
                         conf_min="medium") for i in range(5)])


def bounded_rows():
    """Three unbounded rows plus two bounded ones that straddle the median.

    Medians: unbounded 9.0, midpoints 10.0, earliest 8.0, latest 12.0 — four
    distinct numbers, so a table cell wired to the wrong run shows it.
    """
    rows = [clock_row("u%02d" % i, "software_internet", "primary", clock)
            for i, clock in enumerate((8, 9, 12))]
    for i in range(2):
        row = clock_row("b%02d" % i, "software_internet", "primary", 10,
                        bounded="true")
        row["clock_education_min"] = 2
        row["clock_education_max"] = 18
        rows.append(row)
    return rows


def table_row(text, label):
    """The one rendered table line starting with `label`."""
    matches = [l for l in text.splitlines() if l.startswith("| " + label + " |")]
    assert len(matches) == 1, (label, matches)
    return matches[0]


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
        text = report.build_report(sample_rows(), n_floor=0)
        self.assertIn("survivorship", text.lower())

    def test_contains_all_three_strictness_levels(self):
        text = report.build_report(sample_rows(), n_floor=0)
        self.assertIn("Revenue-strict", text)
        self.assertIn("All commercial", text)
        self.assertIn("Pooled", text)

    def test_flag_is_attached_to_the_undersized_row_only(self):
        rows = [clock_row("big%02d" % i, "software_internet", "primary",
                          8 + (i % 7)) for i in range(35)]
        rows += [clock_row("s%02d" % i, "science_research", "equivalent",
                           18 + (i % 4)) for i in range(5)]
        text = report.build_report(rows, n_floor=0)
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
        text = report.build_report(rows, n_floor=0)
        line = [l for l in text.splitlines()
                if l.startswith("| science_research")][0]
        self.assertIn("n=1", line)
        self.assertIn("too small to read", line)

    def test_reports_stopping_rule_numbers(self):
        text = report.build_report(sample_rows(), n_floor=0)
        self.assertIn("Stopping rule", text)
        # 12 of the 23 sample rows are hit_basis == "primary".
        self.assertIn("Revenue-strict n = 12", text)
        self.assertIn("threshold 1.00", text)


class TestConfidenceRuns(unittest.TestCase):
    def rows(self):
        return conf_rows()

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
        return bounded_rows()

    def test_unbounded_only_drops_bounded_rows(self):
        runs = report.bounded_runs(self.rows())
        self.assertEqual(runs["unbounded_only"]["n"], 3)
        self.assertEqual(runs["unbounded_only"]["median"], 9.0)

    def test_midpoint_all_keeps_everything(self):
        runs = report.bounded_runs(self.rows())
        self.assertEqual(runs["midpoint_all"]["n"], 5)
        self.assertEqual(runs["midpoint_all"]["median"], 10.0)

    def test_envelope_brackets_the_midpoint(self):
        # The bounded rows straddle the midpoint median, so a run that
        # ignored the envelope columns — or swapped them — cannot pass.
        runs = report.bounded_runs(self.rows())
        self.assertEqual(runs["envelope_min"]["median"], 8.0)
        self.assertEqual(runs["envelope_max"]["median"], 12.0)
        self.assertLess(runs["envelope_min"]["median"],
                        runs["midpoint_all"]["median"])
        self.assertGreater(runs["envelope_max"]["median"],
                           runs["midpoint_all"]["median"])


class TestNewReportSections(unittest.TestCase):
    def test_report_contains_confidence_section(self):
        text = report.build_report(sample_rows(), n_floor=0)
        self.assertIn("Confidence sensitivity", text)
        self.assertIn("high-confidence rows only", text)

    def test_report_contains_bounded_section(self):
        text = report.build_report(sample_rows(), n_floor=0)
        self.assertIn("Bounded-date sensitivity", text)

    def test_confidence_cells_carry_their_own_medians(self):
        text = report.build_report(conf_rows(), n_floor=0)
        self.assertIn("| 8.0 yr",
                      table_row(text, "high-confidence rows only"))
        self.assertIn("| 14.0 yr", table_row(text, "all included rows"))

    def test_bounded_cells_carry_four_distinct_medians(self):
        text = report.build_report(bounded_rows(), n_floor=0)
        self.assertIn("| 9.0 yr", table_row(text, "bounded rows dropped"))
        self.assertIn("| 10.0 yr",
                      table_row(text, "all rows, span midpoints"))
        self.assertIn("| 8.0 yr",
                      table_row(text, "all rows, earliest possible"))
        self.assertIn("| 12.0 yr",
                      table_row(text, "all rows, latest possible"))

    def test_sensitivity_sections_name_the_pooled_median(self):
        # Both runs pool every bucket and hit basis; the headline defined
        # above them does not, so neither may claim to qualify it.
        text = report.build_report(sample_rows(), n_floor=0)
        self.assertEqual(text.count("not the revenue-strict headline"), 2)

    def test_divergence_warns_about_the_pooled_median(self):
        text = report.build_report(conf_rows(), n_floor=0)
        self.assertIn("**These diverge by 6.0 years.**", text)
        self.assertIn("read the pooled median as a point estimate", text)

    def test_divergence_below_threshold_reports_agreement(self):
        text = report.build_report(conf_rows(10, 11.8), n_floor=0)
        self.assertIn("These agree within 0.9 years.", text)
        self.assertNotIn("These diverge", text)

    def test_all_high_confidence_says_nothing_was_varied(self):
        text = report.build_report(sample_rows(), n_floor=0)
        self.assertIn("0 of 23 rows fall below high confidence.", text)
        self.assertIn("Nothing was varied", text)
        self.assertNotIn("These agree within", text)
        self.assertNotIn("These diverge", text)

    def test_no_bounded_rows_says_nothing_was_varied(self):
        text = report.build_report(sample_rows(), n_floor=0)
        self.assertIn("0 of 23 rows carry one", text)
        self.assertIn("nothing was varied", text)
        self.assertNotIn("full range the data permits", text)


if __name__ == "__main__":
    unittest.main()


class TestExclusionAudit(unittest.TestCase):
    def rows(self):
        rows = [clock_row("k%02d" % i, "software_internet", "primary", 8,
                          country="US") for i in range(5)]
        rows += [clock_row("x%02d" % i, "software_internet", "", None,
                           country="JP", gender="F", excluded="true",
                           exclusion_reason="crossing_undatable")
                 for i in range(2)]
        return rows

    def test_counts_the_discard_pile(self):
        audit = report.exclusion_audit(self.rows())
        self.assertEqual(audit["n_total"], 7)
        self.assertEqual(audit["n_excluded"], 2)
        self.assertAlmostEqual(audit["rate"], 2 / 7.0)

    def test_groups_by_reason(self):
        audit = report.exclusion_audit(self.rows())
        self.assertEqual(audit["reasons"], {"crossing_undatable": 2})

    def test_exposes_an_uneven_exclusion_rate(self):
        """The whole point: US 0%, non-US 100%, visible side by side."""
        cuts = {c["name"]: c for c in report.exclusion_audit(self.rows())
                ["cross_cuts"]}
        self.assertEqual(cuts["US"]["excluded"], 0)
        self.assertEqual(cuts["US"]["rate"], 0.0)
        self.assertEqual(cuts["non-US"]["excluded"], 2)
        self.assertEqual(cuts["non-US"]["rate"], 1.0)

    def test_rate_is_none_for_an_empty_cross_cut(self):
        cuts = {c["name"]: c for c in report.exclusion_audit(self.rows())
                ["cross_cuts"]}
        self.assertIsNone(cuts["men"]["rate"])

    def test_excluded_rows_reach_no_statistic(self):
        """An excluded row with a full clock must not move any median."""
        rows = [clock_row("k%02d" % i, "software_internet", "primary", 8)
                for i in range(5)]
        rows.append(clock_row("bad", "software_internet", "primary", 99,
                              excluded="true"))
        text = report.build_report(rows, n_floor=0)
        self.assertIn("1 of 6 rows excluded", text)
        self.assertNotIn("99.0", text)


class TestExclusionAuditSection(unittest.TestCase):
    def test_section_renders_rates(self):
        rows = [clock_row("k%02d" % i, "software_internet", "primary", 8)
                for i in range(5)]
        rows.append(clock_row("x", "software_internet", "", None,
                              country="JP", excluded="true",
                              exclusion_reason="crossing_undatable"))
        text = report.build_report(rows, n_floor=0)
        self.assertIn("## Exclusion audit", text)
        self.assertIn("crossing_undatable", text)
        self.assertIn("| non-US | 0 | 1 | 100.0% |", text)

    def test_says_so_when_nothing_was_excluded(self):
        text = report.build_report(sample_rows(), n_floor=0)
        self.assertIn("No rows excluded of", text)
        self.assertNotIn("exclusion rate", text)


class TestMediansWithheldBelowTheFloor(unittest.TestCase):
    """Optional stopping is the threat; a number seen once cannot be unseen."""

    def test_no_median_appears_below_the_floor(self):
        text = report.build_report(sample_rows())
        self.assertIn("## Medians withheld", text)
        self.assertIn("revenue-strict rows | 12", text)
        for heading in ("## Definition strictness", "## Confidence sensitivity",
                        "## Bounded-date sensitivity", "## All clocks, pooled"):
            self.assertNotIn(heading, text)

    def test_the_withheld_report_prints_no_year_figures(self):
        text = report.build_report(sample_rows())
        self.assertNotIn(" yr", text)
        self.assertNotIn("95% CI", text)

    def test_the_exclusion_audit_still_prints(self):
        """Exclusions are a data-quality signal, not a result to blind."""
        rows = sample_rows()
        rows.append(clock_row("x", "software_internet", "", None,
                              country="JP", excluded="true",
                              exclusion_reason="crossing_undatable"))
        text = report.build_report(rows)
        self.assertIn("## Exclusion audit", text)
        self.assertIn("crossing_undatable", text)

    def test_tables_return_once_the_floor_is_met(self):
        rows = [clock_row("p%02d" % i, "software_internet", "primary", 8)
                for i in range(30)]
        text = report.build_report(rows)
        self.assertNotIn("## Medians withheld", text)
        self.assertIn("## Definition strictness", text)


class TestSurvivorshipCaveat(unittest.TestCase):
    """The caveat is the point of the document, not decoration.

    It must survive both the withheld and the full report, because the
    withheld version is the only one the reader sees for the first ~10 waves.
    """

    def both_reports(self):
        return (report.build_report(sample_rows()),
                report.build_report(sample_rows(), n_floor=0))

    def test_states_what_the_median_supports(self):
        for text in self.both_reports():
            self.assertIn("Among people who eventually hit, the middle one "
                          "took about 8 years.", text)

    def test_states_what_it_does_not_support(self):
        for text in self.both_reports():
            self.assertIn("If I start now, I have about a 50% chance of "
                          "hitting within 8 years.", text)

    def test_names_the_missing_denominator(self):
        for text in self.both_reports():
            self.assertIn("denominator", text)
