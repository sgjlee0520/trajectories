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

**17 of 110 rows excluded (15.5%).** Excluded rows appear in no other table on this page, so a bias in what gets excluded is only visible here.

| Reason | n |
|---|---|
| criterion_never_met | 1 |
| crossing_undatable | 12 |
| roster_unverified | 4 |

| Cross-cut | included | excluded | exclusion rate |
|---|---|---|---|
| US | 33 | 5 | 13.2% |
| non-US | 60 | 12 | 16.7% |
| women | 34 | 6 | 15.0% |
| men | 59 | 11 | 15.7% |
| bucket: consumer_retail_industrial | 8 | 6 | 42.9% |
| bucket: hardware_deeptech | 17 | 0 | 0.0% |
| bucket: healthcare_biotech | 6 | 5 | 45.5% |
| bucket: investors_finance | 9 | 2 | 18.2% |
| bucket: media_creators | 11 | 0 | 0.0% |
| bucket: science_research | 13 | 0 | 0.0% |
| bucket: software_internet | 26 | 2 | 7.1% |
| bucket: trade_import_logistics | 3 | 2 | 40.0% |

Era is not audited here: it derives from the hit year, which an excluded row usually lacks. Judging a discarded row's era is a human call, not something to infer.

## Definition strictness (primary clock: education → hit)

| Level | Median |
|---|---|
| Revenue-strict ($10M revenue only) | 9.0 yr (95% CI 8.0-12.5), n=45 |
| All commercial (+ IPO/acquisition fallback) | 10.0 yr (95% CI 8.0-13.0), n=53 |
| Pooled (all buckets, mixed definitions) | 13.0 yr (95% CI 9.8-15.0), n=76 |

Revenue-strict is the headline number. It differs from the pooled median by **4.0 years**.

## Confidence sensitivity (pooled, primary clock)

| Rows | Median |
|---|---|
| high-confidence rows only | 18.5 yr (95% CI 10.0-26.0), n=30 |
| all included rows | 13.0 yr (95% CI 9.8-15.0), n=76 |

Both rows pool every bucket and hit basis, so this run qualifies the pooled median, not the revenue-strict headline.

63 of 93 rows fall below high confidence.

**These diverge by 5.5 years.** The dataset is too soft to read the pooled median as a point estimate.

## Bounded-date sensitivity (pooled, primary clock)

| Treatment | Median |
|---|---|
| bounded rows dropped | 15.0 yr (95% CI 10.0-19.0), n=41 |
| all rows, span midpoints | 13.0 yr (95% CI 9.8-15.0), n=76 |
| all rows, earliest possible | 10.5 yr (95% CI 9.0-14.0), n=76 |
| all rows, latest possible | 14.0 yr (95% CI 11.0-16.0), n=76 |

A bounded date records that sources bracket an event without pinning it. 39 of 93 rows carry one, and every figure here is pooled across buckets and hit bases, so this run qualifies the pooled median, not the revenue-strict headline.

The envelope rows show the full range the data permits; the midpoint row is the pooled median.

## All clocks, pooled

| Clock | Median |
|---|---|
| `clock_education` | 13.0 yr (95% CI 9.8-15.0), n=76 |
| `clock_age18` | 19.5 yr (95% CI 17.5-23.0), n=88 |
| `clock_venture` | 5.0 yr (95% CI 4.0-7.0), n=78 |
| `age_at_first_hit` | 37.5 yr (95% CI 35.5-41.0), n=88 |

## By field (primary clock)

| Field | Median |
|---|---|
| consumer_retail_industrial | 11.5 yr (95% CI 4.2-20.5), n=6 — **too small to read as a finding** |
| hardware_deeptech | 12.5 yr (95% CI 5.5-16.0), n=15 — **too small to read as a finding** |
| healthcare_biotech | 9.5 yr (95% CI 4.5-18.5), n=6 — **too small to read as a finding** |
| investors_finance | 16.5 yr (95% CI 10.0-19.0), n=4 — **too small to read as a finding** |
| media_creators | 18.5 yr (95% CI 8.5-34.5), n=6 — **too small to read as a finding** |
| science_research | 28.0 yr (95% CI 24.0-39.0), n=13 — **too small to read as a finding** |
| software_internet | 9.5 yr (95% CI 7.0-13.0), n=25 — **too small to read as a finding** |
| trade_import_logistics | n=1, too few to summarise — **too small to read as a finding** |

Per-slice medians need roughly 30 rows each before they mean anything. Slices below that are flagged above.

## By era (primary clock)

| Era | Median |
|---|---|
| post1995 | 13.0 yr (95% CI 9.2-15.5), n=56 |
| pre1995 | 13.5 yr (95% CI 9.0-19.8), n=20 — **too small to read as a finding** |

Per-slice medians need roughly 30 rows each before they mean anything. Slices below that are flagged above.

## By country (primary clock)

| Country | Median |
|---|---|
| AE | n=1, too few to summarise — **too small to read as a finding** |
| AR | n=1, too few to summarise — **too small to read as a finding** |
| AU | n=1, too few to summarise — **too small to read as a finding** |
| BJ | n=0, too few to summarise — **too small to read as a finding** |
| CA | 28.5 yr (95% CI 28.0-29.0), n=2 — **too small to read as a finding** |
| CH | n=0, too few to summarise — **too small to read as a finding** |
| CN | 10.0 yr (95% CI 9.0-17.5), n=7 — **too small to read as a finding** |
| CZ | n=1, too few to summarise — **too small to read as a finding** |
| DE | 22.0 yr (95% CI 10.0-28.0), n=5 — **too small to read as a finding** |
| ES | n=0, too few to summarise — **too small to read as a finding** |
| FR | 25.0 yr (95% CI 24.0-39.0), n=3 — **too small to read as a finding** |
| GB | 19.5 yr (95% CI 16.5-22.2), n=6 — **too small to read as a finding** |
| HK | n=1, too few to summarise — **too small to read as a finding** |
| ID | n=1, too few to summarise — **too small to read as a finding** |
| IN | 7.0 yr (95% CI 4.5-8.0), n=7 — **too small to read as a finding** |
| IT | n=1, too few to summarise — **too small to read as a finding** |
| JP | n=1, too few to summarise — **too small to read as a finding** |
| KR | n=1, too few to summarise — **too small to read as a finding** |
| NG | n=1, too few to summarise — **too small to read as a finding** |
| NL | n=1, too few to summarise — **too small to read as a finding** |
| NZ | n=1, too few to summarise — **too small to read as a finding** |
| RO | n=0, too few to summarise — **too small to read as a finding** |
| SE | n=1, too few to summarise — **too small to read as a finding** |
| SN | n=0, too few to summarise — **too small to read as a finding** |
| TN | n=1, too few to summarise — **too small to read as a finding** |
| TW | n=1, too few to summarise — **too small to read as a finding** |
| UA | n=1, too few to summarise — **too small to read as a finding** |
| US | 10.0 yr (95% CI 8.0-15.5), n=30 |
| ZA | n=0, too few to summarise — **too small to read as a finding** |

Per-slice medians need roughly 30 rows each before they mean anything. Slices below that are flagged above.

## Stopping rule

Revenue-strict n = 45, CI half-width 2.25 yr (threshold 1.00).

Wave-over-wave median history is tracked in `analysis/wave_medians.txt`; the rule needs three wave medians before it can fire.
