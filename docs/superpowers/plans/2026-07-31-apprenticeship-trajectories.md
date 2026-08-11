# Apprenticeship Trajectories Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build the tooling and frozen sampling frame needed to collect dated career anchors for an open-ended sample of outlier achievers, then compute the median years from career start to first meaningful hit with an honest error bar.

**Architecture:** Five small stdlib-only Python modules under `src/`, each with one responsibility: column spec and row validation, wave allocation, clock computation, bootstrap statistics and the stopping rule, and report generation. Data lives in CSVs that agents write during research waves; the modules validate and analyse those CSVs. No database, no web framework, no third-party dependencies.

**Tech Stack:** Python 3.9.6 (system python3), stdlib only — `csv`, `statistics`, `random`, `unittest`. No pandas, no pytest, no pip installs.

## Global Constraints

- **Python 3.9.6.** No `match` statements, no PEP 604 `int | None` annotations, no `dict[str, int]` subscripting at runtime. Use `typing` imports or omit annotations.
- **Stdlib only.** Do not add dependencies. `pandas` and `pytest` are not installed and must not be installed.
- **Tests use `unittest`.** Run from repo root: `python3 -m unittest discover -s tests -t . -v`
- **Repo root is `~/trajectories`.** All paths below are relative to it.
- **Year precision throughout.** Dates are 4-digit year strings. The literal string `unknown` marks an absent anchor.
- **Anchors are never inferred.** An unfindable anchor is `unknown` with `_conf = none`. This is the core invariant the validator enforces.
- **Bucket names are the canonical snake_case keys** defined in Task 2 and used verbatim everywhere: `software_internet`, `hardware_deeptech`, `consumer_retail_industrial`, `science_research`, `investors_finance`, `media_creators`, `healthcare_biotech`, `trade_import_logistics`.
- **Hit criterion codes:** `rev10`, `ipo`, `acq50`, `prize`, `aud1m`, `fund100`.
- **Hit basis values:** `primary`, `fallback`, `equivalent`.
- **Confidence values:** `high`, `medium`, `low`, `none`.
- **Stopping rule constants:** N floor 30, max drift 0.5 years across two consecutive wave deltas, max bootstrap CI half-width 1.0 year, wave size 25, audit fraction 0.15, audit void threshold 0.10.

---

## File Structure

```
~/trajectories/
  frame.md                    frozen sampling frame (Task 1)
  README.md                   how to run everything (Task 1)
  src/
    __init__.py
    schema.py                 column spec + row validation (Task 2)
    allocate.py               largest-remainder wave allocation (Task 3)
    clocks.py                 anchors -> clocks, CSV IO (Task 4)
    stats.py                  bootstrap median CI + stopping rule + audit (Task 5)
    report.py                 analysis.md generation (Task 6)
  tests/
    __init__.py
    test_schema.py
    test_allocate.py
    test_clocks.py
    test_stats.py
    test_report.py
  data/
    roster.csv                names + bucket + source (Task 7)
    anchors.csv               the research output (Task 7 pilot, Task 8 waves)
    audit.csv                 blind second-pass results (Task 8)
  analysis/
    clocks.csv                computed per-person clocks
    analysis.md               the report
  docs/superpowers/
    specs/2026-07-31-apprenticeship-trajectories-design.md
    plans/2026-07-31-apprenticeship-trajectories.md
    RUNBOOK.md                wave execution procedure (Task 8)
```

---

### Task 1: Repo scaffolding and the frozen frame

**Files:**
- Create: `frame.md`
- Create: `README.md`
- Create: `.gitignore`
- Create: `src/__init__.py`

**Interfaces:**
- Consumes: nothing
- Produces: `frame.md`, the frozen sampling frame that Task 3's allocator and Task 7's roster both read percentages from. No code interface.

- [ ] **Step 1: Create `.gitignore`**

```
__pycache__/
*.pyc
.DS_Store
```

- [ ] **Step 2: Create the package markers**

Both files are empty. `src/__init__.py` makes `from src.schema import ...` resolve when tests run with `-t .` from the repo root; `tests/__init__.py` makes `from tests.test_schema import valid_row` resolve, which Task 4's tests rely on to reuse the row fixture.

```bash
mkdir -p src tests
touch src/__init__.py tests/__init__.py
```

- [ ] **Step 3: Create `frame.md`**

```markdown
# Sampling Frame — FROZEN

Frozen 2026-07-31. Do not edit after wave 1 begins. Changing the frame
mid-collection invalidates the stopping rule, because the sample composition
would no longer be stable across waves.

## Field quotas

| Bucket key | Label | Share |
|---|---|---|
| `software_internet` | Software & internet | 25% |
| `hardware_deeptech` | Hardware & deep tech | 15% |
| `consumer_retail_industrial` | Consumer, retail & industrial | 13% |
| `science_research` | Science & research | 12% |
| `investors_finance` | Investors & finance | 10% |
| `media_creators` | Media & creators | 10% |
| `healthcare_biotech` | Healthcare & biotech | 10% |
| `trade_import_logistics` | Trade, import & logistics | 5% |

Total: 100%.

## Enforced cross-cuts

Floors, checked against the cumulative sample after every wave. A wave that
would push any floor below its threshold is rebalanced before research begins.

- Non-US primary career: >= 30%
- First hit before 1995: >= 25%
- Women: >= 20%

## Named source lists

Every roster entry cites the list it came from. No name enters by free recall.

- Forbes 400 (self-made score 6-10)
- Forbes World's Billionaires (self-made)
- Midas List; Midas List Europe
- Fortune 40 Under 40
- Nobel Prizes (Physics, Chemistry, Medicine, Economics)
- Turing Award
- Fields Medal
- Breakthrough Prize
- Time 100
- Y Combinator Top Companies
- Hurun Rich List (China, India)
- Nikkei / Toyo Keizai rankings (Japan)
- Maeil Business / Chosun Ilbo rankings (Korea)
- Sunday Times Rich List (UK)
- Pulitzer Prize, Academy Awards, Grammy Awards
- Endeavor Entrepreneur network (emerging markets)

## Hit criteria

Commercial buckets (`software_internet`, `hardware_deeptech`,
`consumer_retail_industrial`, `healthcare_biotech`, `trade_import_logistics`):

1. `rev10` — first year the person's own venture reached $10M annual revenue. Basis `primary`.
2. Only if revenue is never publicly documented: `ipo` or `acq50` (acquisition above $50M), whichever is earlier. Basis `fallback`.

Non-commercial buckets:

- `science_research` -> `prize` (Nobel, Turing, Fields, Breakthrough). Basis `equivalent`.
- `media_creators` -> `aud1m` (1M+ audience for their own work). Basis `equivalent`.
- `investors_finance` -> `fund100` (first fund closed above $100M). Basis `equivalent`.
```

