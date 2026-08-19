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

**UPDATE after wave 2 (n=60): the geographic half of this bias did not
survive contact with data.** The pilot's 40% non-US vs 0% US exclusion gap has
closed completely:

| cross-cut | pilot (n=10) | cumulative (n=60) |
|---|---|---|
| US excluded | 0% | 18.2% |
| non-US excluded | 40% | 18.4% |
| women excluded | 25% | 19.2% |
| men excluded | 17% | 17.6% |

All four are now within two points of each other. The pilot's gap was two rows
out of ten — real in the sample, and not a real property of the frame.

What remains is entirely **bucket-level**, which is bias 4c below:
`healthcare_biotech` 66.7%, `consumer_retail_industrial` 37.5%, against 0% for
`hardware_deeptech`, `science_research`, and `trade_import_logistics`. The
mechanism is industry disclosure practice, not geography — and the demographic
correlation the pilot showed was that mechanism in disguise, because the
pilot's two undatable rows happened to be non-US private manufacturers.

This entry is kept rather than deleted. A bias that was hypothesised, measured,
and disconfirmed is a result, and the reasoning that produced it would
otherwise be repeated.

**Mitigation:** the exclusion audit prints exclusion counts and rates by
geography, gender, and bucket in every wave's report. It is the only table
where this is visible, since excluded rows appear nowhere else.

The `trade_import_logistics` case was acted on rather than merely recorded:
after the pilot excluded the bucket entirely, the frame gained `rank1` for it,
dating private importers by published volume rankings instead of revenue they
never disclosed. Zhang Yin was rescued on it and the bucket went 100% to 0%
excluded. That fixes one bucket. It does not fix the general pattern — watch
the audit for the next bucket or region that fails the same way.

## 4c. Confirmed at wave scale: whole buckets fail, not scattered rows

The pilot showed this as a pattern. Wave 1 showed it as a mechanism, in two
buckets whose exclusion is near-total rather than elevated.

`healthcare_biotech` came in at **three of four excluded**, all
`crossing_undatable`. The cause is uniform: private generics, enzyme, API, and
medical-device makers publish nothing until they list, and by then they are two
decades past the bar. Kiran Mazumdar-Shaw has a sourced 1998 figure at 335% of
that year's bar and **no revenue figure for any year 1978-1997** after six
attempts, so the bracket is twenty years. Zhong Huijuan fails the mirror image:
a good 1997 lower end, and the earliest company-level figure anywhere is 2011.

`trade_import_logistics` failed the same way in the pilot, at 100%.

The shape to watch for: a bucket fails when its *industry* keeps revenue
private until listing, not when its people are obscure. Both buckets are full
of famous people with undocumented balance sheets.

**Direction:** removes entire industries rather than random rows, so the
surviving sample over-represents industries that disclose early — software,
semiconductors, anything venture-funded or US-listed.

**Mitigation:** partial and per-bucket. `rank1` rescued the trade bucket by
dating on published volume rankings instead of revenue. No equivalent
third-party series exists for private pharma. The exclusion audit reports the
rate per bucket every wave, which is how this was caught.

## 4a. The trade fix carries its own bias

The mitigation above is not free, and it points the opposite way from bias 4.

The canonical volume ranking for containerized trade is the Journal of
Commerce / PIERS Top 100, built from **US** bill-of-lading data and available
in usable form only from roughly 2000 onward. So `rank1` in this bucket
reliably rescues traders whose freight touches US ports after 2000, and
reliably fails for a Rotterdam-to-Lagos operator, an intra-Asia trader, or
anyone whose career predates the series.

Demonstrated on the row that motivated it: Zhang Yin came back at 2001, which
files `post1995`. Her exclusion was fixed; the pre-1995 shortfall was not
touched. Expect the same shape at wave scale.

**Direction:** narrows the trade bucket toward recent, US-facing operators.
Un-empties the bucket without broadening it.

**Mitigation:** none. Recorded so that a future reader does not mistake a 0%
exclusion rate in this bucket for even coverage of it.

## 4b. The self-description trap

Several biases above are fixed by finding a third-party source. In practice the
failure mode is subtler than "no source exists": a company's own claim to be
the largest propagates verbatim into trade press, LinkedIn, and data-broker
profiles until it is indistinguishable from a ranking in a search snippet.

