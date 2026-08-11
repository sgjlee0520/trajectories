import unittest

from src import schema


def valid_row(**overrides):
    """A minimal valid commercial row. Override fields to make it invalid."""
    row = {
        "person_id": "p001",
        "name": "Test Person",
        "bucket": "software_internet",
        "source_list": "Forbes 400",
        "country_primary": "US",
        "gender": "f",
        "hit_entity": "Test Corp",
        "hit_criterion": "rev10",
        "hit_basis": "primary",
        "excluded": "false",
        "exclusion_reason": "",
        "notes": "",
    }
    dates = {
        "a1_birth": "1964",
        "a2_education_end": "1986",
        "a3_first_domain_job": "1986",
        "a4_first_venture": "1994",
        "a5_first_hit": "1997",
        "a6_scale_hit": "1999",
    }
    for anchor, year in dates.items():
        row[anchor + "_date"] = year
        row[anchor + "_src"] = "https://example.org/" + anchor
        row[anchor + "_conf"] = "high"
    row.update(overrides)
    return row


class TestColumns(unittest.TestCase):
    def test_header_has_identity_anchors_and_trailing(self):
        cols = schema.columns()
        self.assertEqual(cols[0], "person_id")
        self.assertIn("a5_first_hit_date", cols)
        self.assertIn("a5_first_hit_src", cols)
        self.assertIn("a5_first_hit_conf", cols)
        self.assertIn("hit_basis", cols)
        self.assertEqual(len(cols), 6 + 6 * 3 + 6)

    def test_shares_sum_to_100(self):
        self.assertEqual(sum(schema.BUCKET_SHARES.values()), 100)


class TestParseYear(unittest.TestCase):
    def test_parses_four_digit_year(self):
        self.assertEqual(schema.parse_year("1994"), 1994)

    def test_unknown_is_none(self):
        self.assertIsNone(schema.parse_year("unknown"))

    def test_garbage_is_none(self):
        self.assertIsNone(schema.parse_year("mid-90s"))
        self.assertIsNone(schema.parse_year(""))


class TestParseSpan(unittest.TestCase):
    def test_single_year_becomes_a_degenerate_span(self):
        self.assertEqual(schema.parse_span("1994"), (1994, 1994))

    def test_bounded_span(self):
        self.assertEqual(schema.parse_span("1960-1961"), (1960, 1961))

    def test_unknown_is_empty(self):
        self.assertEqual(schema.parse_span("unknown"), (None, None))

    def test_blank_is_empty(self):
        self.assertEqual(schema.parse_span(""), (None, None))

    def test_reversed_span_rejected(self):
        self.assertEqual(schema.parse_span("1961-1960"), (None, None))

    def test_overwide_span_rejected(self):
        # A range this wide carries almost no information and is far more
        # likely a typo than a real bound.
        self.assertEqual(schema.parse_span("1960-1990"), (None, None))

    def test_span_at_the_width_limit_accepted(self):
        self.assertEqual(schema.parse_span("1960-1970"), (1960, 1970))

    def test_garbage_rejected(self):
        for bad in ("mid-90s", "199-1995", "1960-", "-1960", "1960-61"):
            self.assertEqual(schema.parse_span(bad), (None, None),
                             "should reject %r" % bad)


