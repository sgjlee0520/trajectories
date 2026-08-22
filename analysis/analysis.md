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

**26 of 160 rows excluded (16.2%).** Excluded rows appear in no other table on this page, so a bias in what gets excluded is only visible here.

| Reason | n |
|---|---|
| criterion_never_met | 1 |
| crossing_undatable | 22 |
| roster_unverified | 3 |

| Cross-cut | included | excluded | exclusion rate |
|---|---|---|---|
| US | 48 | 8 | 14.3% |
| non-US | 86 | 18 | 17.3% |
| women | 45 | 6 | 11.8% |
| men | 89 | 20 | 18.3% |
| bucket: consumer_retail_industrial | 13 | 8 | 38.1% |
| bucket: hardware_deeptech | 24 | 0 | 0.0% |
| bucket: healthcare_biotech | 9 | 7 | 43.8% |
| bucket: investors_finance | 14 | 2 | 12.5% |
| bucket: media_creators | 14 | 2 | 12.5% |
| bucket: science_research | 19 | 0 | 0.0% |
| bucket: software_internet | 36 | 4 | 10.0% |
| bucket: trade_import_logistics | 5 | 3 | 37.5% |

Era is not audited here: it derives from the hit year, which an excluded row usually lacks. Judging a discarded row's era is a human call, not something to infer.

## Definition strictness (primary clock: education → hit)

| Level | Median |
|---|---|
| Revenue-strict ($10M revenue only) | 9.2 yr (95% CI 8.5-13.0), n=60 |
| All commercial (+ IPO/acquisition fallback) | 10.0 yr (95% CI 8.5-13.5), n=68 |
| Pooled (all buckets, mixed definitions) | 14.0 yr (95% CI 10.0-15.0), n=103 |

Revenue-strict is the headline number. It differs from the pooled median by **4.8 years**.

## Confidence sensitivity (pooled, primary clock)

| Rows | Median |
|---|---|
| high-confidence rows only | 21.0 yr (95% CI 14.0-27.5), n=38 |
| all included rows | 14.0 yr (95% CI 10.0-15.0), n=103 |

Both rows pool every bucket and hit basis, so this run qualifies the pooled median, not the revenue-strict headline.

96 of 134 rows fall below high confidence.

**These diverge by 7.0 years.** The dataset is too soft to read the pooled median as a point estimate.

## Bounded-date sensitivity (pooled, primary clock)

| Treatment | Median |
|---|---|
| bounded rows dropped | 16.0 yr (95% CI 13.0-19.0), n=54 |
| all rows, span midpoints | 14.0 yr (95% CI 10.0-15.0), n=103 |
| all rows, earliest possible | 12.0 yr (95% CI 9.0-14.0), n=103 |
| all rows, latest possible | 14.0 yr (95% CI 12.0-18.0), n=103 |

A bounded date records that sources bracket an event without pinning it. 65 of 134 rows carry one, and every figure here is pooled across buckets and hit bases, so this run qualifies the pooled median, not the revenue-strict headline.

The envelope rows show the full range the data permits; the midpoint row is the pooled median.

## All clocks, pooled

| Clock | Median |
|---|---|
| `clock_education` | 14.0 yr (95% CI 10.0-15.0), n=103 |
| `clock_age18` | 20.0 yr (95% CI 18.0-23.0), n=121 |
| `clock_venture` | 5.0 yr (95% CI 4.0-6.5), n=114 |
| `age_at_first_hit` | 38.0 yr (95% CI 36.0-41.0), n=121 |

## By field (primary clock)

| Field | Median |
|---|---|
| consumer_retail_industrial | 11.8 yr (95% CI 7.8-20.5), n=10 — **too small to read as a finding** |
| hardware_deeptech | 14.0 yr (95% CI 8.8-16.0), n=20 — **too small to read as a finding** |
| healthcare_biotech | 10.0 yr (95% CI 4.5-18.0), n=7 — **too small to read as a finding** |
| investors_finance | 15.0 yr (95% CI 11.0-18.0), n=7 — **too small to read as a finding** |
| media_creators | 16.0 yr (95% CI 7.0-27.0), n=9 — **too small to read as a finding** |
| science_research | 29.0 yr (95% CI 25.0-41.0), n=19 — **too small to read as a finding** |
| software_internet | 9.0 yr (95% CI 7.0-13.0), n=29 — **too small to read as a finding** |
| trade_import_logistics | 12.0 yr (95% CI 6.0-18.0), n=2 — **too small to read as a finding** |