America Chung Nam's own site says "recognized as a top American exporter to
China since 2001" and names no ranking body. Three broker profiles repeat it.
Coding from those would have produced the correct year by luck. The anchor
instead rests on 2002 trade press attributing the ranking to the Journal of
Commerce, and on JOC's own "10th year in a row" in 2011.

**Direction:** unsigned, but it manufactures false confidence — a wrong year
sourced to three places reads stronger than a right year sourced to one.

**Mitigation:** the frame requires a ranking to be published by a third party
and to name a first year, and the 15% blind re-research audit each wave is the
check that a researcher applied that rule rather than taking the snippet.

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

## 12. Two buckets have no sampling list

`frame.md` names sixteen source lists. None of them enumerates **analysts or
economists**, and none enumerates **freight or trade operators**.

That leaves two buckets sampled by accident rather than by frame. The
`investors_finance` bucket's `rank1` half can only be reached through Time 100,
which admits perhaps a dozen finance people a decade, mostly central bankers.
The `trade_import_logistics` bucket's wave-1 name had to come off Y Combinator
Top Companies — a startup list — because no trade list in the frame enumerates
people at all. Institutional Investor's All-America Research Team and the JOC
Top 100 are named in the frame as *hit-dating* sources, not sampling sources.

**Direction:** these two buckets are drawn from whatever adjacent list happens
to contain someone plausible, which is exactly the free-recall failure the
named-list rule exists to prevent.

**Mitigation:** none yet. Adding an analyst-ranking list and a trade-ranking
list as sampling sources would close it. Recorded here rather than fixed
mid-wave, because changing the frame between waves is itself a bias.

## 13. Roster membership is asserted, then verified late

The named-list rule requires every roster entry to cite the list it came from.
In practice a name is proposed from knowledge and the list is attached to it,
which is recall with a citation rather than sampling from an enumerated list.

Wave 1's roster was built this way. Membership is therefore verified during
*research*, where each person's sources are being gathered anyway, and anyone
whose list membership cannot be confirmed is dropped before contributing to any
median.

**Direction:** unsigned, but it admits the possibility of a name that no list
actually contains — which would silently reintroduce free recall.

**Mitigation:** membership verification is a required output of each research
batch, and failures are reported rather than quietly corrected.

## 14. The sample mixes two sampling designs

Wave 1 and the pilot were collected under enforced cross-cut floors: non-US
>= 30%, pre-1995 hit >= 25%, women >= 20%, with any wave that would breach one
rebalanced before research. Their composition was therefore **steered by hand**
and came in at 50% pre-1995, 69% non-US, 42% women — well above what the source
lists would have produced unaided.

After wave 1 the study author removed the floors. Country, era, and sex are now
recorded covariates only; the sole standard for entry is the money criterion.

**Direction:** unsigned, but it is a discontinuity, not a gradient. Rows 1-35
oversample old, non-US, and female careers relative to rows 36 onward. If the
apprenticeship clock differs by era — and there is good reason to think it
does, since capital availability and market size changed around the internet
era — then the pooled median is a weighted blend of two eras whose weights were
set by a design change partway through, not by anything about the world.

**Mitigation:** the shares are printed every wave, so the drift is visible. The
honest reading once N is large is to report the median for the post-change rows
separately and check it against the pooled figure. Do NOT retro-fit the early
rows out; they are correctly collected data, just collected under a different
rule.

## 15. The audit threshold was unreachable for three waves

`AUDIT_VOID_THRESHOLD` is 0.10 and `AUDIT_FRACTION` is 0.15, so a 25-row wave
audited 4 rows. One disagreement scores 0.25. **The rule as written could never
tolerate a single disagreement** — it meant "perfect reproduction or void,"
which is not what the spec says and not what was intended.

Waves 1 and 2 scored 0.000 and it never surfaced. Wave 3 failed on one row of
four and was declared void.

**Resolution.** The wave was NOT voided on that score. Instead ten wave-3 rows
were re-researched blind on **six independent platforms** — Perplexity, Gemini,
Antigravity (Gemini 3.1 Pro and Opus 4.6), Cursor, and VS Code — none of which
saw the recorded answers or each other's. Result across 60 comparisons:

| | count |
|---|---|
| agree | 46 |
| **conflict** | **0** |
| one side `unknown` | 14 |

