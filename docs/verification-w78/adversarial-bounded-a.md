# Adversarial verification — widest bounded anchors (batch A)

Verifier pass, 2026-08-22. Six rows, the widest `a5_first_hit_date` spans in
`data/anchors.csv`. Read-only: nothing in `data/` was touched.

Bars used throughout are `PYTHONUTF8=1 python -m src.cpi <year>` (constant 2026
dollars, expressed nominal for the revenue year):

| year | rev10 bar | year | rev10 bar |
|---|---|---|---|
| 1988 | $3,674,564 | 1999 | $5,174,829 |
| 1990 | $4,059,725 | 2000 | $5,348,773 |
| 1991 | $4,230,563 | 2001 | $5,500,974 |
| 1992 | $4,357,914 | 2002 | $5,587,946 |
| 1993 | $4,488,372 | 2007 | $6,440,333 |
| 1995 | $4,733,757 | 2012 | $7,131,511 |
| 1997 | $4,985,355 | 2017 | $7,613,770 |
| 1998 | $5,063,008 | 2021 | $8,416,707 |
|      |            | 2024 | $9,743,619 |

**Headline: 5 of 6 rows are wrong, all in the same direction — the recorded span
is wider than the evidence requires, so the midpoint the clocks use is off.**
Four rows have a sourced above-bar figure earlier than the one recorded (p12,
p124, p71, and p141 by implication); one row (p121) has sourced below-bar dollar
figures for years after the founding year that were never used. Only p75 holds.

---

## p12 — Judy Faulkner — Epic Systems — current `1988-1997` (span 9)

### Verdict: **TIGHTEN → `1988-1995`** (span 7; midpoint 1992.5 → 1991.5)

**Q1, lower end.** Genuinely sourced, not a founding-year floor. Acquired's Epic
briefing states Epic was "reaching $1.5 million in revenue by 1988"
(https://www.acquiredbriefing.com/p/epic-systems — verified verbatim in the raw
page). $1.5M is 41% of the 1988 bar of $3,674,564. This end is clean.

**Q2, upper end. Not the earliest above-bar figure — and the row's own note
predicted this.** The note says a "$18 million in 1995" figure "is widely
repeated" but that two fetch attempts failed, so it was not relied on. It is
recoverable. The Acquired episode page carries the full transcript; the text is
in the page body but a summarising fetch misses it. Retrieved with `curl` and
grepped directly:

> **David: "So by 1995, they hit $18 million in revenue, up from $1.5 million in
> 1988."**
>
> **Ben: "In 1995, Epic did $18 million. In 1995, Microsoft had gone public and
> shipped Windows 95 and did $6 billion in revenue."**
>
> — https://www.acquired.fm/episodes/epic-systems-mychart

$18,000,000 vs the 1995 bar of $4,733,757 = **3.8x above bar**. This is the same
publisher as the row's existing lower-end source (acquiredbriefing.com is the
Acquired newsletter, and the $1.5M/1988 figure originates in this very transcript
sentence), so accepting one end of the sentence and refusing the other is not
defensible.

