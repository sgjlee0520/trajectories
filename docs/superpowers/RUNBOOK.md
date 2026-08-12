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

Below a total revenue-strict n of 30 the median and CI are withheld: the
tool prints n, the floor, and the stopping-rule verdict, and nothing else.
The N floor exists to prevent optional stopping, and a number that has been
seen cannot be unseen.

`analysis/analysis.md` withholds them on the same rule, so there is no way
around the floor short of editing the code. It still prints the exclusion
audit every wave — exclusions are a data-quality signal, not a result, and
that table is the only place a bias in what gets discarded is visible.

If the printed verdict is `STOP: True`, the collection is finished. If
`STOP: False`, the reason states what is still missing. Return to step 1.

## Expected duration

The rule tracks the revenue-strict subset, which is roughly half of all rows.
Expect it to fire at a total N around 350-500.