- [ ] **Step 4: Create `README.md`**

```markdown
# Apprenticeship Trajectories

Measures years from career start to first meaningful hit across a
quota-balanced sample of outlier achievers.

Read `docs/superpowers/specs/2026-07-31-apprenticeship-trajectories-design.md`
first. `frame.md` is frozen and must not be edited after wave 1.

## Run the tests

    python3 -m unittest discover -s tests -t . -v

## Validate the collected data

    python3 -m src.schema data/anchors.csv

## Compute clocks and build the report

    python3 -m src.clocks data/anchors.csv analysis/clocks.csv
    python3 -m src.report data/anchors.csv analysis/clocks.csv analysis/analysis.md

## Check the stopping rule

    python3 -m src.stats analysis/clocks.csv

No dependencies. Python 3.9 stdlib only.
```

- [ ] **Step 5: Commit**

```bash
git add .gitignore README.md frame.md src/__init__.py tests/__init__.py
git commit -m "Add frozen sampling frame and repo scaffolding"
```

---

### Task 2: Row schema and validation

**Files:**
- Create: `src/schema.py`
- Test: `tests/test_schema.py`

**Interfaces:**
- Consumes: nothing
- Produces:
  - `BUCKET_SHARES` — dict of bucket key -> int percentage
  - `COMMERCIAL_BUCKETS` — set of bucket keys
  - `CRITERION_BASIS` — dict criterion code -> basis string
  - `ANCHORS` — list of the six anchor prefixes
  - `columns()` -> list of str, the full ordered CSV header
  - `parse_year(value)` -> int or None
  - `validate_row(row)` -> list of str error messages, empty when valid
  - `load_rows(path)` -> list of dict

- [ ] **Step 1: Write the failing test**

Create `tests/test_schema.py`:

```python
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


if __name__ == "__main__":
    unittest.main()
```

- [ ] **Step 2: Run test to verify it fails**

Run: `python3 -m unittest tests.test_schema -v`
Expected: FAIL with `ModuleNotFoundError: No module named 'src.schema'`

- [ ] **Step 3: Write the implementation**

Create `src/schema.py`:

```python
"""Column specification and row validation for data/anchors.csv.

The central invariant: an anchor is either a sourced 4-digit year, or the
literal string 'unknown' with confidence 'none' and no source. There is no
third state. A plausible-looking guessed date is the failure mode this whole
project exists to prevent, because it is invisible in the output and moves
the median.
"""

import csv
import re
import sys

BUCKET_SHARES = {
    "software_internet": 25,
    "hardware_deeptech": 15,
    "consumer_retail_industrial": 13,
    "science_research": 12,
    "investors_finance": 10,
    "media_creators": 10,
    "healthcare_biotech": 10,
    "trade_import_logistics": 5,
}

COMMERCIAL_BUCKETS = {
    "software_internet",
    "hardware_deeptech",
    "consumer_retail_industrial",
    "healthcare_biotech",
    "trade_import_logistics",
}

COMMERCIAL_CRITERIA = {"rev10", "ipo", "acq50"}

BUCKET_CRITERIA = {
    "science_research": {"prize"},
    "media_creators": {"aud1m"},
    "investors_finance": {"fund100"},
}

CRITERION_BASIS = {
    "rev10": "primary",
    "ipo": "fallback",
    "acq50": "fallback",
    "prize": "equivalent",
    "aud1m": "equivalent",
    "fund100": "equivalent",
}

ANCHORS = [
    "a1_birth",
    "a2_education_end",
    "a3_first_domain_job",
    "a4_first_venture",
    "a5_first_hit",
    "a6_scale_hit",
]

IDENTITY = [
    "person_id",
    "name",
    "bucket",
    "source_list",
    "country_primary",
    "gender",
]

TRAILING = [
    "hit_entity",
    "hit_criterion",
    "hit_basis",
    "excluded",
    "exclusion_reason",
    "notes",
]

CONFIDENCE = {"high", "medium", "low", "none"}

# A source must look like a real URL: scheme, ://, and a dotted host. The
# permissive check this replaces accepted the bare string "http", which
# would let an uncited anchor pass as fully sourced.
URL_PATTERN = re.compile(r"^https?://[^\s/]+\.[^\s]")

MIN_BIRTH_YEAR = 1850
MAX_BIRTH_YEAR = 2010


def columns():
    """Full ordered CSV header."""
    cols = list(IDENTITY)
    for anchor in ANCHORS:
        cols.extend([anchor + "_date", anchor + "_src", anchor + "_conf"])
    cols.extend(TRAILING)
    return cols


def parse_year(value):
    """Return an int year, or None for 'unknown', blank, or malformed input."""
    text = (value or "").strip()
    if len(text) == 4 and text.isdigit():
        return int(text)
    return None


def allowed_criteria(bucket):
    """Criterion codes permitted for a bucket."""
    if bucket in COMMERCIAL_BUCKETS:
        return COMMERCIAL_CRITERIA
    return BUCKET_CRITERIA.get(bucket, set())


def validate_row(row):
    """Return a list of human-readable error strings. Empty means valid."""
    missing = [c for c in columns() if c not in row]
    if missing:
        return ["missing columns: " + ", ".join(missing)]

    errors = []
    bucket = row["bucket"].strip()
    if bucket not in BUCKET_SHARES:
        errors.append("unknown bucket: %r" % bucket)

    for anchor in ANCHORS:
        date = row[anchor + "_date"].strip()
        src = row[anchor + "_src"].strip()
        conf = row[anchor + "_conf"].strip()

        if conf not in CONFIDENCE:
            errors.append("%s_conf must be one of %s, got %r"
                          % (anchor, sorted(CONFIDENCE), conf))
            continue

        if conf == "none":
            if date != "unknown":
                errors.append("%s_conf=none requires %s_date='unknown', got %r"
                              % (anchor, anchor, date))
            if src:
                errors.append("%s_conf=none requires an empty %s_src"
                              % (anchor, anchor))
        else:
            if parse_year(date) is None:
                errors.append("%s_date must be a 4-digit year, got %r"
                              % (anchor, date))
            if not URL_PATTERN.match(src):
                errors.append("%s_src must be a URL when %s_conf=%s, got %r"
                              % (anchor, anchor, conf, src))

    # An unknown birth year is permitted — it costs the two clocks that need
    # it, not the whole row. An implausible one is a data error.
    birth = parse_year(row["a1_birth_date"])
    if birth is not None and not (MIN_BIRTH_YEAR <= birth <= MAX_BIRTH_YEAR):
        errors.append("a1_birth_date must be a year in [%d, %d], got %r"
                      % (MIN_BIRTH_YEAR, MAX_BIRTH_YEAR,
                         row["a1_birth_date"]))

    excluded = row["excluded"].strip().lower()
    if excluded not in ("true", "false"):
        errors.append("excluded must be 'true' or 'false', got %r"
                      % row["excluded"])

    hit = parse_year(row["a5_first_hit_date"])
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
            value = parse_year(row[earlier + "_date"])
            if value is not None and value > hit:
                errors.append("%s (%d) is after a5_first_hit (%d)"
                              % (earlier, value, hit))

    return errors


def load_rows(path):
    """Read anchors.csv into a list of dicts."""
    with open(path, newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def main(argv):
    """Validate a CSV and print every error, one per line."""
    if len(argv) != 2:
        print("usage: python3 -m src.schema <anchors.csv>")
        return 2
    rows = load_rows(argv[1])
    total = 0
    for index, row in enumerate(rows, start=2):  # line 1 is the header
        for error in validate_row(row):
            print("line %d (%s): %s"
                  % (index, row.get("person_id", "?"), error))
            total += 1
    print("%d rows checked, %d errors" % (len(rows), total))
    return 1 if total else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `python3 -m unittest tests.test_schema -v`
Expected: PASS, 24 tests

- [ ] **Step 5: Commit**

```bash
git add src/schema.py tests/test_schema.py
git commit -m "Add row schema and cite-or-flag validation"
```

---

### Task 3: Wave allocation

**Files:**
- Create: `src/allocate.py`
- Test: `tests/test_allocate.py`

**Interfaces:**
- Consumes: `src.schema.BUCKET_SHARES`
- Produces:
  - `apportion(total, shares)` -> dict bucket -> int, summing to `total`
  - `allocate_wave(cumulative, wave_size, shares=None)` -> dict bucket -> int, summing to `wave_size`

- [ ] **Step 1: Write the failing test**

Create `tests/test_allocate.py`:

```python
import unittest