The 1997 figure the row currently uses ("In 1997, Epic earned net income of
$6.6 million on sales of $30.9 million",
https://www.referenceforbusiness.com/history2/65/Epic-Systems-Corporation.html)
is confirmed accurate but is **not** the earliest. That directory entry contains
no 1995 revenue at all — verified: its only revenue years are 1997, 2000 and
2002 — which is why the first pass could not close this from there.

**Q3, further narrowing — attempted, rejected.** danielscrivner.com's Epic
breakdown asserts "In 1993, they had 150 employees and $20 million in revenue".
**Rejected as unreliable:** the International Directory entry puts Epic at 49
employees in 1993 and 125 in 1995, and $30.9M of sales on ~200 staff in 1997
(~$155K/head). $20M on 150 staff in 1993 contradicts both the headcount series
and the revenue series and reads as a misdated recollection. A weaker
qualitative signal points the same way as the row's own headcount inference — the
Acquired hosts describe Epic after the 1992 EpicCare launch as having "got enough
functionality that it's not going to stay a small business for long", i.e. still
small in 1992 — but that is not a below-bar dollar figure and is not enough to
move the lower end.

**Proposed correction:** `a5_first_hit_date` = `1988-1995`; `a5_first_hit_src` =
https://www.acquired.fm/episodes/epic-systems-mychart for the upper end, with
https://www.acquiredbriefing.com/p/epic-systems retained for the lower. Confidence
stays `medium`. Keep the referenceforbusiness 1997 citation in notes as
corroboration that the crossing was long past by 1997.

---

## p71 — Radhakishan Damani — Avenue Supermarts (DMart) — current `2002-2012` (span 10, at cap)

### Verdict: **TIGHTEN → `2002-2007`** (span 5; midpoint 2007 → 2004.5), with a stated source-quality caveat

**Q1, lower end.** Founding-year floor. Legitimate per frame.md ("the sourced
founding (or first-production) year of the hit entity brackets a crossing from
below"), and the row says so honestly. **No source establishes DMart below the
bar in any year.** Not a defect, but it is the weaker of the two legitimate
lower-bound types, and it matters more here than elsewhere because a single
large-format Indian supermarket plausibly clears the bar in its first or second
year (see Q3).

**Q2, upper end. This is the defect: 2012 is nowhere near the earliest
above-bar year, and the row's own note shows the researcher stopped where the
RHP summary started.** The note says "No sourced FY figure inside the window that
is still below the bar was located (two attempts: RHP summaries begin at
FY2012)" — but the frame's test is not "the earliest figure in the IPO
prospectus", it is the earliest sourced above-bar figure anywhere.

Earlier above-bar evidence found:

- **FY2006-07: Rs 260 crore.** "D-Mart had revenues of Rs. 260 crores in
  2006-07"; the same case-study text elsewhere as "expanded to Ahmedabad in 2007,
  achieving revenues of 260 CR". Rs 2.60bn at the FY07 average (~45.3 INR/USD)
  = **~US$57M**, or ~US$63M at the calendar-2007 average (~41.3). Either way
  **~9x the 2007 bar of $6,440,333.**
  Sources: https://www.nextbigbrand.in/the-rise-and-rise-of-d-mart-building-supermarts-the-right-way/
  and https://www.tvisha.com/blog/dmart-success-story
- **CY2010: "over Rs 1,000 crore" on ~25 stores** — also far above bar, and
  consistent with the store-count timeline published by the India Brand Equity
  Foundation (a Ministry of Commerce trust): "2010 The store count of the company
  crossed 25 stores ... 2007 The company opened its first store in Gujarat"
  (https://www.ibef.org/industry/retail-india/showcase/D-Mart).

**Source-quality caveat, stated plainly.** The Rs 260 crore figure is a
widely-copied trade/case-study claim, not a filing, and the two pages carrying it
are of lower quality than the row's existing ipocentral.in citation (itself a
secondary IPO blog rather than the RHP). I could not corroborate it from a filing
or a national business title: the DMart RHP restated financials genuinely begin
at FY2012, and the shared WebSearch budget ran out (see Budget note) before I
could work the Business Standard / Forbes India / rating-agency angle.

**If the reviewer rejects blog sourcing, the row still cannot stay at
2002-2012.** IBEF's 25 stores by 2010, set against the RHP's Rs 2,222 crore on
~50 stores in FY2012 (~Rs 44 crore per store), makes an above-bar 2010
near-certain — and the 2010 bar of $6,773,124 is only ~Rs 31 crore, i.e. **less
than one average DMart store's annual sales**.

**Q3, how much narrower the truth probably is.** At Rs ~44 crore per store, the
2003 bar ($5,587,946 at ~46.6 INR/USD = ~Rs 26 crore) is cleared by **a single
store**. The real crossing is likely 2003-2005 — so this is the one row in the
batch where the recorded midpoint (2007) is probably *late* rather than early,
because the founding-year floor is nearly correct while the ceiling is wildly
loose. Either way the recorded span is not a measurement.

**Proposed correction:** `a5_first_hit_date` = `2002-2007`, conf `medium`, citing
the Rs 260 crore FY2006-07 figure with an explicit note that the source is trade
press, not a filing. **Recommend a new open question:** *"What was Avenue
Supermarts Limited's total revenue in any fiscal year from FY2003 to FY2011?
Quote the figure and the source URL."* A single CRISIL/ICRA rating rationale or
an Images Retail "Top Retailers" turnover table would close it and could tighten
this row to a 2-3 year span.

---

## p75 — Jason Kelly — Ginkgo Bioworks — current `2008-2017` (span 9)

### Verdict: **HOLDS**

This is the row I tried hardest to break and could not.

**Q1, lower end.** Founding-year floor (2008), correctly labelled as such in the
notes. No source puts Ginkgo below the bar in any specific later year.
Legitimate per frame.md.

**Q2, upper end — attacked directly, survives.** The recorded upper end is
Forbes' Next Billion-Dollar Startups 2017, "Estimated 2017 revenue: More than $20
million"
(https://www.forbes.com/sites/susanadams/2017/09/26/the-next-billion-dollar-startups-2017/),
$20M vs the 2017 bar of $7,613,770 = 2.6x. The obvious way to beat it is the
prior year's edition of the same list, **so I fetched it: Ginkgo Bioworks is not
on Forbes' Next Billion-Dollar Startups 2016**
(https://www.forbes.com/sites/amyfeldman/2016/10/19/next-billion-dollar-startups-2016/
— all 25 names checked, Ginkgo absent). No earlier dollar figure of any kind
surfaced in the SynBioBeta / BusinessWire Series B coverage, the Century of Bio
company history, or MIT Technology Review's 2021 retrospective. The audited
series in the SPAC 424B3 (2019 $54.184M, 2020 $76.657M) starts later still. 2017
is the earliest sourced above-bar figure that exists.

**Q3, possible tightening — flagged, deliberately not proposed.** Ginkgo was in
**Y Combinator's Summer 2014 batch** (the first biotech YC funded), pitching at
Demo Day that year, before a $45M Series B in July 2015
(https://www.businesswire.com/news/home/20150723005161/en/3552124/Ginkgo-Bioworks-Secures-45-Million-from-Viking-Global-OS-Fund-Y-Combinator-and-Felicis-Ventures).
A company doing YC Demo Day is a seed-stage company, which would argue for a 2014
lower bound and a `2014-2017` span. **I am not proposing it:** "was in a YC batch"
is a stage inference, not a sourced statement that revenue was under $7,353,351,
and manufacturing a tightening from it is exactly the error this pass exists to
catch. Worth a line in notes as the direction a future researcher should push —
ideally by finding a dated 2015 or 2016 revenue figure.

**Proposed correction:** none. Row stands at `2008-2017`, conf `medium`.

---

## p121 — Rodney Brooks — iRobot (IS Robotics) — current `1990-2000` (span 10, at cap)

### Verdict: **TIGHTEN → `1992-2000`** (span 8; midpoint 1995 → 1996). `1993-2000` also defensible.

**Q1, lower end. A founding-year floor that did not need to be one.** The note
says the lower end is "founding August 1990 (company cannot earn before it
exists)". That is legitimate, but the search for below-bar figures stopped too
early. The International Directory of Company Histories entry for iRobot — the
same reference series the p12 row cites for Epic — carries **explicit dated
dollar figures for the early 1990s, all far below bar**:

> "It also led to the introduction of Genghis to the market in 1991. ... **About
> 60 robots a year were sold for $3,000 a piece**, mostly to universities."
> → ~$180,000/yr, **4% of the 1991 bar** of $4,230,563.
>
> "FIRST MAJOR RESEARCH CONTRACT: 1992 ... **The first significant break came in
> 1992 when the company secured $500,000 from the Japanese government** to
> develop minuscule medical robots"
> → $500,000, **11% of the 1992 bar** of $4,357,914 — and explicitly the largest
> revenue event in the company's life to that date.
>
> "**The following year, a $50,000 contract was received** from ... DARPA ... and
> the Office of Naval Research"
> → 1993, **1% of the 1993 bar** of $4,488,372.
>
> "Angle and Greiner, along with six employees, worked for $30,000 a year";
> Greiner to the Wall Street Journal: "There were times when we didn't know how
> we were going to meet payroll, but a grant or project would always somehow come
> through."
>
> — https://www.encyclopedia.com/books/politics-and-business-magazines/irobot-corporation

An eight-person company whose *first significant break* was a $500K contract was
not booking $4.36M in 1992. The lower end should move to **1992** on that stated
dollar figure. **1993** is also defensible (the $50K DARPA/ONR contract, still
~8 staff, payroll uncertainty), giving span 7; I propose 1992 as the conservative
reading, because 1992 has a stated dollar amount while 1993's total revenue is
bounded only qualitatively.

**Q2, upper end — checked, holds.** FY2000 total revenue $10,750K (product
$1,904K + contract $8,846K) is the first line of the S-1's Selected Consolidated
Financial Data, 2.0x the 2000 bar of $5,348,773. I re-downloaded the full S-1
(`curl` with a user agent; SEC 403s the plain fetcher) and swept every occurrence
of `199[0-9]`: **the filing contains no pre-2000 revenue figure of any kind.**
Its only 1990s financial facts are corporate — Series A of 1,336,370 shares at
$1.16 (~$1.55M) in **November 1998**, Series B in August 1999, and a 1998 Hasbro
development-agreement warrant valued at ~$7,000.
https://www.sec.gov/Archives/edgar/data/1159167/000095013505004187/b55709icsv1.htm

That Series A detail cuts *against* the row's speculation that "contract revenue
of $8.8M in FY2000 reads as an established, non-new revenue line" and that a
1990s crossing is "likely": a company raising its first institutional round of
$1.55M in November 1998 was not a $5M-revenue business in 1997. That strengthens
the case for a late-1990s crossing and for the tightened lower end.

**Q3, further narrowing.** Nothing dated between 1994 and 1999 attaches a dollar
figure or an "already large/leading" claim. The 1996 Ariel launch, the 1996
Hasbro IT prototype, the 1998 Hasbro R&D funding and the 1998 DARPA Tactical
Mobile Robot award are all revenue-silent ("Military work remained a key source of
revenue for the company in the late 1990s" — no figure). Five VC rounds totalling
$27.5M spanned 1998-2004. The top of the bracket cannot be closed further.

**Proposed correction:** `a5_first_hit_date` = `1992-2000`; add
https://www.encyclopedia.com/books/politics-and-business-magazines/irobot-corporation
to `a5_first_hit_src` alongside the S-1; conf stays `medium`. This also lifts the
row off the 10-year cap, which is worth doing on its own — a row sitting exactly
on the cap is the row most likely to have been widened to fit.

---

## p124 — Xu Hang — Shenzhen Mindray — current `1991-2001` (span 10, at cap)

### Verdict: **TIGHTEN → `1991-1997`** (span 6; midpoint 1996 → 1994)

**Q1, lower end.** Founding-year floor (1991), correctly labelled. Nothing
establishes Mindray below the bar in a specific later year. The Jiemian history
below does say that from 1992 Mindray shifted focus to R&D, "即便公司的研发人员只有
寥寥数人，利润一度无法覆盖研发费用" (only a handful of R&D staff; profits at one point
could not cover R&D spend) — qualitatively small, but not a below-bar dollar
figure, so I do not propose moving the lower end on it.

**Q2, upper end. Defect: 2001 is not the earliest above-bar figure. 1997 is, by
four years.** The row's upper end is the F-1's Selected Consolidated Financial
Data, whose earliest year is 2001 (net revenues RMB 201.8M ~ US$24.4M). The note
correctly observes that no figure appears earlier *in the filing* and that "a
genuine earlier crossing is likely" — then stops. Chinese-language business media
has the figure:

> **"在1997年末，公司的营收达到了一亿元，两年后，公司的自主研发产品营收也突破了一亿元。"**
> ("At the end of 1997 the company's revenue reached RMB 100 million; two years
> later, revenue from its self-developed products also passed RMB 100 million.")
>
> — 界面新闻 / 阿尔法工场研究院, "迈瑞医疗三十年，国产替代的惊险两跃", 2021-05-11,
> https://www.jiemian.com/article/6074885.html (verified verbatim in the raw page)

RMB 100,000,000 at the 1997 average of ~8.29 RMB/USD — inside the peg period the
F-1 itself describes as running "from 1997" at 8.2765 — = **~US$12.06M**, against
the **1997 bar of $4,985,355 = 2.4x above bar**.

The second clause is independently corroborated for 1999: "1999年，迈瑞基本形成了
三大产品线… 一年营收超亿元" (Tencent News, 2021-06-24,
https://news.qq.com/rain/a/20210624A01NP900). The two sources agree on the 1999
milestone, which is what makes the 1997 clause credible rather than a typo — they
describe two different RMB-100M milestones (total revenue in 1997, own-developed
product revenue in 1999), and only Jiemian carries the earlier one.

**Which figure applies.** The criterion is the venture's revenue, not its
own-product revenue, so the 1997 total — which included Mindray's
distribution/agency business for foreign brands, described in both the F-1 and
the Jiemian piece — is the correct one. If the reviewer insists on two
independent sources for the same clause, **fall back to `1991-1999`** (span 8;
RMB 100M in 1999 = ~US$12.08M vs the 1999 bar of $5,174,829, 2.3x): still a
two-year improvement on the recorded 2001, and doubly sourced.

**Reliability caveat, stated.** Both are Chinese business-media retrospectives,
not filings, and there is one internal tension: Tencent's piece says Mindray's
*first* outside financing was only RMB 2M in 1998, which sits oddly beside RMB
100M of 1997 revenue. That is explicable (a specific engineering-centre
financing, with the F-1's own 1997 Walden International raise a separate event),
but it is a reason to keep confidence at `medium`, not to raise it.

**Q3, further narrowing.** No dated figure exists for 1992-1996, and the Jiemian
narrative frames the 1996-97 county-hospital sales push as what produced the RMB
100M — i.e. the crossing sits near the top of the bracket, not the middle.
Nothing supports moving the lower end.

**Proposed correction:** `a5_first_hit_date` = `1991-1997`; add
https://www.jiemian.com/article/6074885.html to `a5_first_hit_src` alongside the
F-1; conf `medium`. Alternative `1991-1999` with the Tencent corroboration if
single-sourcing on Jiemian is judged unacceptable.

---

## p141 — Yoshi Yokokawa — Alpaca (AlpacaDB, Inc.) — current `2015-2024` (span 9)

### Verdict: **TIGHTEN → `2021-2024`** (span 3; midpoint 2019.5 → 2022.5). **Do NOT exclude.**

This row is open question **Q5** in `docs/OPEN-QUESTIONS.md`, which asks (a) what
year Alpaca was founded, given four conflicting answers — 2013 (Ikkyo Technology,
Kobe), 2015 (AlpacaDB/Sacra), 2017 (Keio), 2018 (MEXT) — and (b) what Alpaca's
revenue was in any year before 2024; and which warns that **"On the 2013 lineage
the span is 11 years and the row must instead be `crossing_undatable`."** Both
parts are now answerable, and the answer removes the exclusion risk altogether.

**Q5(a) — founding year: 2015, now three-sourced.** Two sources beyond the row's
existing Sacra / research.nicoxz pair:

- English Wikipedia: "Alpaca was co-founded in 2015 by Yoshi Yokokawa and Hitoshi
  Harada." Its history runs 2015 founding → MarketStore → registration of Alpaca
  Securities LLC in March 2017 → FINRA approval 2018 → the 2018 pivot to
  brokerage APIs → $3M pre-Series A in 2018 → **Y Combinator Winter 2019 (W19)**
  batch. No mention of Ikkyo Technology.
  https://en.wikipedia.org/wiki/AlpacaDB
- TechCrunch, 12 Oct 2023: "brings the Y Combinator-backed startup's **total
  raised to $120 million since its inception in 2015**."
  https://techcrunch.com/2023/10/12/stock-trading-api-developer-alpaca-raises-15m-convertible-note-from-sbi-group/

The Keio (2017) and MEXT (2018) dates are reconciled rather than contradicted by
that history: March 2017 is when Alpaca Securities LLC was registered, and 2018 is
when FINRA approved it and the brokerage-API pivot happened. Those pages are
dating the US brokerage entity, not the company.

**Q5(b) — pre-2024 revenue: recoverable as a bound, and it is below the bar.**
The same TechCrunch piece states verbatim:

> **"Since its $50 million Series B in 2021, the company's revenue has increased
> by 17 times"**

and, as the row already notes, the CEO "declined to provide the baseline of the
revenue". The baseline is not needed, because the row's own upper-end source
supplies a ceiling from the other side. Sacra (https://sacra.com/c/alpaca/):
Alpaca hit "$100M in annualized revenue in September 2025, **up from $60M at the
end of 2024**". Revenue at Oct 2023 therefore cannot exceed $60M without
contradicting Sacra's own monotone series. So:

    revenue(Aug 2021) = revenue(Oct 2023) / 17 <= $60,000,000 / 17 = $3,529,412

against the **2021 bar of $8,416,707** — **at most 42% of bar, and that is the
generous extreme**, since it assumes Alpaca grew not at all between Oct 2023 and
end-2024, which Sacra's "up from" denies. For 2021 to have been *at* the bar,
Oct-2023 revenue would have had to be >= $143M — nearly two and a half times what
Sacra reports for fifteen months later. **2021 is below the bar on the study's
own sources.**

This is arithmetic on two sourced figures, not a guess, and it is internally
binding: **if you trust Sacra's $60M for the upper end, you must accept the
implied sub-$3.5M 2021 as the lower end.** Rejecting the lower end means
rejecting the upper end too, which sends the row to `crossing_undatable` for want
of any usable figure — it does not send it back to 2015-2024.

**What this does to Q5.** The 2013-vs-2015 founding dispute becomes **moot**. The
lower bound is no longer a founding-year floor; it is a sourced below-bar year
(2021). Whether the lineage starts at Ikkyo Technology in Kobe in 2013 or
AlpacaDB in California in 2015 no longer touches the span, because neither year
is used. **Q5 can be closed and the row kept.**

**Corroborating the direction.** The row's own note predicted this: "The 17x
growth since 2021 makes it likely that the true crossing sits late in the
bracket, around 2022-2023, so the bracket midpoint of 2019-2020 that the clocks
will use is probably several years early." Correct — and now fixable. Independent
signals agree the company was small through 2019: a $3M pre-Series A in 2018 and
a **YC W19 batch** (an accelerator seed batch is not where a $7.9M-revenue
company sits), plus TechCrunch's Aug-2021 Series B coverage quoting growth in
*brokerage accounts* (1500% YTD) rather than any revenue figure.

**Latka.** getlatka.com's $5.7M "2024" estimate remains an order-of-magnitude
contradiction of Sacra's $60M and is still not used. Note the real fragility,
unchanged by this pass: if Latka were believed, Alpaca would be *below* the 2024
bar and the upper end would collapse. Confidence must stay `low`.

**Proposed correction:** `a5_first_hit_date` = `2021-2024`; `a5_first_hit_src` =
https://techcrunch.com/2023/10/12/stock-trading-api-developer-alpaca-raises-15m-convertible-note-from-sbi-group/
(lower end, via the 17x bound) plus https://sacra.com/c/alpaca/ (upper end, and
the ceiling that makes the lower bound work); conf stays `low`; `excluded` stays
`false`. Close Q5 with the finding that the founding year no longer bears on
admissibility. Record in notes that the lower end is a bound derived from two
sourced figures, so a reviewer who rejects derivation should read the row as
`2015-2024` or exclude it — not as anything in between.

---

## Summary

| id | name | current | verdict | proposed | span | midpoint shift |
|---|---|---|---|---|---|---|
| p12 | Judy Faulkner | 1988-1997 | TIGHTEN | **1988-1995** | 9 → 7 | 1992.5 → 1991.5 |
| p71 | R. Damani | 2002-2012 | TIGHTEN | **2002-2007** | 10 → 5 | 2007 → 2004.5 |
| p75 | Jason Kelly | 2008-2017 | **HOLDS** | 2008-2017 | 9 | — |
| p121 | Rodney Brooks | 1990-2000 | TIGHTEN | **1992-2000** | 10 → 8 | 1995 → 1996 |
| p124 | Xu Hang | 1991-2001 | TIGHTEN | **1991-1997** | 10 → 6 | 1996 → 1994 |
| p141 | Y. Yokokawa | 2015-2024 | TIGHTEN | **2021-2024** | 9 → 3 | 2019.5 → 2022.5 |

All three rows sitting exactly at the 10-year cap (p71, p121, p124) were widened
rather than measured. That is the failure mode frame.md names, and it is worth
sweeping the remaining bounded rows for the same pattern — specifically for rows
whose upper end is "the earliest year in the IPO filing" rather than the earliest
year in any source, which is what broke p71, p121 (partially) and p124.

**Budget note:** the shared WebSearch budget was exhausted during this pass
(200/200 WebSearch calls, session-wide) at the point where I was trying to
corroborate the DMart FY2007 figure from a filing or a national business title.
WebFetch and `curl` still work. The only finding materially weakened by this is
p71's source quality; every other citation above was verified by direct fetch of
the page.
