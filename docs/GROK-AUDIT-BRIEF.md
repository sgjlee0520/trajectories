# Audit brief for Grok — blind second pass

You are re-researching people someone else already researched. You have NOT
been shown their answers and you must not go looking for them. The entire value
of this pass is that it is independent: if you reproduce their date you confirm
it, and if you contradict it you have caught an error worth more than a new row.

`GROK-RESEARCH-BRIEF.md` sits next to this file. **Every rule in it applies**,
with the four overrides below. Read it first.

## Overrides for an audit pass

1. **You are in a clean directory on purpose.** There is no `data/anchors.csv`
   and no `src/schema` here. Ignore sections 0 and 7-item-2 of the research
   brief, and item 7 of its section 8. Everything else stands.
2. **You need ONE anchor per person: `a5_first_hit`.** Not the other five.
   Section 3 of the research brief tells you how to date it.
3. **Do not search for this project, its repository, its CSVs, or any prior
   write-up of these people's dates.** Go to primary sources. If you stumble
   onto a page that is plainly a previous pass's notes, close it and say so in
   your report.
4. **Output columns are `person_id,second_pass,evidence`** — not the anchors
   schema. One row per person, appended as you finish each one.

## `second_pass` values

Exactly as section 4 of the research brief: a sourced year (`1987`), a sourced
bounded range (`1984-1990`, ≤10 years, both ends sourced), or the literal
`unknown`. Nothing else.

`unknown` is a real answer and is scored as a miss, not as a contradiction —
it does not count against the wave. **A confident wrong year does.** So when
the evidence is thin, `unknown` is the cheap correct move and guessing is the
expensive one. Do not reach for a date to look thorough.

## `evidence`

One quoted-CSV field per person carrying:

- the exact quoted sentence from each source, with its URL
- the pasted output of `python3 -m src.cpi <year>` for the year you used
- for non-USD, the spot rate for that revenue year and the arithmetic
- for a bounded range, the below-bar figure at the low end and the at-or-above
  figure at the high end
- what you looked for and could not find

A row whose evidence has no pasted `src.cpi` output is rejected, same as in the
research brief.

## Your report

Per person: the year or range, the criterion, the figure against that year's
computed bar, and your confidence. Then: which ones you could not date, every
place you were uncertain, and any margin under 20% above the bar.

Be blunt. This pass exists to find mistakes, including the possibility that
there are none.
