# Second Pilot Review — under the revised frame

Ten people, re-coded under the rules adopted after `PILOT-REVIEW.md`. No new
people were added. Commit `054bed4`; validator reports `10 rows checked, 0 errors`.

**Verdict: proceed to wave 1 after one small addition.** See §6.

---

## 1. Did the fallback-lag defect close?

Yes, decisively, on the row that exposed it.

| | first pilot | second pilot |
|---|---|---|
| p04 Moore `a5_first_hit` | 1971 (Intel IPO, `fallback`) | 1959-1960 (Fairchild `rev10`, `primary`) |
| p04 `clock_education` | **17.0** | **5.5** (envelope 5-6, `bounded=true`) |

An 11.5-year correction, close to the ~6 years the first review predicted. The
bound comes from a single Computer History Museum document that carries both
ends: Fairchild Semiconductor sales ~$500,000 in 1958 (below the 1958 bar of
$897,674) and ~$21,000,000 in 1960 (23x the 1960 bar of $919,417). No
FSC-only 1959 figure exists there, so the crossing is bounded, not pinned —
which is exactly what the bounded-date machinery was built for.

**Does any row still record a hit later than the real crossing? No.** The two
rows where that was still true — p03 Yanai and p10 Zhang Yin — are now
`excluded` rather than carrying a known-late IPO date. That is the rule working
as designed, and it is also the source of this review's main finding (§5).

Worth stating plainly: the correction was not mostly the fallback ban. It was
**constant dollars**. The 1960 `rev10` bar is **$919,417**, not $10M. Under the
old nominal threshold Fairchild would have had to be ~11x larger in real terms
before it counted, and the crossing would have been undatable no matter how good
the sourcing was.

## 2. What is the `primary` share now?

**50.0%** — 4 of 8 included rows (`primary` 4, `equivalent` 3, `fallback` 1).
The first pilot came in at 20% against a spec forecast of ~50%. The forecast is
now met exactly.

This is the single largest practical result in this review. The stopping rule
tracks the revenue-strict subset, so at 20% the floor of 30 revenue-strict rows
implied a total N near **1000**. At 50%, with the observed 20% exclusion rate,
it implies a total N near **75**.

Treat that as an order-of-magnitude estimate, not a plan. It rests on a share
measured from 8 rows. But the difference between "about 75 people" and "about
1000 people" is the difference between a project that finishes and one that
does not.

The CI arm of the stopping rule is not currently binding: half-width is 2.25 yr
at n=4 against a 1.0 threshold, and scales roughly as 1/sqrt(n), so it should
clear around n≈20 — before the n=30 floor. Expect the floor to be what fires.

## 3. Unknown rate

**6 of 60 anchors = 10.0%**, up from 8.3%. Bounded dates did **not** reduce it,
and it is worth being precise about why, because the naive reading is wrong:

- The one bounded date (p04) replaced a *sourced but wrong* date, not an unknown.
- p08's unknown was cleared by reaching SEC EDGAR, not by bounding.
- The increase is entirely p03's `a5` becoming unknown on exclusion.

So bounded dates bought accuracy, not coverage. That is still worth having, but
the spec should not claim the feature reduces unknowns.

**A tooling result that outranks the data changes:** SEC EDGAR *is* reachable.
The first pilot recorded five straight 403s and excluded Robin Li over one
missing table cell. EDGAR rejects the fetch tool's default User-Agent but serves
`curl` with a declared one. The audited statement of operations in Baidu's F-1
supplies the 2003 row the summary table omits — RMB 38.6M net at the pegged
8.2765/US$ = US$4.67M against a 2003 bar of $5,715,297, below; 2004 = US$13.4M,
above. So p08 **pins to 2004 exactly**, better than the `2003-2004` bound the
plan anticipated, and at `high` confidence.

Every future wave should use the header-bearing fetch for EDGAR. For US public
companies this converts the most common `fallback` case into `primary`.

## 4. Do the sensitivity runs disagree with the headline?

| | median | n |
|---|---|---|
| Revenue-strict (headline) | **7.5 yr** (95% CI 5.5-10.0) | 4 |
| All commercial | 7.0 yr (95% CI 5.5-10.0) | 5 |
| Pooled | 8.0 yr (95% CI 6.0-10.0) | 8 |
| Confidence: high-only | 10.0 yr (95% CI 6.0-39.0) | 3 |
| Confidence: all rows | 8.0 yr (95% CI 6.0-10.0) | 8 |
| Bounded: dropped / midpoint / earliest / latest | 8.0 / 8.0 / 8.0 / 8.0 | 7 / 8 / 8 / 8 |

**Strictness: agrees.** Revenue-strict and pooled differ by 0.5 yr. At the first
pilot this comparison was meaningless (n=2 revenue-strict); it is still too small
to lean on, but it is no longer absurd.

**Confidence: diverges by 2.0 yr, and the divergence is noise.** The report says
so, correctly and automatically. But the high-only median rests on 3 rows, one of
which is Karikó's 39-year clock. At n=3 this run reports sampling variance, not
softness. The warning is firing for the right reason at the wrong scale — it
should be read as "wait for n" rather than "the data is soft."

