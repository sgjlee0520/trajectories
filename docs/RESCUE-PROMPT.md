# Rescue pass — for Antigravity (use your strongest model, e.g. Opus 4.6)

Copy everything below the line. Produce ONE markdown file, `rescue-antigravity.md`, and save it in `~/trajectories/`.

Context you should know: an earlier six-platform blind cross-check on this project found that a single research pass has a real miss rate — one row was recorded as "not findable" and Antigravity/Opus was the only platform of six that actually found it, using a 1986 India Today article. That row is now good data. This task is the same thing at scale.

---

## TASK

Below are 14 people whose "first hit" year a previous researcher could NOT determine, plus one disputed row. For each, find the first year the criterion fired — or confirm honestly that it cannot be found.

Dig harder than a normal search. Archived newspapers, company histories, IPO prospectuses, court filings, trade press, non-English sources, Wayback Machine copies of dead pages. The whole point is finding what a first pass missed.

## THE THRESHOLD — READ CAREFULLY

For revenue rows the bar is **$10 million US in constant 2026 dollars**, NOT $10 million nominal. Older years have a far lower bar:

| Revenue year | Company must exceed |
|---|---|
| 1955 | $1,141,000 |
| 1960 | $919,417 |
| 1965 | $1,000,000 |
| 1970 | $1,343,000 |
| 1975 | $1,893,000 |
| 1980 | $2,559,459 |
| 1985 | $3,342,206 |
| 1990 | $4,059,725 |
| 1995 | $4,733,757 |
| 2000 | $5,348,772 |
| 2005 | $6,058,000 |
| 2010 | $7,166,000 |
| 2015 | $7,362,079 |
| 2020 | $8,039,031 |
| 2025 | $9,700,000 |

A Japanese retailer doing $3M in 1980 HAS crossed. A Chinese manufacturer doing $5M in 1990 HAS crossed. Convert non-USD at that year's exchange rate and state the rate.

## THE PEOPLE

| id | person | what to date |
|---|---|---|
| p03 | Tadashi Yanai | Fast Retailing / Ogori Shoji / Uniqlo — first year revenue crossed the bar |
| p21 | Kiran Mazumdar-Shaw | Biocon India — first year revenue crossed the bar. ANY revenue figure for any year 1978-1997 would settle it |
| p23 | Zhong Huijuan | Hansoh Pharmaceutical (江苏豪森药业) — company-level revenue, any year 1997-2010 |
| p24 | Alfred Mann | Which of HIS companies crossed FIRST — Spectrolab (1956), Heliotek (1960), or Pacesetter Systems (1969-72). Critical sub-question: what did Textron pay for Spectrolab in Aug 1960? One source says $300,000, another says $11 million. The Los Angeles Times of 2 August 1960 reported it |
| p27 | Kim Sung-joo | Sungjoo International / MCM Korea — revenue any year 1990-2009. Korean-language sources (성주인터내셔널) |
| p32 | Raghuram Rajan | A published third-party RANKING that named him #1 in a datable year. Not a prize, not an appointment. If none exists say so |
| p33 | Toni Morrison | First of her books to reach 1,000,000+ cumulative sales — likely Song of Solomon (1977) or Beloved (1987). A sourced sales figure, not an award |
| p47 | Aliko Dangote | Dangote Group — first year revenue crossed the bar. Founded 1977 as a trading company |
| p59 | Cyrus Poonawalla | Serum Institute of India — first year revenue crossed the bar. Founded 1966 |
| p69 | Terry Gou | Hon Hai / Foxconn — first year revenue crossed the bar. Founded 1974 |
| p76 | Trevor Martin | Mammoth Biosciences — first year revenue crossed the bar, or confirm it never has |
| p78 | Eileen Burbidge | Passion Capital — first fund she raised as a named partner above $100M in constant 2026 dollars |
| p85 | Wang Wei | SF Express (顺丰速运) — first year revenue crossed the bar. Founded 1993. Chinese sources |
| p75 | Jason Kelly | DISPUTED ROW, adjudicate. Ginkgo Bioworks, founded 2008. One researcher bounded the crossing to 2008-2017 using a Forbes 2017 estimate of "more than $20 million". Another said 2019, the first SEC-audited figure ($54.184M). Which is right? Is there any revenue figure for Ginkgo before 2019? |

## RULES

1. **Never infer or guess a year.** Each answer is a single sourced year, a sourced bounded range `YYYY-YYYY` (max 10 years, BOTH ends sourced), or the literal `unknown`.
2. A range needs a source BELOW the bar in the earlier year and a source AT OR ABOVE it in the later year. **A company's founding year is a valid lower end** — a company cannot earn before it exists.
3. **If the gap between your two sourced ends exceeds 10 years, the answer is `unknown`.** Do NOT report the later year. Reporting the first year a company happened to disclose revenue dates the career years too late, and that is the single worst error available here.
4. An IPO or acquisition year is usually years AFTER the real crossing. Do not use it as the answer.
5. **`unknown` is a good answer and several of these should stay unknown.** These 14 already defeated one researcher. A confident wrong year is far worse than an honest unknown.
6. Quote the exact sentence and give the URL for every figure.

## OUTPUT FORMAT

Start with this table:

```
| id | answer | confidence |
|---|---|---|
| p03 | 1984-1990 | medium |
| p21 | unknown | none |
```

Then a detailed section per person: the answer, the lower-end figure with its quoted sentence and URL, the upper-end figure the same way, the year's bar you compared against, any currency conversion with the rate, what you could not find, and your doubts.

Be exhaustive on sources. Where you fail, say specifically what you searched so it is not repeated.
