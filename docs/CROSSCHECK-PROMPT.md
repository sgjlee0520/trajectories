# Cross-check research task

Copy everything below the line into Perplexity, Gemini, Cursor, Antigravity, VS Code Copilot, or any other assistant. Run the SAME prompt on each platform independently, save each result as its own file (`crosscheck-<platform>.md`), and hand them all back.

Do not show one platform another platform's answers. The whole value is independence.

---

## TASK

For each of the 10 people below, find **the first calendar year** in which the named company's annual revenue crossed **$10 million US dollars measured in constant 2026 dollars** — or, where the criterion says `prize`, the **announcement year** of the prize.

Produce a markdown file. Format is specified at the bottom. Be detailed: I need your sources, not just your answers.

## THE CRITICAL RULE — READ TWICE

The threshold is **NOT $10 million nominal.** It is inflation-adjusted to 2026 dollars, so for older years the actual dollar figure is far smaller. Use this table. Find the row for the revenue year you are checking, and compare the company's revenue **that year** against the number in the right column.

| Revenue year | Company must exceed |
|---|---|
| 1950 | $748,579 |
| 1955 | $832,445 |
| 1960 | $919,417 |
| 1965 | $978,434 |
| 1970 | $1,205,182 |
| 1975 | $1,671,103 |
| 1980 | $2,559,459 |
| 1985 | $3,342,206 |
| 1990 | $4,059,724 |
| 1995 | $4,733,757 |
| 2000 | $5,348,772 |
| 2005 | $6,066,291 |
| 2010 | $6,773,124 |
| 2011 | $6,986,920 |
| 2012 | $7,131,510 |
| 2013 | $7,235,970 |
| 2014 | $7,353,351 |
| 2015 | $7,362,079 |
| 2016 | $7,454,953 |
| 2017 | $7,613,770 |
| 2018 | $7,799,734 |
| 2019 | $7,941,064 |
| 2020 | $8,039,031 |
| 2021 | $8,416,707 |
| 2022 | $9,090,273 |
| 2023 | $9,464,470 |
| 2024 | $9,743,619 |
| 2025 | $10,000,000 |
| 2026 | $10,000,000 |

(Years not listed: interpolate between neighbours. If a company's revenue in year Y exceeds the figure for year Y, it has crossed.)

**Worked example.** A company with $1.2M revenue in 1976 HAS crossed, because the 1976 bar is about $1.77M — no wait, $1.2M is *below* $1.77M, so it has NOT crossed. A company with $2.0M in 1976 HAS crossed. Check the arithmetic yourself every time; this is the single most common error on this task.

Convert non-USD revenue at the exchange rate for that revenue year, and state the rate you used.

## THE PEOPLE

| id | person | company | criterion |
|---|---|---|---|
| p62 | Shiv Nadar | HCL (Hindustan Computers Limited) | rev10 |
| p63 | Harshil Mathur | Razorpay | rev10 |
| p64 | Sid Sijbrandij | GitLab | rev10 |
| p65 | Chris Wanstrath | GitHub | rev10 |
| p71 | Radhakishan Damani | Avenue Supermarts (DMart) | rev10 |
| p72 | Zhong Shanshan | Nongfu Spring | rev10 |
| p73 | He Xiangjian | Midea | rev10 |
| p78 | Eileen Burbidge | Passion Capital | rev10 |
| p81 | Simon Brendle | Breakthrough Prize in Mathematics | prize |
| p82 | Maryna Viazovska | Fields Medal | prize |

## RULES YOU MUST FOLLOW

1. **Never infer, estimate, or guess a year.** Your answer for each person is one of:
   - a single year (e.g. `2011`), or
   - a bounded range (e.g. `2008-2014`) where you have a source showing revenue BELOW the bar in the earlier year and a source showing it AT OR ABOVE the bar in the later year, or
   - the literal word `unknown`.
2. **A range may span at most 10 years.** If the gap between your two sourced ends is more than 10 years, the answer is `unknown` — do NOT report the later year as the answer. Reporting the first year a company happened to disclose revenue is wrong: the real crossing was earlier, and you would be dating the career too late. This is the single most damaging error possible here.
3. **A company's founding year is a valid lower end of a range** — a company cannot earn revenue before it exists.
4. **`unknown` is a good answer.** Many private companies never published early revenue. A confident wrong year is far worse than an honest `unknown`. Do not stretch weak evidence to produce a number.
5. **Quote your evidence.** For every figure, give the exact sentence and the URL. A claim with no quotable source does not count as found.
6. If a company was acquired or listed, note that its IPO or acquisition year is usually **years after** the real crossing. Do not use it as the answer unless you have no revenue data at all, and if so say so explicitly.

## OUTPUT FORMAT — follow exactly

Produce a markdown file that starts with this table:

```
| id | answer | confidence |
|---|---|---|
| p62 | 1985 | high |
| p63 | unknown | none |
...
```

Confidence is `high`, `medium`, `low`, or `none`.

Then, for EACH person, a detailed section:

```
### p62 — Shiv Nadar / HCL

**Answer:** 1985

**Lower end:** [figure] in [year], vs the bar of [amount] for that year — below.
> "exact quoted sentence from the source"
Source: [URL]

**Upper end:** [figure] in [year], vs the bar of [amount] for that year — above.
> "exact quoted sentence from the source"
Source: [URL]

**Currency conversion:** [rate used, if any]

**What I could not find:** [be specific about the gaps]

**Doubts:** [anything that would change the answer]
```

Be thorough in these sections. The summary table gets compared across platforms automatically; the detail is what lets a human adjudicate when platforms disagree.
