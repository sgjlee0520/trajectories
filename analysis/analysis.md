# Apprenticeship Trajectories — Analysis

## Survivorship caveat

This sample is conditioned on the outcome. Everyone in it succeeded. These medians describe **time-to-hit among winners** and say nothing about the probability of becoming one.

## Exclusion audit

**2 of 10 rows excluded (20.0%).** Excluded rows appear in no other table on this page, so a bias in what gets excluded is only visible here.

| Reason | n |
|---|---|
| crossing_undatable | 2 |

| Cross-cut | included | excluded | exclusion rate |
|---|---|---|---|
| US | 5 | 0 | 0.0% |
| non-US | 3 | 2 | 40.0% |
| women | 3 | 1 | 25.0% |
| men | 5 | 1 | 16.7% |
| bucket: consumer_retail_industrial | 1 | 1 | 50.0% |
| bucket: hardware_deeptech | 1 | 0 | 0.0% |
| bucket: investors_finance | 1 | 0 | 0.0% |
| bucket: media_creators | 1 | 0 | 0.0% |
| bucket: science_research | 1 | 0 | 0.0% |
| bucket: software_internet | 3 | 0 | 0.0% |
| bucket: trade_import_logistics | 0 | 1 | 100.0% |

Era is not audited here: it derives from the hit year, which an excluded row usually lacks. Judging a discarded row's era is a human call, not something to infer.

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

5 of 8 rows fall below high confidence.

**These diverge by 2.0 years.** The dataset is too soft to read the pooled median as a point estimate.

## Bounded-date sensitivity (pooled, primary clock)

| Treatment | Median |
|---|---|
| bounded rows dropped | 8.0 yr (95% CI 7.0-10.0), n=7 — **too small to read as a finding** |
| all rows, span midpoints | 8.0 yr (95% CI 6.0-10.0), n=8 — **too small to read as a finding** |
| all rows, earliest possible | 8.0 yr (95% CI 6.0-10.0), n=8 — **too small to read as a finding** |
| all rows, latest possible | 8.0 yr (95% CI 6.0-10.0), n=8 — **too small to read as a finding** |

A bounded date records that sources bracket an event without pinning it. 1 of 8 rows carry one, and every figure here is pooled across buckets and hit bases, so this run qualifies the pooled median, not the revenue-strict headline.

The envelope rows show the full range the data permits; the midpoint row is the pooled median.

## All clocks, pooled

| Clock | Median |
|---|---|
| `clock_education` | 8.0 yr (95% CI 6.0-10.0), n=8 — **too small to read as a finding** |
| `clock_age18` | 14.2 yr (95% CI 11.0-19.0), n=8 — **too small to read as a finding** |
| `clock_venture` | 3.0 yr (95% CI 2.0-9.0), n=7 — **too small to read as a finding** |
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

Per-slice medians need roughly 30 rows each before they mean anything. Slices below that are flagged above.

## By era (primary clock)

| Era | Median |
|---|---|
| post1995 | 8.0 yr (95% CI 7.0-10.0), n=7 — **too small to read as a finding** |
| pre1995 | n=1, too few to summarise — **too small to read as a finding** |

Per-slice medians need roughly 30 rows each before they mean anything. Slices below that are flagged above.

## By country (primary clock)

| Country | Median |
|---|---|
| CN | n=1, too few to summarise — **too small to read as a finding** |
| KR | n=1, too few to summarise — **too small to read as a finding** |
| SE | n=1, too few to summarise — **too small to read as a finding** |
| US | 8.0 yr (95% CI 5.5-39.0), n=5 — **too small to read as a finding** |

Per-slice medians need roughly 30 rows each before they mean anything. Slices below that are flagged above.

## Stopping rule

Revenue-strict n = 4, CI half-width 2.25 yr (threshold 1.00).

Wave-over-wave median history is tracked in `analysis/wave_medians.txt`; the rule needs three wave medians before it can fire.
