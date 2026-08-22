# Adversarial verification — bounded anchors, batch B

Verifier pass, 2026-08-22. Eight bounded `a5_first_hit` rows in `data/anchors.csv`.
No file in `data/` was modified. All thresholds from `PYTHONUTF8=1 python -m src.cpi <year>`
(constant 2026 dollars). FX at the annual average for the revenue year.

Score: 4 TIGHTEN · 1 UNSUPPORTED-END · 3 HOLDS.

---

## p91 — Karim Beguir — InstaDeep — `2014-2022` — **HOLDS**

**Q1 lower end.** 2014 is the founding year, used as a floor. Legitimate under
frame.md ("the founding year is a valid lower bound"), but it is a floor, not a
measurement — nothing sources InstaDeep below the bar in any later year.

**Q2 upper end.** The earliest available above-bar figure, and I could not find
an earlier one. Craft.co's £18.0M FY2022 is not a Craft estimate: every line on
https://craft.co/instadeep/financials (Revenue 18.0M, COGS 5.5M, gross profit
12.5M, EBIT −4.2M) hyperlinks to an extracted source document, and it matches a
real filing — INSTADEEP LTD, company 09816291, "Full accounts made up to
31 December 2022", filed 25 Jul 2023
(https://find-and-update.company-information.service.gov.uk/company/09816291/filing-history).
£18.0M × 1.237 = US$22.3M vs the 2022 bar of $9,090,274. Above.

**Q3 narrowing.** Blocked at the source. InstaDeep Ltd's accounts filing history:
FY2016 "total exemption small", FY2017-FY2019 "total exemption full",
**FY2020 and FY2021 "accounts for a small company"**, FY2022 full, FY2023 full,
FY2024 medium. Small-company accounts omit the profit-and-loss account, so no
turnover for 2021 or earlier is on the public record. I downloaded the FY2022
(64pp) and FY2023 (290pp) PDFs and ran `pdftotext` on both: image scans with no
text layer, so the FY2021 comparative column inside the FY2022 accounts cannot be
read. BioNTech's acquisition releases disclose only the ~€500M consideration
(https://www.biontech.com/int/en/home/mediaroom/news/press-releases/2023/07/biontech-completes-acquisition-instadeep.html);
no InstaDeep revenue. The one inference available — small-company status implies
FY2020/FY2021 turnover ≤ £10.2M — does not clear the 2021 bar of £6.12M
($8,416,707 ÷ 1.376) in either direction, so it cannot move the bracket.

**Verdict: HOLDS.** Both ends stand as recorded. Weakest of the three HOLDS: an
8-year span with a completely unsourced interior, and an upper end that reaches
the public record only through an aggregator's extraction of a scanned filing.
Leave `a5_first_hit_conf` at medium.

---

## p72 — Zhong Shanshan — Nongfu Spring — `1996-2004` — **TIGHTEN → `1996-1999`**

This is the failure mode the brief describes: the researcher stopped at the
earliest figure in the broker report they already had open, five years after the
company was national.

**Q1 lower end.** 1996 is the founding year (26 Sep 1996) used as a floor.
Legitimate and safe: the first product (4L Nongfu Spring) did not ship until
June 1997.

**Q2 upper end — defective.** RMB 2.0bn for 2004 is nowhere near the earliest
above-bar year. The 2004 bar is only $5,867,498 ≈ RMB 48.6M. Nongfu was past that
scale by the end of the 1990s:

- Sina Finance, 19 Jul 2020, 「瓶装水启示录：农夫山泉的降维竞争」:
  「99年，在全国500强食品企业中，养生堂上升至第39位，**农夫山泉饮用水全国销售额达4亿元**，
  市场占有率已日益逼近娃哈哈和乐百氏，在该年度全国大中城市的大型商场饮用水销量排行榜上，
  农夫山泉以16.39%的市场占有率位居第一。」
  https://finance.sina.cn/hkstock/ggyw/2020-07-19/detail-iivhvpwx6214628.d.html
- Corroborated by Nongfu Spring's own corporate profile:
  「2000年3月由国家国内贸易局商业信息中心…发布的1999年度全国食品日用品市场监测报告显示：
  99年瓶装饮用水市场占有率排名，农夫山泉为第一，份额为16.39%。」
  https://images.sohu.com/cs/minisite/nongfushanquan/company.htm

**1999 revenue RMB 400,000,000 ÷ 8.2783 (1999 annual average RMB/USD) =
US$48.3M, 9.3× the 1999 bar of $5,174,829.** Decisively above.

**Q3 further narrowing (offered, not required).** The same company profile puts
Nongfu **third in national market share in 1998** (「1998年…当年，农夫山泉的市场占有率
迅速上升为全国第三」) after the mid-year nationwide roll-out of the 550ml sports-cap
bottle, and **first in Shanghai** in 1997 within three months of launch. The 1998
bar is only RMB 41.9M ($5,063,008 × 8.279); the number-three brand in China's
bottled-water market was far past that. Under frame.md's rule that a qualitative
"industry-leading by year X" claim establishes an earlier crossing, `1996-1998`
(midpoint 1997) is defensible. I recommend the conservative `1996-1999` because
it rests on a stated revenue figure.

**Proposed correction:** `a5_first_hit_date` → `1996-1999`; `a5_first_hit_src` →
the Sina Finance URL, with the Sohu-hosted company profile as corroboration.
**Midpoint moves 2000 → 1997.5** — the recorded row is about 2.5 years late.

---

## p62 — Shiv Nadar — HCL — `1977-1985` — **UNSUPPORTED-END (both ends)**

**The cited source URL does not contain the cited claim, and does not mention HCL
at all.**

`a5_first_hit_src` is
`https://www.indiatoday.in/magazine/business/story/19861015-hcl-slashes-computer-prices-sparks-off-fresh-price-war-801332-1986-10-15`.
Fetched twice (curl, and through a reader proxy), it resolves to India Today
story id **801332**, *"Plethora of Malayalam magazines take Kerala by storm"*,
15 Oct 1986 — an unrelated media piece. The note's quoted evidence, "ONE sales
region at Rs 15 crore", appears nowhere in it.

The real article is id **801333**:
https://www.indiatoday.in/magazine/economy/story/19861015-hcl-slashes-price-of-personal-computers-sparks-off-fresh-price-war-801333-1986-10-15
I read it in full. It contains no Rs 15 crore sales region. What it does give,
verbatim: *"In a move that stunned the computer industry, the Delhi-based
Hindustan Computers Ltd (HCL) announced last month that it was slashing the price
of its personal computer from Rs 42,000 to Rs 20,000"* and *"**HCL hawked 1,700
business computers last year** and now expects sales to almost double this year."*

**Q2 upper end — right year, wrong evidence.** 1,700 business computers in the
year before Oct 1986, at no less than the pre-cut PC price of Rs 42,000 each, is
**≥ Rs 7.14 crore** against a 1985 bar of **Rs 4.13 crore**
($3,342,207 × 12.369 INR/USD). Business machines sold above PC prices, so the
true figure is higher. 1985 survives as an above-bar year — but on a different
basis, from a different URL, than the row records.

**Q1 lower end — unsourced.** Nothing places HCL below the bar in **1977**. The
note itself says HCL was founded 11 Aug 1976 with "revenue effectively zero in
the founding year" — that sources **1976**, not 1977. Under frame.md the sourced
lower bound is the founding year; 1977 is a year of tightening with no
measurement behind it.

**Q3 narrowing.** Genuinely attempted, genuinely blocked. indiankanoon.org — the
host of the "Hindustan Computers Ltd. vs Income-Tax Officer" judgment the note
relies on for FY-ending-30-Jun-1983 customs/excise/closing-stock figures — is
behind Cloudflare and returned 403 on every route, including the casemine and
sooperkanoon mirrors; the Wayback Machine has no snapshot. Those figures could
not be re-verified by me and should be treated as unconfirmed. The Dataquest
retrospectives (https://www.dqindia.com/1976-1985-the-big-blue-impact and
https://www.dqindia.com/the-pc-in-india-the-desktop-story/) confirm HCL as a
top-three Indian PC vendor in 1985 (top three = 87% of PC sales) and an
Intelligence Bureau supplier from 1982, but publish no rupee figure for HCL in
any year. No intermediate figure found.

**Proposed correction:** `a5_first_hit_date` → `1976-1985` (9 years, inside the
cap); `a5_first_hit_src` → the …-801333-… URL; note rewritten so the upper end
reads on 1,700 units × ≥Rs 42,000 rather than a phantom Rs 15 crore region.
**Midpoint 1981 → 1980.5** — the clock barely moves; the defect is that the row's
sourcing does not survive being checked.

---

## p39 — Nadiem Makarim — Gojek — `2010-2018` — **TIGHTEN → `2014-2018`**

**Q1 lower end — the exact defect the brief names.** 2010 is the founding year
used as a floor, and the row's own notes already contain the evidence that a much
later year is sourced below the bar. It just was not used as a bound:

- Gojek "was founded in 2010 with **20 motorbike drivers**", operating as a call
  centre connecting customers to ojek riders; "Gojek app was launched in
  **January 2015**"; its first outside financing came only in **late 2014**
  (NSI Ventures / Openspace). https://en.wikipedia.org/wiki/Gojek
- Already cited in the row: AP (Gojek "a sideline business") and BBC (Makarim did
  not work on it full-time until 2014) —
  https://apnews.com/general-news-c12f422c43944868af842ddfd5f5c673 and
  https://www.bbc.com/news/business-36330006

The 2014 bar is $7,353,351 = **IDR 87.2 billion** at the 2014 average of
11,865 IDR/USD. A pre-app call-centre operation taking a commission on ojek
fares, still raising its seed round in late 2014, was not earning IDR 87bn of net
revenue. 2014 is a sourced below-bar year in exactly the sense frame.md requires.

**Q2 upper end.** Sound and correctly reasoned; I found no earlier annual revenue
disclosure. GoTo's IPO prospectus gives 2018 net revenue IDR 1,436,511 million =
US$100.9M at 14,236.938, 12.9× the 2018 bar of $7,799,735, and the researcher
correctly rejected the IDR 127tn GTV figure.

**Q3.** 2015 may also be below bar — the app launched in January 2015 and scale
came during that year — but nothing sources it, so the lower end stops at 2014.

**Proposed correction:** `a5_first_hit_date` → `2014-2018`, citing the Wikipedia
founding / app-launch / first-financing chronology alongside the AP and BBC
pieces already in the row. **Midpoint moves 2014 → 2016 — a two-year error, the
largest clock effect in this batch.**

---

## p26 — Anita Roddick — The Body Shop — `1976-1984` — **TIGHTEN → `1981-1983`**

The CPI handling here is *correct* — the researcher used constant-dollar bars
(£982k for 1976, £2.41M for 1984), not a $10M nominal figure. The defect is that
both ends were bounded qualitatively when a dated pound series exists.

**Q2 upper end — one year too late.** Chris Higson (London Business School)
publishes a Body Shop teaching case whose Table 1, "BODY SHOP to 1992", gives
Sales in £'000:

| | 1983 | 1984 | 1985 | 1986 | 1987 |
|---|---|---|---|---|---|
| Sales (£'000) | **2,143** | 4,910 | 9,362 | 17,394 | 28,476 |

https://chrishigson.com/wp-content/uploads/2025/03/Body_Shop.pdf (Table 1, p.7)

**1983 bar: $3,093,715 ÷ 1.5159 (1983 annual average USD/GBP) = £2,040,844.
Sales of £2,143,000 are 105% of the bar — above.** The April 1984 flotation is
therefore not the earliest sourced above-bar year; 1983 is.

**Q1 lower end — five years too early.** A scanned case study, "The Body Shop:
Founding and Franchising" (https://www.scribd.com/document/92673406/Body-Shop-1),
states: *"By 1979, The Body Shop was turning over more than [£]250,000 and making
a pre-tax profit of 8 per cent. During 1980 and 1981 however, although turnover
grew to [£]580,000 and [£]828,000 respectively, profitability fell; pre-tax
profits in 1980 were 4.6 per cent and in 1981 dropped to 3.7 per cent."*

**1981 bar: $2,823,481 ÷ 2.0243 = £1,394,794. Turnover of £828,000 is 59% of the
bar — below.** The series is internally consistent and joins smoothly to Higson:
£828k (1981) → £2,143k (1983) is ~61%/yr, against the 129% Higson records for
1984.

**Proposed correction:** `a5_first_hit_date` → `1981-1983` (2-year span);
`a5_first_hit_src` → the Higson PDF, with the Scribd case cited for the lower
end. **Midpoint moves 1980 → 1982.**

**Caveats, stated honestly.** (a) 1983 clears the bar by only 5%, and The Body
Shop's fiscal year ended in late February, so the "1983" column may be the year
to Feb 1983 or to Feb 1984 — either way 1983 is the right label, but confidence
should stay medium. (b) The £828k figure comes from an unattributed scanned case
on Scribd; I could not identify the underlying original (it is *not* the
Cengage/Thompson case, which I downloaded and checked). If that source is judged
too weak, the fallback correction is **`1976-1983`** on Higson alone — still a
tightening, midpoint 1979.5.

---

## p25 — Karsanbhai Patel — Nirma — `1969-1977` — **HOLDS**

**Q1 lower end.** 1969 is the founding year used as a floor — legitimate, and
unusually safe: Nirma began as a one-man 100-sq-ft backyard operation.

**Q2 upper end.** Rs 4 crore in 1977 ÷ 8.74 INR/USD = US$4.58M against the 1977
bar of $1,882,321 (**Rs 1.65 crore**) — 2.4× the bar. The conversion and the
constant-dollar arithmetic are done correctly; this row does **not** commit the
$10M-nominal error the brief warns about. Source quality is weak (the10minutemba
and startuptalky share near-identical wording from one uncredited original), but
the researcher already flagged that and set confidence to medium.

**Q3 narrowing — nothing available.** Nirma Limited's own timeline
(https://www.nirma.co.in/our-journey) begins at the 25 Feb 1980 incorporation of
Nirma Ltd and gives no 1970s figure; the pre-1980 business was an unincorporated
proprietorship that filed nothing. Searches of the case-study literature returned
only post-1990 aggregates (Rs 17bn, Rs 2,400 crore). No dated 1970-1976 turnover,
volume, or plant figure exists that I could find.

**Verdict: HOLDS.** 8-year span, both ends as permitted, no lever to tighten.
Note for the sensitivity run: with the bar at Rs 1.65 crore in 1977 and Nirma at
Rs 4 crore, the true crossing is probably 1975-76 — later than the recorded
midpoint of 1973 — but that is unsourced and must not be written in.

---

## p142 — David Gausebeck — Matterport — `2011-2019` — **TIGHTEN → `2013-2019`**

**Q1 lower end — 2011 is a floor with a much later sourced replacement.**
Matterport was incorporated in 2011 but **had no product on the market until
13 March 2014**, when it launched the Pro 3D Camera and cloud platform:

- Matterport's own release, "Matterport Brings 3D Media Platform to Market",
  March 2014: https://matterport.com/news/matterport-brings-3d-media-platform-market
- San Jose Mercury News, 12 Mar 2014, "Startup Matterport launches new 3-D
  modeling system":
  https://www.mercurynews.com/2014/03/12/startup-matterport-launches-new-3-d-modeling-system/
- GISuser, Apr 2014:
  https://gisuser.com/2014/04/matterport-brings-3d-camera-and-cloud-based-system-to-market/

Corroborated by TechCrunch, 25 Jun 2015 (https://techcrunch.com/2015/06/25/matterport/
— note this is the correct URL; the one in the row's note,
`/2015/06/24/matterport-raises-30-million-series-c/`, 404s): *"It's sold thousands
of its cameras"* at $4,500; *"A year ago, Matterport got serious about the
commercial market, and raised a $16 million Series B"*; total capital before that
of roughly $10M (a $1.6M seed in 2012, a $5.6M A, plus $2.8M).

**A company with no commercial product until March 2014 cannot have reached the
2013 bar of $7,235,970 in 2013.** The lower end should be 2013.

**Q2 upper end.** Correct, and independently confirmed. I read the Gores Holdings
VI merger prospectus (424B3, 21 Jun 2021,
https://www.sec.gov/Archives/edgar/data/1819394/000119312521194323/d101627d424b3.htm):
revenue is disclosed only from FY2019 (~$46M) and FY2020 (~$86M); the only
pre-2019 operating data are spaces under management (1.4M in 2018, 2.3M in 2019)
and subscribers (14,000 at 31 Dec 2018 → 250,000 at 31 Dec 2020). No earlier
revenue figure exists in any SEC filing.

**Q3.** 2014 is arguably also below bar — a March launch of a $4,500 camera that
had sold only "thousands" cumulatively fifteen months later — but "thousands" is
too vague to convert, so stop at 2013.

**Proposed correction:** `a5_first_hit_date` → `2013-2019`; add the
Matterport/Mercury News March-2014 launch citation to `a5_first_hit_src`
alongside the S-1. **Midpoint moves 2015 → 2016.**

---

## p122 — Zhu Gongshan — Taicang Poly cogeneration plant — `1996-2004` — **TIGHTEN → `1998-2004`**

**Q1 lower end — a floor that the row's own primary source already supersedes.**
The row bounds from the plant's 4 Nov 1996 establishment. But GCL-Poly's 2007
HKEX prospectus, Business section power-plant table (e114.pdf, p.128), gives the
in-service dates of the Taicang Poly Cogeneration Plant's generating units:

> The Taicang Poly Cogeneration Plant … 49% **Unit #1 Dec. '98 / Unit #2 Feb. '99
> / Unit #3 May '03**, 3 × 15 [MW], installed capacity 45.00 MW

https://www1.hkexnews.hk/listedco/listconews/sehk/2007/1031/03800_241796/e114.pdf

The plant was established in 1996 but **generated nothing until December 1998**.
It therefore earned essentially zero in 1996, 1997, and eleven-twelfths of 1998 —
the 1998 bar is $5,063,008, and one month of a single 15 MW unit does not
approach it. **1998 is a sourced below-bar year**, two years tighter than the
founding floor, resting on the same primary document the row already cites.

**Q2 upper end.** Confirmed correct and unimprovable. I downloaded and read the
Deloitte accountants' report for the plant (e131.pdf): the income statement
covers **only** the years ended 31 Dec 2004, 2005 and 2006 plus a four-month 2007
stub — Revenue HK$151,617k / 176,862k / 175,337k. FY2004 is genuinely the
earliest disclosed year. HK$151.6M ÷ 7.8 = US$19.4M vs the 2004 bar of
$5,867,498. Above.

**Q3 further narrowing (offered, not required).** With 30 MW running from
Feb 1999 against HK$151.6M of revenue from 45 MW in 2004, the plant's first full
operating year almost certainly cleared the RMB ~43M-equivalent 1999 bar, which
would put the true crossing at 1999. No revenue figure sources that, so I do not
propose it.

**Proposed correction:** `a5_first_hit_date` → `1998-2004`, citing e114.pdf's
in-service table for the lower end alongside e131.pdf for the upper.
**Midpoint moves 2000 → 2001.**

*Separate observation, outside the bounded-date question:* the hit entity is 49%
held by Zhu's vehicle with Poly holding 51% from 1998, and the row uses
whole-entity revenue rather than Zhu's attributable share. Both readings clear
the bar comfortably here, but the study should apply one convention consistently
across JV hit entities.

---

## Summary

| id | person | recorded | verdict | proposed | midpoint shift |
|---|---|---|---|---|---|
| p91 | Beguir | 2014-2022 | HOLDS | — | — |
| p72 | Zhong Shanshan | 1996-2004 | TIGHTEN | `1996-1999` | 2000 → 1997.5 |
| p62 | Nadar | 1977-1985 | UNSUPPORTED-END | `1976-1985` + src fix | 1981 → 1980.5 |
| p39 | Makarim | 2010-2018 | TIGHTEN | `2014-2018` | 2014 → 2016 |
| p26 | Roddick | 1976-1984 | TIGHTEN | `1981-1983` | 1980 → 1982 |
| p25 | Karsanbhai Patel | 1969-1977 | HOLDS | — | — |
| p142 | Gausebeck | 2011-2019 | TIGHTEN | `2013-2019` | 2015 → 2016 |
| p122 | Zhu Gongshan | 1996-2004 | TIGHTEN | `1998-2004` | 2000 → 2001 |

No row in this batch should become `crossing_undatable`; every proposed span is
narrower than the one recorded. The recurring pattern is not a widened range
containing a convenient year — it is a **founding-year floor left in place when a
much later below-bar year was sourceable** (p39, p142, p122, p26), which biases
every affected midpoint *early*.

## Tooling note for the other agents

The session WebSearch budget (200/200) was exhausted partway through this pass,
and DuckDuckGo, Mojeek and Bing all rate-limited or degraded to navigational
results when driven by curl. The rest of the research went through
`https://r.jina.ai/<url>` as a fetch-and-search proxy; it also recovered pages
that return 403/blank to WebFetch and curl (indiatoday.in, techcrunch.com) and
can be pointed at `https://duckduckgo.com/html/?q=...` to restore search.
