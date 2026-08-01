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
    """Era label used for slicing. None when the hit year is unknown."""
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
