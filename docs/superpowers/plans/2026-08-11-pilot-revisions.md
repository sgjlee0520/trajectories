# Pilot Revisions Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Close the four measurement defects the 10-person pilot exposed, so that `a5_first_hit` records when a career's first success actually happened rather than when it happened to become citable.

**Architecture:** Four independent defects, each fixed at the lowest layer that can hold it. Bounded dates become a new primitive in `schema.py` that `clocks.py` resolves to a midpoint plus a min/max envelope. The constant-dollar threshold needs no pipeline change at all — the code never sees revenue, so it ships as a lookup table researchers consult. The two missing sensitivity runs need confidence data carried into `clocks.csv`, which it currently drops.

**Tech Stack:** Python 3.9.6, stdlib only — `csv`, `random`, `re`, `statistics`, `sys`. Tests use `unittest`.

## Why this plan exists

The pilot found that Gordon Moore's row is impeccably sourced and roughly eleven years wrong. Fairchild Semiconductor passed $10M in revenue around 1960, but no source pins the year, so the `ipo` fallback fired at Intel's 1971 IPO instead. Every date in that row has a real URL and the validator passes it clean. The error is in the definition, not the research — which makes it exactly the failure the cite-or-flag standard was built to prevent, arriving through the back door.

Read `docs/PILOT-REVIEW.md` before starting. It is the evidence for every change here.

## Global Constraints

- **Python 3.9.6.** No `match`, no PEP 604 `int | None` annotations, no runtime `dict[str, int]` subscripting.
- **Stdlib only.** `pandas`, `pytest`, and `numpy` are not installed and must not be installed. Tests use `unittest`.
- **Test command**, from repo root `/Users/slee/trajectories`: `python3 -m unittest discover -s tests -t . -v`
- **Baseline: 88 tests passing** before any change in this plan.
- **Anchors are never inferred.** An anchor is a sourced date, or the literal `unknown` with `_conf = none` and an empty `_src`. This plan widens what "a sourced date" may look like; it does not weaken the rule.
- **Bounded date format:** `YYYY-YYYY`, low year first, both years plausible, span width at most 10 years.
- **Canonical bucket keys:** `software_internet`, `hardware_deeptech`, `consumer_retail_industrial`, `science_research`, `investors_finance`, `media_creators`, `healthcare_biotech`, `trade_import_logistics`.
- **Hit criterion codes after this plan:** `rev10`, `ipo`, `acq50`, `prize`, `aud1m`, `fund100`, **`rank1`** (new).
- **Hit basis values:** `primary`, `fallback`, `equivalent`. Mapping: `rev10`→primary; `ipo`,`acq50`→fallback; `prize`,`aud1m`,`fund100`,`rank1`→equivalent.
- **`investors_finance` accepts two criteria** after this plan: `fund100` and `rank1`.
- **Constant-dollar base year: 2026.** The $10M threshold is in constant 2026 dollars.
- **Era split stays 1995.** Stopping-rule constants stay: N floor 30, max drift 0.5 yr, max CI half-width 1.0 yr, wave size 25, audit fraction 0.15, void threshold 0.10.

---

## File Structure

```
src/
  cpi.py        NEW  annual CPI-U series + constant-dollar threshold lookup
  schema.py     MOD  parse_span, bounded-date validation, rank1 criterion
  clocks.py     MOD  span midpoint, min/max envelope, confidence propagation
  report.py     MOD  bounded-sensitivity run, conf=high sensitivity run
  allocate.py   unchanged
  stats.py      unchanged
tests/
  test_cpi.py   NEW
  test_schema.py test_clocks.py test_report.py   MOD
frame.md                              MOD  criteria, threshold, conventions
docs/superpowers/specs/2026-07-31-apprenticeship-trajectories-design.md  MOD
docs/PILOT-REVIEW-2.md                NEW  second-pilot verdict
data/anchors.csv                      MOD  10 rows re-coded under new rules
```

---

### Task 1: Spec and frame text

**Files:**
- Modify: `frame.md`
- Modify: `docs/superpowers/specs/2026-07-31-apprenticeship-trajectories-design.md`

**Interfaces:**
- Consumes: nothing
- Produces: the written definitions every later task encodes. No code interface.

`frame.md` carries a freeze notice. The freeze binds **after wave 1 begins**; wave 1 has not begun, so this revision is in scope. Update the freeze line to record that it was revised post-pilot.

- [ ] **Step 1: Rewrite the hit-criteria section of `frame.md`**

Replace the whole `## Hit criteria` section with:

