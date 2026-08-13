# Known biases

Every bias this design is aware of, what direction it pushes the number, and
whether anything mitigates it. Read this before quoting any median from
`analysis/analysis.md`.

The short version: **this is a sample of extreme winners, dated at a modest
milestone.** Both halves of that sentence bias the answer, and they bias it in
opposite directions.

---

## 1. Survivorship — the missing denominator

Everyone in the sample succeeded. Nobody appears who worked at it for twelve
years, or twenty, and never crossed the threshold. **Those people exist in
enormous numbers and no list samples them.** They are not rare, they are not
unserious, and many of them worked exactly as hard as the people in this
dataset. They are simply invisible to every sampling frame available.

So a median of 8 years supports:

> Among people who eventually hit, the middle one took about 8 years.

It does not support:

> If I start now, I have about a 50% chance of hitting within 8 years.

The second needs a denominator — everyone who started — and this dataset has
none. Timing how long lottery winners held their tickets gives a real number,
correctly computed, that says nothing about whether buying tickets is wise.

**Direction:** not a bias in the median's *value* so much as a hard limit on
what the value can mean. It cannot be corrected by more data. N=1000 makes the
median precise and leaves it exactly as uninformative about odds.

**Mitigation:** none possible. Stated in `analysis.md` above every figure.

## 2. Extreme-outcome selection, modest-milestone dating

The buckets are filled from Forbes, Midas, Nobel, Hurun, Fortune, the Academy
Awards — lists that select the very top. But each person is dated at their
**first $10M-constant crossing**, a milestone most of them passed decades
before the achievement that got them listed.

That combination is deliberate and mostly favorable: it measures the early
stretch of the trajectory, which is the part a person standing at the start is
actually in. But people who ultimately reached Bezos scale probably crossed
$10M *faster* than people who crossed $10M and stopped there — and the latter
never enter the sample to say so.

**Direction: biases the median SHORT.** Treat it as a floor for a normal
successful career, not a typical value.

**Mitigation:** none in the data. The frame cannot sample "moderately
successful" people because no list enumerates them.

## 3. Selection into `primary` is non-random

The revenue-strict headline uses only rows where a `$10M` crossing could be
dated. A crossing is datable mainly when the company disclosed revenue early —
which happens for companies that IPO'd young, filed early, or grew fast enough
to be newsworthy. Slow builders whose revenue first appears in an IPO
prospectus fifteen years later cannot be dated at all.

**Direction: biases the headline SHORT.** The fast risers are over-represented
in exactly the subset the stopping rule tracks.

**Mitigation:** partial. The definition-strictness run prints revenue-strict,
all-commercial, and pooled medians side by side, so divergence is visible.

## 4. Exclusion correlates with era and geography

A row whose crossing cannot be dated or bounded is excluded. That correlates
almost perfectly with *old*, *non-US*, and *privately held before scale* —
because those are the ventures that never published early revenue.

Observed in the second pilot: non-US rows excluded at 40%, US rows at 0%.
Pre-1995 rows fell to 12.5% against a 25% frame floor. `trade_import_logistics`
came in at 100% excluded — the entire bucket.

**Direction:** narrows the sample toward recent US companies with early
filings. Effect on the median is unsigned but the *composition* is provably
skewed, which makes any era or geography slice untrustworthy before it is
unreadable.

**Mitigation:** the exclusion audit prints exclusion counts and rates by
geography, gender, and bucket in every wave's report. It is the only table
where this is visible, since excluded rows appear nowhere else.

## 5. Fallback lag (largely fixed, not gone)

Where revenue is undisclosed, an IPO or $50M+ acquisition stands in. Both
typically happen years *after* the real crossing. This produced the first
pilot's worst row: Gordon Moore dated at Intel's 1971 IPO, about eleven years
late, giving a 17-year clock against a true ~5.5.

**Direction: biases affected rows LONG.**

**Mitigation:** mostly closed. The fallback is now barred whenever revenue is
documented from *after* the crossing, and constant-dollar thresholds let old
companies qualify on their real early figures. Residual lag remains on rows
that legitimately use the fallback — `hit_basis` tags every one, and the
strictness run isolates them.

## 6. The threshold itself is a choice

`$10M` in constant 2026 dollars is a judgment, not a natural boundary. It was
chosen as "unambiguously a real business." Constant dollars removes the era
bias a nominal figure would carry — the 1960 bar is $919,417 — but the level is
still arbitrary, and a different level would produce a different median.

**Direction:** unknown. A lower bar would shorten every clock; a higher bar
would lengthen them and shrink the sample.

**Mitigation:** the six raw anchors are stored per person, so the threshold can
be re-cut in post without re-researching anyone.

## 7. Non-commercial equivalents are not commensurable

A Nobel, a million-person audience, and a $100M fund are treated as equivalent
to $10M in revenue. They are not the same kind of event and there is no
principled exchange rate. Pilot 1 showed `fund100` mis-dating analysts by 23
years, which is why `rank1` exists.

**Direction:** unknown per criterion; adds variance to the pooled median.

**Mitigation:** the revenue-strict median is the headline precisely so the
mixing never enters the reported number. Pooled is printed alongside it, and
divergence is stated.

## 8. Anchor definitions are judgment calls

`a2_education_end` for a dropout, `a3_first_domain_job` for someone who never
held a job in the field before founding, `a4_first_venture` for a writer whose
first "venture" is an essay — each is a defensible reading with a defensible
alternative. Pilot rows carry explicit `JUDGMENT CALL` notes where this bit.

**Direction:** unknown, but not random — a single researcher applying a
consistent reading produces consistently shifted anchors.

**Mitigation:** all six anchors stored raw; a 15% blind re-research audit each
wave, voiding the wave above 10% disagreement.

## 9. Confidence is uneven

In the second pilot, 7 of 10 rows carried at least one anchor below `high`
confidence.

**Direction:** unknown; adds noise rather than skew.

**Mitigation:** the confidence sensitivity run prints high-only against
all-rows medians and states the divergence.

## 10. English-language sourcing

Research is conducted in English with occasional Japanese and Chinese sources.
Non-US careers are systematically less documented at the level of detail this
frame requires, which is a major driver of bias 4.

**Direction:** compounds the geographic narrowing in bias 4.

**Mitigation:** none currently. Non-US quota floors force the attempt, and
failures land visibly in the exclusion audit rather than disappearing.

## 11. Current-list bias

Forbes and Hurun list people who are rich *now*. Someone who crossed $10M in
1994, built a real company, and lost it in 2001 appears on no current list.

**Direction:** removes a whole class of genuine hits — those that did not
persist — from the sample.

**Mitigation:** none. Prize and award lists are historical and partially offset
this within their buckets.

---

## Which way does it all point?

| Bias | Direction on the median |
|---|---|
| 2. Extreme winners, modest milestone | **shorter** |
| 3. Non-random selection into `primary` | **shorter** |
| 5. Residual fallback lag | longer |
| 4, 10, 11. Exclusion, language, current lists | composition, not level |
| 6, 7, 8, 9 | unsigned |

The two strongest identified effects both push **short**. The working
assumption should therefore be that the true median for a normal successful
career is **longer** than whatever this study reports — that the number is a
floor.

And bias 1 sits above all of it, uncorrectable: however precise the figure
becomes, it describes people who made it. The ones who worked twenty years and
did not are absent by construction, not by rarity.
