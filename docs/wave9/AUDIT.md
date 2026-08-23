# Wave 9 audit

Blind second pass 2026-08-23 via `scripts/grok-audit.sh` into
`data/audit7-secondpass.csv`. Assignment:
`docs/wave9/audit-assignment.txt` (entity and criterion only). Scratch dir
held only the two briefs and `src/cpi.py`.

Sample, from `stats.audit_sample` on the last 25 ids:
`p211 p213 p214 p218 p221 p225 p226 p231 p232 p233`.

Two entity strings had the first pass's year in parentheses
(`Barksdale Group (1999 fund)`, `Reason to Stay (2018 single)`). Those years
were stripped so the assignment would stay blind.

Wave 7–8 pairs moved to `docs/wave9/audit-w78-previous.csv` before
`data/audit.csv` was rebuilt.

## Pairs

| person_id | name | first_pass | second_pass | reading |
|---|---|---|---|---|
| p211 | Alex Solomon | 2013-2014 | 2009-2017 | overlap |
| p213 | Patrick Collison | 2009-2014 | 2009-2014 | agree |
| p214 | Bill Clerico | 2008-2017 | unknown | miss (first only) |
| p218 | François Pinault | unknown | unknown | both unknown |
| p221 | Allan Alcorn | 1997 | 1993-1998 | overlap |
| p225 | Sulaiman Al Habib | unknown | unknown | both unknown |
| p226 | Seo Jung-jin | 2007 | 2002-2007 | overlap |
| p231 | Danny Rimer | 1999 | 1999 | agree |
| p232 | Susie Neilson | unknown | unknown | both unknown |
| p233 | Olivia Dean | 2018-2019 | unknown | miss (first only) |

```
disagreement: 0.0
misses first_only, second_only: (2, 0)
```

**Wave passes.** Threshold is 0.10. No contradictions.

## Misses (rescue signals, not faults)

- **p214 Bill Clerico / WePay, 2008-2017.** Second pass found no calendar-year
  total it was willing to use. An Inc.com snippet of "$24.9 million in 2014"
  did not appear in the article body it opened, and it refused to date from a
  snippet. The first pass's 9-year range stands.
- **p233 Olivia Dean / Reason to Stay, 2018-2019.** Second pass would not
  convert Spotify lifetime plays or 2021 artist-level stream counts into
  `aud1m`. The first pass's range stands.

## Method difference that did not contradict

**p211 PagerDuty.** First pass dated `rev10` from ARR ($3M in 2013 below the
bar, $10M ARR summer 2014 above). Second pass refused ARR as not calendar-year
revenue and bounded founding (2009) to the first S-1 GAAP figure (2017). The
spans overlap, so this is agreement under the rule. The surviving row is the
ARR dating. Flagged in `docs/OPEN-FOR-PI.md` — collector has no authority to
rewrite it.

p221 and p226 are the same shape in reverse: first pass a single year, second
pass a bound that contains it.

p218 / p225 / p232 were excluded by the first pass and the second pass also
could not date them.
