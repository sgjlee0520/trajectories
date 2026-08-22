# Adversarial review of the eight `hit_basis = fallback` rows

Scope: for each row, one question only — **is there any source indicating the hit entity
reached meaningful scale BEFORE the acquisition year recorded?** Nothing in `data/` was
edited.

Constant-2026-dollar bars used (from `python -m src.cpi <year>`):

| year | rev10 | acq50 |
|---|---|---|
| 1995 | $4,733,757 | $23,668,786 |
| 2000 | $5,348,773 | $26,743,865 |
| 2003 | $5,715,297 | $28,576,487 |
| 2005 | $6,066,291 | $30,331,456 |
| 2012 | $7,131,511 | $35,657,554 |
| 2016 | $7,454,953 | $37,274,766 |
| 2018 | $7,799,735 | $38,998,674 |
| 2019 | $7,941,064 | $39,705,321 |
| 2020 | $8,039,032 | $40,195,159 |
| 2021 | $8,416,707 | $42,083,537 |

**Summary: 3 rows break (p67, p70, p94 — the latter two are one event), 5 hold.**

---

## p07 — Kevin Systrom — Instagram — acq50 2012 — **HOLDS**

Attacked and failed to break. Instagram charged for nothing and carried no advertising
until 2013; at the April 2012 acquisition it was a 13-person company with ~30M users and
no business model. Facebook's own S-1/A describes the consideration (22,999,412 shares +
$300M cash) without any Instagram revenue, because there was none to report.

- https://www.sec.gov/Archives/edgar/data/0001326801/000119312512235588/d287954ds1a.htm
- https://techcrunch.com/2012/04/09/facebook-to-acquire-instagram-for-1-billion/

No source suggests any pre-2012 crossing, and the 2012 acq50 bar ($35.66M) is cleared by
$1B ≈ 28×. This is the shape of case the fallback was written for. **No change.**

---

## p16 — Shola Akinlade — Paystack — acq50 2020 — **HOLDS (with a flagged arithmetic error in the row note)**

No source found states, in any year before 2020, that Paystack was already large,
profitable, or market-leading. The "more than half of all online transactions in Nigeria"
and 60,000-merchant descriptions are all pinned to the October 2020 acquisition itself.
Nairametrics' September 2018 "17,000 businesses / over 15% of all online payments" is a
real business but not a leadership claim. On the frame's evidentiary standard the fallback
is not barred, and — as the row already notes — a 2020 rev10 crossing would give the same
anchor year anyway. **Verdict HOLDS.**

**But the row's supporting arithmetic is wrong and should not be relied on.** Paystack's
own milestone post (dated 1 Nov 2018, milestone transaction 26 Oct 2018) gives:
₦10bn/month transaction value, **2,964,008 transactions/month**, 23,523 live merchants,
39 staff — https://paystack.com/blog/company-news/10billion

The row computes revenue as ~1.5% of volume (≈$4–5M/yr) and **omits the ₦100 flat
per-transaction fee entirely**. At an average ticket of ₦10bn / 2.96M ≈ ₦3,375, the flat
component dominates: even assuming the ₦100 is waived on half of all transactions,
2.96M × (1.5%×₦3,375 + ₦50) ≈ ₦298M/month ≈ ₦3.6bn/yr ≈ **$9.9M** at ₦360/$ — above the
2018 bar of $7,799,735, not below it. My figure is an estimate too and dates nothing, so
it cannot bar the fallback; the point is that the row's note reads as if arithmetic
*positively excluded* an earlier crossing, and it does not. Two defensible responses:
soften the note to "no sourced figure either way", or, if the study wants to be
conservative about gross processing revenue, bound `2018-2020` (Oct-2018 milestone post →
Oct-2020 Stripe close). I do not recommend the bound on present evidence, because no
source states a crossing — but the note's arithmetic claim should be corrected either way.

---

## p38 — Rana el Kaliouby — Affectiva — acq50 2021 — **HOLDS (strongest of the eight)**

