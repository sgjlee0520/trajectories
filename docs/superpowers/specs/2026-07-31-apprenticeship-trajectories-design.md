# Apprenticeship Trajectories — Design

**Date:** 2026-07-31
**Status:** Approved, pending implementation plan

## 1. Purpose

Measure how long it actually takes to go from "starting out" to "first meaningful success,"
using dated career anchors from a large, deliberately balanced sample of people who reached
outlier outcomes across many fields.

The deliverable is a **distribution**, not a collection of biographies. The anecdotes are raw
material; the median and its error bar are the product.

### Research question

> Given that someone eventually succeeded, how many years elapsed between when they started
> and when their first real hit landed — and how much does that vary by field, era, and
> geography?

### What this explicitly does not answer

This is a sample conditioned on the outcome. Everyone in it succeeded. The resulting median
therefore describes **time-to-hit among winners**, and says nothing whatsoever about the
probability of becoming one. Any use of the output must carry this caveat; it is printed in
the analysis output itself, not left to memory.

### Non-goals

- Applying the finished number to the author's own timeline. That is a separate project
  that cannot start until the number exists.
- Estimating odds of success, base rates, or failure counts.
- Any database, web app, or UI. Output is CSV and Markdown.

## 2. Pipeline

Four stages, each producing a file the next stage reads. Hard boundaries so an error in a
later stage never forces a redo of an earlier one.

```
frame.md        quotas, cross-cuts, named source lists   (hand-written, frozen first)
   |
   v
roster.csv      candidate names + bucket + source + why  (approved before research runs)
   |
   v
anchors.csv     6 dated anchors x (date, source, conf)   (waves; the expensive stage)
   |
   v
clocks.csv      computed clocks per person
analysis.md     medians, CIs, slices, caveats
```

**Ordering is load-bearing.** The frame is frozen before names are chosen; the roster is
frozen before dates are collected. This prevents the sample from drifting toward whoever
turned out to have convenient documentation.

## 3. Sampling frame

### Field quotas (proportions, applied cumulatively)

| Bucket | Share |
|---|---|
| Software & internet | 25% |
| Hardware & deep tech | 15% |
| Consumer, retail & industrial | 13% |
| Science & research | 12% |
| Investors & finance | 10% |
| Media & creators | 10% |
| Healthcare & biotech | 10% |
| Trade, import & logistics | 5% |

### Enforced cross-cuts

- Non-US primary career: **>= 30%**
- First hit before 1995: **>= 25%**
- Women: **>= 20%**

These are floors, checked against the cumulative sample after every wave. A wave that would
push any cross-cut below its floor is rebalanced before research begins.

### Named source lists

Every roster entry cites the list it came from. No name enters by free recall.

- Forbes 400 (self-made score 6–10) and Forbes World's Billionaires (self-made)
- Midas List, Midas List Europe
- Fortune 40 Under 40
- Nobel Prizes (Physics, Chemistry, Medicine, Economics); Turing Award; Fields Medal;
  Breakthrough Prize
- Time 100
- Y Combinator Top Companies
- Hurun Rich List (China, India)
- Nikkei / Toyo Keizai rankings (Japan)
- Maeil Business / Chosun Ilbo rankings (Korea)
- Sunday Times Rich List (UK)
- Pulitzer Prize, Academy Awards, Grammy Awards (media & creators)
- Endeavor Entrepreneur network (emerging markets)

## 4. Row schema

One row per person in `anchors.csv`.

### Identity block

`person_id`, `name`, `bucket`, `source_list`, `country_primary`, `gender`, `birth_year`

### Anchors

Each anchor stored as three columns: `<anchor>_date`, `<anchor>_src`, `<anchor>_conf`.

| Anchor | Definition |
|---|---|
| `a1_birth` | Birth year. |
| `a2_education_end` | Date of last formal credential, or of dropping out. |
| `a3_first_domain_job` | First full-time paid work in the field of the eventual hit. |
| `a4_first_venture` | First thing they founded or independently authored. |
| `a5_first_hit` | **Load-bearing.** See threshold definition below. |
| `a6_scale_hit` | When the thing they are famous for now became that. Best-effort. |

### Trailing columns

`hit_entity`, `hit_criterion`, `excluded` (bool), `exclusion_reason`, `notes`

### `a5_first_hit` threshold definition

The **earliest** date on which the person's own venture or work crossed **any** of:

- $10M+ annual revenue
- IPO
- Acquisition above $50M
- A top-tier field prize (Nobel, Turing, Fields, Pulitzer, Academy Award)
- 1M+ users, customers, or audience for something they created

Record which criterion fired in `hit_criterion`. Where multiple criteria are met, take the
earliest date and record that criterion.

### Date precision

**Year precision throughout.** The output is a median measured in years; month-level
precision is false precision that costs real research time for no gain.

## 5. Verification standard — cite-or-flag