from src import allocate
from src import schema


class TestApportion(unittest.TestCase):
    def test_sums_to_total(self):
        result = allocate.apportion(25, schema.BUCKET_SHARES)
        self.assertEqual(sum(result.values()), 25)

    def test_exact_at_100(self):
        result = allocate.apportion(100, schema.BUCKET_SHARES)
        self.assertEqual(result["software_internet"], 25)
        self.assertEqual(result["trade_import_logistics"], 5)

    def test_zero_total(self):
        result = allocate.apportion(0, schema.BUCKET_SHARES)
        self.assertEqual(sum(result.values()), 0)

    def test_largest_remainder_favours_biggest_share(self):
        # 10 items across the frame: software (25%) must get the most.
        result = allocate.apportion(10, schema.BUCKET_SHARES)
        self.assertEqual(sum(result.values()), 10)
        self.assertEqual(max(result, key=lambda b: result[b]),
                         "software_internet")


class TestAllocateWave(unittest.TestCase):
    def test_first_wave_sums_to_wave_size(self):
        wave = allocate.allocate_wave({}, 25)
        self.assertEqual(sum(wave.values()), 25)

    def test_never_negative(self):
        skewed = {"software_internet": 40}
        wave = allocate.allocate_wave(skewed, 25)
        self.assertTrue(all(count >= 0 for count in wave.values()))
        self.assertEqual(sum(wave.values()), 25)

    def test_corrects_an_over_represented_bucket(self):
        # Software is wildly over-quota, so the next wave should add few or
        # none of it and backfill the starved buckets instead.
        skewed = {"software_internet": 40, "science_research": 0}
        wave = allocate.allocate_wave(skewed, 25)
        self.assertEqual(wave["software_internet"], 0)
        self.assertGreater(wave["science_research"], 0)

    def test_composition_tracks_frame_across_many_waves(self):
        cumulative = {}
        for _ in range(8):
            wave = allocate.allocate_wave(cumulative, 25)
            for bucket, count in wave.items():
                cumulative[bucket] = cumulative.get(bucket, 0) + count
        total = sum(cumulative.values())
        self.assertEqual(total, 200)
        # Every bucket within 1 person of its exact quota after 200.
        for bucket, share in schema.BUCKET_SHARES.items():
            expected = total * share / 100.0
            self.assertLessEqual(abs(cumulative[bucket] - expected), 1.0,
                                 "%s drifted: %d vs %.1f"
                                 % (bucket, cumulative[bucket], expected))


if __name__ == "__main__":
    unittest.main()
```

- [ ] **Step 2: Run test to verify it fails**

Run: `python3 -m unittest tests.test_allocate -v`
Expected: FAIL with `ModuleNotFoundError: No module named 'src.allocate'`

- [ ] **Step 3: Write the implementation**

Create `src/allocate.py`:

```python
"""Wave composition.

Growing the sample by whichever names are easiest to research next causes
composition drift toward well-documented US software figures as N rises,
which would make a 'stabilising' median partly an artifact of the sample
changing shape. Each wave is therefore apportioned so that cumulative
composition tracks the frozen frame at every N.
"""

import sys

from src import schema


def apportion(total, shares):
    """Largest-remainder apportionment of `total` across percentage `shares`."""
    exact = {b: total * shares[b] / 100.0 for b in shares}
    base = {b: int(exact[b]) for b in shares}
    remainder = total - sum(base.values())
    # Biggest fractional part wins; ties broken by bucket name for determinism.
    order = sorted(shares, key=lambda b: (-(exact[b] - base[b]), b))
    for bucket in order[:remainder]:
        base[bucket] += 1
    return base


