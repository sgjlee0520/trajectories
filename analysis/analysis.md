# Apprenticeship Trajectories — Analysis

## Survivorship caveat

This sample is conditioned on the outcome. Everyone in it succeeded. The buckets are filled from lists that select on extreme outcomes — Forbes, Midas, Nobel, Hurun — so there is nobody here who worked at it for twelve years and never crossed. Those people exist in enormous numbers; no list samples them.

So if the median comes back at 8 years, the sentence it supports is:

> **Among people who eventually hit, the middle one took about 8 years.**

The sentence it does **not** support:

> ~~If I start now, I have about a 50% chance of hitting within 8 years.~~

The second needs a denominator — everyone who started — and this dataset has no denominator at all. It is like timing how long lottery winners held their tickets: a real number, correctly computed, that says nothing about whether buying tickets is a good plan.

What the number is good for is **duration, given success**: how long the middle winner spent before the first real traction. That is worth knowing, and it is not a forecast.

Eleven known biases, their directions, and what mitigates each are catalogued in `docs/BIASES.md`. The two strongest identified effects both push the median **short**, so read it as a floor rather than a typical value.

## Exclusion audit

**22 of 135 rows excluded (16.3%).** Excluded rows appear in no other table on this page, so a bias in what gets excluded is only visible here.

| Reason | n |
|---|---|
| criterion_never_met | 1 |
| crossing_undatable | 18 |
| roster_unverified | 3 |

| Cross-cut | included | excluded | exclusion rate |
|---|---|---|---|
| US | 42 | 6 | 12.5% |
| non-US | 71 | 16 | 18.4% |
| women | 41 | 6 | 12.8% |
| men | 72 | 16 | 18.2% |
| bucket: consumer_retail_industrial | 11 | 7 | 38.9% |
| bucket: hardware_deeptech | 20 | 0 | 0.0% |
| bucket: healthcare_biotech | 8 | 6 | 42.9% |
| bucket: investors_finance | 11 | 2 | 15.4% |
| bucket: media_creators | 12 | 1 | 7.7% |
| bucket: science_research | 16 | 0 | 0.0% |
| bucket: software_internet | 30 | 4 | 11.8% |
| bucket: trade_import_logistics | 5 | 2 | 28.6% |

Era is not audited here: it derives from the hit year, which an excluded row usually lacks. Judging a discarded row's era is a human call, not something to infer.

## Definition strictness (primary clock: education → hit)

| Level | Median |
|---|---|
| Revenue-strict ($10M revenue only) | 9.8 yr (95% CI 8.0-13.0), n=52 |
| All commercial (+ IPO/acquisition fallback) | 10.0 yr (95% CI 8.5-13.5), n=60 |
| Pooled (all buckets, mixed definitions) | 14.0 yr (95% CI 10.0-16.0), n=87 |

Revenue-strict is the headline number. It differs from the pooled median by **4.2 years**.

## Confidence sensitivity (pooled, primary clock)

| Rows | Median |
|---|---|
| high-confidence rows only | 18.5 yr (95% CI 12.0-27.0), n=34 |
| all included rows | 14.0 yr (95% CI 10.0-16.0), n=87 |

Both rows pool every bucket and hit basis, so this run qualifies the pooled median, not the revenue-strict headline.

79 of 113 rows fall below high confidence.

**These diverge by 4.5 years.** The dataset is too soft to read the pooled median as a point estimate.

## Bounded-date sensitivity (pooled, primary clock)

| Treatment | Median |
|---|---|
| bounded rows dropped | 15.5 yr (95% CI 10.0-19.0), n=46 |
| all rows, span midpoints | 14.0 yr (95% CI 10.0-16.0), n=87 |
| all rows, earliest possible | 11.0 yr (95% CI 9.0-14.0), n=87 |
| all rows, latest possible | 14.0 yr (95% CI 12.0-18.0), n=87 |

A bounded date records that sources bracket an event without pinning it. 52 of 113 rows carry one, and every figure here is pooled across buckets and hit bases, so this run qualifies the pooled median, not the revenue-strict headline.

The envelope rows show the full range the data permits; the midpoint row is the pooled median.

## All clocks, pooled