```markdown
## Hit criteria

Revised 2026-08-11 after the 10-person pilot. See `docs/PILOT-REVIEW.md`.

### The threshold is in constant 2026 dollars

`rev10` means **$10M in constant 2026 US dollars**, not $10M nominal. A nominal
threshold would demand that a 1960 founder build a business roughly eleven times
larger in real terms than a 2020 founder to trigger the same "first hit", which
inflates every pre-1995 apprenticeship — and the frame requires at least 25% of
those.

Look up the nominal threshold for a revenue year with:

    python3 -m src.cpi 1960

For non-USD accounts, convert at the **spot rate for the revenue year**, then
compare against that year's nominal threshold.

### Commercial buckets

`software_internet`, `hardware_deeptech`, `consumer_retail_industrial`,
`healthcare_biotech`, `trade_import_logistics`:

1. `rev10` — first year the person's own venture reached the constant-dollar
   $10M threshold. Basis `primary`.
2. `ipo` or `acq50` (acquisition above $50M constant 2026 dollars), whichever is
   earlier. Basis `fallback`. **Permitted only when no earlier crossing is known
   to have occurred.** If sources establish that the venture passed the threshold
   in an earlier year that cannot be pinned exactly, record a bounded `rev10`
   date instead — see below. If it cannot even be bounded, the row is
   `excluded = true` with reason `crossing_undatable`. Dating such a row by a
   later IPO is forbidden: it produces a confidently sourced answer that is years
   wrong.

### Non-commercial buckets

- `science_research` → `prize` (Nobel, Turing, Fields, or Breakthrough). Basis
  `equivalent`. **Record the announcement year**, not the prize's official
  designated year, because the announcement is when recognition actually landed.
  Karikó's Breakthrough Prize is officially the 2022 prize but was announced
  9 September 2021, so the anchor is 2021.
- `media_creators` → `aud1m` (1M+ audience for their own work). Basis
  `equivalent`.
- `investors_finance` → **two criteria, chosen by career type**:
  - Fund managers: `fund100` — first fund closed above $100M constant 2026
    dollars where the person was a named general partner. Basis `equivalent`.
  - Analysts, economists, and other non-fund finance careers: `rank1` — the
    first year the person topped a recognized industry ranking, such as the
    Institutional Investor All-America Research Team. Basis `equivalent`.

  `fund100` alone mis-dates analysts badly: Mary Meeker was among the most
  influential people in technology investing roughly 23 years before Bond
  Capital's 2019 debut fund. Where no recognized ranking exists for a person,
  the anchor is `unknown` and the row is excluded — that is honest, and better
  than dating a career by an event that came decades late.

### Bounded dates

When sources establish that an event happened within a range but not which year,
record the anchor as `YYYY-YYYY` — low year first, at most 10 years wide, with a
source for the bound. Clocks use the midpoint; the report prints a sensitivity
run with bounded rows excluded so the uncertainty stays visible.

A bounded date is a real measurement, not a guess. `1960-1961` says two sources
bracket the event. It is not licence to widen a range until it contains a year
you like.
```

- [ ] **Step 2: Update the freeze line at the top of `frame.md`**

Replace the two-line freeze notice with:

```markdown
Frozen 2026-07-31; revised 2026-08-11 after the 10-person pilot. Do not edit
after wave 1 begins. Changing the frame mid-collection invalidates the stopping
rule, because the sample composition would no longer be stable across waves.
```

- [ ] **Step 3: Mirror the criteria changes into spec §4**

In `docs/superpowers/specs/2026-07-31-apprenticeship-trajectories-design.md`, update the `### a5_first_hit threshold definition` subsection so its criteria table, basis mapping, and prose match `frame.md` exactly: add `rank1` to the non-commercial table with basis `equivalent`, state the constant-2026-dollar threshold, state the announcement-year rule for `prize`, state the fallback restriction, and add a `#### Bounded dates` paragraph.

Also update spec §4's **Date precision** paragraph to read:

```markdown
### Date precision

**Year precision throughout**, with bounded dates permitted where sources
bracket an event without pinning it (`YYYY-YYYY`, at most 10 years wide). The
output is a median measured in years; month-level precision is false precision
that costs real research time for no gain.
```

- [ ] **Step 4: Add the pilot's findings to spec §10**

Append two limitations:

```markdown
7. **Selection into the `primary` subset is non-random.** A venture whose
   threshold crossing is datable is one that either disclosed financials soon
   after crossing or was covered in the press at the time — both describe fast
   risers. Slow burners fall to `fallback` or exclusion, so the revenue-strict
   median is likely biased *downward*. Bounded dates reduce this pressure by
   letting a bracketed crossing qualify, but do not eliminate it.
8. **`a3_first_domain_job` has no state for "this never happened."** A
   founder-first career like Sara Blakely's has no prior domain employment, which
   is a fact about the career rather than a research failure, yet the schema can
   only record `unknown` — the same value used when a job certainly existed but
   is undated. The two are conflated in the unknown rate.
```

- [ ] **Step 5: Commit**

