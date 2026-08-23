# Profile extraction brief

Build one structured profile row per person in `data/anchors.csv`. This feeds a
qualitative companion report to the study.

`docs/GROK-RESEARCH-BRIEF.md` governs anything you look up fresh. Read it.

## Two different jobs, and do not confuse them

1. **EXTRACTION.** Most rows already carry the facts in their `notes` column,
   put there by a researcher who cited a source at the time. 88% of rows mention
   a degree or school. Read the note and lift the fact out. This is not research
   and needs no new source.
2. **GAP-FILLING.** Where the note is silent, look it up, and cite a URL in
   `source` for what you found. Two attempts, then `unknown`.

Mark which one every row came from in the `basis` column: `notes` or `researched`
or `unknown`.

## Columns, exactly

    person_id,name,hit_entity,bucket,nationality,sex,highest_degree,field_of_study,institution,expertise,basis,source

- `highest_degree` — the highest credential **actually completed**. Use
  `PhD`, `MD`, `JD`, `Masters`, `Bachelors`, `Associate`, `HighSchool`, `None`,
  or `unknown`. A dropout is recorded at their last COMPLETED credential, which
  is the same convention the study's `a2` anchor uses — someone who left a PhD
  programme with a BS is `Bachelors`. Honorary degrees are NOT credentials.
- `field_of_study` — the subject of that credential, e.g. `Computer Science`,
  `Physics`, `Fine Arts`. `unknown` if the degree is known but the subject is not.
- `institution` — where it was awarded.
- `expertise` — a short noun phrase for what they are actually expert in, finer
  than the bucket. `distributed systems`, `gene therapy`, `container shipping`,
  `documentary film`. Derive from `hit_entity` and the notes. This is the one
  judgement column; keep it descriptive, never evaluative.
- `nationality` — copy `country_primary` from anchors unless the notes clearly
  say the person's nationality differs from where their career ran, in which
  case use nationality and say so in `source`.
- `sex` — copy `gender` from anchors. Do not re-derive it.

## Rules

- **Never infer a degree.** If someone is called "Dr." with no completed
  doctorate sourced, that is `unknown`, not `PhD`. Attending is not completing.
- `unknown` is a correct answer and is expected on a substantial minority.
- Do not edit `data/anchors.csv` or anything under `src/`.
- **Append each row as you finish it.** Not all at the end.
- Work in `person_id` order so progress is legible.

## Report

How many rows came from notes vs research vs unknown; the distribution of
`highest_degree`; and every person you could not resolve, by name.
