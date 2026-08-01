"""Bootstrap median CI, the pre-registered stopping rule, and the audit check.

The stopping rule is fixed in advance on purpose. Checking after every wave
and stopping the moment the number looks settled preferentially stops on
waves where noise happened to be small, which produces a median that appears
more precise than it is.
"""

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


def main(argv):
    """Report the revenue-strict median and CI for a clocks.csv."""
    if len(argv) != 2:
        print("usage: python3 -m src.stats <clocks.csv>")
        return 2
    rows = clocks.load_clocks(argv[1])
    values = revenue_strict_values(rows)
    if len(values) < 2:
        print("only %d revenue-strict rows; nothing to report" % len(values))
        return 0
    lo, med, hi = bootstrap_median_ci(values)
    print("revenue-strict n = %d" % len(values))
    print("median clock_education = %.1f yr" % med)
    print("95%% CI = [%.1f, %.1f], half-width %.2f yr"
          % (lo, hi, half_width(lo, hi)))
    if len(values) < N_FLOOR:
        print("below N floor of %d - median not to be interpreted yet"
              % N_FLOOR)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
