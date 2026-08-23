# Collection complete

`STOP: True` on 2026-08-23 after the wave 9 audit and recompute.

This file is the collector's handoff to the paper. It is not the paper.

**Among people who eventually hit, the middle one took 9.0 years from the end
of formal education to the first $10M-constant crossing.** That sentence is
the whole claim. The sample is conditioned on the outcome and has no
denominator. People who worked twenty years and never crossed are absent by
construction, not by rarity. The two strongest measured biases both push the
figure short, so it reads as a floor. `docs/BIASES.md` before any quotation.

---

## Final number

| | |
|---|---|
| revenue-strict n | **93** |
| median `clock_education` | **9.0 yr** |
| 95% CI | **[8.0, 10.0]**, half-width **1.00** |
| people researched | 235 (`data/anchors.csv`), schema 0 errors |
| included / excluded | 201 / 34 (14.5%) |
| tests | 207, `python3 -m unittest discover -s tests -t .` — OK |

Definition-strictness (from `analysis/analysis.md`, primary clock):

| Level | Median |
|---|---|
| Revenue-strict ($10M revenue only) | 9.0 yr (95% CI 8.0-10.0), n=93 |
| All commercial (+ IPO/acquisition fallback) | 9.0 yr (95% CI 8.0-12.5), n=103 |
| Pooled (all buckets, mixed definitions) | 13.0 yr (95% CI 10.0-14.5), n=156 |

Revenue-strict and pooled differ by 4.0 years. That gap is the paper's
problem, not a reason to pick the nicer one.

## Wave medians, oldest first

From `analysis/wave_medians.txt`:

| after | n | median |
|---|---|---|
| | 13 | 10.0 |
| | 21 | 9.0 |
| | 28 | 8.8 |
| | 34 | 9.0 |
| | 45 | 9.0 |
| | 52 | 9.8 |
| | 60 | 9.2 |
| waves 7–8 folded together | 83 | 9.0 |
| wave 9 | 93 | 9.0 |

Stopping rule (`src/stats.py`): n ≥ 30, two consecutive |Δmedian| both
< 0.50, CI half-width ≤ 1.00. After wave 9: drift **(0.20, 0.00)**,
half-width **1.00**. Verdict printed by the tool:

```
STOP: True - median stable (0.20, 0.00 yr drift) and CI half-width 1.00 yr at n=93
```

Half-width landed on the threshold, not under it. The comparison is
`ci_half_width > 1.0`, so 1.00 stops. Collector did not keep going.

Waves 7 and 8 share one history line because they were merged and audited as
a pair (n 60 → 83). Wave 9 added 10 rows to the headline clock (83 → 93).
Four more wave 9 rows are dated `rev10` primary but have
`a2_education_end = unknown` (p213 Collison, p215 Doshi, p220 Garcia, p234
Jacobs), so they do not enter `clock_education`. The median did not move;
the interval narrowed from [8.0, 12.5] to [8.0, 10.0].

## Exclusions

34 of 235 rows excluded.

| Reason | n |
|---|---|
| crossing_undatable | 30 |
| roster_unverified | 3 |
| criterion_never_met | 1 |

Cross-cuts (from `analysis/analysis.md`): non-US excluded at 17.1% vs US
11.3%; healthcare_biotech 41.7%; consumer_retail_industrial 32.3%;
trade_import_logistics 33.3%; hardware_deeptech 0%; science_research 0%.

Wave 9 contributed 5 of the 34, all `crossing_undatable`: p218 François
Pinault, p219 Todd Graves, p225 Sulaiman Al Habib, p232 Susie Neilson,
p235 Kjell Inge Røkke. The audit resampled three of those (Pinault, Al
Habib, Neilson) and also could not date them.

## Audits, wave by wave

Contradiction rates under the current rule (misses are not disagreements).
Waves 3 and 4 were originally scored under the older rule that counted
misses; those episodes are `docs/BIASES.md` 15 and 19.

| wave | contradiction | misses | notes |
|---|---|---|---|
| 1 | 0.000 | (not separately logged here) | |
| 2 | 0.000 | (not separately logged here) | |
| 3 | 0 conflicts in the six-platform re-test (60 comparisons, 14 one-sided unknowns) | original 4-row sample failed 1/4 under the old arithmetic; wave kept after the stronger instrument | `BIASES.md` 15 |
| 4 | 0.000 after rescoring | one miss each way; second-pass miss became p107 | originally 0.200 when misses counted; `BIASES.md` 19 |
| 5 | clean (commit `04e05c5`) | | auditor found first-pass files in the scratchpad and declined to open them; `BIASES.md` 22 |
| 6 | 0.00 | one second-only (p146) | isolation leak caught by hand; `BIASES.md` 22 |
| 7–8 (one audit) | 0.000 | one first-only (p183 HelloSign) | `data/audit6-secondpass.csv` |
| 9 | **0.000** | two first-only (p214 WePay, p233 Olivia Dean) | `data/audit7-secondpass.csv`, `docs/wave9/AUDIT.md` |

No audited wave that remains in the file failed the current contradiction
test. Two rule changes sit behind that sentence. They are in `BIASES.md`
and belong in the paper's methods.

## Covariate shares (recorded, never steered)

All 235 rows:

| | all rows | included only |
|---|---|---|
| non-US | 129/235 = **54.9%** | 107/201 = 53.2% |
| women | 60/235 = **25.5%** | 51/201 = 25.4% |
| pre-1995 | 55/235 = 23.4% of all rows; **55/204 = 27.0%** of dated | 52/201 = 25.9% |