```bash
git add frame.md docs/superpowers/specs/2026-07-31-apprenticeship-trajectories-design.md
git commit -m "Revise frame and spec for the pilot's four measurement defects"
```

---

### Task 2: Constant-dollar threshold lookup

**Files:**
- Create: `src/cpi.py`
- Test: `tests/test_cpi.py`

**Interfaces:**
- Consumes: nothing
- Produces:
  - `CPI` — dict of int year -> float annual CPI-U index value
  - `BASE_YEAR` — int, 2026
  - `THRESHOLD_CONSTANT` — int, 10_000_000
  - `nominal_threshold(year, constant_amount=THRESHOLD_CONSTANT)` -> float, the nominal USD figure equivalent to `constant_amount` base-year dollars in `year`
  - `to_constant(amount, year)` -> float, converts a nominal amount in `year` to base-year dollars

**No pipeline code consumes this.** The validator never sees revenue figures — a human researcher decides whether `rev10` fired. This module exists so that decision is made against the right number instead of a nominal one. It is a lookup table with a CLI.

- [ ] **Step 1: Source the CPI data**

Fetch the **annual average CPI-U (all urban consumers, US city average, 1982-84=100)** series from the Bureau of Labor Statistics, covering **1913 through the most recent complete year**. BLS series ID `CUUR0000SA0`, available at <https://www.bls.gov/cpi/data.htm> or via the BLS API.

Write the values into `src/cpi.py` as a literal dict. **Do not invent or interpolate any value.** If the series cannot be retrieved, stop and report BLOCKED rather than writing remembered numbers — a wrong deflator silently distorts every pre-1995 row, which is precisely the class of error this plan exists to remove.

For the current year and any year the published series does not yet cover, carry forward the last published annual average and note it in a module comment.

- [ ] **Step 2: Write the failing test**

Create `tests/test_cpi.py`:

```python
import unittest

from src import cpi


class TestSeries(unittest.TestCase):
    def test_covers_the_project_era(self):
        for year in (1913, 1960, 1980, 2000, 2020):
            self.assertIn(year, cpi.CPI)

    def test_base_year_present(self):
        self.assertIn(cpi.BASE_YEAR, cpi.CPI)

    def test_values_are_positive(self):
        self.assertTrue(all(v > 0 for v in cpi.CPI.values()))

    def test_spot_check_known_annual_averages(self):
        # CPI-U annual averages, 1982-84 = 100. Loose tolerances: these pin the
        # series to the right scale and shape, not to a specific vintage.
        self.assertAlmostEqual(cpi.CPI[1960], 29.6, delta=0.5)
        self.assertAlmostEqual(cpi.CPI[1980], 82.4, delta=1.0)
        self.assertAlmostEqual(cpi.CPI[2000], 172.2, delta=1.5)
        self.assertAlmostEqual(cpi.CPI[2020], 258.8, delta=2.0)

    def test_broadly_increasing(self):
        # Deflation years exist (1930s, 2009), so require the trend rather than
        # strict monotonicity.
        self.assertLess(cpi.CPI[1950], cpi.CPI[1970])
        self.assertLess(cpi.CPI[1970], cpi.CPI[1990])
        self.assertLess(cpi.CPI[1990], cpi.CPI[2010])


class TestNominalThreshold(unittest.TestCase):
    def test_base_year_threshold_is_the_constant_amount(self):
        self.assertAlmostEqual(cpi.nominal_threshold(cpi.BASE_YEAR),
                               float(cpi.THRESHOLD_CONSTANT), delta=1.0)

    def test_1960_threshold_is_roughly_a_tenth(self):
        # $10M constant 2026 dollars was around $0.9-1.1M nominal in 1960.
        value = cpi.nominal_threshold(1960)
        self.assertGreater(value, 700_000)
        self.assertLess(value, 1_400_000)

    def test_older_years_need_smaller_nominal_revenue(self):
        self.assertLess(cpi.nominal_threshold(1960),
                        cpi.nominal_threshold(1990))
        self.assertLess(cpi.nominal_threshold(1990),
                        cpi.nominal_threshold(2020))

    def test_accepts_a_custom_constant_amount(self):
        # The acq50 threshold is $50M constant, five times rev10's.
        self.assertAlmostEqual(cpi.nominal_threshold(1980, 50_000_000),
                               5 * cpi.nominal_threshold(1980), delta=1.0)

    def test_unknown_year_raises(self):
        with self.assertRaises(KeyError):
            cpi.nominal_threshold(1800)


class TestToConstant(unittest.TestCase):
    def test_round_trip(self):
        nominal = cpi.nominal_threshold(1960)
        self.assertAlmostEqual(cpi.to_constant(nominal, 1960),
                               float(cpi.THRESHOLD_CONSTANT), delta=1.0)

    def test_1960_dollars_are_worth_more(self):
        self.assertGreater(cpi.to_constant(1_000_000, 1960), 8_000_000)


if __name__ == "__main__":
    unittest.main()
```