Per-slice medians need roughly 30 rows each before they mean anything. Slices below that are flagged above.

## By era (primary clock)

| Era | Median |
|---|---|
| post1995 | 14.0 yr (95% CI 10.0-16.0), n=81 |
| pre1995 | 14.5 yr (95% CI 9.5-19.0), n=22 — **too small to read as a finding** |

Per-slice medians need roughly 30 rows each before they mean anything. Slices below that are flagged above.

## By country (primary clock)

| Country | Median |
|---|---|
| AE | n=1, too few to summarise — **too small to read as a finding** |
| AR | n=1, too few to summarise — **too small to read as a finding** |
| AU | 13.5 yr (95% CI 13.0-14.0), n=2 — **too small to read as a finding** |
| BG | n=1, too few to summarise — **too small to read as a finding** |
| BJ | n=0, too few to summarise — **too small to read as a finding** |
| CA | 17.5 yr (95% CI 5.5-29.0), n=4 — **too small to read as a finding** |
| CH | n=0, too few to summarise — **too small to read as a finding** |
| CN | 12.0 yr (95% CI 9.0-17.5), n=10 — **too small to read as a finding** |
| CZ | n=1, too few to summarise — **too small to read as a finding** |
| DE | 22.0 yr (95% CI 10.0-28.0), n=5 — **too small to read as a finding** |
| ES | n=0, too few to summarise — **too small to read as a finding** |
| FR | 25.0 yr (95% CI 11.0-43.0), n=5 — **too small to read as a finding** |
| GB | 18.0 yr (95% CI 15.0-21.5), n=7 — **too small to read as a finding** |
| HK | n=1, too few to summarise — **too small to read as a finding** |
| ID | n=1, too few to summarise — **too small to read as a finding** |
| IL | n=1, too few to summarise — **too small to read as a finding** |
| IN | 7.0 yr (95% CI 4.5-8.0), n=7 — **too small to read as a finding** |
| IT | 34.5 yr (95% CI 19.0-50.0), n=2 — **too small to read as a finding** |
| JP | 25.8 yr (95% CI 9.0-42.5), n=2 — **too small to read as a finding** |
| KR | 14.5 yr (95% CI 8.0-21.0), n=2 — **too small to read as a finding** |
| MX | n=1, too few to summarise — **too small to read as a finding** |
| MY | 26.0 yr (95% CI 18.0-34.0), n=2 — **too small to read as a finding** |
| NG | n=1, too few to summarise — **too small to read as a finding** |
| NL | n=1, too few to summarise — **too small to read as a finding** |
| NZ | n=1, too few to summarise — **too small to read as a finding** |
| PR | n=1, too few to summarise — **too small to read as a finding** |
| RO | n=0, too few to summarise — **too small to read as a finding** |
| SE | n=1, too few to summarise — **too small to read as a finding** |
| SN | n=0, too few to summarise — **too small to read as a finding** |
| TN | n=1, too few to summarise — **too small to read as a finding** |
| TW | n=1, too few to summarise — **too small to read as a finding** |
| UA | n=1, too few to summarise — **too small to read as a finding** |
| US | 10.0 yr (95% CI 8.5-16.0), n=39 |
| VN | n=0, too few to summarise — **too small to read as a finding** |
| ZA | n=0, too few to summarise — **too small to read as a finding** |

Per-slice medians need roughly 30 rows each before they mean anything. Slices below that are flagged above.

## Stopping rule

Revenue-strict n = 60, CI half-width 2.25 yr (threshold 1.00).

Wave-over-wave median history is tracked in `analysis/wave_medians.txt`; the rule needs three wave medians before it can fire.