**Bounded: no effect, and the report now says so instead of implying otherwise.**
One row of ten is bounded, spanning one year, so all four treatments return 8.0.
Before the Task 5 fix this table would have printed four identical numbers under
prose claiming to show "the full range the data permits." It now states the group
size and says nothing was varied. That fix earned itself here.

## 5. New defects the revised rules introduced

**5.1 — The exclusion rule is correlated with era and geography. This is the
serious one.**

| cross-cut | frame floor | first pilot | now |
|---|---|---|---|
| pre-1995 hit | >= 25% | 2/10 = 20% | **1/8 = 12.5%** |
| non-US | >= 30% | 5/10 = 50% | 3/8 = 37.5% |
| women | >= 20% | 4/10 = 40% | 3/8 = 37.5% |

Both exclusions (p03 Yanai, JP; p10 Zhang Yin, CN) are pre-1995 and non-US, and
one of the two is a woman. That is not coincidence. The fallback ban excludes
precisely the ventures whose early revenue was never published, and "never
published early revenue" correlates almost perfectly with *old*, *non-US*, and
*privately held before scale*.

The failure mode at wave scale: to hit a 25% pre-1995 quota you must research far
more pre-1995 candidates than you keep, and the ones that survive are
disproportionately US companies with early SEC filings. The revised frame traded
one bias (fallback lag inflating pre-1995 clocks) for a different one (pre-1995
careers dropping out of the sample), and the second is harder to see because
excluded rows leave no trace in any median.

I checked whether a founding-year lower bound would rescue these two — a company
cannot have revenue before it exists, so a founding year is a *sourced* lower
bound, not an inference. It does not rescue either row: Zhang Yin's ventures
bracket to [1990, 2003] = 13 years, over `MAX_SPAN_YEARS`, and Yanai's hit entity
is a going concern his father founded, so its own founding bounds nothing. The
rule is still worth adding to the frame, because it will rescue rows at wave
scale where the entity is young at the crossing. It just does not help here.

**5.2 — `rank1` collapses `clock_venture` to zero.** p06 Meeker now has
`a4 = a5 = 1996`: "The Internet Report" and the first #1 ranking are the same
event. `clock_venture = 0.0` for that row is not a short venture-to-hit gap, it
is a category error — `rank1` measures recognition, not a venture. Low priority:
`clock_venture` is not the headline and the spec already treats per-clock slices
as secondary. But those rows should be dropped from the venture clock rather than
reported as zeros.

**5.3 — Meeker moved 23 years.** `fund100` (2019, Bond Capital) → `rank1` (1996,
Institutional Investor All-America Research Team). This confirms the first
pilot's diagnosis that `fund100` mis-dates analysts, and it is the second-largest
correction in the pilot after Moore. Confidence is `medium`, not `high`: the
source asserts she "reigned over the category since its 1996 introduction"
rather than printing the 1996 table.

## 6. Verdict

**Proceed to wave 1, after adding an exclusion audit to the report.**

The revision achieved what it was for. Defect A is closed and verified on the row
that exposed it. The `primary` share went from 20% to the forecast 50%, cutting
the implied total N from ~1000 to ~75. EDGAR is unlocked. The bounded-date and
sensitivity machinery works and, after the Task 5 fixes, fails loudly when it is
being fed nothing.

I do not think §5.1 justifies a third revision round before any data is
collected. It justifies **measuring it from wave 1 onward**. Specifically, add
one section to `analysis.md`: exclusion count and rate broken out by era,
geography, and gender, printed every wave. Excluded rows currently vanish from
every table in the report, which is exactly how a selection effect of this shape
goes unnoticed until N is large and the research spend is sunk.

That is a small change to `src/report.py` and it should be made before wave 1,
not after — the cost of adding it later is that waves 1-2 are already coded and
the comparison baseline is gone.

Two smaller items to fold into the same change or the frame:

- State the founding-year lower-bound rule explicitly (§5.1). It costs nothing
  and converts some future exclusions into bounded `primary` rows.
- Exclude `rank1` rows from `clock_venture` (§5.2).

Do **not** widen `MAX_SPAN_YEARS` to rescue p03 and p10. A 13-year bound carries
almost no information about a median near 8, and the midpoint of such a span is a
fabrication dressed as data. If those careers matter enough to keep, the correct
treatment is interval censoring with a censoring-aware estimator — real work, and
not worth building until the exclusion audit shows how many rows are affected.

### What this review does not establish

Every figure above is flagged **too small to read as a finding**, correctly. n=8
included, n=4 revenue-strict. Nothing here is a result about how long an
apprenticeship takes. This review is about whether the instrument is sound
enough to start collecting, and the answer is yes.

The survivorship caveat from spec §1 stands undiminished and is not fixable by
any amount of N: this sample is conditioned on the outcome. Whatever median
wave 1 produces describes time-to-hit **among people who made it**, and says
nothing whatever about the odds of making it.
