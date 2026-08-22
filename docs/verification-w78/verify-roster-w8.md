# Roster membership verification — wave 8 (p186–p210)

Verifier: independent re-fetch pass. Every URL below was actually fetched this session
(curl with a Chrome User-Agent). No roster data was modified.
WebSearch was not needed and not used — every citation resolved by direct fetch.

## Summary

| id | name | claimed list | verdict |
|----|------|--------------|---------|
| p186 | Mariya Nurislamova | Y Combinator Top Companies | CONFIRMED |
| p187 | Jim Ratcliffe | Sunday Times Rich List (UK) | CONFIRMED |
| p188 | Lakshmi Mittal | Sunday Times Rich List (UK) | CONFIRMED |
| p189 | Carver Mead | Computer History Museum Fellow Awards | CONFIRMED |
| p190 | Stephen Lake | Y Combinator Top Companies | CONFIRMED |
| p191 | Aleksandr Konotopskyi | Endeavor Entrepreneur network | CONFIRMED |
| p192 | Luca Rossettini | Endeavor Entrepreneur network | CONFIRMED |
| p193 | Murali Divi | Hurun Rich List (India) | CONFIRMED |
| p194 | Zhu Yi | Hurun Rich List (China) | CONFIRMED |
| p195 | Elad Gil | Midas List | CONFIRMED |
| p196 | Trae Stephens | Midas List | CONFIRMED |
| p197 | Billie Eilish | Grammy Awards | CONFIRMED |
| p198 | Bess Wohl | Pulitzer Prize | CONFIRMED |
| p199 | Jill Lepore | Pulitzer Prize | CONFIRMED |
| p200 | Laurent Schwartz | Fields Medal | CONFIRMED |
| p201 | Ragnar Frisch | Nobel Prizes (Economics) | CONFIRMED |
| p202 | Edward Witten | Breakthrough Prize | CONFIRMED |
| p203 | Victor Ho | Y Combinator Top Companies | WRONG-LIST |
| p204 | Larry Ellison | Forbes World's Billionaires (self-made) | CONFIRMED |
| p205 | Michael Nusimow | Y Combinator Top Companies | WRONG-LIST |
| p206 | Zhang Yiming | Hurun Rich List (China) | CONFIRMED |
| p207 | Bo Lu | Y Combinator Top Companies | WRONG-LIST |
| p208 | Ma Huateng | Hurun Rich List (China) | CONFIRMED |
| p209 | Huang Zheng | Hurun Rich List (China) | CONFIRMED |
| p210 | Fred Smith | Forbes World's Billionaires (self-made) | CONFIRMED |

22 CONFIRMED, 3 WRONG-LIST, 0 NAMES-NOBODY, 0 COMPANY-MISMATCH, 0 UNREACHABLE.

---

## p186 — Mariya Nurislamova
- Claimed list: Y Combinator Top Companies
- URLs: https://www.ycombinator.com/companies/scentbird ; https://yc-oss.github.io/api/companies/top.json
- Verdict: **CONFIRMED**
- Company page (HTTP 200, 66KB; embedded JSON, HTML-entity-escaped) returned:
  `"full_name":"Mariya Nurislamova","title":"Founder"` and
  `"one_liner":"Scentbird is a luxury fragrance subscription service."`
- top.json (HTTP 200, 171KB, 91 company objects) returned `"name": "Scentbird"` as the
  58th company object — matches "entry 58 of the 91-company list" exactly.
- why_selected's "direct-to-consumer fragrance subscription business" matches the fetched one_liner.

## p187 — Jim Ratcliffe
- Claimed list: Sunday Times Rich List (UK)
- URL: https://en.wikipedia.org/wiki/Sunday_Times_Rich_List_2025
- Verdict: **CONFIRMED**
- Fetched (HTTP 200, 124KB). Table row text as rendered:
  `07 | £17.046 | Sir Jim Ratcliffe | United Kingdom | Industry ( Ineos )`
- Matches the citation string. Wikipedia article *about* the list = accepted third-party
  evidence per the rubric. "Industrial-chemicals founder" is consistent with the page's own
  industry label "Industry (Ineos)".