def allocate_wave(cumulative, wave_size, shares=None):
    """Return {bucket: count} for the next wave of `wave_size` people."""
    if shares is None:
        shares = schema.BUCKET_SHARES

    total_after = sum(cumulative.get(b, 0) for b in shares) + wave_size
    ideal = apportion(total_after, shares)
    wave = {b: max(0, ideal[b] - cumulative.get(b, 0)) for b in shares}

    def deviation(bucket):
        """How far this bucket sits above its exact quota, if we ship as-is."""
        got = cumulative.get(bucket, 0) + wave[bucket]
        return got - total_after * shares[bucket] / 100.0

    # Clamping at zero can leave the wave over- or under-sized. Trim from the
    # most over-quota bucket, add to the most under-quota one, until exact.
    diff = sum(wave.values()) - wave_size
    while diff > 0:
        bucket = max((b for b in wave if wave[b] > 0), key=deviation)
        wave[bucket] -= 1
        diff -= 1
    while diff < 0:
        bucket = min(wave, key=deviation)
        wave[bucket] += 1
        diff += 1

    return wave


def main(argv):
    """Print the next wave's bucket allocation given cumulative counts."""
    if len(argv) < 2:
        print("usage: python3 -m src.allocate <wave_size> "
              "[bucket=count ...]")
        return 2
    wave_size = int(argv[1])
    cumulative = {}
    for pair in argv[2:]:
        bucket, count = pair.split("=")
        cumulative[bucket] = int(count)
    for bucket, count in sorted(allocate_wave(cumulative, wave_size).items()):
        print("%-30s %d" % (bucket, count))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `python3 -m unittest tests.test_allocate -v`
Expected: PASS, 8 tests

- [ ] **Step 5: Commit**

```bash
git add src/allocate.py tests/test_allocate.py
git commit -m "Add largest-remainder wave allocation"
```

---

### Task 4: Clock computation

**Files:**
- Create: `src/clocks.py`
- Test: `tests/test_clocks.py`

**Interfaces:**
- Consumes: `src.schema.parse_year`, `src.schema.load_rows`
- Produces:
  - `CLOCK_COLUMNS` — list of str, the clocks.csv header
  - `compute_clocks(row)` -> dict with keys `person_id`, `bucket`, `hit_basis`, `country_primary`, `gender`, `era`, `clock_education`, `clock_age18`, `clock_venture`, `age_at_first_hit`. Clock values are int or `None`.
  - `era_of(hit_year)` -> `"pre1995"`, `"post1995"`, or `""` when the hit year is unknown
  - `write_clocks(clock_rows, path)` -> None

- [ ] **Step 1: Write the failing test**

Create `tests/test_clocks.py`:

```python
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
                        "11,15,   ,33\n")
            loaded = clocks.load_clocks(path)
            self.assertIsNone(loaded[0]["clock_venture"])
            self.assertEqual(loaded[0]["clock_age18"], 15)
        finally:
            os.remove(path)


if __name__ == "__main__":
    unittest.main()
```

- [ ] **Step 2: Run test to verify it fails**

Run: `python3 -m unittest tests.test_clocks -v`
Expected: FAIL with `ModuleNotFoundError: No module named 'src.clocks'`

- [ ] **Step 3: Write the implementation**

Create `src/clocks.py`:

```python
"""Turn stored anchors into clocks.

Storing six anchors rather than one pre-computed clock is what makes the
definition of 'apprenticeship' revisable without re-researching anyone. Every
clock here is derived; none is collected.
"""

import csv
import sys

from src import schema

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
]

ERA_SPLIT = 1995


def era_of(hit_year):
    """Era label for slicing: 'pre1995', 'post1995', or '' when the hit
    year is unknown. The empty label is deliberate — such rows contribute
    to no median, and Task 6 renders the group as '(unknown)'."""
    if hit_year is None:
        return ""
    return "pre1995" if hit_year < ERA_SPLIT else "post1995"


def _gap(later, earlier):
    """Years between two anchors, or None when either is unknown."""
    if later is None or earlier is None:
        return None
    return later - earlier


def compute_clocks(row):
    """Derive every clock for one anchors.csv row."""
    hit = schema.parse_year(row["a5_first_hit_date"])
    birth = schema.parse_year(row["a1_birth_date"])
    education = schema.parse_year(row["a2_education_end_date"])
    venture = schema.parse_year(row["a4_first_venture_date"])

    return {
        "person_id": row["person_id"],
        "bucket": row["bucket"],
        "hit_basis": row["hit_basis"],
        "country_primary": row["country_primary"],
        "gender": row["gender"],
        "era": era_of(hit),
        "clock_education": _gap(hit, education),
        "clock_age18": _gap(hit, birth + 18 if birth is not None else None),
        "clock_venture": _gap(hit, venture),
        "age_at_first_hit": _gap(hit, birth),
    }


def write_clocks(clock_rows, path):
    """Write clocks.csv. None becomes an empty cell, never a zero."""
    with open(path, "w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=CLOCK_COLUMNS)
        writer.writeheader()
        for row in clock_rows:
            writer.writerow(
                {k: ("" if row[k] is None else row[k]) for k in CLOCK_COLUMNS})


def load_clocks(path):
    """Read clocks.csv back, restoring None for empty cells."""
    numeric = ("clock_education", "clock_age18", "clock_venture",
               "age_at_first_hit")
    rows = []
    with open(path, newline="", encoding="utf-8") as handle:
        for row in csv.DictReader(handle):
            for key in numeric:
                row[key] = int(row[key]) if row[key].strip() else None
            rows.append(row)
    return rows


def main(argv):
    if len(argv) != 3:
        print("usage: python3 -m src.clocks <anchors.csv> <clocks.csv>")
        return 2
    rows = schema.load_rows(argv[1])
    write_clocks([compute_clocks(r) for r in rows], argv[2])
    print("wrote %d rows to %s" % (len(rows), argv[2]))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `python3 -m unittest tests.test_clocks -v`
Expected: PASS, 12 tests

- [ ] **Step 5: Commit**

```bash
git add src/clocks.py tests/test_clocks.py
git commit -m "Add clock computation from stored anchors"
```

---

### Task 5: Bootstrap statistics, stopping rule, and audit

**Files:**
- Create: `src/stats.py`
- Test: `tests/test_stats.py`

**Interfaces:**
- Consumes: `src.clocks.load_clocks`
- Produces:
  - `bootstrap_median_ci(values, iters=10000, seed=0, level=0.95)` -> tuple `(lo, median, hi)` of floats
  - `half_width(lo, hi)` -> float
  - `check_stopping_rule(median_history, n, ci_half_width, ...)` -> dict with keys `stop` (bool) and `reason` (str)
  - `audit_sample(person_ids, fraction=0.15, seed=0)` -> sorted list of ids
  - `audit_disagreement(pairs)` -> float in [0, 1]
  - `revenue_strict_values(clock_rows, clock="clock_education")` -> list of int
  - `read_history(path)` -> list of float, oldest first
  - `append_history(path, median, n)` -> bool, True if appended
  - `read_audit_pairs(path)` -> list of `(first_pass, second_pass)` int/None pairs

- [ ] **Step 1: Write the failing test**

Create `tests/test_stats.py`:

```python
import os
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
        return [
            {"hit_basis": "primary", "clock_education": 11},
            {"hit_basis": "primary", "clock_education": 9},
            {"hit_basis": "fallback", "clock_education": 40},
            {"hit_basis": "equivalent", "clock_education": 50},
            {"hit_basis": "primary", "clock_education": None},
        ]

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
                 "clock_education": 11}]
        self.assertEqual(
            stats.revenue_strict_values(rows, clock="clock_venture"), [3])

    def test_empty_when_no_primary_rows(self):
        rows = [{"hit_basis": "fallback", "clock_education": 7}]
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
```

- [ ] **Step 2: Run test to verify it fails**

Run: `python3 -m unittest tests.test_stats -v`
Expected: FAIL with `ModuleNotFoundError: No module named 'src.stats'`

- [ ] **Step 3: Write the implementation**

Create `src/stats.py`:

```python
"""Bootstrap median CI, the pre-registered stopping rule, and the audit check.

The stopping rule is fixed in advance on purpose. Checking after every wave
and stopping the moment the number looks settled preferentially stops on
waves where noise happened to be small, which produces a median that appears
more precise than it is.
"""

