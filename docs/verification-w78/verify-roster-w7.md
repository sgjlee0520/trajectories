# Membership verification pass — roster rows p161–p185

Method: every URL below was actually fetched this session (`curl` with a Chrome
User-Agent, saved to disk in this dir, then grepped). No verdict rests on prior
belief about the person. WebSearch was not used at all; no fetch errors occurred.

Verdict counts: 25 CONFIRMED, 0 NAMES-NOBODY, 0 WRONG-LIST, 0 COMPANY-MISMATCH,
0 UNREACHABLE. Documentation caveats noted inline on p169, p179, p181, p183.

---

## p161 — Amancio Ortega
- Claimed list: Forbes World's Billionaires (self-made)
- URL: https://www.forbes.com/profile/amancio-ortega/ — HTTP 200, 879,472 bytes
- Verdict: **CONFIRMED**
- Text returned: `<meta name="description" ... content="Amancio Ortega is #10 on Forbes' 2026 Billionaires list.` and bio bullet `A pioneer in fast fashion, he cofounded Inditex, known for its Zara fashion chain, with his ex-wife Rosalia Mera (d. 2013) in 1975.`
- Cross-check: forbesapi 2026 billionaires JSON returns `10 | Amancio Ortega | selfMade=True | Zara`. Row's "fashion retail / clothing chain" matches "one of the wealthiest clothing retailers in the world".

## p162 — Reinhold Wuerth
- Claimed list: Forbes World's Billionaires (self-made)
- URL: https://www.forbes.com/profile/reinhold-wuerth/ — HTTP 200, 843,094 bytes
- Verdict: **CONFIRMED**
- Text returned: `Reinhold Wuerth & family is #75 on Forbes' 2026 Billionaires list.`; bullets: `Reinhold Wuerth is honorary chairman of the supervisory board of the Wuerth Group, a German hardware manufacturer founded by his father.` / `Wuerth joined the family's wholesale screw business in 1949, at age 14, as the company's second employee and first apprentice.`
- Company-description check: row says "industrial distribution ... a fastener business he joined as its second employee". Forbes calls it a "hardware manufacturer" in one bullet but "wholesale screw business" in the next, and the 2026 API entry is `75 | Reinhold Wuerth & family | selfMade=True | Fasteners`. Both the row's industry description and its "second employee, not founder" claim are supported by the fetched source. No mismatch.

## p163 — Eddy Lu
- Claimed list: Y Combinator Top Companies
- URL: https://www.ycombinator.com/companies/goat-group — HTTP 200, 87,562 bytes
- Verdict: **CONFIRMED**
- Text returned: embedded JSON `"full_name":"Eddy Lu","title":"Founder"`; meta description `Founded in 2015 by Eddy Lu and Daishin Sugano, GOAT Group has 1600 employees based in Los Angeles.`; long description `GOAT Group represents the leading platforms for authentic sneakers, apparel and accessories. Operating four distinct brands-GOAT, Flight Club, Grailed and alias-GOAT Group has a global community of over 50M members across 170 countries.` — verbatim match to the row's quoted company description.
- List check: https://yc-oss.github.io/api/companies/top.json fetched, 91 entries; `goat-group` is entry **10**, exactly as the row states.

## p164 — Ken Olsen
- Claimed list: Computer History Museum Fellow Awards
- URL: https://computerhistory.org/profile/ken-olsen/ — HTTP 200, 79,688 bytes
- Verdict: **CONFIRMED**
- Text returned: `<title>Ken Olsen - CHM</title>`, `1996 Fellow`, citation `For his introduction of the minicomputer as cofounder Digital Equipment Corporation`.

## p165 — Steve Wozniak
- Claimed list: Computer History Museum Fellow Awards
- URL: https://computerhistory.org/profile/steve-wozniak/ — HTTP 200, 78,747 bytes
- Verdict: **CONFIRMED**
- Text returned: `<title>Steve Wozniak - CHM</title>`, `1998 Fellow`, `For co-founding Apple Computer and inventing the Apple I personal computer`.