Pre-wave-9 (210 rows) was 58.6% non-US, 27.1% women, 23.8% pre-1995 of all
rows. Wave 9 was 6/25 non-US and 3/25 women, as the roster notes predicted.
The drop is a finding, not a defect: the lists were walked in published
order (`docs/wave9/NOTES.md`).

Revenue-strict subset (n=93): 48/93 non-US (51.6%), 13/93 women (14.0%),
33/93 pre-1995 (35.5%). Women are thinner in the headline set than in the
file.

97 of 201 included rows carry a bounded `a5`. 45 of 201 have
`a2_education_end = unknown` and contribute nothing to the headline clock.

Wave 1 was collected under geography/era/sex floors; waves 2–9 were not.
The sample is a mixture of two sampling designs (`BIASES.md` 14).

---

## Uncertainties that were never resolved

Collector did not adjudicate these. They are listed so the paper can name
them instead of discovering them as surprises.

### Rows I would not defend as they stand

1. **p211 Alex Solomon / PagerDuty, 2013-2014, `rev10`.** First pass used
   ARR. Wave 9 second pass refused ARR and bounded 2009–2017 on GAAP. Overlap,
   so the wave is not void and the ARR date remains. Midpoints nearly match
   (2013.5 vs 2013), which is why this did not move the median — it is still
   the wrong kind of figure if `rev10` means calendar-year revenue. See
   `docs/OPEN-FOR-PI.md` §1. I did not sweep other SaaS rows for the same
   move.
2. **p214 Bill Clerico / WePay, 2008-2017.** Nine-year range. Second pass
   `unknown`. Survives as a miss. Weakest dated row in wave 9.
3. **p233 Olivia Dean / Reason to Stay, 2018-2019, `aud1m`.** Second pass
   would not turn streams into unique audience. Not in the headline set.
   I would not put weight on it.
4. **p183 Neal O'Mara / HelloSign, 2011-2019.** Already the standing rescue
   candidate from the wave 7–8 audit (`BIASES.md` 19, `docs/PI-STATE.md`).
   Eight-year range on a private company. Still in the revenue-strict set.
5. **p215 Suhail Doshi / Mixpanel, 2009-2018.** Nine-year range, not in the
   audit sample. Same shape as p214.
6. **p141 Yoshi Yokokawa / Alpaca, 2015-2024.** `docs/OPEN-QUESTIONS.md` Q5.
   If the hit entity was founded in 2013 the span is 11 years and the row
   should have been `crossing_undatable`. Confidence is already `low`. Still
   included. I did not re-open it.
7. **p146 Mateo Marietti / CookUnity.** Currently excluded. Wave 6's second
   pass would have included it on a different entity reading
   (`OPEN-QUESTIONS.md` Q7). Disagreement metric cannot see
   unknown-vs-dated.

Wide bounds (≥8 years) on included `rev10` rows, for the paper's bounded-date
sensitivity: p12, p25, p26, p39, p62, p71, p72, p75, p91, p121, p122, p124,
p141, p142, p161, p162, p169, p181, p183, p185, p189, p193, p205, p214,
p215.

### Open questions still unanswered

`docs/OPEN-QUESTIONS.md` Q1–Q7, in full. Highest leverage:

- Q1 Alfred Mann / Spectrolab 1960 purchase price ($300k vs $11M) decides
  whether p24 exists.
- Q2 Kiran Mazumdar-Shaw / Biocon 1978–1997 revenue would rescue p21.
- Q3 Zhong Huijuan / Hansoh 1997–2010 revenue would rescue p23.
- Q5 Alpaca founding year decides whether p141 stays.
- Q7 POP/Sushi Pop group revenue decides whether p146 was correctly
  excluded.

### Shared hit events

Palm (p70 Donna Dubinsky, p76 Jeff Hawkins) is the documented pair
(`BIASES.md` 23). Both `hit_basis=fallback`, so they do not enter
revenue-strict n. They double-count one event in the pooled analysis only.
Wave 9's Alcorn/Bushnell pair was the predicted collision; research attached
Alcorn to Silicon Gaming (1997) and Bushnell to Atari (1972-1974). The audit
confirmed Alcorn's Silicon Gaming bound. Danny Rimer's `fund100` is
Barksdale Group 1999, not Index Ventures IX (p151). Both checks from
`docs/wave9/NOTES.md` held.

### Process failures the methods section should name

- Wave 9 roster was written as one batch at the end, against the incremental
  append rule (`docs/wave9/NOTES.md`). Data survived; a kill would have
  lost the wave.
- Blind-audit isolation has failed in the environment before (`BIASES.md`
  22). Wave 9's second pass ran through `scripts/grok-audit.sh` in a fresh
  temp dir holding only the two briefs and `src/cpi.py`. The auditor said it
  did not stumble on a previous pass. That is a report, not a proof.
- Wave 1 used covariate floors; later waves did not.
- Two audit-rule changes after failing results (`BIASES.md` 15, 19).
- `analysis/analysis.md` still says "Eleven known biases"; `docs/BIASES.md`
  has 24. The generator string in `src/report.py` is stale. Collector did
  not edit `src/`.

### What I did not do

- No rescue pass on p183, p214, p233, or the OPEN-QUESTIONS rows, after
  `STOP: True`. The runbook says stop. Those rows are as the first pass left
  them.
- No paper. No change to `frame.md`. No change to `src/`.
- No new source list.

Everything in `docs/OPEN-FOR-PI.md` is still open.

---

Collection is finished because the pre-registered rule printed `STOP: True`,
not because the file looks done.
