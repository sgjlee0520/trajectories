# Grok: run the study to its stopping rule

**Read this file first, then `docs/PI-STATE.md`, then `frame.md`.**

You are running data collection from here until the stopping rule fires. The
study author has handed you every wave. Claude is out of the loop until
collection is complete, and comes back only to write the paper.

That means **nobody is checking your work between waves.** Every guard in this
file exists because something went wrong on this project before.

---

## 0. Where things stand right now

| | |
|---|---|
| anchors | **235 rows**, `data/anchors.csv`, schema 0 errors |
| roster | 235 names — exhausted, wave 10 needs a fresh draw |
| waves done | pilot (10) + waves 1–9 (25 each) |
| **wave 9** | **researched and merged, NOT YET AUDITED** — this is your first job |
| last computed | n=83, median 9.0 yr, CI [8.0, 12.5] — computed BEFORE wave 9 |
| tests | 207, `python3 -m unittest discover -s tests -t .` |

## 1. Your first job: audit wave 9

Do not recompute anything until this passes.

    python3 -c "import csv; from src import stats; \
      ids=[r['person_id'] for r in csv.DictReader(open('data/anchors.csv'))][-25:]; \
      print(stats.audit_sample(ids))"

    scripts/grok-audit.sh data/audit7-secondpass.csv docs/wave9/audit-assignment.txt

Build `docs/wave9/audit-assignment.txt` first, one line per sampled person:

    person_id|Name|hit_entity|hit_criterion

**It must not contain the first pass's dates.** The script refuses if it spots
any. Then build `data/audit.csv` with columns
`person_id,first_pass,second_pass` and run:

    python3 -c "from src import stats; \
      print(stats.audit_disagreement(stats.read_audit_pairs('data/audit.csv')))"

**> 0.10 voids the wave.** Delete its rows from `data/anchors.csv`, remove its
names from `data/roster.csv`, and draw fresh names for the same allocation.
Those names are never reused. A miss (one pass `unknown`, the other dated) is
NOT a contradiction — it is a rescue signal, not a fault.

## 2. Then repeat this loop until the rule says stop

The full procedure is `docs/superpowers/RUNBOOK.md`. Per wave:

1. **Allocate** — `python3 -m src.allocate 25 <bucket>=<cumulative count> ...`
   Pass the current count for every bucket in `data/anchors.csv`.
2. **Record covariates** — current non-US / pre-1995 / women shares. Write them
   down. **Do not rebalance the wave on them.**
3. **Draw the roster** — `scripts/grok-roster.sh <assignment.md> <out.csv>`,
   briefed by `docs/GROK-ROSTER-BRIEF.md`. Write the assignment the way
   `docs/wave9/assignment.md` is written. Append to `data/roster.csv`.
4. **Research** — `scripts/grok-batch.sh <out.csv> <ids...>`, five people per
   batch, briefed by `docs/GROK-RESEARCH-BRIEF.md`. Batches run in parallel
   safely because each writes its own file. Set `EXTRA="..."` to carry a warning
   into one batch.
5. **Merge and validate** — `scripts/merge-batches.sh <files>`. It refuses on
   column or id problems. Then `python3 -m src.schema data/anchors.csv` must say
   `0 errors`.
6. **Audit** — section 1 above, every wave, no exceptions.
7. **Recompute** —

       python3 -m src.clocks data/anchors.csv analysis/clocks.csv
       python3 -m src.report analysis/clocks.csv analysis/analysis.md

8. **Log and check the rule** —

       python3 -m src.stats analysis/clocks.csv --history analysis/wave_medians.txt

   `STOP: True` → collection is over, go to section 5.
   `STOP: False` → the reason names what is missing. Next wave.

Commit after each wave with a message saying what the wave found. Push to
`origin main`.

## 3. Rules you may not change

These are the study's spine. You have no authority to alter any of them, and a
wave that breaks one is worth less than no wave at all.

1. **Never infer a year.** A sourced date, a sourced `YYYY-YYYY` range of ten
   years or less with both ends sourced, or the literal `unknown`. Nothing else.
2. **Every threshold is constant 2026 dollars**, never nominal. Run
   `python3 -m src.cpi <year>` and paste its real output into the row's notes.
   The 1960 bar is $919,417, not $10M. This single error made one pilot row
   eleven years wrong.
3. **Fix the data, never the validator.** Nothing under `src/` changes to make
   data pass. If a validator rejects a row, the row is wrong.
4. **Selection is money-only.** Country, era, and sex are recorded covariates,
   never selection criteria — in either direction. Do not steer toward or away
   from fame either; both are the same bias.
5. **One row per hit EVENT** (entity plus year), not per person. Co-founders of
   one company share one crossing.
6. **Roster membership needs a URL naming the person.** A list homepage is not
   confirmation.
7. **Append rows incrementally**, never in one batch at the end. Agents on this
   project have been killed mid-task; only the incremental writers kept work.

**`unknown` is a success.** 29 rows are excluded as undatable and every one has
survived independent re-checking. A confident wrong year is a failure that may
never be caught. Do not stretch weak evidence to fill a cell.

## 4. Decisions that are NOT yours

Stop and write the question into `docs/OPEN-FOR-PI.md` — create it if absent —
then carry on with everything that does not depend on the answer:

- Changing any rule in section 3, or anything in `frame.md`.
- Dropping a row for any reason other than the audit-void procedure.
- Resolving a shared hit event between two people already researched.
- Adding a source list not already named in `frame.md`.
- Deciding the study is finished on any basis other than `STOP: True`.
- Anything you want to do because a rule "seems wrong for this case." Record the
  case as `unknown` and say why the rule did not fit.

## 5. When `STOP: True`

Do not write the paper. Do this instead, then stop:

1. Run the full recompute and commit.
2. Write `docs/COLLECTION-COMPLETE.md`: the final n, median, CI, every wave's
   median in order, total excluded with reasons broken out, every audit's
   disagreement rate wave by wave, and the final covariate shares.
3. List in it every uncertainty you hit and never resolved, every row you would
   not defend, and everything in `docs/OPEN-FOR-PI.md`.
4. Push, and tell the study author collection is complete.

Claude returns at that point to write the paper from your files. **The value of
your run is decided by how honestly section 5.3 is written.** A gap you report
costs the paper a sentence. A gap you paper over may never be found.

## 6. What the number means — do not let this drift

The median is **time-to-hit among people who made it.** It says nothing about
the odds of making it: the sample is conditioned on the outcome and has no
denominator. People who worked twenty years and never crossed are absent by
construction, not by rarity. The two strongest measured biases both push the
figure short, so it reads as a floor.

Never report the median without that framing, in any file you write.

## 7. Files

- `docs/PI-STATE.md` — study state, open items, what was decided and why
- `frame.md` — the sampling frame, authority on all rules
- `docs/BIASES.md` — 24 entries, most found the hard way. **Read before quoting any number.**
- `docs/superpowers/RUNBOOK.md` — the 8-step wave procedure
- `docs/GROK-RESEARCH-BRIEF.md` / `GROK-ROSTER-BRIEF.md` / `GROK-AUDIT-BRIEF.md`
- `scripts/grok-batch.sh` / `grok-roster.sh` / `grok-audit.sh` / `merge-batches.sh`
- `docs/wave9/NOTES.md` — the most recent wave's PI notes, as a worked example