## p166 — Gene Amdahl
- Claimed list: Computer History Museum Fellow Awards
- URL: https://computerhistory.org/profile/gene-myron-amdahl/ — HTTP 200, 80,962 bytes
- Verdict: **CONFIRMED**
- Text returned: `<title>Gene Myron Amdahl - CHM</title>`, `1998 Fellow`, `For his fundamental work in computer architecture and design, project management, and leadership`. Body text also supports the row's IBM apprenticeship claim: `as Manager of Architecture for the IBM System/360`.

## p167 — Konrad Zuse
- Claimed list: Computer History Museum Fellow Awards
- URL: https://computerhistory.org/profile/konrad-zuse/ — HTTP 200, 78,631 bytes
- Verdict: **CONFIRMED**
- Text returned: `<title>Konrad Zuse - CHM</title>`, `1999 Fellow`, `For his invention of the first program-controlled, electromechanical, digital computer and the first high-level programming language, "Plankalkul"`.

## p168 — Thomas Frist Jr.
- Claimed list: Forbes World's Billionaires (self-made)
- URL: https://www.forbes.com/profile/thomas-frist-jr/ — HTTP 200, 890,717 bytes
- Verdict: **CONFIRMED**
- Text returned: `Thomas Frist, Jr. & family is #48 on Forbes' 2026 Billionaires list.`; bullets `Thomas Frist Jr., a former Air Force flight surgeon, founded Hospital Corp. of America with his father in 1968.` and `HCA Healthcare owns and operates 190 hospitals and around 2,400 sites of care in 20 U.S. states and the U.K.` — the row's company description matches word for word.
- Cross-check: 2026 API `48 | Thomas Frist, Jr. & family | selfMade=True | Hospitals`.

## p169 — Chung Yong-ji
- Claimed list: Forbes World's Billionaires (self-made)
- URL: https://www.forbes.com/profile/chung-yong-ji/ — HTTP 200, 853,506 bytes
- Verdict: **CONFIRMED** (with a wording caveat)
- WRONG-LIST check applied: the page's meta description headlines a *different* list — `Chung Yong-ji is #26 on Forbes' 2026 Korea's 50 Richest list`. The embedded list data on the same page does carry the Billionaires membership the row cites: `"displayName":"Billionaires 2026","rank":268`, alongside `"listUri":"billionaires"` and `"listUri":"korea-billionaires"`. Cross-checked in the 2026 billionaires API: `268 | Chung Yong-ji | selfMade=True | Biotech`. Right list, right rank.
- Text naming him: `Chung Yong-ji is the founder and CEO of South Korean biotechnology company Caregen, best known for its anti-wrinkle treatment and diabetes supplement.`
- Caveat (not a verdict change): the row's prose says "anti-wrinkle treatment and diabetes **drugs**"; the source says "diabetes **supplement**". Same product line, but "drugs" is not what the cited page says.

## p170 — Alyson Friedensohn
- Claimed list: Fortune 40 Under 40
- URL: https://fortune.com/ranking/40-under-40/2019/alyson-friedensohn-and-erica-johnson/ — HTTP 200, 146,232 bytes
- Verdict: **CONFIRMED**
- Text returned: `<title>Alyson Friedensohn and Erica Johnson | Fortune</title>`; on-page `40 Under 40` heading above `Alyson Friedensohn and Erica Johnson`; description `Industry: Health` and `Modern Health, a mental health startup from Y Combinator alums Friedensohn and Johnson, is just getting started ... The company offers holistic "emotional health services" to corporations, from counseling to career coaching, meditation apps, and other services online. They just completed a $9 million round of Series A funding`. Matches the row's quotes and its B2B-health-services / Series-A framing.

## p171 — Vinod Khosla
- Claimed list: Midas List
- URL: https://www.forbes.com/profile/vinod-khosla/ — HTTP 200, 944,782 bytes
- Verdict: **CONFIRMED**
- Midas-vs-Billionaires trap applied (this is a generic Forbes profile URL and the page carries `"listUri":"billionaires"` and `"listUri":"forbes-400"` too). The page text states Midas membership explicitly: `Vinod Khosla is ranked at No. 1 on the 2026 Midas List, his 19th appearance.` plus `Vinod Khosla is the founder of Khosla Ventures, a Silicon Valley venture capital firm.` and `"listUri":"midas"`.