- [ ] **Step 3: Run test to verify it fails**

Run: `python3 -m unittest tests.test_cpi -v`
Expected: FAIL — `src.cpi` does not exist. Since `src/` is already a package this may surface as `ImportError` rather than `ModuleNotFoundError`; either is the expected RED.

- [ ] **Step 4: Write the implementation**

Create `src/cpi.py`. Use this exact structure, with the `CPI` dict filled from the data sourced in Step 1:

```python
"""Constant-dollar thresholds for the hit criteria.

A nominal $10M threshold is not the same test across eras: crossing $10M in
1960 required a business roughly eleven times larger in real terms than
crossing $10M today. Applied to a sample that is at least 25% pre-1995 by
design, that inflates exactly the careers the frame works hardest to include.

No pipeline code consumes this module. A human researcher decides whether a
criterion fired; this exists so that decision is made against the right number.

Source: US Bureau of Labor Statistics, CPI-U annual averages, all urban
consumers, US city average, 1982-84 = 100 (series CUUR0000SA0).
"""

import sys

BASE_YEAR = 2026
THRESHOLD_CONSTANT = 10_000_000

CPI = {
    1913: 9.9,
    # ... every year through the latest published annual average ...
}


def nominal_threshold(year, constant_amount=THRESHOLD_CONSTANT):
    """The nominal USD figure equivalent to `constant_amount` base-year dollars.

    Raises KeyError for a year outside the published series rather than
    extrapolating — an invented deflator is worse than no answer.
    """
    return constant_amount * CPI[year] / CPI[BASE_YEAR]


def to_constant(amount, year):
    """Convert a nominal amount observed in `year` into base-year dollars."""
    return amount * CPI[BASE_YEAR] / CPI[year]


def main(argv):
    """Print the nominal thresholds a researcher needs for one revenue year."""
    if len(argv) != 2:
        print("usage: python3 -m src.cpi <year>")
        return 2
    year = int(argv[1])
    if year not in CPI:
        print("no CPI data for %d (series covers %d-%d)"
              % (year, min(CPI), max(CPI)))
        return 1
    print("revenue year %d, thresholds in nominal USD:" % year)
    for label, constant in (("rev10", THRESHOLD_CONSTANT),
                            ("acq50", 50_000_000),
                            ("fund100", 100_000_000)):
        print("  {:<8} (${:,} constant {}) = ${:,.0f}".format(
            label, constant, BASE_YEAR, nominal_threshold(year, constant)))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
```

Note: thousands separators use `str.format`, not `%`-formatting — `%` has no comma flag, so `"$%,.0f"` raises `ValueError`. The rest of the codebase uses `%` style; this one loop is the exception, for the separators.

- [ ] **Step 5: Run tests to verify they pass**

Run: `python3 -m unittest tests.test_cpi -v`
Expected: PASS, 12 tests

- [ ] **Step 6: Verify the CLI by hand**

Run: `python3 -m src.cpi 1960`
Expected: three threshold lines; the `rev10` figure should land near $0.9-1.1M. Paste the real output into your report.

- [ ] **Step 7: Commit**

```bash
git add src/cpi.py tests/test_cpi.py
git commit -m "Add constant-dollar threshold lookup"
```

---

### Task 3: Bounded dates and the rank1 criterion in the validator

**Files:**
- Modify: `src/schema.py`
- Test: `tests/test_schema.py`

**Interfaces:**
- Consumes: nothing new
- Produces:
  - `parse_span(value)` -> tuple `(lo, hi)` of ints, or `(None, None)` for `unknown`/blank/malformed
  - `MAX_SPAN_YEARS` — int, 10
  - `parse_year(value)` — unchanged, still returns an int only for a single 4-digit year
  - `CRITERION_BASIS` gains `rank1` -> `equivalent`
  - `BUCKET_CRITERIA["investors_finance"]` becomes `{"fund100", "rank1"}`

- [ ] **Step 1: Write the failing tests**

Add to `tests/test_schema.py`. First a new class, placed immediately after `TestParseYear`:

```python
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
```

Then add to the existing `TestValidateRow` class:

```python
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
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `python3 -m unittest tests.test_schema -v`
Expected: FAIL — `parse_span` does not exist, and the bounded-date and `rank1` cases are rejected.

- [ ] **Step 3: Add `parse_span` and `MAX_SPAN_YEARS`**

In `src/schema.py`, add `MAX_SPAN_YEARS = 10` next to `MIN_BIRTH_YEAR`, and add this function immediately after `parse_year`:

```python
def parse_span(value):
    """Parse an anchor date into (lo, hi) years.

    A single year yields a degenerate span. 'YYYY-YYYY' yields a real one,
    for the case where sources bracket an event without pinning it — the
    alternative is dating the row by a later, citable event that is years
    wrong, which is what the pilot found in three of ten rows.

    Returns (None, None) for unknown, blank, or malformed input, including a
    reversed or implausibly wide range.
    """
    text = (value or "").strip()
    single = parse_year(text)
    if single is not None:
        return (single, single)
    parts = text.split("-")
    if len(parts) != 2:
        return (None, None)
    lo, hi = parse_year(parts[0]), parse_year(parts[1])
    if lo is None or hi is None:
        return (None, None)
    if lo > hi or hi - lo > MAX_SPAN_YEARS:
        return (None, None)
    return (lo, hi)
