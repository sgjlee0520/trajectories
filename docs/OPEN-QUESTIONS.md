# Open questions for a search-first tool (Perplexity)

Seven questions that Claude Code research agents attempted repeatedly and lost.
Each is a single fact. Three would rescue a currently-excluded row; two more,
added in wave 6, decide whether a recorded row should have been excluded.

**How to use this:** paste a block into Perplexity, then paste the answer back.
What matters is the **URL and the exact quoted sentence**, not Perplexity's
summary. A synthesised claim with no citation is worth nothing here — the
frame's rule is that no year is ever inferred, and a confident paraphrase is
exactly how an inferred year gets laundered into data. If Perplexity gives a
figure without a source that states it, that counts as *not found*.

---

## Q1 — Highest value. Decides whether Alfred Mann (p24) is in the study at all.

> In the Los Angeles Times of 2 August 1960, there is a report of Textron
> acquiring Spectrolab, the solar-cell company founded by Alfred E. Mann in
> 1956. What purchase price does that article give? Separately, what was
> Spectrolab's annual revenue in any year between 1956 and 1960? Quote the
> exact sentence and give the source URL for each.

**Why it matters:** two sources conflict by a factor of 37. One account citing
that LA Times piece says Textron paid **$300,000**; the International Directory
of Company Histories says **$11 million**. Under the $300k reading Spectrolab
was below the 1960 threshold ($919,417) and Mann stays excluded. Under the $11M
reading he becomes a bounded 1956-1960 hit — a **pre-1995** row, in a bucket
that has only one dated row. Note the IDCH figure sits one paragraph from an
"$11,200" founding contract, so it may be a transcription corruption. That is
a suspicion, not evidence.

## Q2 — Would rescue Kiran Mazumdar-Shaw (p21).

> What was Biocon India's annual revenue, turnover, or sales in any single year
> between 1978 and 1997? Any year in that range will do. Quote the figure, the
> year, and give the source URL.