import csv
import random
import statistics
import sys

from src import clocks

N_FLOOR = 30
MAX_DRIFT = 0.5
MAX_HALF_WIDTH = 1.0
WAVE_SIZE = 25
AUDIT_FRACTION = 0.15
AUDIT_VOID_THRESHOLD = 0.10


def bootstrap_median_ci(values, iters=10000, seed=0, level=0.95):
    """Return (lo, median, hi) for a percentile bootstrap of the median."""
    if len(values) < 2:
        raise ValueError("need at least 2 values, got %d" % len(values))
    rng = random.Random(seed)
    n = len(values)
    medians = sorted(
        statistics.median(rng.choices(values, k=n)) for _ in range(iters))
    lo_index = int((1.0 - level) / 2.0 * iters)
    hi_index = min(iters - 1, int((1.0 + level) / 2.0 * iters))
    return (medians[lo_index], statistics.median(values), medians[hi_index])


def half_width(lo, hi):
    """Half the width of a confidence interval."""
    return (hi - lo) / 2.0


def check_stopping_rule(median_history, n, ci_half_width,
                        n_floor=N_FLOOR, max_drift=MAX_DRIFT,
                        max_half_width=MAX_HALF_WIDTH):
    """Evaluate the pre-registered stopping rule.

    `median_history` is the revenue-strict median after each wave, oldest
    first, including the current wave. Two consecutive deltas must both be
    under `max_drift`, so three medians are the minimum.
    """
    if n < n_floor:
        return {"stop": False,
                "reason": "below N floor (%d < %d); median not examined"
                          % (n, n_floor)}

    if len(median_history) < 3:
        return {"stop": False,
                "reason": "need three wave medians for two consecutive "
                          "deltas, have %d" % len(median_history)}

    last = abs(median_history[-1] - median_history[-2])
    previous = abs(median_history[-2] - median_history[-3])
    if last >= max_drift or previous >= max_drift:
        return {"stop": False,
                "reason": "median drift too large (%.2f, %.2f yr; need both "
                          "< %.2f)" % (previous, last, max_drift)}

    if ci_half_width > max_half_width:
        return {"stop": False,
                "reason": "CI half-width %.2f yr exceeds %.2f yr"
                          % (ci_half_width, max_half_width)}

    return {"stop": True,
            "reason": "median stable (%.2f, %.2f yr drift) and CI half-width "
                      "%.2f yr at n=%d" % (previous, last, ci_half_width, n)}


def audit_sample(person_ids, fraction=AUDIT_FRACTION, seed=0):
    """Pick the wave rows to re-research blind. At least one, always."""
    ordered = sorted(person_ids)
    if not ordered:
        return []
    k = max(1, int(round(len(ordered) * fraction)))
    return sorted(random.Random(seed).sample(ordered, k))


def audit_disagreement(pairs):
    """Fraction of audited rows where the two passes disagree.

    `pairs` is [(first_pass_year, second_pass_year)], either may be None.
    Disagreement means more than one year apart, or one pass finding a date
    where the other found nothing.
    """
    if not pairs:
        return 0.0
    bad = 0
    for first, second in pairs:
        if first is None or second is None:
            if first is not second:
                bad += 1
        elif abs(first - second) > 1:
            bad += 1
    return bad / float(len(pairs))


def revenue_strict_values(clock_rows, clock="clock_education"):
    """The subset the stopping rule tracks: hit_basis == 'primary'."""
    return [r[clock] for r in clock_rows
            if r["hit_basis"] == "primary" and r[clock] is not None]


def read_history(path):
    """Wave medians logged so far, oldest first.

    Blank lines and comments are skipped rather than crashing: this file is
    machine-appended but human-readable, and a stray blank line must not take
    down the stopping-rule check.
    """
    history = []
    with open(path, encoding="utf-8") as handle:
        for line in handle:
            text = line.strip()
            if text and not text.startswith("#"):
                history.append(float(text))
    return history


def append_history(path, median, n):
    """Log one wave's median. Refuses to double-append the same sample.

    Re-running the wave check must not add a second identical line: two equal
    adjacent entries make the drift between them exactly zero, which would
    satisfy the stopping rule's stability test with fabricated evidence.
    """
    previous_n = None
    with open(path, encoding="utf-8") as handle:
        for line in handle:
            if line.startswith("# last-n:"):
                previous_n = int(line.split(":", 1)[1].strip())
    if previous_n == n:
        return False
    with open(path, "a", encoding="utf-8") as handle:
        handle.write("%.1f\n" % median)
        handle.write("# last-n: %d\n" % n)
    return True


def _audit_year(value):
    """A blank/whitespace cell or the literal 'unknown' is None, else int."""
    text = (value or "").strip()
    if not text or text == "unknown":
        return None
    return int(text)