```

- [ ] **Step 4: Register the `rank1` criterion**

In `src/schema.py`, change the `BUCKET_CRITERIA` entry for investors and add `rank1` to `CRITERION_BASIS`:

```python
BUCKET_CRITERIA = {
    "science_research": {"prize"},
    "media_creators": {"aud1m"},
    # Fund managers use fund100; analysts and other non-fund finance careers
    # use rank1, because fund100 dates an analyst's career decades late.
    "investors_finance": {"fund100", "rank1"},
}

CRITERION_BASIS = {
    "rev10": "primary",
    "ipo": "fallback",
    "acq50": "fallback",
    "prize": "equivalent",
    "aud1m": "equivalent",
    "fund100": "equivalent",
    "rank1": "equivalent",
}
```

- [ ] **Step 5: Switch validation from `parse_year` to `parse_span`**

Three edits inside `validate_row`.

Replace the sourced-date branch condition:

```python
        else:
            if parse_span(date)[0] is None:
                errors.append("%s_date must be a 4-digit year or a "
                              "'YYYY-YYYY' span at most %d years wide, got %r"
                              % (anchor, MAX_SPAN_YEARS, date))
            if not URL_PATTERN.match(src):
                errors.append("%s_src must be a URL when %s_conf=%s, got %r"
                              % (anchor, anchor, conf, src))
```

Replace the birth plausibility check so it reads the low end of a span:

```python
    # An unknown birth year is permitted — it costs the two clocks that need
    # it, not the whole row. An implausible one is a data error.
    birth = parse_span(row["a1_birth_date"])[0]
    if birth is not None and not (MIN_BIRTH_YEAR <= birth <= MAX_BIRTH_YEAR):
        errors.append("a1_birth_date must be a year in [%d, %d], got %r"
                      % (MIN_BIRTH_YEAR, MAX_BIRTH_YEAR,
                         row["a1_birth_date"]))
```

Replace the hit resolution and ordering check. Ordering compares against the **low** end of the hit span, so a violation is flagged only when it is unambiguous:

```python
    hit = parse_span(row["a5_first_hit_date"])[0]
    if hit is None:
        if excluded != "true":
            errors.append("a5_first_hit unknown requires excluded=true")
        if not row["exclusion_reason"].strip():
            errors.append(
                "a5_first_hit unknown requires a non-empty exclusion_reason")
    else:
        criterion = row["hit_criterion"].strip()
        allowed = allowed_criteria(bucket)
        if criterion not in allowed:
            errors.append("hit_criterion %r not allowed for bucket %s "
                          "(allowed: %s)"
                          % (criterion, bucket, sorted(allowed)))
        elif row["hit_basis"].strip() != CRITERION_BASIS[criterion]:
            errors.append("hit_basis for %s must be %s, got %r"
                          % (criterion, CRITERION_BASIS[criterion],
                             row["hit_basis"]))

        for earlier in ("a2_education_end", "a4_first_venture"):
            value = parse_span(row[earlier + "_date"])[0]
            if value is not None and value > hit:
                errors.append("%s (%d) is after a5_first_hit (%d)"
                              % (earlier, value, hit))
```

- [ ] **Step 6: Run tests to verify they pass**

Run: `python3 -m unittest tests.test_schema -v`
Expected: PASS. Report the real count; the additions above are 15 new tests against a prior 24.

- [ ] **Step 7: Commit**

```bash
git add src/schema.py tests/test_schema.py
git commit -m "Accept bounded anchor dates and the rank1 criterion"
```

---

### Task 4: Resolve spans in the clocks

**Files:**
- Modify: `src/clocks.py`
- Test: `tests/test_clocks.py`

**Interfaces:**
- Consumes: `schema.parse_span`
- Produces: `CLOCK_COLUMNS` gains four columns, in this order after `age_at_first_hit`: `clock_education_min`, `clock_education_max`, `bounded`, `conf_min`
  - `clock_education` becomes the **midpoint** value and may be a float ending in `.5`
  - `clock_education_min` / `clock_education_max` — the envelope from the span endpoints
  - `bounded` — `"true"` when any anchor feeding `clock_education` is a real span, else `"false"`
  - `conf_min` — the weakest confidence among the anchors feeding `clock_education` (`a2_education_end`, `a5_first_hit`), ordered `high` > `medium` > `low` > `none`
  - `midpoint(span)` -> float or None
  - `weakest_conf(*confs)` -> str

`conf_min` exists so spec §8's `conf = high` sensitivity run becomes computable. `clocks.csv` currently drops confidence entirely, which is why that run was never implemented.

- [ ] **Step 1: Write the failing tests**

Add to `tests/test_clocks.py`:

```python
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
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `python3 -m unittest tests.test_clocks -v`
Expected: FAIL — `midpoint`, `weakest_conf`, and the four new columns do not exist.