This row is not merely unfalsified — it has a positive disclosure showing the threshold was
*never* crossed. Smart Eye's regulated acquisition announcement states Affectiva's revenue
was **approximately USD 5 million for the twelve months ending 31 March 2021**, at an 86%
gross margin, with **100 FTEs**.

- https://storage.mfn.se/55433235-24a0-42b2-a758-084cf3b0dda8/pr-smart-eye-affectiva-english.pdf
- https://www.inderes.dk/en/releases/smart-eye-enters-into-an-agreement-to-acquire-affectiva-and-intends-to-raise-equity-in-a-directed-share-issue

$5M is 59% of the 2021 rev10 bar ($8,416,707). Affectiva had raised only ~$53M total by
April 2019, so no earlier year plausibly ran materially ahead of the 2021 figure, and no
source gives one. Fortune's 2018 "25% of the world's biggest companies as users" is a
customer-penetration claim, and the frame is explicit that category-leadership language
cannot outweigh a contemporaneous disclosed figure below the bar. **No change.**

---

## p58 — Özlem Türeci — Ganymed Pharmaceuticals — acq50 2016 — **HOLDS**

Ganymed was a clinical-stage antibody developer (IMAB362/zolbetuximab) with no marketed
product and no disclosed partner. Its entire funding history is equity — Series C €33.7M
(2007), Series D (2008), Series E €45M (2013), ~$212M total across six rounds — which is
the financing profile of a company with no revenue line, not one carrying €7.5M+/yr.

- https://www.biospace.com/article/releases/ganymed-pharmaceuticals-ag-raises-euro-33-7-million-in-series-c-financing-round-/
- https://www.biotechnewswire.ai/20131118984/ganymed-pharmaceuticals-closes-eur-45-million-financing-round.html
- https://newsroom.astellas.com/2016-12-21-Astellas-Completes-Acquisition-of-Ganymed-Pharmaceuticals

Ganymed's German statutory accounts (HRB 47318 Mainz) exist but revenue is paywalled at
North Data, so no figure could be read directly; nothing found asserts scale, profitability
or leadership in any earlier year. **No change.** (One residual, out of scope here: if the
statutory accounts ever become readable and show collaboration income above the bar, the
row would need revisiting.)

---

## p67 — Robin Zeng — Amperex Technology Limited (ATL) — acq50 2005 — **SHOULD-BE-BOUNDED**

**This row breaks.** The 2005 rev10 bar is $6,066,291 — a bar ATL was clearing by a wide
margin years before TDK bought it, and several sources say so.

Evidence of earlier scale:

1. **TDK's own acquisition announcement (SEC Form 6-K, 1 June 2005)** — "Establishment:
   July 1999 … Employees: Ca. 3,000 … Net Asset: Ca. US$50 million", manufacturing in
   Dongguan. A 3,000-employee battery manufacturer is by any reading "already large"; the
   $6.07M bar is roughly $2,000 of annual revenue per employee.
   https://www.sec.gov/Archives/edgar/data/203383/000119163805000967/tdk200506016k.txt
2. **The Carlyle Group, 17 June 2003** — headline: "Carlyle Leads a US$30 Million
   Investment with 3i as a co-investor in **a Leading Chinese Battery Maker**, Amperex
   Technology Limited". A dated third-party leadership claim two years before the sale,
   attached to a $30M Series B raised to expand manufacturing capacity.
   https://www.carlyle.com/media-room/news-release-archive/carlyle-leads-us30-million-investment-3i-co-investor-leading
3. **"Five years after its founding, it became the largest supplier of lithium polymer
   batteries in the world"** — i.e. ~2004 — and ATL "earned the trust of Apple in 2003,
   becoming the battery provider of its newly-launched iPod".
   https://interconnected.blog/robin-zeng-catls-prodigious-gambler/
4. Wikipedia: "Two years after establishment, ATL was able to produce batteries for 1
   million devices" (~2001). https://en.wikipedia.org/wiki/ATL_(company)

The frame's bar-check is qualitative and these clear it: "industry-leading by a stated
year … is enough to establish that an earlier crossing occurred". The row's counter-note
("public sources emphasize unit volume … not annual revenue") is answered directly by the
frame — only the *year* needs bounding, not the crossing.