## p188 — Lakshmi Mittal
- Claimed list: Sunday Times Rich List (UK)
- URL: https://en.wikipedia.org/wiki/Sunday_Times_Rich_List_2025
- Verdict: **CONFIRMED**
- Same fetch. Row text: `08 | £15.444 | Lakshmi Mittal and family | India | Steel`
- Matches verbatim; "steel-manufacturing founder" matches the page's "Steel".

## p189 — Carver Mead
- Claimed list: Computer History Museum Fellow Awards
- URL: https://computerhistory.org/profile/carver-mead/
- Verdict: **CONFIRMED**
- Fetched (HTTP 200, 79KB). `<title>Carver Mead - CHM`. Body: `Carver Mead` / `2002 Fellow`
  and the citation `For his contributions in pioneering the automation, methodology and
  teaching of integrated circuit design`.
- Page also corroborates the VLSI/Caltech/Foveon description in why_selected:
  "Chairman and Founder of Foveon, Inc. ... Gordon and Betty Moore professor emeritus at the
  California Institute of Technology, having taught there for over 40 years."

## p190 — Stephen Lake
- Claimed list: Y Combinator Top Companies
- URL: https://yc-oss.github.io/api/companies/top.json
- Verdict: **CONFIRMED**
- Fetched (HTTP 200, 171KB). 35th company object is `"name": "North"`, with
  `"one_liner": "Wearable computing hardware: biosignal gesture recognition"` and
  long_description `Founded in 2012 by three graduates of the University of Waterloo's
  mechatronics engineering program (Stephen Lake, Matthew Bailey, Aaron Grant), Thalmic Labs
  has grown to a world-leading team of engineers, researche…`
- Person named, position 35 correct, hardware description matches.

## p191 — Aleksandr Konotopskyi
- Claimed list: Endeavor Entrepreneur network
- URL: https://endeavor.org/entrepreneurs/ (301 → https://endeavor.org/entrepreneur-companies/)
- Verdict: **CONFIRMED**
- Contrary to the session note, this URL **does** name people in server-rendered HTML when
  fetched with a browser UA (HTTP 200, 244KB). Extracted block:
  `Ajax Systems | Ajax Systems designs and manufactures professional-grade security systems for
  residential and commercial properties. | Outlier Company | Website | Europe | Selected: 2025 |
  Smart City & Climate | Industry 4.0 | Entrepreneurs | Aleksandr Konotopskyi | Local Office |
  Endeavor Ukraine`
- Matches the citation verbatim; "security-system hardware manufacturer" matches the page.
- Caveat (not a defect in what I fetched): this is page 1 of a paginated directory, so the URL
  is not stable evidence over time.

## p192 — Luca Rossettini
- Claimed list: Endeavor Entrepreneur network
- URL: https://endeavor.org/entrepreneurs/?_paged=4 (→ /entrepreneur-companies/?_paged=4)
- Verdict: **CONFIRMED**
- Fetched (HTTP 200, 251KB). Extracted block:
  `D-Orbit | D-Orbit is a satellite technology provider for the traditional and new space sectors.
  It develops and supplies launching, decommissioning, and life extension devices to help satellite
  operators and agencies manage the end of their satellite's life. | Outlier Company | Website |
  Europe | Selected: 2016 | Smart City & Climate | Aerospace, Imaging & Communications |
  Entrepreneurs | Renato Panesi | Luca Rossettini | Local Office | Endeavor Italy`
- Names him; company description matches why_selected exactly.
- Same pagination caveat as p191, more acute: `?_paged=4` will drift as the directory grows.

## p193 — Murali Divi
- Claimed list: Hurun Rich List (India)
- URL: https://www.hurun.net/en-US/Rank/HsRankDetailsList?num=MIJ7F3W6&search=Murali%20Divi&offset=0&limit=5
- Verdict: **CONFIRMED**
- JSON endpoint fetched with Referer header (HTTP 200, 2.2KB). Returned:
  `"hs_Rank_India_Ranking":20`, `"hs_Rank_India_ChaName_En":"Murali Divi"`,
  `"hs_Rank_India_ComName_En":"Divi's Laboratories"`,
  `"hs_Rank_India_Industry_En":"Pharmaceuticals"`, `"hs_Rank_India_Year":"2022"`,
  `"hs_Character_Fullname_En":"Murali Divi"`