- [ ] **Step 3: Extend `CLOCK_COLUMNS` and add the helpers**

In `src/clocks.py`, extend the column list and add two helpers above `compute_clocks`:

```python
CLOCK_COLUMNS = [
    "person_id",
    "bucket",
    "hit_basis",
    "country_primary",
    "gender",
    "era",
    "clock_education",
    "clock_age18",
    "clock_venture",
    "age_at_first_hit",
    "clock_education_min",
    "clock_education_max",
    "bounded",
    "conf_min",
]

CONF_ORDER = ["none", "low", "medium", "high"]


def midpoint(span):
    """Centre of an anchor span, or None when the anchor is unknown."""
    lo, hi = span
    if lo is None:
        return None
    return (lo + hi) / 2.0


def weakest_conf(*confs):
    """The least confident of several anchor confidences."""
    return min(confs, key=lambda c: CONF_ORDER.index(c)
               if c in CONF_ORDER else 0)
```

- [ ] **Step 4: Rewrite `compute_clocks`**

```python
def compute_clocks(row):
    """Derive every clock for one anchors.csv row.

    A bounded anchor contributes its midpoint to the headline clock and its
    endpoints to the envelope, so the uncertainty stays visible downstream
    rather than being flattened into a false point estimate.
    """
    hit = schema.parse_span(row["a5_first_hit_date"])
    birth = schema.parse_span(row["a1_birth_date"])
    education = schema.parse_span(row["a2_education_end_date"])
    venture = schema.parse_span(row["a4_first_venture_date"])

    hit_mid = midpoint(hit)
    birth_mid = midpoint(birth)
    education_mid = midpoint(education)

    bounded = any(span[0] is not None and span[0] != span[1]
                  for span in (hit, education))

    return {
        "person_id": row["person_id"],
        "bucket": row["bucket"],
        "hit_basis": row["hit_basis"],
        "country_primary": row["country_primary"],
        "gender": row["gender"],
        "era": era_of(hit[0]),
        "clock_education": _gap(hit_mid, education_mid),
        "clock_age18": _gap(hit_mid,
                            birth_mid + 18 if birth_mid is not None else None),
        "clock_venture": _gap(hit_mid, midpoint(venture)),
        "age_at_first_hit": _gap(hit_mid, birth_mid),
        "clock_education_min": _gap(hit[0], education[1]),
        "clock_education_max": _gap(hit[1], education[0]),
        "bounded": "true" if bounded else "false",
        "conf_min": weakest_conf(row["a2_education_end_conf"].strip(),
                                 row["a5_first_hit_conf"].strip()),
    }
```

Note the envelope: the **minimum** elapsed time pairs the earliest possible hit with the latest possible education end, and the maximum pairs the latest hit with the earliest education end.

- [ ] **Step 5: Update `load_clocks` for the new columns**

The numeric tuple must include the envelope columns, and they may now hold floats:

```python
def load_clocks(path):
    """Read clocks.csv back, restoring None for empty cells."""
    numeric = ("clock_education", "clock_age18", "clock_venture",
               "age_at_first_hit", "clock_education_min",
               "clock_education_max")
    rows = []
    with open(path, newline="", encoding="utf-8") as handle:
        for row in csv.DictReader(handle):
            for key in numeric:
                row[key] = float(row[key]) if row[key].strip() else None
            rows.append(row)
    return rows
```

- [ ] **Step 6: Run tests to verify they pass**

Run: `python3 -m unittest tests.test_clocks -v`

Two existing tests assert integer clock values (`test_bezos_shaped_row`, `test_roundtrip`). `11 == 11.0` is `True` in Python, so equality assertions still pass; a `assertEqual(out[0]["clock_education"], "11")` string comparison in `test_roundtrip` will **not**, because the written cell is now `11.0`. Update that assertion to `"11.0"` and note the change in your report. Do not weaken any other assertion.

Report the real count.

- [ ] **Step 7: Run the full suite**

Run: `python3 -m unittest discover -s tests -t . -v`
Report the real count.

- [ ] **Step 8: Commit**

```bash
git add src/clocks.py tests/test_clocks.py
git commit -m "Resolve bounded anchors to a midpoint and an envelope"
```

---

### Task 5: The two missing sensitivity runs

