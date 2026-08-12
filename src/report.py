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


def confidence_runs(clock_rows):
    """Spec 8's sensitivity run: high-confidence rows against all rows.

    `conf_min` is derived from the education and hit anchors only, so this
    takes no clock argument — filtering a birth-derived clock on education
    confidence would be a lie.

    Where these diverge, the dataset is soft enough that the pooled median
    should not be read as a point estimate.
    """
    high = [r for r in clock_rows if r["conf_min"] == "high"]
    return {
        "high_only": summarise(_values(high, PRIMARY_CLOCK)),
        "all_rows": summarise(_values(clock_rows, PRIMARY_CLOCK)),
    }


def bounded_runs(clock_rows):
    """How much the answer depends on rows whose hit year is a range.

    Only the primary clock carries an envelope, so this takes no clock
    argument — a parameter that accepted one value would be a lie.
    """
    # Fails open: any value other than "true" is treated as unbounded, so an
    # unexpected cell would quietly drop the row into the unbounded run.
    # clocks.py only ever writes "true"/"false".
    unbounded = [r for r in clock_rows if r["bounded"] != "true"]
    return {
        "unbounded_only": summarise(_values(unbounded, PRIMARY_CLOCK)),
        "midpoint_all": summarise(_values(clock_rows, PRIMARY_CLOCK)),
        "envelope_min": summarise(_values(clock_rows, "clock_education_min")),
        "envelope_max": summarise(_values(clock_rows, "clock_education_max")),
    }


def exclusion_audit(all_rows):
    """Who got thrown away, and whether that was even-handed.

    Excluded rows appear in no median, CI, or slice, so a bias in *what gets
    excluded* is invisible in every other table by construction. The frame
    carries quotas on geography, gender, and era; this checks the discard pile
    against the same cross-cuts.

    Era is deliberately absent. Era derives from the hit year, and an excluded
    row's hit year is usually unknown -- that is typically why it was
    excluded -- so sorting the discard pile by era would mean inferring it.
    """
    excluded = [r for r in all_rows if r["excluded"] == "true"]
    kept = clocks.included(all_rows)

    reasons = {}
    for row in excluded:
        reason = row["exclusion_reason"] or "(none given)"
        reasons[reason] = reasons.get(reason, 0) + 1

    def split(name, predicate):
        inc = sum(1 for r in kept if predicate(r))
        exc = sum(1 for r in excluded if predicate(r))
        total = inc + exc
        return {"name": name, "included": inc, "excluded": exc,
                "rate": (exc / float(total)) if total else None}

    cross = [split("US", lambda r: r["country_primary"] == "US"),
             split("non-US", lambda r: r["country_primary"] != "US"),
             split("women", lambda r: r["gender"] == "F"),
             split("men", lambda r: r["gender"] == "M")]
    cross += [split("bucket: " + b, lambda r, b=b: r["bucket"] == b)
              for b in sorted({r["bucket"] for r in all_rows})]

    return {"n_total": len(all_rows), "n_excluded": len(excluded),
            "rate": (len(excluded) / float(len(all_rows))
                     if all_rows else None),
            "reasons": reasons, "cross_cuts": cross}


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


def build_report(all_rows):
    """Render analysis.md.

    Takes every row, including excluded ones, and filters once here. The
    exclusion audit needs the discard pile; nothing else may see it.
    """
    clock_rows = clocks.included(all_rows)
    lines = ["# Apprenticeship Trajectories — Analysis", ""]

    lines.append("## Survivorship caveat")
    lines.append("")
    lines.append("This sample is conditioned on the outcome. Everyone in it "
                 "succeeded. These medians describe **time-to-hit among "
                 "winners** and say nothing about the probability of becoming "
                 "one.")
    lines.append("")

    audit = exclusion_audit(all_rows)
    lines.append("## Exclusion audit")
    lines.append("")
    if not audit["n_excluded"]:
        lines.append("No rows excluded of %d." % audit["n_total"])
        lines.append("")
    else:
        lines.append("**%d of %d rows excluded (%.1f%%).** Excluded rows appear "
                     "in no other table on this page, so a bias in what gets "
                     "excluded is only visible here."
                     % (audit["n_excluded"], audit["n_total"],
                        100.0 * audit["rate"]))
        lines.append("")
        lines.append("| Reason | n |")
        lines.append("|---|---|")
        for reason, count in sorted(audit["reasons"].items()):
            lines.append("| %s | %d |" % (reason, count))
        lines.append("")
        lines.append("| Cross-cut | included | excluded | exclusion rate |")
        lines.append("|---|---|---|---|")
        for cut in audit["cross_cuts"]:
            rate = "-" if cut["rate"] is None else "%.1f%%" % (100.0 * cut["rate"])
            lines.append("| %s | %d | %d | %s |"
                         % (cut["name"], cut["included"], cut["excluded"], rate))
        lines.append("")
        lines.append("Era is not audited here: it derives from the hit year, "
                     "which an excluded row usually lacks. Judging a discarded "
                     "row's era is a human call, not something to infer.")
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

    conf = confidence_runs(clock_rows)
    weak = [r for r in clock_rows if r["conf_min"] != "high"]
    lines.append("## Confidence sensitivity (pooled, primary clock)")
    lines.append("")
    lines.append("| Rows | Median |")
    lines.append("|---|---|")
    lines.append("| high-confidence rows only | %s |" % _fmt(conf["high_only"]))
    lines.append("| all included rows | %s |" % _fmt(conf["all_rows"]))
    lines.append("")
    lines.append("Both rows pool every bucket and hit basis, so this run "
                 "qualifies the pooled median, not the revenue-strict "
                 "headline.")
    lines.append("")
    lines.append("%d of %d rows fall below high confidence."
                 % (len(weak), len(clock_rows)))
    lines.append("")
    high_med = conf["high_only"]["median"]
    all_med = conf["all_rows"]["median"]
    if not weak:
        lines.append("Nothing was varied: the two rows above are the same "
                     "rows twice, so their agreement is arithmetic, not "
                     "evidence.")
        lines.append("")
    elif high_med is not None and all_med is not None:
        if abs(high_med - all_med) >= 1.0:
            lines.append("**These diverge by %.1f years.** The dataset is too "
                         "soft to read the pooled median as a point estimate."
                         % abs(high_med - all_med))
        else:
            lines.append("These agree within %.1f years."
                         % abs(high_med - all_med))
        lines.append("")

    env = bounded_runs(clock_rows)
    bounded_n = len([r for r in clock_rows if r["bounded"] == "true"])
    lines.append("## Bounded-date sensitivity (pooled, primary clock)")
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
                 "pinning it. %d of %d rows carry one, and every figure here "
                 "is pooled across buckets and hit bases, so this run "
                 "qualifies the pooled median, not the revenue-strict "
                 "headline." % (bounded_n, len(clock_rows)))
    lines.append("")
    if bounded_n:
        lines.append("The envelope rows show the full range the data permits; "
                     "the midpoint row is the pooled median.")
    else:
        lines.append("With no bounded row, nothing was varied: all four "
                     "figures are the same rows treated the same way, not a "
                     "range the data permits.")
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
