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

**34 of 235 rows excluded (14.5%).** Excluded rows appear in no other table on this page, so a bias in what gets excluded is only visible here.

| Reason | n |
|---|---|
| criterion_never_met | 1 |
| crossing_undatable | 30 |
| roster_unverified | 3 |

| Cross-cut | included | excluded | exclusion rate |
|---|---|---|---|
| US | 94 | 12 | 11.3% |
| non-US | 107 | 22 | 17.1% |
| women | 51 | 9 | 15.0% |
| men | 150 | 25 | 14.3% |
| bucket: consumer_retail_industrial | 21 | 10 | 32.3% |
| bucket: hardware_deeptech | 35 | 0 | 0.0% |
| bucket: healthcare_biotech | 14 | 10 | 41.7% |
| bucket: investors_finance | 21 | 2 | 8.7% |
| bucket: media_creators | 19 | 4 | 17.4% |
| bucket: science_research | 28 | 0 | 0.0% |
| bucket: software_internet | 55 | 4 | 6.8% |
| bucket: trade_import_logistics | 8 | 4 | 33.3% |

Era is not audited here: it derives from the hit year, which an excluded row usually lacks. Judging a discarded row's era is a human call, not something to infer.

## Definition strictness (primary clock: education → hit)

| Level | Median |
|---|---|
| Revenue-strict ($10M revenue only) | 9.0 yr (95% CI 8.0-10.0), n=93 |
| All commercial (+ IPO/acquisition fallback) | 9.0 yr (95% CI 8.0-12.5), n=103 |
| Pooled (all buckets, mixed definitions) | 13.0 yr (95% CI 10.0-14.5), n=156 |

Revenue-strict is the headline number. It differs from the pooled median by **4.0 years**.

## Confidence sensitivity (pooled, primary clock)

| Rows | Median |
|---|---|
| high-confidence rows only | 18.0 yr (95% CI 14.0-24.0), n=56 |
| all included rows | 13.0 yr (95% CI 10.0-14.5), n=156 |

Both rows pool every bucket and hit basis, so this run qualifies the pooled median, not the revenue-strict headline.

145 of 201 rows fall below high confidence.

**These diverge by 5.0 years.** The dataset is too soft to read the pooled median as a point estimate.

## Bounded-date sensitivity (pooled, primary clock)

| Treatment | Median |
|---|---|
| bounded rows dropped | 15.0 yr (95% CI 11.0-18.0), n=84 |
| all rows, span midpoints | 13.0 yr (95% CI 10.0-14.5), n=156 |
| all rows, earliest possible | 10.5 yr (95% CI 9.0-13.5), n=156 |
| all rows, latest possible | 13.5 yr (95% CI 11.0-16.0), n=156 |

A bounded date records that sources bracket an event without pinning it. 100 of 201 rows carry one, and every figure here is pooled across buckets and hit bases, so this run qualifies the pooled median, not the revenue-strict headline.

The envelope rows show the full range the data permits; the midpoint row is the pooled median.

## All clocks, pooled

| Clock | Median |
|---|---|
| `clock_education` | 13.0 yr (95% CI 10.0-14.5), n=156 |
| `clock_age18` | 18.5 yr (95% CI 16.2-21.0), n=180 |
| `clock_venture` | 5.0 yr (95% CI 4.0-6.0), n=173 |
| `age_at_first_hit` | 36.5 yr (95% CI 34.2-39.0), n=180 |

## By field (primary clock)

| Field | Median |
|---|---|
| consumer_retail_industrial | 13.0 yr (95% CI 8.0-18.0), n=15 — **too small to read as a finding** |
| hardware_deeptech | 14.0 yr (95% CI 8.5-16.0), n=31 |
| healthcare_biotech | 10.0 yr (95% CI 4.5-18.0), n=11 — **too small to read as a finding** |
| investors_finance | 15.0 yr (95% CI 11.0-18.0), n=13 — **too small to read as a finding** |
| media_creators | 10.0 yr (95% CI 8.5-21.0), n=12 — **too small to read as a finding** |
| science_research | 29.8 yr (95% CI 24.5-40.5), n=28 — **too small to read as a finding** |
| software_internet | 8.0 yr (95% CI 7.0-9.5), n=43 |
| trade_import_logistics | 8.0 yr (95% CI 6.0-18.0), n=3 — **too small to read as a finding** |