def read_audit_pairs(path):
    """Read data/audit.csv into (first_pass, second_pass) year pairs.

    Columns: person_id, first_pass, second_pass. An empty cell or the
    literal 'unknown' becomes None, matching the anchors convention that an
    absent date is never guessed.
    """
    pairs = []
    with open(path, newline="", encoding="utf-8") as handle:
        for row in csv.DictReader(handle):
            pairs.append((_audit_year(row["first_pass"]),
                          _audit_year(row["second_pass"])))
    return pairs


def main(argv):
    """Report the revenue-strict median and CI for a clocks.csv.

    Two forms:
      python3 -m src.stats <clocks.csv>
      python3 -m src.stats <clocks.csv> --history <history.txt>

    The --history form additionally appends the median to the history file
    (refusing to double-log a re-run of the same sample) and evaluates the
    pre-registered stopping rule against the logged history.
    """
    usage = "usage: python3 -m src.stats <clocks.csv> [--history <history.txt>]"
    history_path = None
    if len(argv) == 2:
        clocks_path = argv[1]
    elif len(argv) == 4 and argv[2] == "--history":
        clocks_path = argv[1]
        history_path = argv[3]
    else:
        print(usage)
        return 2

    rows = clocks.load_clocks(clocks_path)
    values = revenue_strict_values(rows)
    if len(values) < 2:
        print("only %d revenue-strict rows; nothing to report" % len(values))
        return 0
    lo, med, hi = bootstrap_median_ci(values)
    n = len(values)
    print("revenue-strict n = %d" % n)
    print("median clock_education = %.1f yr" % med)
    print("95%% CI = [%.1f, %.1f], half-width %.2f yr"
          % (lo, hi, half_width(lo, hi)))
    if n < N_FLOOR:
        print("below N floor of %d - median not to be interpreted yet"
              % N_FLOOR)

    if history_path is not None:
        appended = append_history(history_path, med, n)
        history = read_history(history_path)
        if appended:
            print("appended to history (%d waves logged)" % len(history))
        else:
            print("already logged for n=%d, history unchanged" % n)
        verdict = check_stopping_rule(history, n, half_width(lo, hi))
        print("STOP: %s - %s" % (verdict["stop"], verdict["reason"]))

    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `python3 -m unittest tests.test_stats -v`
Expected: PASS, 32 tests

- [ ] **Step 5: Commit**

```bash
git add src/stats.py tests/test_stats.py
git commit -m "Add bootstrap CI, stopping rule, and audit disagreement check"
```

---

### Task 6: Report generation

**Files:**
- Create: `src/report.py`
- Test: `tests/test_report.py`

**Interfaces:**
- Consumes: `src.clocks.load_clocks`, `src.stats.bootstrap_median_ci`, `src.stats.half_width`
- Produces:
  - `summarise(values)` -> dict with keys `n`, `median`, `iqr_lo`, `iqr_hi`, `ci_lo`, `ci_hi`, `half_width`; returns `{"n": len(values)}` plus `None` values when `n < 2`
  - `strictness_runs(clock_rows, clock)` -> dict with keys `revenue_strict`, `all_commercial`, `pooled`, each a `summarise` dict
  - `slice_by(clock_rows, key, clock)` -> dict of slice value -> `summarise` dict
  - `build_report(clock_rows)` -> str of Markdown

- [ ] **Step 1: Write the failing test**

Create `tests/test_report.py`:

```python
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


if __name__ == "__main__":
    unittest.main()
```

- [ ] **Step 2: Run test to verify it fails**

Run: `python3 -m unittest tests.test_report -v`
Expected: FAIL with `ModuleNotFoundError: No module named 'src.report'`

- [ ] **Step 3: Write the implementation**

Create `src/report.py`:

