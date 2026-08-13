# Open questions for a search-first tool (Perplexity)

Four questions that Claude Code research agents attempted repeatedly and lost.
Each is a single fact. Three of them would rescue a currently-excluded row.

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

---

## What NOT to ask a search-first tool

Do not use it to research a person's anchors from scratch. It synthesises
across sources and will produce a plausible year with a citation that does not
actually contain it. That failure is invisible unless someone opens the link —
and it is the precise mechanism `docs/BIASES.md` 13 describes, where a name
"cited" to a list turned out to be on no list at all.

Use it where the question is narrow, factual, and already stuck. Verify every
URL it returns before the answer enters `data/anchors.csv`.
