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

Pick the rows to re-check:

    python3 -c "from src import stats; print(stats.audit_sample(IDS_FROM_THIS_WAVE))"

Re-research those people **blind** — the second pass must not see the first
pass's answers. Record both `a5_first_hit` years in `data/audit.csv` with
columns `person_id,first_pass,second_pass`.

Then compute disagreement:

    python3 -c "from src import stats; print(stats.audit_disagreement(PAIRS))"

**If disagreement > 0.10, the entire wave is void and re-runs.** Delete the
wave's rows from `data/anchors.csv` and return to step 3.

## 7. Recompute

    python3 -m src.clocks data/anchors.csv analysis/clocks.csv
    python3 -m src.stats analysis/clocks.csv
    python3 -m src.report analysis/clocks.csv analysis/analysis.md

## 8. Log the median and check the rule

Append the revenue-strict median to `analysis/wave_medians.txt`, then:

    python3 -c "from src import stats, clocks; \
      rows = clocks.load_clocks('analysis/clocks.csv'); \
      v = stats.revenue_strict_values(rows); \
      lo, med, hi = stats.bootstrap_median_ci(v); \
      hist = [float(l) for l in open('analysis/wave_medians.txt') \
              if not l.startswith('#')]; \
      print(stats.check_stopping_rule(hist, len(v), stats.half_width(lo, hi)))"

**Do not look at the median before total revenue-strict n reaches 30.** The
N floor exists to prevent optional stopping; reading the number early defeats
it even if the printed rule still says False.

If `stop` is True, the collection is finished. If False, the reason states
what is still missing. Return to step 1.

## Expected duration

The rule tracks the revenue-strict subset, which is roughly half of all rows.
Expect it to fire at a total N around 350-500.
