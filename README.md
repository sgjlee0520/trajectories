# Apprenticeship Trajectories

**How long does it take to get good enough that it pays?**

This study measures the interval from the end of formal education to the first
year an individual's own venture crossed **$10 million in constant 2026
dollars**, across 235 people drawn only from enumerated third-party lists.

**Result: a median of 9.0 years, 95% CI [8.0, 10.0], on the 93 people for whom
that interval is computable from primary revenue evidence.**

## Read this first

The number describes **time-to-hit among people who already made it.** The
sample is conditioned on the outcome and has no denominator. People who worked
for twenty years and never crossed are absent by construction, not by rarity,
and the two strongest measured biases both push the figure short.

**It is a floor on the observed, not a forecast for the aspiring.** No figure in
this repository supports a statement about the odds of succeeding.

## The papers

- [sgjlee0520.github.io/trajectories-site](https://sgjlee0520.github.io/trajectories-site/) — English and Korean pages with the PDFs embedded
- [`analysis/paper.pdf`](analysis/paper.pdf) — the study, in English
- [`analysis/paper-ko.pdf`](analysis/paper-ko.pdf) — 한국어판

Sources: `analysis/paper.tex` (pdflatex) and `analysis/paper-ko.tex` (xelatex +
kotex).

## The more useful findings

The pooled median is a mixture, not a constant.

| | n | median | 95% CI |
|---|---|---|---|
| Hit before 1995 | 33 | **13.0 yr** | [9.0, 18.0] |
| Hit after 1995 | 60 | **8.0 yr** | [6.5, 9.0] |
| **From first venture**, all eras | 118 | **4.2 yr** | [4.0, 5.0] |

The sample is 74% post-1995, so the pooled 9.0 is a weighted average of two eras
five years apart. The venture clock is the best-measured quantity here: it
retains 98% of eligible rows against the headline clock's 77%.

## What is in here

| path | what |
|---|---|
| `frame.md` | the sampling frame — frozen, authority on every rule |
| `docs/BIASES.md` | **24 biases**, direction and mitigation for each. Read before quoting any number. |
| `data/anchors.csv` | 235 people, six dated anchors each, every date with a source URL |
| `data/roster.csv` | who was drawn, from which list, with the membership citation |
| `data/audit*.csv` | blind second-pass audits and their pairings |
| `src/` | clocks, bootstrap, stopping rule, CPI conversion, schema validator |
| `analysis/archive/` | superseded interim reports, kept as evidence — see its README |
| `GROK-RUN-THE-STUDY.md` | the standing orders collection was run under |

## Reproducing the result

```bash
python3 -m src.schema data/anchors.csv
python3 -m src.clocks data/anchors.csv analysis/clocks.csv
python3 -m src.stats analysis/clocks.csv
python3 -m unittest discover -s tests -t .
```

The first must report `0 errors`; the last runs 207 tests. The bootstrap uses a
fixed seed, so the interval reproduces exactly.

## Two things a reader should know before citing this

**The stopping rule fired on the boundary.** The final CI half-width was exactly
1.00 against a test that fails only above 1.0. Across 300 bootstrap seeds the
rule passes in 272 (90.7%); the other 28 give [8.0, 11.0]. The seed was fixed in
advance, so the stop is legitimate under the pre-specified procedure — but it is
a boundary stop and the paper reports it as one.

**Missing education dates remove 23% of the eligible sample.** 28 of 121
people with a hit dated on primary revenue evidence have no sourced
education-end year. The missingness is structural: the clock is anchored to a
credential, and a credential is exactly what self-taught founders lack.

Both are discussed in the paper, along with what the study would not defend.

## How it was collected

Names entered only by enumerating a named third-party list in published order.
Country, era and sex were recorded but never used to select, in either
direction. Every wave was audited by a blind second pass that could not see the
first pass's answers; a wave voided above a 0.10 contradiction rate.

Collection was executed by language models following the written briefs in
`docs/`, with a human deciding methodology. Every batch log, audit pairing and
rejection is committed.

## License

Data, documentation and papers: [CC BY 4.0](LICENSE-DATA).
Code under `src/`, `scripts/` and `tests/`: [MIT](LICENSE-CODE).
