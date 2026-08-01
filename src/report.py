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
