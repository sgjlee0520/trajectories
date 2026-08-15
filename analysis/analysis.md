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

**15 of 85 rows excluded (17.6%).** Excluded rows appear in no other table on this page, so a bias in what gets excluded is only visible here.

| Reason | n |
|---|---|
| crossing_undatable | 13 |
| roster_unverified | 2 |

| Cross-cut | included | excluded | exclusion rate |
|---|---|---|---|
| US | 25 | 5 | 16.7% |
| non-US | 45 | 10 | 18.2% |
| women | 26 | 6 | 18.8% |
| men | 44 | 9 | 17.0% |
| bucket: consumer_retail_industrial | 8 | 3 | 27.3% |
| bucket: hardware_deeptech | 12 | 1 | 7.7% |
| bucket: healthcare_biotech | 4 | 5 | 55.6% |
| bucket: investors_finance | 7 | 2 | 22.2% |
| bucket: media_creators | 7 | 1 | 12.5% |
| bucket: science_research | 10 | 0 | 0.0% |
| bucket: software_internet | 19 | 2 | 9.5% |
| bucket: trade_import_logistics | 3 | 1 | 25.0% |

Era is not audited here: it derives from the hit year, which an excluded row usually lacks. Judging a discarded row's era is a human call, not something to infer.

## Definition strictness (primary clock: education → hit)

| Level | Median |
|---|---|
| Revenue-strict ($10M revenue only) | 9.0 yr (95% CI 7.5-13.0), n=34 |
| All commercial (+ IPO/acquisition fallback) | 9.5 yr (95% CI 7.5-13.5), n=40 |
| Pooled (all buckets, mixed definitions) | 13.0 yr (95% CI 9.0-15.0), n=56 |

Revenue-strict is the headline number. It differs from the pooled median by **4.0 years**.

## Confidence sensitivity (pooled, primary clock)

| Rows | Median |
|---|---|
| high-confidence rows only | 15.0 yr (95% CI 9.5-24.5), n=20 — **too small to read as a finding** |
| all included rows | 13.0 yr (95% CI 9.0-15.0), n=56 |

Both rows pool every bucket and hit basis, so this run qualifies the pooled median, not the revenue-strict headline.

50 of 70 rows fall below high confidence.

**These diverge by 2.0 years.** The dataset is too soft to read the pooled median as a point estimate.

## Bounded-date sensitivity (pooled, primary clock)

| Treatment | Median |
|---|---|
| bounded rows dropped | 14.0 yr (95% CI 10.0-18.0), n=31 |
| all rows, span midpoints | 13.0 yr (95% CI 9.0-15.0), n=56 |
| all rows, earliest possible | 10.0 yr (95% CI 9.0-14.0), n=56 |
| all rows, latest possible | 14.0 yr (95% CI 10.0-16.0), n=56 |

A bounded date records that sources bracket an event without pinning it. 28 of 70 rows carry one, and every figure here is pooled across buckets and hit bases, so this run qualifies the pooled median, not the revenue-strict headline.

The envelope rows show the full range the data permits; the midpoint row is the pooled median.

## All clocks, pooled

| Clock | Median |
|---|---|
| `clock_education` | 13.0 yr (95% CI 9.0-15.0), n=56 |
| `clock_age18` | 19.0 yr (95% CI 16.5-23.0), n=66 |
| `clock_venture` | 6.0 yr (95% CI 4.0-8.5), n=58 |
| `age_at_first_hit` | 37.0 yr (95% CI 34.5-41.0), n=66 |

## By field (primary clock)

| Field | Median |
|---|---|
| consumer_retail_industrial | 11.5 yr (95% CI 4.2-20.5), n=6 — **too small to read as a finding** |
| hardware_deeptech | 12.5 yr (95% CI 5.5-16.0), n=11 — **too small to read as a finding** |
| healthcare_biotech | 7.2 yr (95% CI 4.5-24.0), n=4 — **too small to read as a finding** |
| investors_finance | 15.0 yr (95% CI 10.0-18.0), n=3 — **too small to read as a finding** |
| media_creators | 16.0 yr (95% CI 8.0-21.0), n=3 — **too small to read as a finding** |
| science_research | 26.5 yr (95% CI 17.0-39.5), n=10 — **too small to read as a finding** |
| software_internet | 9.5 yr (95% CI 6.5-13.5), n=18 — **too small to read as a finding** |
| trade_import_logistics | n=1, too few to summarise — **too small to read as a finding** |

Per-slice medians need roughly 30 rows each before they mean anything. Slices below that are flagged above.

## By era (primary clock)

| Era | Median |
|---|---|
| post1995 | 10.0 yr (95% CI 8.0-15.0), n=38 |
| pre1995 | 14.5 yr (95% CI 10.0-21.5), n=18 — **too small to read as a finding** |

Per-slice medians need roughly 30 rows each before they mean anything. Slices below that are flagged above.

## By country (primary clock)

| Country | Median |
|---|---|
| AU | n=1, too few to summarise — **too small to read as a finding** |
| CA | 28.5 yr (95% CI 28.0-29.0), n=2 — **too small to read as a finding** |
| CH | n=0, too few to summarise — **too small to read as a finding** |
| CN | 15.0 yr (95% CI 9.0-60.0), n=5 — **too small to read as a finding** |
| DE | 17.5 yr (95% CI 10.0-24.0), n=4 — **too small to read as a finding** |
| ES | n=0, too few to summarise — **too small to read as a finding** |
| FR | 24.5 yr (95% CI 24.0-25.0), n=2 — **too small to read as a finding** |
| GB | 18.0 yr (95% CI 15.0-23.0), n=5 — **too small to read as a finding** |
| HK | n=1, too few to summarise — **too small to read as a finding** |
| ID | n=1, too few to summarise — **too small to read as a finding** |
| IN | 7.0 yr (95% CI 4.5-14.0), n=5 — **too small to read as a finding** |
| IT | n=1, too few to summarise — **too small to read as a finding** |
| JP | n=1, too few to summarise — **too small to read as a finding** |
| KR | n=1, too few to summarise — **too small to read as a finding** |
| NG | n=1, too few to summarise — **too small to read as a finding** |
| NL | n=1, too few to summarise — **too small to read as a finding** |
| NZ | n=0, too few to summarise — **too small to read as a finding** |
| RO | n=0, too few to summarise — **too small to read as a finding** |
| SE | n=1, too few to summarise — **too small to read as a finding** |
| SN | n=0, too few to summarise — **too small to read as a finding** |
| TW | n=1, too few to summarise — **too small to read as a finding** |
| UA | n=1, too few to summarise — **too small to read as a finding** |
| US | 9.2 yr (95% CI 6.0-15.0), n=22 — **too small to read as a finding** |

Per-slice medians need roughly 30 rows each before they mean anything. Slices below that are flagged above.

## Stopping rule

Revenue-strict n = 34, CI half-width 2.75 yr (threshold 1.00).

Wave-over-wave median history is tracked in `analysis/wave_medians.txt`; the rule needs three wave medians before it can fire.