**Files:**
- Modify: `src/report.py`
- Test: `tests/test_report.py`

**Interfaces:**
- Consumes: `clocks.load_clocks` rows now carrying `bounded` and `conf_min`
- Produces:
  - `confidence_runs(clock_rows, clock="clock_education")` -> dict with keys `high_only` and `all_rows`, each a `summarise` dict
  - `bounded_runs(clock_rows)` -> dict with keys `unbounded_only`, `midpoint_all`, `envelope_min`, `envelope_max`
  - `build_report` gains two sections

Spec §8 has required the confidence run since the original design; it was never implementable because `clocks.csv` carried no confidence. It is not decorative — the pilot came in at 35% of anchors below `high`.

- [ ] **Step 1: Write the failing tests**

The existing `clock_row` helper in `tests/test_report.py` must grow the new keys. Replace it with:

```python
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
```

Then add:

```python
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
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `python3 -m unittest tests.test_report -v`
Expected: FAIL — `confidence_runs` and `bounded_runs` do not exist.

- [ ] **Step 3: Add the two run functions**

In `src/report.py`, after `strictness_runs`:

```python
def confidence_runs(clock_rows, clock=PRIMARY_CLOCK):
    """Spec 8's sensitivity run: high-confidence rows against all rows.

    Where these diverge, the dataset is soft enough that the headline should
    not be read as a point estimate.
    """
    high = [r for r in clock_rows if r["conf_min"] == "high"]
    return {
        "high_only": summarise(_values(high, clock)),
        "all_rows": summarise(_values(clock_rows, clock)),
    }


def bounded_runs(clock_rows):
    """How much the answer depends on rows whose hit year is a range.

    Only the primary clock carries an envelope, so this takes no clock
    argument — a parameter that accepted one value would be a lie.
    """
    unbounded = [r for r in clock_rows if r["bounded"] != "true"]
    return {
        "unbounded_only": summarise(_values(unbounded, PRIMARY_CLOCK)),
        "midpoint_all": summarise(_values(clock_rows, PRIMARY_CLOCK)),
        "envelope_min": summarise(_values(clock_rows, "clock_education_min")),
        "envelope_max": summarise(_values(clock_rows, "clock_education_max")),
    }
```

- [ ] **Step 4: Add both sections to `build_report`**

Insert immediately after the definition-strictness block, before the `## All clocks, pooled` section:

```python
    conf = confidence_runs(clock_rows)
    lines.append("## Confidence sensitivity (primary clock)")
    lines.append("")
    lines.append("| Rows | Median |")
    lines.append("|---|---|")
    lines.append("| high-confidence rows only | %s |" % _fmt(conf["high_only"]))
    lines.append("| all included rows | %s |" % _fmt(conf["all_rows"]))
    lines.append("")
    high_med = conf["high_only"]["median"]
    all_med = conf["all_rows"]["median"]
    if high_med is not None and all_med is not None:
        if abs(high_med - all_med) >= 1.0:
            lines.append("**These diverge by %.1f years.** The dataset is too "
                         "soft to read the headline as a point estimate."
                         % abs(high_med - all_med))
        else:
            lines.append("These agree within %.1f years."
                         % abs(high_med - all_med))
        lines.append("")

    env = bounded_runs(clock_rows)
    lines.append("## Bounded-date sensitivity (primary clock)")
    lines.append("")
    lines.append("| Treatment | Median |")
    lines.append("|---|---|")
    lines.append("| bounded rows dropped | %s |"
                 % _fmt(env["unbounded_only"]))
    lines.append("| all rows, span midpoints | %s |"
                 % _fmt(env["midpoint_all"]))
    lines.append("| all rows, earliest possible | %s |"
                 % _fmt(env["envelope_min"]))
    lines.append("| all rows, latest possible | %s |"
                 % _fmt(env["envelope_max"]))
    lines.append("")
    lines.append("A bounded date records that sources bracket an event without "
                 "pinning it. The envelope rows show the full range the data "
                 "permits; the midpoint row is what the headline uses.")
    lines.append("")
```

- [ ] **Step 5: Run tests to verify they pass**

Run: `python3 -m unittest tests.test_report -v`
Report the real count.

- [ ] **Step 6: Run the full suite**

Run: `python3 -m unittest discover -s tests -t . -v`
Report the real count.

- [ ] **Step 7: Commit**

```bash
git add src/report.py tests/test_report.py
git commit -m "Add the confidence and bounded-date sensitivity runs"
```

---

### Task 6: Re-code the pilot and re-review

**Files:**
- Modify: `data/anchors.csv`
- Regenerate: `analysis/clocks.csv`, `analysis/analysis.md`
- Create: `docs/PILOT-REVIEW-2.md`

**Interfaces:**
- Consumes: every module above
- Produces: the second pilot verdict, which is a human review gate