```python
"""Build analysis.md.

Every median printed here carries its n and its CI. The pooled median mixes
revenue, prizes, audience, and fund size, so the three strictness levels are
always printed together and the revenue-strict figure is the headline.
"""

import statistics
import sys

from src import clocks
from src import stats

MIN_SLICE_N = 30
CLOCKS = ["clock_education", "clock_age18", "clock_venture",
          "age_at_first_hit"]
PRIMARY_CLOCK = "clock_education"


def summarise(values):
    """Median, IQR, and bootstrap CI for one set of clock values."""
    empty = {"n": len(values), "median": None, "iqr_lo": None, "iqr_hi": None,
             "ci_lo": None, "ci_hi": None, "half_width": None}
    if len(values) < 2:
        return empty
    lo, median, hi = stats.bootstrap_median_ci(values)
    quartiles = statistics.quantiles(values, n=4) if len(values) >= 4 else None
    return {
        "n": len(values),
        "median": median,
        "iqr_lo": quartiles[0] if quartiles else None,
        "iqr_hi": quartiles[2] if quartiles else None,
        "ci_lo": lo,
        "ci_hi": hi,
        "half_width": stats.half_width(lo, hi),
    }


def _values(rows, clock):
    return [r[clock] for r in rows if r[clock] is not None]


def strictness_runs(clock_rows, clock=PRIMARY_CLOCK):
    """The three required definition-strictness levels."""
    strict = [r for r in clock_rows if r["hit_basis"] == "primary"]
    commercial = [r for r in clock_rows
                  if r["hit_basis"] in ("primary", "fallback")]
    return {
        "revenue_strict": summarise(_values(strict, clock)),
        "all_commercial": summarise(_values(commercial, clock)),
        "pooled": summarise(_values(clock_rows, clock)),
    }


def slice_by(clock_rows, key, clock=PRIMARY_CLOCK):
    """Group rows by a slice key and summarise each group."""
    groups = {}
    for row in clock_rows:
        groups.setdefault(row[key], []).append(row)
    return {name: summarise(_values(rows, clock))
            for name, rows in sorted(groups.items())}


def _fmt(summary):
    """One table cell: median, CI, and n — or a reason there is none.

    The undersized flag applies to every slice below MIN_SLICE_N, including
    those too small to have a median at all. A one-person slice is the most
    misreadable of all, not the least.
    """
    if summary["median"] is None:
        text = "n=%d, too few to summarise" % summary["n"]
    else:
        text = "%.1f yr (95%% CI %.1f-%.1f), n=%d" % (
            summary["median"], summary["ci_lo"], summary["ci_hi"],
            summary["n"])
    if summary["n"] < MIN_SLICE_N:
        text += " — **too small to read as a finding**"
    return text


def build_report(clock_rows):
    """Render analysis.md."""
    lines = ["# Apprenticeship Trajectories — Analysis", ""]

    lines.append("## Survivorship caveat")
    lines.append("")
    lines.append("This sample is conditioned on the outcome. Everyone in it "
                 "succeeded. These medians describe **time-to-hit among "
                 "winners** and say nothing about the probability of becoming "
                 "one.")
    lines.append("")

    runs = strictness_runs(clock_rows)
    lines.append("## Definition strictness (primary clock: education → hit)")
    lines.append("")
    lines.append("| Level | Median |")
    lines.append("|---|---|")
    lines.append("| Revenue-strict ($10M revenue only) | %s |"
                 % _fmt(runs["revenue_strict"]))
    lines.append("| All commercial (+ IPO/acquisition fallback) | %s |"
                 % _fmt(runs["all_commercial"]))
    lines.append("| Pooled (all buckets, mixed definitions) | %s |"
                 % _fmt(runs["pooled"]))
    lines.append("")

    strict = runs["revenue_strict"]["median"]
    pooled = runs["pooled"]["median"]
    if strict is not None and pooled is not None:
        lines.append("Revenue-strict is the headline number. It differs from "
                     "the pooled median by **%.1f years**."
                     % abs(strict - pooled))
        lines.append("")

    lines.append("## All clocks, pooled")
    lines.append("")
    lines.append("| Clock | Median |")
    lines.append("|---|---|")
    for clock in CLOCKS:
        lines.append("| `%s` | %s |"
                     % (clock, _fmt(summarise(_values(clock_rows, clock)))))
    lines.append("")

    for key, title in (("bucket", "field"), ("era", "era"),
                       ("country_primary", "country")):
        lines.append("## By %s (primary clock)" % title)
        lines.append("")
        lines.append("| %s | Median |" % title.capitalize())
        lines.append("|---|---|")
        for name, summary in slice_by(clock_rows, key).items():
            lines.append("| %s | %s |" % (name or "(unknown)", _fmt(summary)))
        lines.append("")
        lines.append("Per-slice medians need roughly %d rows each before they "
                     "mean anything. Slices below that are flagged above."
                     % MIN_SLICE_N)
        lines.append("")

    strict_values = stats.revenue_strict_values(clock_rows)
    lines.append("## Stopping rule")
    lines.append("")
    if len(strict_values) < 2:
        lines.append("Revenue-strict n = %d. Not enough to evaluate."
                     % len(strict_values))
    else:
        half = runs["revenue_strict"]["half_width"]
        lines.append("Revenue-strict n = %d, CI half-width %.2f yr "
                     "(threshold %.2f)."
                     % (len(strict_values), half, stats.MAX_HALF_WIDTH))
        lines.append("")
        lines.append("Wave-over-wave median history is tracked in "
                     "`analysis/wave_medians.txt`; the rule needs three "
                     "wave medians before it can fire.")
    lines.append("")

    return "\n".join(lines)


def main(argv):
    if len(argv) != 3:
        print("usage: python3 -m src.report <clocks.csv> <analysis.md>")
        return 2
    rows = clocks.load_clocks(argv[1])
    with open(argv[2], "w", encoding="utf-8") as handle:
        handle.write(build_report(rows))
    print("wrote %s from %d rows" % (argv[2], len(rows)))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `python3 -m unittest tests.test_report -v`
Expected: PASS, 12 tests

- [ ] **Step 5: Run the whole suite**

Run: `python3 -m unittest discover -s tests -t . -v`
Expected: PASS, 88 tests total

- [ ] **Step 6: Commit**

```bash
git add src/report.py tests/test_report.py
git commit -m "Add report generation with strictness runs and slice flagging"
```

---

### Task 7: Pilot — 10 stress-case rows

**Files:**
- Create: `data/roster.csv`
- Create: `data/anchors.csv`
- Create: `docs/PILOT-REVIEW.md`

**Interfaces:**
- Consumes: `src.schema.columns()` for the header, `src.schema.validate_row` for the gate
- Produces: a validated 10-row `data/anchors.csv`, and a written verdict on whether `a3_first_domain_job` and `a5_first_hit` survived contact with awkward careers

**This task is research, not code.** Its purpose is to break the schema on 10 rows rather than 400.

- [ ] **Step 1: Write the roster header and pick the 10 stress cases**

Create `data/roster.csv` with header:

```
person_id,name,bucket,source_list,country_primary,gender,why_selected
```

Select exactly 10 people, chosen to stress the schema rather than to be representative. The required shapes:

1. A career-switcher whose eventual field differs from their first job — tests whether `a3_first_domain_job` has a defensible answer
2. A research scientist from `science_research` — tests the `prize` equivalent
3. A non-US operator — tests source availability outside English-language lists
4. Someone whose hit predates 1980 — tests whether old careers can be sourced at all
5. Someone from `media_creators` — tests the `aud1m` equivalent
6. Someone from `investors_finance` — tests the `fund100` equivalent
7. A founder whose company stayed private with undisclosed revenue — tests the `fallback` path
8. A founder with clearly documented $10M revenue — tests the `primary` path
9. A university dropout — tests `a2_education_end` when there is no credential
10. A `trade_import_logistics` operator — the thinnest-documented bucket

Every entry must cite a `source_list` from `frame.md`. No free recall.

- [ ] **Step 2: Write the anchors header**

```bash
python3 -c "from src import schema; print(','.join(schema.columns()))" > data/anchors.csv
```

- [ ] **Step 3: Research all 10 people and fill anchors.csv**

For each person, find all six anchors. Rules that are not negotiable:

- Every dated anchor needs a real source URL in its `_src` column and a `_conf` of `high`, `medium`, or `low`.
- After **two** failed source attempts, write `unknown` in `_date`, leave `_src` empty, and set `_conf` to `none`. **Do not infer.** A guessed date is worse than a missing one because it is invisible downstream.
- `hit_criterion` must be legal for the bucket, and `hit_basis` must match it. Task 2's validator enforces both.
- Year precision only. No months.

- [ ] **Step 4: Run the validator until it is clean**

Run: `python3 -m src.schema data/anchors.csv`
Expected: `10 rows checked, 0 errors`

Fix every reported error. Do not edit the validator to make a row pass — if a real career genuinely cannot be expressed under the schema, that is the pilot doing its job, and it belongs in the review document in Step 6.

- [ ] **Step 5: Compute clocks and eyeball them**

```bash
python3 -m src.clocks data/anchors.csv analysis/clocks.csv
python3 -m src.report analysis/clocks.csv analysis/analysis.md
```

Expected: both commands succeed; `analysis/analysis.md` flags every slice as too small to read, since n=10.

- [ ] **Step 6: Write the pilot review**

Create `docs/PILOT-REVIEW.md` answering, with the specific rows as evidence:

1. **Did `a3_first_domain_job` have a defensible answer for the career-switcher?** If it required a judgment call, state the call made and the rule that would generalise it.
2. **Did any bucket's hit criterion fail to fire?** Which, and what would have to change.
3. **What fraction of anchors came back `unknown`?** If materially above 10%, the sourcing standard or the anchor set needs revising before waves begin.
4. **Did any real career fail to fit the schema at all?** Describe it exactly.
5. **Verdict:** proceed to wave 1, or revise the spec first.

- [ ] **Step 7: Commit**

```bash
git add data/roster.csv data/anchors.csv analysis/clocks.csv analysis/analysis.md docs/PILOT-REVIEW.md
git commit -m "Add 10-person pilot and schema review verdict"
```

**STOP HERE.** The pilot verdict is a human review gate. Do not begin wave 1 until the spec author has read `docs/PILOT-REVIEW.md` and either approved or revised the spec.

---

### Task 8: Wave runbook

**Files:**
- Create: `docs/superpowers/RUNBOOK.md`
- Create: `analysis/wave_medians.txt`

**Interfaces:**
- Consumes: every module from Tasks 2–6
- Produces: the repeatable per-wave procedure. No new code.

- [ ] **Step 1: Create the wave median log**

```bash
echo "# Revenue-strict median of clock_education after each wave, one per line." > analysis/wave_medians.txt
```

- [ ] **Step 2: Write the runbook**

Create `docs/superpowers/RUNBOOK.md`:

```markdown
# Wave Runbook