The one contrary datum, Wikipedia's "ATL had been in financial difficulty before the
acquisition", is about profitability and cash, not revenue scale; a 3,000-employee
manufacturer in difficulty still books revenue two orders of magnitude above $6M.

What I could **not** find, after checking TDK's Form 6-K, TDK's FY2006 Form 20-F
(https://www.sec.gov/Archives/edgar/data/203383/000114554906001085/k01184e20vf.htm — the
ATL note gives goodwill ¥3,803M and intangibles ¥3,497M but **no** pro-forma revenue; TDK
ran pro formas for Lambda Power only), and trade press, is a dated dollar revenue figure.
That is exactly the situation the bounded-date rule exists for.

**Proposed correction**
- `a5_first_hit_date` = **`1999-2004`** (span 5)
- lower bound: ATL established July 1999 — TDK 6-K (primary source, link above)
- upper bound: world's largest lithium-polymer battery supplier by 2004 — interconnected.blog
- `hit_criterion` = `rev10`, `hit_basis` = `primary`, `excluded` = false
- Tighter alternative if the study prefers the better-sourced upper end: **`1999-2003`**,
  upper bound = Carlyle's 17 June 2003 "leading Chinese battery maker" release. Midpoints
  are 2001.5 vs 2001, so the choice barely moves the clock; I lean `1999-2004` because both
  ends are then unambiguous.

Effect: the anchor moves ~3.5 years earlier than the recorded 2005.

---

## p70 / p94 — Donna Dubinsky and Jeff Hawkins — Palm Computing — acq50 1995 — **SHOULD-BE-BOUNDED (one investigation, two rows)**

Treated as a single event, as instructed: both rows date the same 1 September 1995 sale of
Palm Computing to U.S. Robotics, and both must move together.

**This row breaks, and it breaks on a hard number.** Harvard Business School case *Palm
Computing, Inc. 1995: Financing Challenges* (Dodson & Hart, HBS/Harvard Business
Publishing; teaching note ref. 5-899-071) carries the case-setting descriptor:

> Location: Los Altos, CA · Industry: Computing devices, software ·
> **Size: Start-up, 30 employees, USD10 million revenues** · Other setting(s): 1995

and its abstract places the case *before* the sale — "The president, Donna Dubinsky, and
the chairman and founder, Jeff Hawkins, discuss an opportunity to sell their company to
U.S. Robotics. They must weigh this option versus accepting venture capital funding…"

- https://www.thecasecentre.org/products/view?id=44421 (Case Centre listing, full metadata)
- https://www.hbs.edu/faculty/Pages/item.aspx?num=25521 (HBS faculty record; bot-blocked to
  automated fetch but the same case)

$10M against the 1995 rev10 bar of $4,733,757 is **2.1× the bar**, at a company that was
still independent. So a rev10 crossing is *known* to have occurred no later than 1995 and
independently of the acquisition — which bars the acq50 fallback outright. The row notes
for both p70 and p94 currently assert the opposite ("no sourced revenue figure places Palm
above the 1995 rev10 bar … before the sale"); that assertion is false.

Consistency check, not contradiction: U.S. Robotics' FY1996 Form 10-K states the Palm
pooling-of-interests was not restated because "the aggregated historical operations of ISC
and Palm prior to the dates of combination were not material to the Company's consolidated
results of operations and financial position". USR's FY1995 net sales were $889.3M, so
$10M is 1.1% — immaterial to USR and simultaneously 2.1× the study's bar.
https://www.sec.gov/Archives/edgar/data/933353/0000950137-96-002722.txt (Selected Financial
Data table; Palm/ISC pooling note)

The qualitative record that the rows lean on — "by 1995, Hawkins and Palm Computing CEO,
Donna Dubinsky, were running out of time and money … With the last pennies of its venture
funding" (University of Michigan Business School case 18,
https://websites.umich.edu/~afuah/cases/case18.html) — describes a **cash** crisis in a
company burning ahead of a hardware launch, not an absence of revenue. Both can be true at
once, and the HBS figure says they were.