- Year field 2022 + the India rank schema corroborate "Hurun India Rich List 2022"; the
  `num=MIJ7F3W6` detail page renders under "Hurun Rich List series".
- Industry "Pharmaceuticals" is consistent with the row's API/custom-synthesis description
  (the endpoint carries no finer granularity, so it neither confirms nor contradicts
  "API and custom synthesis" specifically).

## p194 — Zhu Yi
- Claimed list: Hurun Rich List (China)
- URL: https://www.hurun.net/en-US/Rank/HsRankDetailsList?num=ODQWW2BI&search=Zhu%20Yi&offset=0&limit=5
- Verdict: **CONFIRMED**
- Fetched (HTTP 200, 6.4KB). First result: `"hs_Rank_Rich_Ranking":30`,
  `"hs_Rank_Rich_ChaName_En":"Zhu Yi"`, `"hs_Rank_Rich_ComName_En":"Biokin Pharmaceutical"`,
  `"hs_Rank_Rich_Industry_En":"Pharmaceuticals"`, `"hs_Rank_Rich_Year":"2025"`
- Matches citation verbatim. (Search is a prefix match — it also returned Zhu Yiming /
  GigaDevice at 584 and Zhu Yinghui / Rongtai at 1267; the cited record is the first.)

## p195 — Elad Gil
- Claimed list: Midas List
- URL: https://www.forbes.com/profile/elad-gil/
- Verdict: **CONFIRMED**
- Fetched (HTTP 200, 837KB). Page text: `Elad Gil is ranked at No. 6 on the 2026 Midas List,
  his 2nd appearance.` and meta description `Elad Gil is #6 on Forbes' 2026 The Midas List:
  Top Tech Investors list.`
- The profile page itself states the Midas List ranking, so it is evidence of Midas membership,
  not merely a generic Forbes profile.

## p196 — Trae Stephens
- Claimed list: Midas List
- URL: https://www.forbes.com/profile/trae-stephens/
- Verdict: **CONFIRMED**
- Fetched (HTTP 200, 841KB). Page text: `Trae Stephens is ranked at No. 7 on the 2026 Midas List,
  his 3rd appearance.` and `Trae Stephens is #7 on Forbes' 2026 The Midas List: Top Tech
  Investors list.`
- Page also carries `Debut Midas listers including Anduril cofounder Trae Stephens and Google
  Voice creator Wesley Chan inked huge deals in defense, consumer`, corroborating the Anduril
  claim in why_selected.

## p197 — Billie Eilish
- Claimed list: Grammy Awards
- URL: https://www.grammy.com/awards/68th-annual-grammy-awards-2025/
- Verdict: **CONFIRMED**
- Fetched with curl + browser UA (HTTP 200, 500KB).
  `<title>68th Annual Grammy Awards 2026 | Grammy` — the slug says 2025, the page title says
  2026 (the counterintuitive slug flagged in the session notes).
- Winners table row: `Song Of The Year | Billie Eilish, Finneas O'Connell | WILDFLOWER`,
  under the `Winners` / `Category | Winner | Title` header.
- Full credit line on the page: `Billie Eilish O'Connell & Finneas O'Connell, songwriters
  (Billie Eilish)` — matches the citation.

## p198 — Bess Wohl
- Claimed list: Pulitzer Prize
- URL: https://www.pulitzer.org/prize-winners-by-year/2026
- Verdict: **CONFIRMED**
- Fetched (HTTP 200, 118KB). `<title>2026 Prize Winners and Finalists | The Pulitzer Prizes`.
  Drama section: `Drama | Liberation | , by Bess Wohl | A striking blend of comedy and sincerity
  that explores the legacy of the consciousness-raising feminist groups of the 1970s, using the
  story of the playwright's mother…` followed by `Finalists:` — so Wohl occupies the winner slot,
  not a finalist slot.