**Why it matters:** an upper bound already exists (Rs 70 crore in 1998, 335% of
that year's bar). Any single figure from 1978-1997 that is *below* the bar for
its year closes the bracket and converts an exclusion into a dated `primary`
row. Six attempts found nothing: Biocon's own history pages, the FY2004 annual
report, the 2004 IPO prospectus (scanned images, not text), an MIT Sloan case,
and a WIPO case study.

## Q3 — Would rescue Zhong Huijuan (p23).

> What was the annual revenue of Hansoh Pharmaceutical (豪森药业 / Jiangsu
> Hansoh) in any year between 1997 and 2010? Company-level revenue, not the
> sales of a single product. Quote the figure, the year, and the source URL.
> Chinese-language sources are welcome.

**Why it matters:** the lower end is soft but present (1997), and the earliest
company-level figure found anywhere is 2011 — a fourteen-year gap, over the
ten-year limit. Any company-level figure between 1997 and 2010 closes it.
Seven attempts failed, including Hengrui's 2007 annual report from cninfo,
which names Hansoh as a related party but discloses no Hansoh financials.

## Q4 — Lowest value, ask last. Two rows already excluded on it.

> Does any published ranking or rich list name Kazuhiko Nishi (西和彦), founder
> of ASCII Corporation — for example a Nikkei or Toyo Keizai ranking, or a
> Japanese 長者番付 / 高額納税者番付 list? Separately: has Sandra Kurtzig,
> founder of ASK Computer Systems, ever appeared on the Forbes 400? Give the
> year and source URL for either.

**Why it matters:** both are excluded as `roster_unverified` — researched in
full, but no source list in `frame.md` could be confirmed to contain them. A
single confirmed listing reinstates a fully-researched row. Already checked and
negative: Women in Technology International Hall of Fame (1996-2021) and
Computer History Museum Fellows (1987-present) contain neither. Kurtzig's ASK
stake was worth about $65-67M in 1981-83 against a $75M bar for the inaugural
1982 Forbes 400, so she was probably just under the cut — expect this one to
come back negative, and that is a fine answer.

## Q5 — Wave 6. Decides whether a row stays in or is excluded.

> In what year was Alpaca (the US brokerage-infrastructure company founded by
> Yoshi Yokokawa, legal entity AlpacaDB, Inc.) founded, and what was its
> revenue in any year before 2024? Four sources give four different founding
> years — 2013 (Ikkyo Technology, the Kobe predecessor), 2015 (AlpacaDB/Sacra),
> 2017 (Keio) and 2018 (MEXT). Quote the figure or year and the source URL.

**Why it matters:** p141 is recorded as a bounded `rev10` of 2015-2024 (span 9),
using the 2015 AlpacaDB founding as the lower bound and a $60M end-2024 figure as
the upper. **On the 2013 lineage the span is 11 years and the row must instead be
`crossing_undatable`.** The first-pass researcher raised this against its own row.
TechCrunch (Oct 2023) reports revenue grew 17x since 2021 but the company declined
to give the baseline, which implies the true crossing is around 2022-2023 while the
recorded midpoint is 2019-2020 — so this row probably dates the hit several years
early. `a5_first_hit_conf` is `low` for that reason. Already checked and negative:
all four Alpaca Securities LLC X-17A-5 filings on EDGAR (CIK 0001702580) — the
public portion is a statement of financial condition only, with no income statement.

## Q6 — Wave 6. Would resolve which of two ventures is the hit.

> Did Ready Chemical (M) Sdn. Bhd. or Multiview Enterprise Sdn. Bhd. — both
> established in Malaysia in 1984 by Loi Tuan Ee, later sold into Century Bond
> Bhd — ever report annual revenue, employee numbers, or any statement of
> scale? Any year. Quote the figure and the source URL.

**Why it matters:** p147's hit is recorded as Farm Fresh / The Holstein Milk
Company (bounded 2012-2016), but Loi is a serial founder and those two 1984
companies came first. No source of any kind attaches revenue, headcount or a scale
claim to either, so the frame gives no basis to date them — an unsourced suspicion
is not grounds for exclusion. If either crossed first, p147's hit year moves back by
nearly three decades. Already checked and negative: Farm Fresh Berhad's FY2024
annual report (names both companies, no financials), NUS-held Century Bond annual
reports (HTTP 401), EMIS/CTOS/D&B (paywalled).

## Q7 — Wave 6. The two passes split on whether this row exists at all.

> What was the annual revenue of POP / Sushi Pop (the Argentine restaurant group
> co-founded by Mateo Marietti and Diego Araujo in 2007/08, which grew to eight
> brands in four countries) in any year between 2010 and 2021? Group revenue, not
> the Sushi Pop brand alone. Quote the figure, the year and the source URL.

**Why it matters:** this is the one row where the blind audit's second pass reached
a different verdict than the first, and the disagreement metric could not see it
because the first pass returned `unknown`.

The first pass excluded p146 as `crossing_undatable`: Endeavor Argentina's bio says
POP grew to eight brands in four countries with 1,000+ employees, which under
frame.md is a qualitative claim sufficient to establish an earlier crossing — and
the only sourced below-bar year is 2009, making the bracket 2009-2021, twelve years
and over the limit.

The second pass independently checked the same earlier venture, found dated figures
in both directions, and concluded it never demonstrably crossed: ARS 3M for 2009
(El Cronista) = US$0.8M = 12% of that year's bar, and ARS 200M projected for 2018
(La Nación) = US$7.1M = 91% of that year's bar. On that reading CookUnity is the hit
and the row is a bounded 2018-2025.

**The two are not actually contradictory** — the dated figures describe the Sushi Pop
*brand*, while the qualitative claim describes the eight-brand *group*, and a
1,000-employee group booking US$7.1M would be implausible. So they are probably
measuring different entities. A single group-level revenue figure settles it.

The row is currently **excluded**, the conservative reading: frame.md says a
qualitative scale claim establishes an earlier crossing, and an honest exclusion
beats a stretched date. Note the direction, though — including it would add a clock
of roughly 14 years, which is long, and the study's two strongest known biases both
push the median short.

---

## What NOT to ask a search-first tool

Do not use it to research a person's anchors from scratch. It synthesises
across sources and will produce a plausible year with a citation that does not
actually contain it. That failure is invisible unless someone opens the link —
and it is the precise mechanism `docs/BIASES.md` 13 describes, where a name
"cited" to a list turned out to be on no list at all.

Use it where the question is narrow, factual, and already stuck. Verify every
URL it returns before the answer enters `data/anchors.csv`.