## p172 — Eric Vishria
- Claimed list: Midas List
- URL: https://www.forbes.com/profile/eric-vishria/ — HTTP 200, 840,905 bytes
- Verdict: **CONFIRMED**
- Text returned: `Eric Vishria is #3 on Forbes' 2026 The Midas List: Top Tech Investors list.`; embedded `"name":"The Midas List: Top Tech Investors","year":2026` and `"section":"midas"`. `"listUri":"midas"` is the only list on this profile.

## p173 — Peter Thiel
- Claimed list: Midas List
- URL: https://www.forbes.com/profile/peter-thiel/ — HTTP 200, 892,821 bytes
- Verdict: **CONFIRMED**
- Text returned: `Peter Thiel returns to the Midas List for a 16th time as the cofounder and general partner of venture fund Founders Fund.` and `"The Midas List: Top Tech Investors 2026" ... "rank":5`. Verbatim match to the row's quote.

## p174 — Paul Thomas Anderson
- Claimed list: Academy Awards
- URL: https://en.wikipedia.org/wiki/98th_Academy_Awards — HTTP 200, 512,080 bytes
- Verdict: **CONFIRMED**
- Text returned: `<title>98th Academy Awards - Wikipedia</title>`; caption `Paul Thomas Anderson, Best Picture co-winner, and Best Director and Best Adapted Screenplay winner`; Best Picture producer line `... Sara Murphy, and Paul Thomas Anderson, producers`; `Best Directing` -> `Paul Thomas Anderson - One Battle After Another`; `Best Writing (Adapted Screenplay)` -> `One Battle After Another - Paul Thomas Anderson`.
- Note: Wikipedia as third-party evidence of the ceremony's contents is acceptable under the rules; oscars.org 403s and the row already documents that.

## p175 — SZA
- Claimed list: Grammy Awards
- URL: https://www.grammy.com/awards/68th-annual-grammy-awards-2025/ — HTTP 200, 499,970 bytes
- Verdict: **CONFIRMED**
- Text returned: `<title>68th Annual Grammy Awards 2026 | Grammy</title>`; parsed category block `['Record Of The Year', 'See all', 'Winner', 'Nominees', 'luther', 'Kendrick Lamar', ',', 'SZA', 'Credits', ...]` and the winners summary `['Record Of The Year', 'Kendrick Lamar', ',', 'SZA', 'luther']`. Page names SZA as a Record Of The Year winner, as the row claims. (URL slug says 2025; the page it serves is the 68th ceremony, 2026.)

## p176 — Alan J. Perlis
- Claimed list: Turing Award
- URL: https://amturing.acm.org/byyear.cfm — HTTP 200, 17,998 bytes
- Verdict: **CONFIRMED**
- Text returned: heading `CHRONOLOGICAL LISTING OF A.M. TURING AWARD WINNERS`; the year token `(1966)` immediately followed by `Perlis, Alan J *`.

## p177 — Maurice V. Wilkes
- Claimed list: Turing Award
- URL: https://amturing.acm.org/byyear.cfm — HTTP 200, 17,998 bytes
- Verdict: **CONFIRMED**
- Text returned: `(1967)` immediately followed by `Wilkes, Maurice V.*` in the same chronological listing.

## p178 — Lars Valerian Ahlfors
- Claimed list: Fields Medal
- URL: https://www.mathunion.org/imu-awards/fields-medal — HTTP 200, 58,670 bytes
- Verdict: **CONFIRMED**
- Text returned: laureate listing `1936` -> `Lars Valerian Ahlfors` / `Jesse Douglas`.

## p179 — Zach Sims
- Claimed list: Y Combinator Top Companies
- URL: https://www.ycombinator.com/companies/codecademy — HTTP 200, 81,838 bytes
- Verdict: **CONFIRMED** (with a sourcing caveat)
- Text returned: meta description `The leading online learning platform for technical skills. Founded in 2011 by Zach Sims, Codecademy has 225 employees based in New York City.` — verbatim match to the row's quote; embedded `"full_name":"Zach Sims","title":"Founder/CEO"`.
- Caveat: the YC company page names him but carries no "Top Company" marker anywhere in the HTML, so on its own it evidences the YC company directory, not the Top Companies list. Verified independently: top.json (91 entries) has `codecademy` at entry **6**. The row would be tighter if it cited that list URL the way p163 does.