## p199 — Jill Lepore
- Claimed list: Pulitzer Prize
- URL: https://www.pulitzer.org/prize-winners-by-year/2026
- Verdict: **CONFIRMED**
- Same fetch. History section: `History | We the People: A History of the U.S. Constitution |
  , by Jill Lepore (Liveright) | A lively and engaging narrative that investigates why the
  Constitution is so difficult to amend…` followed by `Finalists:` — winner slot.

## p200 — Laurent Schwartz
- Claimed list: Fields Medal
- URL: https://www.mathunion.org/imu-awards/fields-medal
- Verdict: **CONFIRMED**
- Plain curl (HTTP 200, 59KB). Laureate listing renders as:
  `… 1954 | Kunihiko Kodaira | Jean-Pierre Serre | 1950 | Laurent Schwartz | Atle Selberg | 1936 …`
- Named under year 1950 exactly as cited.

## p201 — Ragnar Frisch
- Claimed list: Nobel Prizes (Economics)
- URL: https://www.nobelprize.org/prizes/economic-sciences/1969/summary/
- Verdict: **CONFIRMED**
- curl + browser UA (HTTP 200, 159KB). Page text:
  `The Sveriges Riksbank Prize in Economic Sciences in Memory of Alfred Nobel 1969 was awarded
  jointly to Ragnar Frisch and Jan Tinbergen` plus a standalone `Ragnar Frisch` laureate heading.
- Matches the citation.

## p202 — Edward Witten
- Claimed list: Breakthrough Prize
- URL: https://breakthroughprize.org/Laureates/1/P1/Y2012
- Verdict: **CONFIRMED**
- Plain curl (HTTP 200, 5.9KB — small, but server-rendered, not a JS shell).
  `<title>2012 Breakthrough Prize in Fundamental Physics Laureates`. Body:
  `The Breakthrough Prize in Fundamental Physics was founded in 2012 with the naming of nine
  inaugural laureates, establishing the first Selection Committee to choose future winners.`
  followed by `Edward Witten | Ashoke Sen | Nathan Seiberg | Juan Maldacena | Andrei Linde |
  Maxim Kontsevich | Alexei Kitaev | Alan Guth | Nima Arkani-Hamed`
- Nine names, Witten first, exactly as cited.

## p203 — Victor Ho
- Claimed list: Y Combinator Top Companies
- URL: https://www.ycombinator.com/companies/fivestars
- Verdict: **WRONG-LIST**
- The page names him: `"full_name":"Victor Ho","title":"Founder/CEO"` (also `Matt Doka`,
  `Founder/CTO`), and `"one_liner":"Customer loyalty and payments platform for small businesses."`
  — the company description in why_selected is accurate.
- But this is a YC company **directory profile**, not the **Top Companies** list. I searched the
  fetched HTML (entity-unescaped) case-insensitively for `top compan*` and for a `top_company`
  JSON field — zero hits. Nothing on the page states Top Companies membership, so the cited URL
  does not evidence the claimed list. Same failure shape as the Forbes-profile / Midas-List
  example in the rubric.
- Substance is fine: I independently fetched https://yc-oss.github.io/api/companies/top.json and
  `"name": "Fivestars"` is the 9th of 91 company objects. This is a citation defect — swapping in
  the top.json URL (as p186 and p190 already do) would fix it.

## p204 — Larry Ellison
- Claimed list: Forbes World's Billionaires (self-made)
- URL: https://www.forbes.com/profile/larry-ellison/
- Verdict: **CONFIRMED**
- Fetched (HTTP 200, 940KB). Page text: `Larry Ellison is #6 on Forbes' 2026 Billionaires list.`
  Profile header field: `Oracle, Self Made` — confirms both the source of wealth (Oracle =
  enterprise software, matching "pre-1995 enterprise-software founder") and the self-made flag
  the source_list qualifier requires.

## p205 — Michael Nusimow
- Claimed list: Y Combinator Top Companies
- URL: https://www.ycombinator.com/companies/drchrono
- Verdict: **WRONG-LIST**
- The page names him: `"full_name":"Michael Nusimow","title":"Founder/CEO"` (also
  `Daniel Kivatinos`, `Founder/COO`), `"one_liner":"The essential platform for modern medical
  practices and patients."` and long_description `DrChrono develops the essential platform and
  services for modern medical practices … The open platform powers telehealth, electronic health
  record (EHR), practice management, medical billing, a…` — "vertical-SaaS … medical practice
  software" is accurate.
