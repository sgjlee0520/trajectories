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
MAX_SPAN_YEARS = 10


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
            if parse_span(date)[0] is None:
                errors.append("%s_date must be a 4-digit year or a "
                              "'YYYY-YYYY' span at most %d years wide, got %r"
                              % (anchor, MAX_SPAN_YEARS, date))
            if not URL_PATTERN.match(src):
                errors.append("%s_src must be a URL when %s_conf=%s, got %r"
                              % (anchor, anchor, conf, src))

    # An unknown birth year is permitted — it costs the two clocks that need
    # it, not the whole row. An implausible one is a data error.
    birth_lo, birth_hi = parse_span(row["a1_birth_date"])
    if birth_lo is not None and not (MIN_BIRTH_YEAR <= birth_lo
                                     and birth_hi <= MAX_BIRTH_YEAR):
        errors.append("a1_birth_date must be a year in [%d, %d], got %r"
                      % (MIN_BIRTH_YEAR, MAX_BIRTH_YEAR,
                         row["a1_birth_date"]))

    excluded = row["excluded"].strip().lower()
    if excluded not in ("true", "false"):
        errors.append("excluded must be 'true' or 'false', got %r"
                      % row["excluded"])

    hit_lo, hit_hi = parse_span(row["a5_first_hit_date"])
    hit = hit_lo
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

        # Flag only certain violations: the earliest possible earlier-anchor
        # date must fall after the latest possible hit. A validator that
        # rejects a correct bounded row teaches researchers to edit dates
        # until the tool goes quiet, which is the one habit this project
        # cannot afford.
        for earlier in ("a2_education_end", "a4_first_venture"):
            value = parse_span(row[earlier + "_date"])[0]
            if value is not None and value > hit_hi:
                errors.append("%s (%d) is after the latest possible "
                              "a5_first_hit (%d)" % (earlier, value, hit_hi))

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
