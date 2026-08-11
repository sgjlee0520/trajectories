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

`hit_entity`, `hit_criterion`, `hit_basis`, `excluded` (bool), `exclusion_reason`, `notes`

### `a5_first_hit` threshold definition

**$10M annual revenue, in constant 2026 US dollars, is the primary criterion.**
Non-commercial buckets get one fixed equivalent each, specified here rather than chosen per
person, so that no coder ever decides what counts as a hit while looking at a specific
career.

#### The threshold is in constant 2026 dollars

`rev10` means **$10M in constant 2026 US dollars**, not $10M nominal. A nominal threshold
would demand that a 1960 founder build a business roughly eleven times larger in real terms
than a 2020 founder to trigger the same "first hit", which inflates every pre-1995
apprenticeship — and the frame requires at least 25% of those.

Look up the nominal threshold for a revenue year with:

    python3 -m src.cpi 1960

For non-USD accounts, convert at the **spot rate for the revenue year**, then compare against
that year's nominal threshold.

#### Commercial buckets

Software & internet, hardware & deep tech, consumer/retail/industrial, healthcare & biotech,
trade/import/logistics:

| Rank | Criterion | Code | `hit_basis` |
|---|---|---|---|
| 1 | First year the person's own venture reached the constant-dollar **$10M threshold** | `rev10` | `primary` |
| 2 | Earliest of IPO or acquisition above $50M constant 2026 dollars | `ipo` / `acq50` | `fallback` |

The fallback is **permitted only when no earlier crossing is known to have occurred.** If
sources establish that the venture passed the threshold in an earlier year that cannot be
pinned exactly, record a bounded `rev10` date instead — see Bounded dates below. If it cannot
even be bounded, the row is `excluded = true` with reason `crossing_undatable`. Dating such a
row by a later IPO is forbidden: it produces a confidently sourced answer that is years wrong.

**What "known" means here.** A qualitative claim in a source — that the venture
was already large, profitable, or industry-leading by a stated year — is enough
to establish that an earlier crossing occurred, even with no dollar figure
attached. Only the *year* needs pinning or bounding, not the crossing itself.
So a company that first disclosed revenue at IPO has a known earlier crossing
whenever any source describes it as substantial beforehand, and the fallback is
barred. Use the fallback only when no source suggests the venture reached
meaningful scale before the IPO or acquisition — which, for a company large
enough to list, is rare. Expect exclusion or a bounded date to be the normal
outcome, and the fallback to be the exception.

#### Non-commercial buckets

| Bucket | Equivalent | Code | `hit_basis` |
|---|---|---|---|
| Science & research | Top-tier prize: Nobel, Turing, Fields, or Breakthrough. **Record the announcement year**, not the prize's official designated year, because the announcement is when recognition actually landed — Karikó's Breakthrough Prize is officially the 2022 prize but was announced 9 September 2021, so the anchor is 2021. | `prize` | `equivalent` |
| Media & creators | 1M+ audience for their own work | `aud1m` | `equivalent` |
| Investors & finance — fund managers | First fund closed above $100M constant 2026 dollars where the person was a named general partner | `fund100` | `equivalent` |
| Investors & finance — analysts, economists, and other non-fund finance careers | First year the person topped a recognized industry ranking, such as the Institutional Investor All-America Research Team | `rank1` | `equivalent` |

`investors_finance` uses **two criteria, chosen by career type**: `fund100` for fund managers,
`rank1` for everyone else. `fund100` alone mis-dates analysts badly: Mary Meeker was among the
most influential people in technology investing roughly 23 years before Bond Capital's 2019
debut fund. Where no recognized ranking exists for a person, the anchor is `unknown` and the
row is excluded — that is honest, and better than dating a career by an event that came
decades late.

#### Bounded dates

When sources establish that an event happened within a range but not which year, record the
anchor as `YYYY-YYYY` — low year first, at most 10 years wide (arithmetic difference, so
1960-1970 is the widest permitted range), with a source for the bound.
Clocks use the midpoint; the report prints a sensitivity run with bounded rows excluded so the
uncertainty stays visible.

A bounded date is a real measurement, not a guess. `1960-1961` says the sources place the
event in those two years — whether that is two sources bracketing it from either side, or one
source stating the range directly. It is not licence to widen a range until it contains a year
you like.