- Every anchor carries a `_src` URL and a `_conf` value of `high` / `medium` / `low`.
- An anchor not found after **two** source attempts is recorded as `unknown` with
  `_conf = none`. **It is never inferred.** A plausible-looking guessed date is the precise
  failure mode this whole design exists to prevent, because it is invisible in the output
  and moves the median.
- A row with `a5_first_hit = unknown` is **excluded from all medians**, but retained in the
  file with `excluded = true` so the exclusion rate stays visible.

### Audit (the one runnable check)

After each wave, **15% of that wave's rows** are independently re-researched by a second
agent that cannot see the first agent's answers. If the two passes disagree on
`a5_first_hit` by more than one year on **more than 10%** of audited rows, the entire wave
is void and re-runs.

Without this audit, "cite-or-flag" is a claim rather than a verified property of the data.

## 6. Wave protocol and stopping rule

There is **no fixed target N.** The sample grows until the median stabilizes.

### Waves

- Wave size: **25 people**.
- Each wave is filled **quota-proportionally**, allocated by the largest-remainder method
  against cumulative targets, so that the sample composition at any N matches the frame.
- Rationale: growing the sample by whichever names are easiest to research next causes
  composition drift toward well-documented US software figures as N rises, which would make
  a "stabilizing" median partly an artifact of the sample changing shape.

### Stopping rule (pre-registered, fixed before wave 1)

After each wave, compute the median and a 95% bootstrap confidence interval for the primary
clock (`education_end -> first_hit`). Stop when **both** hold:

1. The median moved **< 0.5 years** across two consecutive waves, **and**
2. The bootstrap CI half-width is **<= 1.0 year**

### Hard floor

**The median is not examined at all before N = 30.**

This guards against optional stopping. Checking after every wave and stopping the moment the
number looks settled preferentially stops on waves where noise happened to be small, which
produces a median that appears more precise than it is. The rule is fixed in advance
specifically so that the stop is honest.

### Expected N

Median standard error scales as approximately `1.25 * sigma / sqrt(n)`. Assuming
`sigma ~ 6 years`:

| N | CI half-width |
|---|---|
| 30 | ±2.7 yr |
| 100 | ±1.5 yr |
| 200 | ±1.0 yr — rule expected to fire |
| 400 | ±0.7 yr |
| 800 | ±0.5 yr |

Expect the rule to fire around **N = 150–250**. This is a forecast, not a target; the
bootstrap reports the truth regardless of whether sigma comes in above or below 6.

## 7. Pilot

Before wave 1: **10 people, end to end, through all four stages.**

The 10 are chosen deliberately to stress the schema, not to be representative:

- a career-switcher (tests whether `a3_first_domain_job` has a defensible answer)
- a research scientist
- a non-US operator
- someone whose hit predates 1980
- someone whose hit is an artistic work rather than a company
- and five ordinary cases for contrast

**Purpose:** find out whether `a3_first_domain_job` and `a5_first_hit` survive contact with
awkward careers. If a definition breaks, it breaks across 10 rows rather than 200.

The pilot is about schema survival, not sample size, and is unaffected by the open-ended N.

## 8. Analysis outputs

`clocks.csv` computes, per person, from the stored anchors:

- `clock_education` = `a5_first_hit - a2_education_end`
- `clock_age18` = `a5_first_hit - (a1_birth + 18)`
- `clock_venture` = `a5_first_hit - a4_first_venture`
- `age_at_first_hit` = `a5_first_hit - a1_birth`

`analysis.md` reports:

- Median and IQR for each clock, pooled
- Median and IQR for each clock, sliced by bucket, era, and geography
- Distribution of age at first hit
- **Sensitivity run:** medians computed on `conf = high` rows only, printed side by side
  with medians on all included rows. Where these diverge, the report states so rather than
  presenting the more attractive figure.
- **Per-slice N and CI printed next to every sliced median.** Per-bucket medians stabilize
  far later than the pooled median — each bucket needs roughly its own 30 rows before its
  median means anything, making reliable field-level comparison an N≈400 proposition. The
  pooled median will look settled while per-field contrasts are still noise, so every slice
  is annotated to make a 12-person bucket unreadable as a finding.
- The survivorship caveat from §1, stated in the document.

## 9. Repository layout

```
~/trajectories/
  docs/superpowers/specs/     this spec
  frame.md                    frozen sampling frame
  data/
    roster.csv
    anchors.csv
    audit.csv
  analysis/
    clocks.csv
    analysis.md
```

## 10. Known limitations

1. **Survivorship.** Sampled on the outcome; describes winners only. Stated in output.
2. **Documentation bias.** Even within named lists, better-documented people yield
   higher-confidence anchors. The confidence tiers and sensitivity run make the size of this
   effect measurable rather than eliminating it.
3. **`a3_first_domain_job` requires judgment** for career-switchers. The pilot exists to
   find out how often, and to fix the rule before scale. Because all six anchors are stored
   rather than a single pre-computed clock, a later change to how "domain" is read can be
   applied in post without re-researching anyone.
4. **List bias is inherited, not removed.** The quotas and cross-cuts bound it and make it
   visible; they do not eliminate it.
