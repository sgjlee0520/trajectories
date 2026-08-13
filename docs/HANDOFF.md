# Handoff — wave 1 close-out

Written for an agent picking this up cold in another tool (Cursor, etc.).
The Claude Code session that built this is out of budget. Everything below is
self-contained; you do not need that conversation.

Run everything from the repo root, `~/trajectories`, on branch `main`.

---

## What this project is

It measures the median years from career start to "first hit" across many
successful people, to answer how long an apprenticeship actually takes. Data is
collected in waves of 25. Wave 1 is nearly done.

**Read `frame.md` first — it is the authority on every rule.** Then
`docs/BIASES.md` for what the study already knows it gets wrong, and
`docs/superpowers/RUNBOOK.md` for the wave procedure.

## Hard rules — violating these is worse than doing nothing

1. **Never infer a year.** Every anchor is a sourced date, a sourced bounded
   range `YYYY-YYYY` (max 10-year span, BOTH ends sourced), or the literal
   `unknown` with an empty `_src` and `_conf=none`.
2. **Every dollar threshold is in constant 2026 dollars, never nominal.** Run
   `python3 -m src.cpi <year>` for that year's real bar. The 1960 `rev10` bar
   is **$919,417**, not $10M. Applying $10M nominally to an old company is the
   single defect that wrecked the first pilot — it dated one row eleven years
   late and another six.
3. **Fix the data, never the validator.** Do not edit anything under `src/`.
4. **An honest exclusion beats a fabricated date.** Seven rows are already
   excluded and every one was correct. If a crossing cannot be dated or bounded
   within 10 years, set `excluded=true` and `exclusion_reason=crossing_undatable`.
5. **Two genuine source attempts per anchor, then `unknown`.**
6. **Append rows incrementally**, never in one batch at the end. Several agents
   have died mid-task here; the survivors wrote as they went.

## Current state

- Branch `main`, working tree should be clean. `git log --oneline -5` for recent work.
- `python3 -m src.schema data/anchors.csv` must report **0 errors** at all times.
- 197 tests: `python3 -m unittest discover -s tests -t .`
- Wave 1 roster is `data/roster.csv` rows p11–p35. Anchors are `data/anchors.csv`.
- If rows p31–p35 are missing or incomplete, a research agent was killed
  mid-bucket. Their briefs are recoverable from `data/roster.csv` plus the rules
  above; see "If research is unfinished" below.

## STEP 1 — Research is COMPLETE. Skip to Step 2.

All 35 rows are researched, validated, and committed (`2eada9c`). Nothing to do
here. The material below is kept only in case a row must be redone.

Check: `python3 -c "import csv; print(len(list(csv.DictReader(open('data/anchors.csv')))))"`
Should be **35**. If fewer, research the missing roster ids.

Six anchors per person, all from `frame.md`:
`a1_birth`, `a2_education_end`, `a3_first_domain_job`, `a4_first_venture`,
`a5_first_hit`, `a6_scale_hit` — each with a `_date`, `_src` (a real URL), and
`_conf` (`high`/`medium`/`low`/`none`).

Match the column order and the `notes` style of existing rows exactly. Good
templates: p17–p22, p25–p30. Notes should record judgment calls, currency
conversions with the rate used, and the revenue figure against that year's bar.

**Also verify list membership.** `data/roster.csv` claims each person came from
a named source list in `frame.md`. Those claims were asserted, not verified, and
**three of eighteen checked so far have failed.** A feature article or interview
is NOT a ranking. If you cannot confirm membership after two attempts, add
`LIST MEMBERSHIP UNCONFIRMED` to that row's `notes` and report it — do not drop
the row yourself.

Then:
```
python3 -m src.schema data/anchors.csv
git add data/anchors.csv
git commit -m "Research wave 1: <buckets>"
```

## STEP 2 — The blind audit (runbook step 6)

This is the quality gate on the whole wave. Pick the rows:

```
python3 -c "import csv; from src import stats; \
  ids = [r['person_id'] for r in csv.DictReader(open('data/anchors.csv'))][-25:]; \
  print(stats.audit_sample(ids))"
```

Re-research **only `a5_first_hit`** for those people, **blind** — the second
pass must not look at what `data/anchors.csv` already says. Open a fresh context
if you can. Then write `data/audit.csv` with columns
`person_id,first_pass,second_pass` (the first-pass value comes from
`anchors.csv` only *after* you have recorded your own answer), and run:

```
python3 -c "from src import stats; \
  print(stats.audit_disagreement(stats.read_audit_pairs('data/audit.csv')))"
```

**If disagreement > 0.10 the entire wave is void.** Delete the wave's rows from
`data/anchors.csv`, remove those names from `data/roster.csv`, and draw fresh
names — the voided names must NOT be reused. See runbook step 6 for why.

Ideally run this pass on a **non-Claude model**. Two passes from the same model
share blind spots and trust the same sources; an independent system is what the
protocol is reaching for.

## STEP 3 — Close the wave

```
python3 -m src.clocks data/anchors.csv analysis/clocks.csv
python3 -m src.report analysis/clocks.csv analysis/analysis.md
python3 -m src.stats analysis/clocks.csv --history analysis/wave_medians.txt
git add -A && git commit -m "Close wave 1"
```

**The median will not print, and that is correct.** Revenue-strict n will be
around 14 against a floor of 30. Both the CLI and `analysis.md` withhold every
median below that floor, deliberately: optional stopping is the named threat,
and a number that has been seen cannot be unseen. Do not edit the code to see
it. `analysis.md` still prints the exclusion audit, which is the table worth
reading every wave.

## STEP 4 — Report to the user

State: rows added, exclusions and their reasons, any `LIST MEMBERSHIP
UNCONFIRMED`, the audit disagreement rate, and the cross-cut shares
(non-US ≥30%, pre-1995 hit ≥25%, women ≥20%). Do not state the median.

---

## Open items the user already knows about

- `docs/OPEN-QUESTIONS.md` — four stuck factual questions. Q1 (the price
  Textron paid for Spectrolab in 1960, per the *LA Times* of 2 Aug 1960)
  decides whether a currently-excluded row becomes a pre-1995 hit. Two sources
  differ by a factor of 37.
- Two rows are excluded as `roster_unverified` (p14 Nishi, p15 Kurtzig): fully
  researched, but no source list could be confirmed to contain them. Reinstate
  only on a confirmed listing.
- `investors_finance` and `trade_import_logistics` have no sampling list in the
  frame — see `docs/BIASES.md` 12. Do not fix this mid-wave; changing the frame
  between waves is itself a bias.

## Wave 2, when it comes

Start at `docs/superpowers/RUNBOOK.md` step 1. Allocation comes from
`python3 -m src.allocate 25 <bucket>=<cumulative count> ...` — pass the current
count for every bucket, and it returns the next wave's composition.