**Not one platform contradicted a recorded date.** Every gap was a platform
returning `unknown` where a date exists, which is absence of evidence rather
than evidence against — Perplexity accounted for 5 of the 14, consistent with a
search tool rather than an agent that can work through filings.

`stats.audit_sample` now enforces `MIN_AUDIT_ROWS = 10`, so the smallest
non-zero score is exactly 0.10 and lands at tolerance rather than four times
over it.

**Honesty note on the sequence.** The flaw is structural and was provable
before wave 3 — 4 rows and a 0.10 threshold are incompatible arithmetic
regardless of any result. But it was only noticed once it bit, and the fix was
made after seeing the outcome it produced. That ordering is exactly what
pre-registration exists to prevent, so it is recorded here rather than quietly
corrected. The mitigating fact is that the wave was re-tested with a *stronger*
instrument, not a weaker one, and passed 60-0.

## 16. One disputed row remains unresolved

p75 (Ginkgo Bioworks) is the row that failed wave 3's original audit and it was
NOT among the ten drawn for the cross-check, so it has never been adjudicated
by an independent pass.

Recorded: bounded 2008-2017, upper end a Forbes 2017 estimate of "more than
$20 million" against that year's bar of $7.6M. The second pass instead pinned
2019, the first SEC-audited figure, having missed the Forbes data point — and
pinning to the first *disclosed* figure when the true bound exceeds ten years
is the fallback-lag error this study was rebuilt to eliminate. The recorded
value is the rule-compliant one, which is why it stands.

**Direction:** if the recorded value is wrong it is wrong *early*, and the
error would shorten that row's clock. Add p75 to the next cross-check.

## 17. The education clock is conditioned on documented schooling

The headline clock counts from `a2_education_end`, so a row needs a sourced
year for when formal education ended. Ten otherwise-complete rows lacked one; a
targeted second pass resolved six.

The four that stayed `unknown` are Olugbenga Agboola (NG), Enric Asuncion (ES),
Radhakishan Damani (IN), and He Xiangjian (CN). **All four are non-US.** The
six resolved skew Western and recent.

That is not chance. "When did this person finish school" is well documented for
US and UK figures and poorly documented for Indian and Chinese founders of the
1970s-80s, and for anyone whose path did not run through a credential worth
reporting. So the education clock is silently conditioned on people whose
schooling was recorded — Western, credentialed, recent — even though selection
into the study is money-only.

**Direction:** unsigned on the median itself, but it drops precisely the
careers most likely to differ. A founder with no documented schooling plausibly
started earning earlier, which would *lengthen* their apprenticeship measured
from any fixed start — so the loss may bias the education clock **short**.

**Mitigation:** `clock_age18` (n=36) and `clock_venture` (n=37) do not need an
education year and both carry more rows. All three are printed together, and a
divergence between the education clock and the age-18 clock is the signal that
this bias is biting. Do not switch the headline to a different clock merely
because it has more rows — that is choosing the measurement to get a result.

## 18. Single-pass research has a measured miss rate

Two independent multi-platform passes have now re-examined rows the first pass
gave up on, and the miss rate is not small.

**Cross-check (10 wave-3 rows, 6 platforms):** one row recorded `unknown` was
dated by exactly one platform of six (p62 Shiv Nadar / HCL, from a 1986 India
Today article). Five platforms returned `unknown` on a row where a sourced
answer existed.

**Rescue pass (14 excluded rows, Antigravity/Opus):** of 13 rows excluded as
`crossing_undatable`, **three were datable** — Toni Morrison (a 1998 TIME
interview where she states the million-copy figure herself), Terry Gou (Chinese
sources giving Hon Hai's 1985 revenue), and Kim Sung-joo (Forbes Korea giving
1995 revenue). A fourth, Eileen Burbidge, was mis-labelled rather than
undatable: her funds are all findable and simply never reached the threshold.

So roughly **one excluded row in four was recoverable**, and the recoveries
skew non-US and pre-1995 — Japanese, Chinese, Korean, Indian sources that an
English-first search pass does not reach.

**Direction:** this compounds bias 10 (English-language sourcing). Exclusions
are not a random sample of hard cases; they are disproportionately cases whose
evidence sits in another language or an offline archive. Every exclusion left
standing is therefore weaker evidence of "undatable" than it appears.