**This task is research.** It re-codes the existing ten people under the revised rules. It does **not** add new people.

- [ ] **Step 1: Re-code the four defective rows**

Read `docs/PILOT-REVIEW.md` first. Four rows need new `a5_first_hit` values under the revised frame:

- **p04 Gordon Moore** — Fairchild Semiconductor's revenue history. Find sources bracketing the year it passed the constant-dollar threshold (run `python3 -m src.cpi 1960` for the nominal figure). Record a bounded `rev10` date with basis `primary` if the bound holds, or `excluded = true` with reason `crossing_undatable` if it cannot be bounded within 10 years. **Do not leave the 1971 Intel IPO in place.**
- **p03 Tadashi Yanai** — same treatment for Fast Retailing / Uniqlo, converting yen at the spot rate for the revenue year.
- **p10 Zhang Yin** — same treatment for Nine Dragons Paper, converting RMB.
- **p08 Robin Li** — Baidu's F-1 bounds the crossing to 2003 or 2004. Record `a5_first_hit = 2003-2004`, `rev10`, basis `primary`, confidence `medium`, sourced to the F-1. This row is currently excluded; it should now carry data. If SEC EDGAR is still unreachable, cite a secondary source that quotes the same audited figures and mark confidence `medium`.

Two further rows change under the revised conventions:

- **p02 Katalin Karikó** — confirm the `prize` anchor is the Breakthrough Prize **announcement** year, 2021, not the official 2022 designation.
- **p06 Mary Meeker** — re-code from `fund100` to `rank1`: the first year she topped a recognized industry ranking, such as the Institutional Investor All-America Research Team. If no such ranking year can be sourced, record `unknown` and exclude the row rather than falling back to a fund date.

The same sourcing rules apply as in the first pilot: two genuine attempts per anchor, then `unknown`. **Never infer a year.** A bounded date needs a source for the bound, not a guess at the range.

- [ ] **Step 2: Validate**

Run: `python3 -m src.schema data/anchors.csv`
Expected: `10 rows checked, 0 errors`

Fix the data, never the validator. Do not edit anything in `src/`.

- [ ] **Step 3: Regenerate the analysis**

```bash
python3 -m src.clocks data/anchors.csv analysis/clocks.csv
python3 -m src.report analysis/clocks.csv analysis/analysis.md
```

Both must succeed. Confirm `analysis/analysis.md` now contains the confidence and bounded-date sections, and that every slice is still flagged too small to read at n=10.

- [ ] **Step 4: Commit the data before writing the review**

```bash
git add data/anchors.csv analysis/clocks.csv analysis/analysis.md
git commit -m "Re-code pilot rows under the revised frame"
```

- [ ] **Step 5: Write `docs/PILOT-REVIEW-2.md`**

Answer these, citing specific rows:

1. **Did the fallback-lag defect close?** Give Moore's `clock_education` before and after. State whether any row still records a hit date known to be later than the real crossing.
2. **What is the `primary` share now?** The first pilot was 20% against a spec forecast of ~50%. Report the new figure and what it implies for total N, given the stopping rule tracks the revenue-strict subset.
3. **What is the unknown rate now**, and did bounded dates reduce it?
4. **Do the confidence and bounded-date sensitivity runs disagree with the headline?** Quote the numbers from `analysis/analysis.md`.
5. **Did any new defect appear** that the revised rules introduced?
6. **Verdict:** proceed to wave 1, or revise again.

Be blunt. A second "revise again" is a valid and useful answer.

- [ ] **Step 6: Commit**

```bash
git add docs/PILOT-REVIEW-2.md
git commit -m "Add second pilot review under the revised frame"
```

**STOP HERE.** The verdict is a human review gate. Do not begin wave 1 until the spec author has read `docs/PILOT-REVIEW-2.md`.

---

## Coverage

| Pilot finding | Task |
|---|---|
| Defect A — fallback lags the true hit | 1 (rule), 3 (bounded dates), 6 (re-code) |
| Defect B — `prize` announcement-year convention | 1 |
| Defect B — `fund100` mis-dates analysts | 1 (rule), 3 (`rank1`), 6 (Meeker) |
| Defect B — no currency rule | 1 |
| Nominal threshold is an era bias | 1, 2 |
| p08 bounded date unrepresentable | 3, 4, 6 |
| Spec §8 confidence run unimplemented | 4 (`conf_min`), 5 |
| Selection into `primary` is non-random | 1 (spec §10.7) |
| `a3` has no "never happened" state | 1 (spec §10.8), not fixed in code |

Two pilot recommendations are deliberately **not** implemented: rule R1 for `a3_first_domain_job`, and a fourth `na` confidence state. `a3` feeds no clock, so neither affects a median. They are recorded in spec §10.8 and can be taken up if the second pilot shows the unknown rate is being distorted by the conflation.