#### Resolution

Record the code in `hit_criterion` and the tier in `hit_basis`. Where multiple criteria are
met, take the **earliest** date and record the criterion that fired at that date.

**The pooled median mixes definitions.** This is a known and accepted cost of keeping the
full frame; §8 requires the revenue-strict median to be reported alongside it so the size of
the effect is always visible.

### Date precision

**Year precision throughout**, with bounded dates permitted where sources
bracket an event without pinning it (`YYYY-YYYY`, at most 10 years wide
(arithmetic difference, so 1960-1970 is the widest permitted range)). The
output is a median measured in years; month-level precision is false precision
that costs real research time for no gain.

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
clock (`education_end -> first_hit`), on the **revenue-strict subset**
(`hit_basis = primary`). Stop when **both** hold:

1. The median moved **< 0.5 years** across two consecutive waves, **and**
2. The bootstrap CI half-width is **<= 1.0 year**

The rule tracks the revenue-strict median rather than the pooled one because §8 designates
revenue-strict as the headline number, and a rule that fires on pooled stability could stop
while the headline is still noisy. The pooled median stabilizes earlier and is reported
throughout, but does not control the stop.

### Hard floor

**The median is not examined at all before N = 30.**

This guards against optional stopping. Checking after every wave and stopping the moment the
number looks settled preferentially stops on waves where noise happened to be small, which
produces a median that appears more precise than it is. The rule is fixed in advance
specifically so that the stop is honest.

### Expected N

Median standard error scales as approximately `1.25 * sigma / sqrt(n)`. Assuming
`sigma ~ 6 years`:

| Revenue-strict n | CI half-width |
|---|---|
| 30 | ±2.7 yr |
| 100 | ±1.5 yr |
| 200 | ±1.0 yr — rule fires |
| 400 | ±0.7 yr |
| 800 | ±0.5 yr |

Because the rule is evaluated on the revenue-strict subset, **total roster N is roughly
double the n in this table.** Commercial buckets are 68% of the frame, and some share of
those will code as `fallback` rather than `primary`, so `primary` rows are expected to be
roughly half of all rows. Expect the rule to fire at a **total N around 350–500**, reaching
a revenue-strict n near 200.

This is a forecast, not a target; the bootstrap reports the truth regardless of whether sigma
comes in above or below 6, and the realized `primary` share is measured from the pilot
onward rather than assumed.

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
- **Definition-strictness run (required).** Three medians printed together:
  1. `hit_basis = primary` only — the revenue-strict median, $10M constant-dollar revenue and nothing else
  2. all commercial rows — `primary` + `fallback`
  3. pooled — all included rows across every bucket

  Because the pooled median mixes revenue, prizes, audience, and fund size, this run is what
  keeps that mixing honest. If the revenue-strict median and the pooled median diverge
  materially, the revenue-strict figure is the one reported as the headline number and the
  divergence is stated explicitly.
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
5. **The pooled median mixes definitions.** A Nobel, a 1M-person audience, a $100M fund, and
   $10M constant-dollar revenue are not the same event, and pooling them produces a number whose units are
   "reaching the top of your field, whatever that means here." This is deliberate — it keeps
   research careers in the sample — but it is why §8 designates the revenue-strict median as
   the headline and requires all three strictness levels to be reported together.
6. **Revenue disclosure is uneven.** Public and acquired companies document revenue far
   better than private ones, so the `primary` subset skews toward companies that exited. The
   `hit_basis` tag makes this measurable: comparing `primary` against `fallback` medians
   shows how much the exit-visibility effect moves the number.
7. **Selection into the `primary` subset is non-random.** A venture whose
   threshold crossing is datable is one that either disclosed financials soon
   after crossing or was covered in the press at the time — both describe fast
   risers. Slow burners fall to `fallback` or exclusion, so the revenue-strict
   median is likely biased *downward*. Bounded dates reduce this pressure by
   letting a bracketed crossing qualify, but do not eliminate it.
8. **`a3_first_domain_job` has no state for "this never happened."** A
   founder-first career like Sara Blakely's has no prior domain employment, which
   is a fact about the career rather than a research failure, yet the schema can
   only record `unknown` — the same value used when a job certainly existed but
   is undated. The two are conflated in the unknown rate.
