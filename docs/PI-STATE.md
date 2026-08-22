# PI state — read this first after a context reset

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
| people researched | **210** (`data/anchors.csv`) |
| included | 181 · excluded 29 (14%) |
| roster | 210 names, fully drawn |
| revenue-strict n | run `python3 -m src.stats analysis/clocks.csv` |
| median at n=52 | 9.8 yr, 95% CI [8.0, 13.0] |
| stopping rule | not met — drift 0.80 yr (needs <0.50), half-width 2.50 (needs ≤1.0) |
| tests | 207, `python3 -m unittest discover -s tests -t .` |
| composition | pre-1995 27%, non-US 57%, women 27% — all recorded covariates, none steered |

Waves done: pilot (10), waves 1–8 (25 each). Waves 7–8 were researched on a
second machine, merged here, and are **NOT YET AUDITED**.

## OPEN ITEMS, in priority order

1. **Waves 7–8 have never been audited.** The sample was drawn:
   `p164 p165 p182 p183 p184 p195 p196 p202 p206 p210`. A blind second pass on
   those ten must be run — Grok is fine for this, in a CLEAN working directory
   (see `docs/BIASES.md` 22: a previous auditor found the first pass's scraped
   files in a shared scratch dir). Then build `data/audit.csv` and run
   `stats.audit_disagreement`. Contradictions above 0.10 void the wave; misses
   are NOT contradictions and are rescue signals (`BIASES.md` 19).
2. **The Palm pair is unresolved.** p70 Dubinsky and p94 Hawkins both date to
   1995 at Palm Computing — one event, two rows, which falsely narrows the
   bootstrap CI the stopping rule depends on (`BIASES.md` 23). Decide whether
   to drop one. This is a PI decision and needs the author's input.
3. **Wave 9 onward.** Roster is exhausted at 210; a new roster must be drawn
   before more research. Enumerate lists, do not recall then verify
   (`BIASES.md` 20), and do not steer toward or away from fame (`BIASES.md` 24).
4. **The LaTeX paper.** Not started. Claude's job. Should carry: the survivorship
   framing, the constant-dollar method, the full bias catalogue, the audit
   methodology including its two rule changes and why, and the median with its
   actual interval.

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
- `scripts/grok-batch.sh` — run one Grok batch
- `scripts/merge-batches.sh` — merge batch files, refuses on column/id problems
