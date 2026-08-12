# Apprenticeship Trajectories — Analysis

## Survivorship caveat

This sample is conditioned on the outcome. Everyone in it succeeded. These medians describe **time-to-hit among winners** and say nothing about the probability of becoming one.

## Definition strictness (primary clock: education → hit)

| Level | Median |
|---|---|
| Revenue-strict ($10M revenue only) | 7.5 yr (95% CI 5.5-10.0), n=4 — **too small to read as a finding** |
| All commercial (+ IPO/acquisition fallback) | 7.0 yr (95% CI 5.5-10.0), n=5 — **too small to read as a finding** |
| Pooled (all buckets, mixed definitions) | 8.0 yr (95% CI 6.0-10.0), n=8 — **too small to read as a finding** |

Revenue-strict is the headline number. It differs from the pooled median by **0.5 years**.

## Confidence sensitivity (pooled, primary clock)

| Rows | Median |
|---|---|
| high-confidence rows only | 10.0 yr (95% CI 6.0-39.0), n=3 — **too small to read as a finding** |
| all included rows | 8.0 yr (95% CI 6.0-10.0), n=8 — **too small to read as a finding** |

Both rows pool every bucket and hit basis, so this run qualifies the pooled median, not the revenue-strict headline.

7 of 10 rows fall below high confidence.

**These diverge by 2.0 years.** The dataset is too soft to read the pooled median as a point estimate.

## Bounded-date sensitivity (pooled, primary clock)

| Treatment | Median |
|---|---|
| bounded rows dropped | 8.0 yr (95% CI 7.0-10.0), n=7 — **too small to read as a finding** |
| all rows, span midpoints | 8.0 yr (95% CI 6.0-10.0), n=8 — **too small to read as a finding** |
| all rows, earliest possible | 8.0 yr (95% CI 6.0-10.0), n=8 — **too small to read as a finding** |
| all rows, latest possible | 8.0 yr (95% CI 6.0-10.0), n=8 — **too small to read as a finding** |

A bounded date records that sources bracket an event without pinning it. 1 of 10 rows carry one, and every figure here is pooled across buckets and hit bases, so this run qualifies the pooled median, not the revenue-strict headline.

The envelope rows show the full range the data permits; the midpoint row is the pooled median.

## All clocks, pooled

| Clock | Median |
|---|---|
| `clock_education` | 8.0 yr (95% CI 6.0-10.0), n=8 — **too small to read as a finding** |
| `clock_age18` | 14.2 yr (95% CI 11.0-19.0), n=8 — **too small to read as a finding** |
| `clock_venture` | 2.8 yr (95% CI 1.0-9.0), n=8 — **too small to read as a finding** |
| `age_at_first_hit` | 32.2 yr (95% CI 29.0-37.0), n=8 — **too small to read as a finding** |

## By field (primary clock)

| Field | Median |
|---|---|
| consumer_retail_industrial | n=1, too few to summarise — **too small to read as a finding** |
| hardware_deeptech | n=1, too few to summarise — **too small to read as a finding** |
| investors_finance | n=1, too few to summarise — **too small to read as a finding** |
| media_creators | n=1, too few to summarise — **too small to read as a finding** |
| science_research | n=1, too few to summarise — **too small to read as a finding** |
| software_internet | 7.0 yr (95% CI 6.0-10.0), n=3 — **too small to read as a finding** |
| trade_import_logistics | n=0, too few to summarise — **too small to read as a finding** |

Per-slice medians need roughly 30 rows each before they mean anything. Slices below that are flagged above.

## By era (primary clock)

| Era | Median |
|---|---|
| (unknown) | n=0, too few to summarise — **too small to read as a finding** |
| post1995 | 8.0 yr (95% CI 7.0-10.0), n=7 — **too small to read as a finding** |
| pre1995 | n=1, too few to summarise — **too small to read as a finding** |

Per-slice medians need roughly 30 rows each before they mean anything. Slices below that are flagged above.

## By country (primary clock)

| Country | Median |
|---|---|
| CN | n=1, too few to summarise — **too small to read as a finding** |
| JP | n=0, too few to summarise — **too small to read as a finding** |
| KR | n=1, too few to summarise — **too small to read as a finding** |
| SE | n=1, too few to summarise — **too small to read as a finding** |
| US | 8.0 yr (95% CI 5.5-39.0), n=5 — **too small to read as a finding** |

Per-slice medians need roughly 30 rows each before they mean anything. Slices below that are flagged above.

## Stopping rule

Revenue-strict n = 4, CI half-width 2.25 yr (threshold 1.00).

Wave-over-wave median history is tracked in `analysis/wave_medians.txt`; the rule needs three wave medians before it can fire.
