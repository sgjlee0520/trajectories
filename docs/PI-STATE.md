# PI state — read this first after a context reset

> **2026-08-22: collection is handed to Grok.** The study author has given Grok
> every remaining wave. Claude does not run waves any more and returns only to
> write the paper once `STOP: True`. Grok's standing orders are
> **`GROK-RUN-THE-STUDY.md`** at the repo root. This file stays the record of
> state and decisions.

**Division of labour, set by the study author on 2026-08-22:**

- **Claude is the PI.** Methodology decisions, rule changes, adjudicating
  disputed rows, deciding what gets excluded, reading audits, judging when the
  study stops, and writing the LaTeX paper. Claude does NOT do bulk research.
- **Grok does the research.** Volume lookups, wave batches, rescue passes.
  Driven headless via `scripts/grok-batch.sh`, briefed by
  `docs/GROK-RESEARCH-BRIEF.md`.
- **Grok tends toward sloppiness**, so its brief is deliberately more literal
  and more prescriptive than `docs/RESEARCH-RULES.md`. Keep it that way. When
  writing any new Grok prompt: state the refusal conditions explicitly, demand
  quoted sentences rather than summaries, and require pasted command output
  rather than remembered numbers.

## Where the study stands (commit at time of writing: see `git log -1`)

| | |
|---|---|
| collection | **COMPLETE** — `STOP: True` 2026-08-23. Handoff: `docs/COLLECTION-COMPLETE.md` |
| people researched | **235** (`data/anchors.csv`), schema 0 errors |
| included | 201 · excluded 34 (14.5%) |
| roster | **235 names**; all 235 researched |
| revenue-strict n | **93** |
| median at n=93 | **9.0 yr**, 95% CI [8.0, 10.0], half-width **1.00** |
| median history | 10.0, 9.0, 8.8, 9.0, 9.0, 9.8, 9.2, 9.0, 9.0 |
| stopping rule | **met** — drift (0.20, 0.00) both <0.50; half-width 1.00 ≤ 1.0 |
| tests | 207, `python3 -m unittest discover -s tests -t .` |
| composition | pre-1995 23.4% of all rows (27.0% of dated), non-US 54.9%, women 25.5% — recorded covariates, none steered |

Waves done: pilot (10), waves 1–9 (25 each). Wave 9 audited 2026-08-23 —
contradiction rate **0.000**, two first-only misses. Wave passes. Rows are in
`analysis/clocks.csv`. Collector did not start wave 10.

## OPEN ITEMS, in priority order

1. **The LaTeX paper.** Not started. Claude's job. Should carry: the survivorship
   framing, the constant-dollar method, the full bias catalogue, the audit
   methodology including its two rule changes and why, the median with its
   actual interval, and everything in `docs/COLLECTION-COMPLETE.md` § uncertainties.
   Decisions for the PI: `docs/OPEN-FOR-PI.md`.

2. **Rescue candidates, not collection.** p183 HelloSign `2011-2019`, p214 WePay
   `2008-2017`, p233 Olivia Dean `2018-2019`. First-pass dates stand. None of
   them can un-fire STOP.

3. **Wave 9 did move the covariates, as predicted.** Drawn wave 6/25 non-US and
   3/25 women against a pre-wave-9 file at 59% and 27%. Pooled file is now
   54.9% non-US and 25.5% women. Recorded, not corrected (`frame.md`).

## Done since the last reset (2026-08-22)

- **Wave 9 audited and collection stopped.** Blind second pass on
  `p211 p213 p214 p218 p221 p225 p226 p231 p232 p233`. Contradiction 0.000,
  two first-only misses. Recompute: n=93, median 9.0, CI [8.0, 10.0],
  half-width 1.00. `STOP: True`. Handoff in `docs/COLLECTION-COMPLETE.md`.
  Paper is Claude's. No further waves.
- **Waves 7–8 audited.** Blind second pass on the drawn sample
  `p164 p165 p182 p183 p184 p195 p196 p202 p206 p210`, run by Grok in a scratch
  directory holding only the two briefs and `src/cpi.py` (`BIASES.md` 22).
  Contradiction rate **0.000**, one miss. Wave passes.
  Second pass and full report: `data/audit6-secondpass.csv`,
  `docs/audit-w78/`. Pairs in `data/audit.csv` (wave 6's pairs were moved to
  `docs/audit-w78/audit-w6-previous.csv`).
- **The Palm pair is resolved: keep both rows, document the correlation.**
  `BIASES.md` 23 had claimed the pair attacks the stopping rule directly; it
  does not, and the entry now carries the correction. Both Palm rows are
  `hit_basis=fallback` and the rule reads only `hit_basis == 'primary'`, so
  dropping p70 leaves revenue-strict n unchanged at 60. The pair double-counts
  one event in the **pooled** analysis only. A sweep of all 210 rows found Palm
  to be the only shared hit event in the study.
- **`frame.md` amended** with "One row per hit event", the de-duplication rule
  enforced at roster draw since wave 6.
- **Recomputed** `analysis/clocks.csv`, `analysis/analysis.md`, and the median
  history. 207 tests pass.
- **Wave 9 roster drawn** (p211–p235) by walking the named lists in published
  order. The new one-row-per-hit-event rule made five rejections on its first
  use, and the anti-fame steer from `BIASES.md` 24 did not recur — Knight and
  Huang were taken in rank order with the temptation to skip them logged.
  Details, the two rows to watch, and one process failure: `docs/wave9/NOTES.md`.

## The rules that must not drift

1. Never infer a year. Sourced date, sourced `YYYY-YYYY` range (≤10 yr), or `unknown`.
2. Every threshold is constant 2026 dollars. `python3 -m src.cpi <year>`. The 1960 bar is $919,417.
3. Fix the data, never the validator. Nothing under `src/` changes to make data pass.
4. Selection is money-only. Country, era, sex are recorded, never steered — in either direction.
5. One row per hit EVENT. Co-founders of one company share one crossing.
6. Roster membership needs a URL naming the person. A list homepage is not confirmation.
7. Append rows incrementally, never in one batch.

## What the number means, and this belongs in the paper

The median describes **time-to-hit among people who made it**. It says nothing
about the odds of making it — the sample is conditioned on the outcome and has
no denominator. The people who worked twenty years and never crossed are absent
by construction, not by rarity. The two strongest measured biases both push the
figure **short**, so it reads as a floor.

## Key files

- `frame.md` — the sampling frame, authority on all rules
- `docs/BIASES.md` — 24 entries, several found the hard way. Read before quoting any number.
- `docs/GROK-RESEARCH-BRIEF.md` — the research brief for Grok
- `docs/RESEARCH-RULES.md` — the older brief for Claude-family agents
- `docs/HANDOFF.md` — cold-start instructions for any tool
- `docs/superpowers/RUNBOOK.md` — the 8-step wave procedure
- `scripts/grok-batch.sh` — run one Grok research batch
- `scripts/grok-audit.sh` — run a blind second pass in a clean scratch dir
- `scripts/grok-roster.sh` — draw a wave's roster; regenerates the exclusion list first
- `docs/GROK-ROSTER-BRIEF.md` — the roster brief; carries the two ways drawing has gone wrong
- `docs/GROK-AUDIT-BRIEF.md` — the audit brief; overrides four points of the research brief
- `scripts/merge-batches.sh` — merge batch files, refuses on column/id problems