| Clock | Median |
|---|---|
| `clock_education` | 14.0 yr (95% CI 10.0-16.0), n=87 |
| `clock_age18` | 19.0 yr (95% CI 17.5-23.0), n=104 |
| `clock_venture` | 4.0 yr (95% CI 3.5-6.0), n=94 |
| `age_at_first_hit` | 37.0 yr (95% CI 35.5-41.0), n=104 |

## By field (primary clock)

| Field | Median |
|---|---|
| consumer_retail_industrial | 11.8 yr (95% CI 7.0-19.0), n=8 — **too small to read as a finding** |
| hardware_deeptech | 13.2 yr (95% CI 7.0-16.0), n=18 — **too small to read as a finding** |
| healthcare_biotech | 10.0 yr (95% CI 4.5-18.0), n=7 — **too small to read as a finding** |
| investors_finance | 16.5 yr (95% CI 10.0-19.0), n=4 — **too small to read as a finding** |
| media_creators | 16.0 yr (95% CI 8.0-27.0), n=7 — **too small to read as a finding** |
| science_research | 28.5 yr (95% CI 23.5-39.0), n=16 — **too small to read as a finding** |
| software_internet | 9.5 yr (95% CI 7.0-13.0), n=25 — **too small to read as a finding** |
| trade_import_logistics | 12.0 yr (95% CI 6.0-18.0), n=2 — **too small to read as a finding** |

Per-slice medians need roughly 30 rows each before they mean anything. Slices below that are flagged above.

## By era (primary clock)

| Era | Median |
|---|---|
| post1995 | 13.0 yr (95% CI 9.5-16.0), n=65 |
| pre1995 | 14.5 yr (95% CI 9.5-19.0), n=22 — **too small to read as a finding** |

Per-slice medians need roughly 30 rows each before they mean anything. Slices below that are flagged above.

## By country (primary clock)

| Country | Median |
|---|---|
| AE | n=1, too few to summarise — **too small to read as a finding** |
| AR | n=1, too few to summarise — **too small to read as a finding** |
| AU | 13.5 yr (95% CI 13.0-14.0), n=2 — **too small to read as a finding** |
| BJ | n=0, too few to summarise — **too small to read as a finding** |
| CA | 28.0 yr (95% CI 7.0-29.0), n=3 — **too small to read as a finding** |
| CH | n=0, too few to summarise — **too small to read as a finding** |
| CN | 10.0 yr (95% CI 8.5-19.0), n=9 — **too small to read as a finding** |
| CZ | n=1, too few to summarise — **too small to read as a finding** |
| DE | 22.0 yr (95% CI 10.0-28.0), n=5 — **too small to read as a finding** |
| ES | n=0, too few to summarise — **too small to read as a finding** |
| FR | 25.0 yr (95% CI 24.0-39.0), n=3 — **too small to read as a finding** |
| GB | 18.0 yr (95% CI 15.0-21.5), n=7 — **too small to read as a finding** |
| HK | n=1, too few to summarise — **too small to read as a finding** |
| ID | n=1, too few to summarise — **too small to read as a finding** |
| IN | 7.0 yr (95% CI 4.5-8.0), n=7 — **too small to read as a finding** |
| IT | n=1, too few to summarise — **too small to read as a finding** |
| JP | n=1, too few to summarise — **too small to read as a finding** |
| KR | n=1, too few to summarise — **too small to read as a finding** |
| MY | n=1, too few to summarise — **too small to read as a finding** |
| NG | n=1, too few to summarise — **too small to read as a finding** |
| NL | n=1, too few to summarise — **too small to read as a finding** |
| NZ | n=1, too few to summarise — **too small to read as a finding** |
| RO | n=0, too few to summarise — **too small to read as a finding** |
| SE | n=1, too few to summarise — **too small to read as a finding** |
| SN | n=0, too few to summarise — **too small to read as a finding** |
| TN | n=1, too few to summarise — **too small to read as a finding** |
| TW | n=1, too few to summarise — **too small to read as a finding** |
| UA | n=1, too few to summarise — **too small to read as a finding** |
| US | 12.5 yr (95% CI 8.0-16.0), n=35 |
| ZA | n=0, too few to summarise — **too small to read as a finding** |

Per-slice medians need roughly 30 rows each before they mean anything. Slices below that are flagged above.

## Stopping rule

Revenue-strict n = 52, CI half-width 2.50 yr (threshold 1.00).

Wave-over-wave median history is tracked in `analysis/wave_medians.txt`; the rule needs three wave medians before it can fire.