- Same defect as p203: a company directory profile, no Top Companies statement anywhere in the
  fetched HTML.
- Substance is fine: `"name": "DrChrono"` is the 11th of 91 objects in top.json.

## p206 — Zhang Yiming
- Claimed list: Hurun Rich List (China)
- URL: https://www.hurun.net/en-US/Rank/HsRankDetailsList?num=ODQWW2BI&search=&offset=0&limit=60
- Verdict: **CONFIRMED**
- Fetched with Referer header (HTTP 200, 142KB). Record:
  `"hs_Rank_Rich_Ranking":2` … `"hs_Character_Fullname_En":"Zhang Yiming"` …
  `"hs_Rank_Rich_ChaName_En":"Zhang Yiming"` … `"hs_Rank_Rich_ComName_En":"ByteDance"` …
  `"hs_Rank_Rich_Industry_En":"Social Media"` … `"hs_Rank_Rich_Year":"2025"`
- Matches citation verbatim. `num=ODQWW2BI` resolves to a Hurun Rich-List-series detail page.

## p207 — Bo Lu
- Claimed list: Y Combinator Top Companies
- URL: https://www.ycombinator.com/companies/futureadvisor
- Verdict: **WRONG-LIST**
- The page names him: `"full_name":"Bo Lu","title":"Founder/CEO"`,
  `"one_liner":"The online financial management service for everyone."` and long_description
  `FutureAdvisor is an award-winning digital wealth management firm serving client households
  nationwide from our offices in San Francisco. We use software to power a wealth management
  experience accessible to everyone…` — "consumer fintech advisory service" is accurate.
- Same defect as p203/p205: company directory profile, no Top Companies statement in the HTML.
- Substance is fine: `"name": "FutureAdvisor"` is the 13th of 91 objects in top.json.

## p208 — Ma Huateng
- Claimed list: Hurun Rich List (China)
- URL: https://www.hurun.net/en-US/Rank/HsRankDetailsList?num=ODQWW2BI&search=&offset=0&limit=60
- Verdict: **CONFIRMED**
- Same fetch. Record: `"hs_Rank_Rich_Ranking":3` … `"hs_Character_Fullname_En":"Ma Huateng"` …
  `"hs_Rank_Rich_ComName_En":"Tencent"` … `"hs_Rank_Rich_Industry_En":"Gaming, Telecoms"`
- Matches citation verbatim; "messaging portal" is consistent with the page's Tencent /
  "Gaming, Telecoms" labelling.

## p209 — Huang Zheng
- Claimed list: Hurun Rich List (China)
- URL: https://www.hurun.net/en-US/Rank/HsRankDetailsList?num=ODQWW2BI&search=&offset=0&limit=60
- Verdict: **CONFIRMED**
- Same fetch. Record: `"hs_Rank_Rich_Ranking":7` … `"hs_Character_Fullname_En":"Huang Zheng"` …
  `"hs_Rank_Rich_ComName_En":"Pinduoduo"` … `"hs_Rank_Rich_Industry_En":"E-Commerce"`
- Matches citation verbatim; "serial e-commerce founder" matches the page's E-Commerce label.

## p210 — Fred Smith
- Claimed list: Forbes World's Billionaires (self-made)
- URL: https://www.forbes.com/forbesapi/person/billionaires/2025/position/true.json
- Verdict: **CONFIRMED**
- Fetched with `?limit=2000` (HTTP 200, 3.97MB). Record:
  `"rank":605,"listUri":"billionaires","visible":true,"position":615,…"finalWorth":5800.0,
  "category":"Logistics",…"personName":"Fred Smith","age":80,"country":"United States",
  "state":"Tennessee","city":"Memphis","source":"FedEx","industries":["Logistics"],
  "countryOfCitizenship":"United States","organization":"FedEx",…"selfMade":true,…
  "listDescription":"The World's Billionaires","title":"Founder and Executive Chairman"`
- Every field asserted in why_selected (rank 605, personName, source, industries, citizenship,
  selfMade) matches exactly. "Express-freight carrier" matches source FedEx / industry Logistics.