class TestValidateRow(unittest.TestCase):
    def test_valid_row_has_no_errors(self):
        self.assertEqual(schema.validate_row(valid_row()), [])

    def test_missing_column_reported(self):
        row = valid_row()
        del row["hit_basis"]
        errors = schema.validate_row(row)
        self.assertTrue(any("missing columns" in e for e in errors))

    def test_unknown_bucket_rejected(self):
        errors = schema.validate_row(valid_row(bucket="crypto_bros"))
        self.assertTrue(any("unknown bucket" in e for e in errors))

    def test_inferred_date_without_source_rejected(self):
        # The core invariant: a confident date must carry a source URL.
        errors = schema.validate_row(valid_row(a5_first_hit_src=""))
        self.assertTrue(any("a5_first_hit_src" in e for e in errors))

    def test_bare_http_string_is_not_a_source(self):
        # "http" satisfied the old startswith check while citing nothing.
        errors = schema.validate_row(valid_row(a5_first_hit_src="http"))
        self.assertTrue(any("a5_first_hit_src" in e for e in errors))

    def test_malformed_url_rejected(self):
        for bad in ("httpIforgot", "https:/typo", "ftp://example.org/x",
                    "https://nodot"):
            errors = schema.validate_row(valid_row(a5_first_hit_src=bad))
            self.assertTrue(any("a5_first_hit_src" in e for e in errors),
                            "should reject %r" % bad)

    def test_conf_none_requires_unknown_date(self):
        errors = schema.validate_row(valid_row(a3_first_domain_job_conf="none"))
        self.assertTrue(any("requires a3_first_domain_job_date='unknown'" in e
                            for e in errors))

    def test_conf_none_with_unknown_and_blank_src_is_valid(self):
        row = valid_row(
            a6_scale_hit_conf="none",
            a6_scale_hit_date="unknown",
            a6_scale_hit_src="",
        )
        self.assertEqual(schema.validate_row(row), [])

    def test_unknown_hit_must_be_excluded(self):
        row = valid_row(
            a5_first_hit_conf="none",
            a5_first_hit_date="unknown",
            a5_first_hit_src="",
            excluded="false",
        )
        errors = schema.validate_row(row)
        self.assertTrue(any("requires excluded=true" in e for e in errors))

    def test_unknown_hit_excluded_with_reason_is_valid(self):
        row = valid_row(
            a5_first_hit_conf="none",
            a5_first_hit_date="unknown",
            a5_first_hit_src="",
            excluded="true",
            exclusion_reason="revenue never disclosed, no exit",
            hit_criterion="",
            hit_basis="",
        )
        self.assertEqual(schema.validate_row(row), [])

    def test_prize_criterion_rejected_for_commercial_bucket(self):
        errors = schema.validate_row(
            valid_row(hit_criterion="prize", hit_basis="equivalent"))
        self.assertTrue(any("not allowed for bucket" in e for e in errors))

    def test_science_bucket_requires_prize(self):
        errors = schema.validate_row(
            valid_row(bucket="science_research", hit_criterion="rev10",
                      hit_basis="primary"))
        self.assertTrue(any("not allowed for bucket" in e for e in errors))

    def test_science_bucket_with_prize_is_valid(self):
        row = valid_row(bucket="science_research", hit_criterion="prize",
                        hit_basis="equivalent")
        self.assertEqual(schema.validate_row(row), [])

    def test_basis_must_match_criterion(self):
        errors = schema.validate_row(
            valid_row(hit_criterion="ipo", hit_basis="primary"))
        self.assertTrue(any("hit_basis for ipo must be fallback" in e
                            for e in errors))

    def test_ipo_is_fallback_basis(self):
        row = valid_row(hit_criterion="ipo", hit_basis="fallback")
        self.assertEqual(schema.validate_row(row), [])

    def test_education_after_hit_rejected(self):
        errors = schema.validate_row(valid_row(a2_education_end_date="2001"))
        self.assertTrue(any("is after a5_first_hit" in e for e in errors))

    def test_venture_after_hit_rejected(self):
        errors = schema.validate_row(valid_row(a4_first_venture_date="1999"))
        self.assertTrue(any("is after a5_first_hit" in e for e in errors))

    def test_implausible_birth_year_rejected(self):
        errors = schema.validate_row(valid_row(a1_birth_date="1700"))
        self.assertTrue(any("a1_birth_date must be a year in" in e
                            for e in errors))

    def test_unknown_birth_year_is_allowed(self):
        # Obscure people genuinely lack a documented birth year. That costs
        # two clocks, not the row.
        row = valid_row(
            a1_birth_conf="none",
            a1_birth_date="unknown",
            a1_birth_src="",
        )
        self.assertEqual(schema.validate_row(row), [])

    def test_bounded_hit_date_accepted(self):
        row = valid_row(a5_first_hit_date="1960-1961",
                        a2_education_end_date="1954",
                        a4_first_venture_date="1957",
                        a1_birth_date="1929")
        self.assertEqual(schema.validate_row(row), [])

    def test_bounded_date_still_needs_a_source(self):
        errors = schema.validate_row(
            valid_row(a5_first_hit_date="1960-1961", a5_first_hit_src=""))
        self.assertTrue(any("a5_first_hit_src" in e for e in errors))

    def test_overwide_bounded_date_rejected(self):
        errors = schema.validate_row(valid_row(a5_first_hit_date="1960-1990"))
        self.assertTrue(any("a5_first_hit_date" in e for e in errors))

    def test_ordering_uses_the_low_end_of_a_bounded_hit(self):
        # education in 1962 is after the earliest possible hit in 1960.
        errors = schema.validate_row(
            valid_row(a5_first_hit_date="1960-1961",
                      a2_education_end_date="1962"))
        self.assertTrue(any("is after a5_first_hit" in e for e in errors))

    def test_rank1_allowed_for_investors(self):
        row = valid_row(bucket="investors_finance", hit_criterion="rank1",
                        hit_basis="equivalent")
        self.assertEqual(schema.validate_row(row), [])

    def test_fund100_still_allowed_for_investors(self):
        row = valid_row(bucket="investors_finance", hit_criterion="fund100",
                        hit_basis="equivalent")
        self.assertEqual(schema.validate_row(row), [])

    def test_rank1_rejected_for_commercial_bucket(self):
        errors = schema.validate_row(
            valid_row(hit_criterion="rank1", hit_basis="equivalent"))
        self.assertTrue(any("not allowed for bucket" in e for e in errors))


if __name__ == "__main__":
    unittest.main()