Per-slice medians need roughly 30 rows each before they mean anything. Slices below that are flagged above.

## By era (primary clock)

| Era | Median |
|---|---|
| post1995 | 11.0 yr (95% CI 9.2-14.5), n=112 |
| pre1995 | 13.5 yr (95% CI 9.0-17.0), n=44 |

Per-slice medians need roughly 30 rows each before they mean anything. Slices below that are flagged above.

## By country (primary clock)

| Country | Median |
|---|---|
| AE | n=1, too few to summarise — **too small to read as a finding** |
| AR | n=1, too few to summarise — **too small to read as a finding** |
| AU | 13.5 yr (95% CI 13.0-14.0), n=2 — **too small to read as a finding** |
| BG | n=1, too few to summarise — **too small to read as a finding** |
| BJ | n=0, too few to summarise — **too small to read as a finding** |
| CA | 8.0 yr (95% CI 5.5-29.0), n=5 — **too small to read as a finding** |
| CH | n=0, too few to summarise — **too small to read as a finding** |
| CN | 10.0 yr (95% CI 8.5-15.0), n=13 — **too small to read as a finding** |
| CZ | n=1, too few to summarise — **too small to read as a finding** |
| DE | 22.0 yr (95% CI 13.0-24.0), n=7 — **too small to read as a finding** |
| ES | n=1, too few to summarise — **too small to read as a finding** |
| FI | n=1, too few to summarise — **too small to read as a finding** |
| FR | 24.5 yr (95% CI 9.0-41.0), n=6 — **too small to read as a finding** |
| GB | 18.0 yr (95% CI 14.0-23.0), n=9 — **too small to read as a finding** |
| HK | n=1, too few to summarise — **too small to read as a finding** |
| ID | n=1, too few to summarise — **too small to read as a finding** |
| IL | n=1, too few to summarise — **too small to read as a finding** |
| IN | 7.0 yr (95% CI 4.5-8.0), n=8 — **too small to read as a finding** |
| IT | 19.0 yr (95% CI 15.0-50.0), n=3 — **too small to read as a finding** |
| JP | 25.8 yr (95% CI 9.0-42.5), n=2 — **too small to read as a finding** |
| KR | 12.5 yr (95% CI 6.0-21.0), n=4 — **too small to read as a finding** |
| MX | n=1, too few to summarise — **too small to read as a finding** |
| MY | 26.0 yr (95% CI 18.0-34.0), n=2 — **too small to read as a finding** |
| NG | n=1, too few to summarise — **too small to read as a finding** |
| NL | n=1, too few to summarise — **too small to read as a finding** |
| NO | n=1, too few to summarise — **too small to read as a finding** |
| NZ | n=1, too few to summarise — **too small to read as a finding** |
| PR | n=1, too few to summarise — **too small to read as a finding** |
| RO | n=0, too few to summarise — **too small to read as a finding** |
| SE | n=1, too few to summarise — **too small to read as a finding** |
| SN | n=0, too few to summarise — **too small to read as a finding** |
| TN | n=1, too few to summarise — **too small to read as a finding** |
| TW | n=1, too few to summarise — **too small to read as a finding** |
| UA | 8.2 yr (95% CI 7.5-9.0), n=2 — **too small to read as a finding** |
| US | 10.0 yr (95% CI 9.0-14.0), n=75 |
| VN | n=0, too few to summarise — **too small to read as a finding** |
| ZA | n=0, too few to summarise — **too small to read as a finding** |

Per-slice medians need roughly 30 rows each before they mean anything. Slices below that are flagged above.

## Stopping rule

Revenue-strict n = 93, CI half-width 1.00 yr (threshold 1.00).

Wave-over-wave median history is tracked in `analysis/wave_medians.txt`; the rule needs three wave medians before it can fire.