**Mitigation:** a second independent pass on excluded rows before any final
median. One rescue candidate was also correctly REJECTED — an *Economist*
guest-network poll offered as a `rank1` ranking for Raghuram Rajan, which is
not a recognised industry ranking. Rescue passes need the same scepticism as
first passes; the rescue is not automatically right because it found something.

## 19. The audit rule was recalibrated against a measured miss rate

Wave 4's audit scored 0.200 against a 0.10 void threshold. Both disagreements
were one pass returning `unknown` where the other found a date. **Neither was a
contradiction** — there were no two datings that could not both be true.

Entry 18 had already measured a single-pass miss rate near 25%, from a
six-platform cross-check and a rescue pass. On ten audited rows that predicts
two to three `unknown`-versus-dated gaps from search thoroughness alone, on
data containing no wrong dates at all. So the rule as written would void
almost every wave regardless of quality.

`audit_disagreement` now counts only contradictions: datings more than a year
apart that do not overlap. Misses are returned separately by `audit_misses` and
treated as **rescue signals** — the better-sourced pass wins and its date is
recorded. Wave 4 rescored 0.000 with one miss each way, and the second-pass
miss became a real row (p107 Verge Genomics, dated 2023 from CB Insights).

**Honesty note on the sequence.** This is the second time a rule has been
changed after it produced a failing result, and that ordering is exactly what
pre-registration exists to prevent. Two things distinguish it from
rationalisation, and a reader should weigh them rather than take the word:

1. The justifying evidence — the 25% miss rate — was measured and written down
   in entry 18 **before** this audit ran, not constructed afterwards.
2. The change makes the test *stricter* about what counts as a real problem. A
   contradiction still voids a wave. What no longer voids one is two
   researchers differing in how hard they looked.

The residual risk is real and is not argued away: a rule that has now been
relaxed twice is a rule with a track record of being relaxed. Any future change
to the audit definition should be treated with more suspicion than this one,
and ideally decided before the result that motivates it is known.

## 20. Verified membership is not the same as sampling from a list

Wave 5's roster was built without web search — the session's budget was gone —
so the agent generated candidate names from memory and then verified each one
against its source list, discarding roughly a dozen that did not check out.

Every surviving name is genuinely on the list it cites. That fixes the wave 4
failure (a citation naming nobody) but it does **not** fix the failure the
named-list rule was written for. Recall proposes the candidate; the list only
ratifies it. A famous Forbes billionaire recalled from memory and then
confirmed on Forbes is still a famous billionaire selected by fame.

The observable damage looks small — wave 5 drew Qin Yinglin (hog farming), Zhu
Gongshan (polysilicon), Xu Hang (medical devices), Martua Sitorus (palm oil),
Kishore Biyani (Indian retail) — not a list of household names. But that is a
judgement about the output, not a property of the method, and it will not hold
every time.

**Direction:** biases toward the more famous members of each list, which
correlates with larger outcomes and probably with faster ones — so it may bias
the median **short**.

**Mitigation:** none applied this wave. The fix is to enumerate the list first
and sample from the enumeration, which requires working search. Where search is
unavailable, this limitation should be recorded on the wave rather than
presented as an equivalent roster.

## 21. Some upper bounds are qualitative, not numeric

`frame.md` says a bounded date needs a figure below the bar in the earlier year
and a figure at or above it in the later year. Two wave-5 rows do not have the
second figure and use a qualitative claim instead:

- **p118 Diane Hendricks / ABC Supply** — ranked #1 on the Inc. 500 in 1986,
  "after which it was too large to list." No dollar figure was ever found.
- **p117 Wang Chuanfu / BYD** — the world's largest NiCd battery maker with 65%
  share by 2002. No RMB revenue figure was located.

Both are almost certainly true and both clear their bars by a wide margin — a
company with 65% of a global market is not near a $5.6M threshold. But the
inference is about *magnitude*, not about the date, which makes it a much safer
class of inference than guessing a year. Both are recorded at `medium`
confidence with the gap stated in the row notes.

**Direction:** unsigned. The risk is not that these dates are wrong; it is that
"clearly very large by year Y" gives no purchase on whether the crossing was in
year Y or several years earlier, so the bound may be wider than the evidence
truly supports and the midpoint correspondingly arbitrary.

**Mitigation:** the confidence sensitivity run separates high-confidence rows
from the rest, and the bounded-date sensitivity run shows what the envelope
does to the median. If either diverges materially, rows like these are why.

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
