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
    "clock_education_min",
    "clock_education_max",
    "bounded",
    "conf_min",
    "excluded",
    "exclusion_reason",
]

CONF_ORDER = ["none", "low", "medium", "high"]

ERA_SPLIT = 1995


def era_of(hit_year):
    """Era label for slicing: 'pre1995', 'post1995', or '' when the hit
    year is unknown. The empty label is deliberate — such rows contribute
    to no median, and Task 6 renders the group as '(unknown)'.

    Takes the same midpoint the clocks take: filing a 1994-1996 hit as
    pre1995 would put the row in a slice its own clock denies."""
    if hit_year is None:
        return ""
    return "pre1995" if hit_year < ERA_SPLIT else "post1995"


def clamp_hit(hit, earlier):
    """Narrow a hit span to the part that can actually follow `earlier`.

    A bracketed hit is not as wide as it looks: the ordering rule says the
    hit is no earlier than the anchor before it, so the years below that
    anchor are not possible hit years. Averaging over them understates every
    clock by up to half the bracket width, always in the same direction.

    Returns (None, None) when nothing is left -- the certain ordering
    violation schema.validate_row already rejects. No number is better than
    a negative one.
    """
    lo, hi = hit
    if lo is None or earlier[1] is None:
        return hit
    lo = max(lo, earlier[1])
    return (None, None) if lo > hi else (lo, hi)


def _gap(later, earlier):
    """Years between two anchors, or None when either is unknown."""
    if later is None or earlier is None:
        return None
    return later - earlier


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

    after_education = clamp_hit(hit, education)
    after_venture = clamp_hit(hit, venture)

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
        "era": era_of(hit_mid),
        "clock_education": _gap(midpoint(after_education), education_mid),
        "clock_age18": _gap(hit_mid,
                            birth_mid + 18 if birth_mid is not None else None),
        # rank1 dates a recognition, not a venture: the ranked work and the
        # ranking are usually the same event, so a venture clock of 0.0 would
        # be a category error rather than a short gap.
        "clock_venture": (None if row["hit_criterion"].strip() == "rank1"
                          else _gap(midpoint(after_venture),
                                    midpoint(venture))),
        "age_at_first_hit": _gap(hit_mid, birth_mid),
        "clock_education_min": _gap(after_education[0], education[1]),
        "clock_education_max": _gap(after_education[1], education[0]),
        "bounded": "true" if bounded else "false",
        "conf_min": weakest_conf(row["a2_education_end_conf"].strip(),
                                 row["a5_first_hit_conf"].strip()),
        "excluded": row["excluded"].strip().lower(),
        "exclusion_reason": row["exclusion_reason"].strip(),
    }


def included(clock_rows):
    """Rows that belong in a statistic.

    Every median, CI, and slice must route through this. Excluded rows used to
    fall out only because an undatable hit left their clocks None -- an
    accident, not a rule. A row excluded for any other reason, with its dates
    intact, would otherwise enter every figure in the report.
    """
    return [r for r in clock_rows
            if r["excluded"].strip().lower() != "true"]


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
               "age_at_first_hit", "clock_education_min",
               "clock_education_max")
    rows = []
    with open(path, newline="", encoding="utf-8") as handle:
        for row in csv.DictReader(handle):
            for key in numeric:
                row[key] = float(row[key]) if row[key].strip() else None
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