## p180 — Larry Page
- Claimed list: Forbes World's Billionaires (self-made)
- URL: https://www.forbes.com/profile/larry-page/ — HTTP 200, 1,011,884 bytes
- Verdict: **CONFIRMED**
- Text returned: `Larry Page is #2 on Forbes' 2026 Billionaires list.`; bullet `He cofounded Google in 1998 with fellow Stanford Ph.D. student Sergey Brin.` supports the row's "PhD-track researcher" framing. API cross-check: `2 | Larry Page | selfMade=True | Google`.

## p181 — Ilya Volodarsky
- Claimed list: Y Combinator Top Companies
- URL: https://www.ycombinator.com/companies/segment — HTTP 200, 80,879 bytes
- Verdict: **CONFIRMED** (same sourcing caveat as p179)
- Text returned: `Software and APIs to collect, clean, and control customer data. Founded in 2011 by Ilya Volodarsky, Segment has 550 employees based in San Francisco.` — verbatim match; embedded `"full_name":"Ilya Volodarsky","title":"Founder"`. The developer-infrastructure / B2B-data description in the row matches.
- List membership verified independently: `segment` is entry **7** of top.json.

## p182 — Jeff Bezos
- Claimed list: Forbes World's Billionaires (self-made)
- URL: https://www.forbes.com/profile/jeff-bezos/ — HTTP 200, 945,229 bytes
- Verdict: **CONFIRMED**
- Text returned: `Jeff Bezos is #4 on Forbes' 2026 Billionaires list.`; bullet `Jeff Bezos founded e-commerce giant Amazon in 1994 out of his Seattle garage.` API: `4 | Jeff Bezos | selfMade=True | Amazon`.
- Note: the fetched page says nothing about his pre-Amazon quantitative-trading years; the row's "roughly eight years in quantitative trading" is its own research claim, not attributed to this URL. Membership and company description are fine.

## p183 — Neal O'Mara
- Claimed list: Y Combinator Top Companies
- URL: https://www.ycombinator.com/companies/hellosign — HTTP 200, 80,932 bytes
- Verdict: **CONFIRMED** (same sourcing caveat as p179)
- Text returned: `<title>HelloSign: eSignature software for small and mid-market businesses. | Y Combinator</title>`; meta description `eSignature software for small and mid-market businesses. Founded in  by Neal O&#39;Mara, HelloSign has 100 employees based in San Francisco.`; founders array contains `full_name":"Neal O'Mara`. The odd empty founding year ("Founded in by Neal O'Mara") that the row reproduces is present in the source itself — YC's bug, not the row's.
- List membership verified independently: `hellosign` is entry **8** of top.json.

## p184 — Mark Zuckerberg
- Claimed list: Forbes World's Billionaires (self-made)
- URL: https://www.forbes.com/profile/mark-zuckerberg/ — HTTP 200, 1,036,928 bytes
- Verdict: **CONFIRMED**
- Text returned: `Mark Zuckerberg is #5 on Forbes' 2026 Billionaires list.`; bullet `A 19-year-old Mark Zuckerberg started Facebook in 2004 for students to match names with photos of classmates.` supports the row's "undergraduate dropout" framing. API: `5 | Mark Zuckerberg | selfMade=True | Facebook`.

## p185 — Gautam Adani
- Claimed list: Forbes World's Billionaires (self-made)
- URL: https://www.forbes.com/forbesapi/person/billionaires/2025/position/true.json — HTTP 200, 3,966,268 bytes, 2,000 entries
- Verdict: **CONFIRMED**
- Text returned: `{'rank': 28, 'personName': 'Gautam Adani', 'source': 'Infrastructure, commodities', 'countryOfCitizenship': 'India', 'selfMade': True}` — every field the row asserts, matched.
- Secondary URL also fetched: https://www.forbes.com/profile/gautam-adani/ (HTTP 200, 852,148 bytes) returns `Adani grew his company, which began in 1988 as a commodities trading firm, into new sectors through debt-financing acquisitions` — verbatim match to the row's quote — and `Adani ... also controls Mundra Port, India's largest by cargo capacity, in his home state of Gujarat`, supporting the row's Mundra rank1 fallback. That profile's meta description headlines "2025 India's Richest", but the cited membership URL is the billionaires API, which is the list the column claims.
