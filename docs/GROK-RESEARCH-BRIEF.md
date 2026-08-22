# Research brief for Grok

This is the standing brief for research work on this study. It is deliberately
stricter and more explicit than `docs/RESEARCH-RULES.md`, which is written for
agents that infer intent well. **Follow it literally.**

You are doing the research. You are NOT deciding methodology. If a rule here
seems wrong for a case in front of you, do not improvise around it — record the
case as `unknown` and say in your report why the rule did not fit. A methodology
decision made mid-batch is worse than a missing row.

---

## 0. Before you write a single row

Run this and paste the output into your report:

    python3 -m src.schema data/anchors.csv

If it does not say `0 errors`, stop and report that instead of researching.

## 1. What you are finding

For each assigned person, six dated anchors:

| field | meaning |
|---|---|
| `a1_birth` | birth year |
| `a2_education_end` | year their last COMPLETED credential was awarded. For a dropout this is the previous completed credential, NOT the year they left |
| `a3_first_domain_job` | first paid work in the field the hit eventually came from |
| `a4_first_venture` | first thing they founded or independently authored |
| `a5_first_hit` | **the one that matters** — see §3 |
| `a6_scale_hit` | a much later, much larger milestone (IPO, billion users, Nobel) |

Each has three columns: `_date`, `_src` (a real URL), `_conf` (`high`/`medium`/`low`/`none`).

## 2. THE THRESHOLD IS INFLATION-ADJUSTED. THIS IS THE #1 ERROR.

The hit is **$10 million in CONSTANT 2026 DOLLARS**, never $10M nominal.

For every revenue year you consider, you MUST run:

    python3 -m src.cpi <year>

and **paste that command's actual output into your notes for that row.** Not a
number you remembered — the command's output. A row whose notes do not contain a
pasted `src.cpi` output for the year used will be rejected.

Worked example. The 1960 bar is **$919,417**. A 1960 company with $1.2M revenue
HAS crossed. Applying $10M nominally to that company would push its date a
decade later and corrupt the study's central number. This exact error made one
row eleven years wrong in an early pilot.

Convert non-USD at the spot rate **for that revenue year** and write the rate
into the notes, e.g. `¥1.0bn ÷ 219.14 (1979 avg) = US$4.56M`.

## 3. How to date `a5_first_hit`

In priority order:

1. **`rev10`** — first calendar year annual revenue crossed the constant-dollar bar. Basis `primary`. Always prefer this.
2. **`ipo` / `acq50`** — ONLY where revenue was never published. Basis `fallback`. **BARRED** if revenue is documented from any year after the crossing, because then you know the IPO date is later than the truth.
3. **Bucket equivalents** — `prize` (announcement year), `aud1m` (1M+ audience), `fund100` ($100M+ constant fund), `rank1` (first year atop a published third-party ranking). Basis `equivalent`.

An appointment is not a ranking. A single-winner award is not a ranking. An
informal magazine poll is not a ranking.

**Serial founders:** the hit is the FIRST company of theirs to cross, not the
famous one. Check for earlier ventures before you settle.

**Inherited going concerns:** if the person took over a business someone else
founded, you may NOT use that business's founding year as a lower bound.

## 4. Three allowed answers. Nothing else.

For every anchor:

- **A single sourced year** — `1987`
- **A sourced bounded range** — `1984-1990`, maximum 10 years apart, with a source for BOTH ends
- **The literal word `unknown`** — with `_src` empty and `_conf=none`

A bounded range needs a figure **below** the bar in the earlier year and a
figure **at or above** it in the later year. A company's founding year is a
valid lower end (it cannot earn before it exists) — try that before giving up.

**If your two sourced ends are more than 10 years apart, the answer is
`unknown`** and the row is `excluded=true`, `exclusion_reason=crossing_undatable`.
Do NOT report the later year. Reporting the first year a company happened to
disclose revenue dates the career too late and is the worst error available.

## 5. Behaviours that will get your batch rejected

Read this list twice. Each one has actually happened on this project.

- Writing a year you did not find in a source. **Never infer, estimate, interpolate, or reason your way to a date.**
- Citing a URL that does not contain the fact. Every URL you give must have the quoted sentence in it.
- Citing a list's homepage as proof of membership. The page must NAME the person or their company.
- Summarising a source instead of quoting it. Notes need the exact sentence.
- Comparing revenue against $10M instead of that year's computed bar.
- Stretching a bound to exactly 10 years to avoid an exclusion. If it lands at exactly 10, say so explicitly and justify it.
- Reporting a count you did not verify. If you researched 4 of 5, say 4 of 5.
- Writing all rows at the end instead of incrementally.
- Inventing a person or a company when you cannot find one. If the roster names someone who appears not to exist, write `SUSPECTED FABRICATED ROSTER ENTRY` and move on.

## 6. `unknown` is a good answer

25 rows in this study are excluded as undatable and every one has held up under
independent re-checking by other models. Private companies genuinely do not
publish early revenue. **An honest `unknown` is a success. A confident wrong
year is a failure that may never be caught.**

Do not stretch weak evidence to fill a cell.

## 7. Output mechanics

- Write to the **exact output file named in your assignment**, never directly to `data/anchors.csv` unless told to.
- Use the same column order as `data/anchors.csv`. Copy its header row verbatim.
- **Append each person as you finish them.** Agents on this project have been killed mid-task; only the incremental writers kept their work.
- Do not edit anything under `src/`. Do not run `git commit`.

## 8. Self-check before you report

Go through every row you wrote and confirm:

1. Every `_date` is a year, a `YYYY-YYYY` range, or `unknown` — nothing else.
2. Every non-`unknown` date has a real URL in `_src`.
3. Every `unknown` has empty `_src` and `_conf=none`.
4. The notes contain a pasted `python3 -m src.cpi <year>` output for the year used.
5. The notes contain the exact quoted sentence for each figure.
6. No bounded range exceeds 10 years.
7. `python3 -m src.schema data/anchors.csv` still reports `0 errors`.

Then run the schema check one final time and paste the output.

## 9. Your report

Per person: the six anchors, `hit_criterion`, `hit_basis`, the revenue figure
against that year's computed bar, and the list-membership verdict.

Then: who you excluded and why, how many have a pre-1995 hit, and **every place
you were uncertain**. Flag any margin under 20% above the bar explicitly.

Be blunt about what you could not find. Reporting a gap honestly is worth more
to this study than filling it.