Repeat until the stopping rule fires. Wave size 25.

## 1. Allocate the wave

    python3 -m src.allocate 25 software_internet=12 hardware_deeptech=7 ...

Pass the cumulative count for every bucket currently in `data/anchors.csv`.
The allocator returns the bucket counts for this wave.

## 2. Check the cross-cut floors

Compute current shares of non-US, pre-1995 hit, and women from
`data/anchors.csv`. If adding this wave would push any below its floor
(30%, 25%, 20%), rebalance the wave's name selection before researching.

## 3. Extend the roster

Add exactly the allocated number of names per bucket to `data/roster.csv`,
each citing a source list from `frame.md`. No free recall.

## 4. Research

Append rows to `data/anchors.csv`. Two source attempts per anchor, then
`unknown` / empty src / `conf=none`. Never infer a date.

## 5. Validate

    python3 -m src.schema data/anchors.csv

Must report 0 errors before proceeding.

## 6. Audit

Pick the rows to re-check — this wave's person_ids are the last 25 rows
appended to `data/anchors.csv`:

    python3 -c "import csv; from src import stats; \
      ids = [r['person_id'] for r in csv.DictReader(open('data/anchors.csv'))][-25:]; \
      print(stats.audit_sample(ids))"

Re-research those people **blind** — the second pass must not see the first
pass's answers. Record both `a5_first_hit` years in `data/audit.csv` with
columns `person_id,first_pass,second_pass`.

Then compute disagreement:

    python3 -c "from src import stats; \
      print(stats.audit_disagreement(stats.read_audit_pairs('data/audit.csv')))"

**If disagreement > 0.10, the entire wave is void and re-runs.** Delete the
wave's rows from `data/anchors.csv`, and remove that wave's names from
`data/roster.csv`. Those names must NOT be reused — a name whose dates two
researchers could not reproduce is exactly the kind of poorly-documented case
that would bias the sample if forced in. Draw fresh names for the same
bucket allocation, then return to step 3.

## 7. Recompute

    python3 -m src.clocks data/anchors.csv analysis/clocks.csv
    python3 -m src.stats analysis/clocks.csv
    python3 -m src.report analysis/clocks.csv analysis/analysis.md

## 8. Log the median and check the rule

    python3 -m src.stats analysis/clocks.csv --history analysis/wave_medians.txt

**Do not look at the median before total revenue-strict n reaches 30.** The
N floor exists to prevent optional stopping; reading the number early defeats
it even if the printed verdict still says False.

If the printed verdict is `STOP: True`, the collection is finished. If
`STOP: False`, the reason states what is still missing. Return to step 1.

## Expected duration

The rule tracks the revenue-strict subset, which is roughly half of all rows.
Expect it to fire at a total N around 350-500.
```

- [ ] **Step 3: Verify the full suite still passes**

Run: `python3 -m unittest discover -s tests -t . -v`
Expected: PASS, 88 tests

- [ ] **Step 4: Commit**

```bash
git add docs/superpowers/RUNBOOK.md analysis/wave_medians.txt
git commit -m "Add wave runbook with audit and stopping-rule procedure"
```

---

## Spec Coverage

| Spec section | Task |
|---|---|
| §1 Purpose, survivorship caveat | Task 6 (`build_report`) |
| §2 Pipeline, stage ordering | Tasks 1, 7, 8 |
| §3 Field quotas | Task 1 (`frame.md`), Task 2 (`BUCKET_SHARES`) |
| §3 Cross-cuts | Task 8 step 2 |
| §3 Named source lists | Task 1 (`frame.md`) |
| §4 Row schema | Task 2 (`columns`) |
| §4 Hit threshold, basis, fallback | Task 2 (`validate_row`) |
| §4 Year precision | Task 2 (`parse_year`) |
| §5 Cite-or-flag | Task 2 (`validate_row`) |
| §5 Exclusion of unknown hits | Task 2, Task 6 |
| §5 15% blind audit, 10% void | Task 5 (`audit_sample`, `audit_disagreement`), Task 8 step 6 |
| §6 Wave size, quota-proportional fill | Task 3 |
| §6 Stopping rule, N floor | Task 5 (`check_stopping_rule`) |
| §6 Revenue-strict subset tracked | Task 5 (`revenue_strict_values`) |
| §7 Pilot, 10 stress cases | Task 7 |
| §8 Clocks | Task 4 |
| §8 Strictness runs | Task 6 (`strictness_runs`) |
| §8 Slices with N and CI | Task 6 (`slice_by`, `_fmt`) |
| §9 Repository layout | Task 1 |
| §10 Limitations | Task 6 (caveat section), Task 7 (pilot review) |
