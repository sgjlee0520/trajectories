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
import zlib

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


def audit_sample(person_ids, fraction=AUDIT_FRACTION, seed=None):
    """Pick the wave rows to re-research blind. At least one, always.

    The seed defaults to a digest of the ids themselves. A constant seed
    draws the same *positions* out of every wave of the same size, and the
    runbook has researchers append names in bucket-allocation order, so the
    same few buckets would be audited every wave and the rest never.

    crc32, not the builtin hash(): string hashing is salted per process, and
    an audit selection that changes between runs cannot be reproduced by
    whoever checks the work. Pass `seed` to pin it.
    """
    ordered = sorted(person_ids)
    if not ordered:
        return []
    k = max(1, int(round(len(ordered) * fraction)))
    if seed is None:
        seed = zlib.crc32("|".join(ordered).encode("utf-8"))
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
    return [r[clock] for r in clocks.included(clock_rows)
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
