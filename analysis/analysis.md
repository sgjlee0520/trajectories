# Apprenticeship Trajectories — Analysis

## Survivorship caveat

This sample is conditioned on the outcome. Everyone in it succeeded. These medians describe **time-to-hit among winners** and say nothing about the probability of becoming one.

## Definition strictness (primary clock: education → hit)

| Level | Median |
|---|---|
| Revenue-strict ($10M revenue only) | 7.5 yr (95% CI 7.0-8.0), n=2 — **too small to read as a finding** |
| All commercial (+ IPO/acquisition fallback) | 8.0 yr (95% CI 6.0-23.0), n=5 — **too small to read as a finding** |
| Pooled (all buckets, mixed definitions) | 12.5 yr (95% CI 7.0-31.0), n=8 — **too small to read as a finding** |

Revenue-strict is the headline number. It differs from the pooled median by **5.0 years**.

## All clocks, pooled

| Clock | Median |
|---|---|
| `clock_education` | 12.5 yr (95% CI 7.0-31.0), n=8 — **too small to read as a finding** |
| `clock_age18` | 24.0 yr (95% CI 11.0-42.0), n=9 — **too small to read as a finding** |
| `clock_venture` | 10.0 yr (95% CI 2.0-21.0), n=9 — **too small to read as a finding** |
| `age_at_first_hit` | 42.0 yr (95% CI 29.0-60.0), n=9 — **too small to read as a finding** |

## By field (primary clock)

| Field | Median |
|---|---|
| consumer_retail_industrial | 15.5 yr (95% CI 8.0-23.0), n=2 — **too small to read as a finding** |
| hardware_deeptech | n=1, too few to summarise — **too small to read as a finding** |
| investors_finance | n=1, too few to summarise — **too small to read as a finding** |
| media_creators | n=1, too few to summarise — **too small to read as a finding** |
| science_research | n=1, too few to summarise — **too small to read as a finding** |
| software_internet | 6.5 yr (95% CI 6.0-7.0), n=2 — **too small to read as a finding** |
| trade_import_logistics | n=0, too few to summarise — **too small to read as a finding** |

Per-slice medians need roughly 30 rows each before they mean anything. Slices below that are flagged above.

## By era (primary clock)

| Era | Median |
|---|---|
| (unknown) | n=0, too few to summarise — **too small to read as a finding** |
| post1995 | 8.0 yr (95% CI 6.5-36.0), n=6 — **too small to read as a finding** |
| pre1995 | 20.0 yr (95% CI 17.0-23.0), n=2 — **too small to read as a finding** |

Per-slice medians need roughly 30 rows each before they mean anything. Slices below that are flagged above.

## By country (primary clock)

| Country | Median |
|---|---|
| CN | n=0, too few to summarise — **too small to read as a finding** |
| JP | n=1, too few to summarise — **too small to read as a finding** |
| KR | n=1, too few to summarise — **too small to read as a finding** |
| SE | n=1, too few to summarise — **too small to read as a finding** |
| US | 17.0 yr (95% CI 6.0-39.0), n=5 — **too small to read as a finding** |

Per-slice medians need roughly 30 rows each before they mean anything. Slices below that are flagged above.

## Stopping rule

Revenue-strict n = 2, CI half-width 0.50 yr (threshold 1.00).

Wave-over-wave median history is tracked in `analysis/wave_medians.txt`; the rule needs three wave medians before it can fire.