No source pins the crossing year. Palm was founded January 1992; the Zoomer (whose software
Palm supplied) shipped October 1993; standalone Graffiti shipped September 1994; the
earliest published revenue figure is the 1995 $10M. That is precisely the frame's
"earliest published figure is already above threshold" case, which directs a bound from the
entity's founding to that figure's year.

**Proposed correction (identical on both rows)**
- `a5_first_hit_date` = **`1992-1995`** (span 3)
- lower bound: Palm Computing founded 1992 — Michigan case 18 ("Hawkins founded Palm
  Computing in 1992"); corroborated by CHM and https://en.wikipedia.org/wiki/Palm,_Inc.
- upper bound: USD10 million revenues, 30 employees, 1995 setting, pre-sale — HBS case via
  Case Centre listing above
- `hit_criterion` = `rev10`, `hit_basis` = `primary`, `excluded` = false
- `a5_first_hit_src`: https://www.thecasecentre.org/products/view?id=44421

Effect: both anchors move from 1995 to midpoint 1993.5, ~1.5 years earlier.

Caveat worth recording in the row note: the $10M is HBS's own "Size" metadata for the case
company, not a quoted line from the case text, and no fiscal period is stated. It is
published, attributable, and dated to the 1995 setting, but it is a case-abstract
descriptor. If the study wants a second leg, the case itself (HBS 899-045) would supply it.

---

## p93 — Sophie Wilson — Element 14 — acq50 2000 — **HOLDS**

Attacked via Broadcom's SEC filings, which are decisive against an earlier crossing.
Broadcom's FY2000 Form 10-K
(https://www.sec.gov/Archives/edgar/data/1054374/0000892569-01-000057.txt):

- Element 14's purchase-price allocation is **negative $18,805 thousand of assets
  (liabilities) assumed**, $383.8M goodwill/intangibles, $70.6M deferred compensation,
  $64.6M IPR&D — total $505.1M. A company with negative net assets acquired almost entirely
  for goodwill and unfinished technology.
- The IPR&D table values Element 14's DSL projects at **49% complete**, one year from
  completion, $13.2M still to spend — i.e. no shipping product, and Broadcom states
  "Shipment volumes of products from the above-acquired technologies are not material".
- Pro-forma FY2000 net revenue for Broadcom *plus all eight* fiscal-2000 purchase
  acquisitions is $1,127.6M against actual net revenue of $1,096.2M — $31.4M of full-year
  revenue across all eight companies combined; Element 14's share of that is a fraction of
  the 2000 rev10 bar of $5,348,773.
- Broadcom reported the Element 14 completion under Item 9 (30 Nov 2000) and filed no
  Rule 3-05 Form 8-K/A with Element 14 audited financials, unlike Innovent, Altima, NewPort
  and Silicon Spice — consistent with an operationally insignificant acquiree.

Element 14 also only existed from 1999 to November 2000, so even if a crossing were later
found, the maximum permissible bound would be `1999-2000` and the clock would move by at
most half a year. **No change.**

---

## Bottom line

| row | verdict | proposed anchor | shift |
|---|---|---|---|
| p07 Systrom | HOLDS | 2012 unchanged | — |
| p16 Akinlade | HOLDS (fix note arithmetic) | 2020 unchanged | — |
| p38 el Kaliouby | HOLDS | 2021 unchanged | — |
| p58 Türeci | HOLDS | 2016 unchanged | — |
| p67 Zeng | **SHOULD-BE-BOUNDED** | `1999-2004` rev10/primary | −3.5 yr |
| p70 Dubinsky | **SHOULD-BE-BOUNDED** | `1992-1995` rev10/primary | −1.5 yr |
| p93 Wilson | HOLDS | 2000 unchanged | — |
| p94 Hawkins | **SHOULD-BE-BOUNDED** | `1992-1995` rev10/primary | −1.5 yr |

Three of eight fallbacks are dating a hit years late — but only two distinct events
(ATL; Palm Computing). Five survive, and two of those (p07, p38) are cases where the
threshold demonstrably was never crossed before the deal at all, which is the fallback
working as designed.

No file in `data/` was modified.
