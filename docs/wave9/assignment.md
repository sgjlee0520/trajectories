# Wave 9 roster assignment

25 people, ids **p211 through p235**, assigned in the order below. The bucket
counts come from `python3 -m src.allocate` and are fixed — do not move a slot
between buckets.

Each bucket names the list to walk and where to start. Every list is
self-resuming: walk it in order and skip anyone in `already-used.md`, which is
rejection 1. That is how you land past where earlier waves stopped without
needing a stored pointer.

| ids | bucket | n | list to walk | order |
|---|---|---|---|---|
| p211-p216 | software_internet | 6 | Y Combinator Top Companies | published rank order, from the top |
| p217-p220 | consumer_retail_industrial | 4 | Forbes World's Billionaires (self-made) | rank order, from rank 1, `selfMade: true` only |
| p221-p223 | hardware_deeptech | 3 | Computer History Museum Fellow Awards | year order, most recent year first |
| p224-p226 | healthcare_biotech | 3 | Forbes World's Billionaires (self-made) | rank order, from rank 1, `selfMade: true` only |
| p227 | science_research | 1 | Nobel Prizes (Economics) | year order, most recent first |
| p228 | science_research | 1 | Nobel Prizes (Physics) | year order, most recent first |
| p229 | science_research | 1 | Breakthrough Prize | year order, most recent first |
| p230 | investors_finance | 1 | Midas List | rank order, from rank 1 |
| p231 | investors_finance | 1 | Midas List Europe | rank order, from rank 1 |
| p232 | media_creators | 1 | Pulitzer Prize | year order, most recent first |
| p233 | media_creators | 1 | Grammy Awards | year order, most recent first |
| p234-p235 | trade_import_logistics | 2 | Forbes World's Billionaires (self-made) | rank order, from rank 1, `selfMade: true` only |

## Why these lists

Each bucket draws from the list it has drawn from most so far, which continues
the existing sampling design rather than introducing a new one mid-study. The
three multi-prize buckets are the exception: `science_research` takes its three
slots from its three least-used prize lists, and `media_creators` takes Pulitzer
and Grammy, so that no one list inside a bucket runs away with it. Both are
choices about list mix, not about who qualifies.

For a Forbes bucket, walk the full ranking and take the entries whose industry
puts them in the bucket you are filling. A Forbes entry in the wrong industry is
rejection 3, not a reason to stop walking.

## Composition, for the record only

At 210 rows the study is 24% pre-1995, 59% non-US, 27% women. These are recorded
covariates. **Do not use them.** Do not pick, skip, or reorder to move any of
these numbers in either direction — if a wave moves them, that is a finding for
the analysis, not a defect for you to correct (`frame.md`, Recorded covariates).

## Output

`docs/wave9/roster-w9.csv`, header already present, columns exactly as
`data/roster.csv`. Append each row as you finish it.
