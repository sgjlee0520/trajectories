# Wave 9 roster — PI notes

Drawn 2026-08-22 by Grok via `scripts/grok-roster.sh`, merged into
`data/roster.csv` as p211–p235. Roster is now 235 names; 210 researched.

Full skip log and per-bucket walk in `grok-run.log`.

## Accepted

Every row carries a membership URL with a quoted sentence or JSON field, bucket
counts match the allocator exactly, no id collides, and no name repeats one of
the 210 already drawn. The walk order and every skip is logged per bucket.

## The one-row-per-hit-event rule fired five times on its first use

Added to `frame.md` earlier the same day; these are its first live rejections.

| skipped | reason |
|---|---|
| Ed Colligan | Palm Computing, already a hit entity |
| Andreas Struengmann | Hexal, same event as his brother |
| Li Xiting | Mindray, same event as Xu Hang (p-row already in study) |
| Rafaela Aponte-Diamant | MSC, same event as Gianluigi Aponte |
| Clarke, Martinis (2025 Physics) | share the 2025 Nobel with Devoret, already p157 |

Without the rule, four co-founder pairs and a shared prize year would have
entered this wave and each would have falsely narrowed the interval.

## Two rows to watch in research

1. **p221 Allan Alcorn and p222 Nolan Bushnell are both Atari people.** Grok kept
   both on the reasoning that Bushnell cofounded Atari while Alcorn was an
   employee whose own ventures came later (Zowie, Silicon Gaming), so Alcorn's
   `a5_first_hit` should attach to his own venture, not to Atari. That is
   sound under the frame — the hit is the person's own thing — but it is a
   **prediction, not a settled fact.** If research finds Alcorn's hit entity is
   Atari, the two rows are one event and one must go. Flag at research time
   rather than letting the merge absorb it.
2. **p231 Danny Rimer is at Index Ventures, and p151 Martin Mignot's hit entity
   is Index Ventures IX (2018).** Rimer opened Index's London office in 2002, so
   his first $100M fund should be a much earlier and different vehicle. Same
   firm, different fund, different vintage — allowed. But `fund100` attaches to
   a specific fund, so confirm the fund is not IX before accepting the row.

p230 Douglas Leone (Sequoia US) against p150 Neil Shen (Sequoia Capital China,
2005–2007) was checked and is clear: different fund family, different vintage.

## Composition, recorded not corrected

Wave 9 is 6/25 non-US and 3/25 women, against a study running at 59% non-US and
27% women. The wave is materially more US and more male than the sample it joins.

This is **not** a defect and must not be corrected. The lists were walked in
published order and this is what they produced; `frame.md` is explicit that a
covariate drifting hard is a finding for the analysis, not a reason to steer.
Record it, and expect the pooled shares to move when these 25 are researched.

## Process failure to note in the paper's methods

Grok wrote all 25 rows in a single batch at the end of a twenty-minute run,
against an explicit instruction to append incrementally — its own log says
"Next I'll append the 25 roster rows in id order." No data was affected, but a
kill at minute nineteen would have lost the wave. `docs/GROK-ROSTER-BRIEF.md`
now says to write each bucket's rows before walking the next list.

## Positive control: BIASES 24 held

The draw took Phil Knight, Jensen Huang, John Hopfield, Patrick Collison and
Brian Chesky in rank order and said plainly that it had been tempted to skip
Knight and Huang as "too obvious" and did not. Khosla and Thiel — the names
BIASES 24 was written about — were skipped only because they are already in the
study. The anti-fame steer that corrupted wave 6 did not recur.
