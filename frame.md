# Sampling Frame — FROZEN

Frozen 2026-07-31. Do not edit after wave 1 begins. Changing the frame
mid-collection invalidates the stopping rule, because the sample composition
would no longer be stable across waves.

## Field quotas

| Bucket key | Label | Share |
|---|---|---|
| `software_internet` | Software & internet | 25% |
| `hardware_deeptech` | Hardware & deep tech | 15% |
| `consumer_retail_industrial` | Consumer, retail & industrial | 13% |
| `science_research` | Science & research | 12% |
| `investors_finance` | Investors & finance | 10% |
| `media_creators` | Media & creators | 10% |
| `healthcare_biotech` | Healthcare & biotech | 10% |
| `trade_import_logistics` | Trade, import & logistics | 5% |

Total: 100%.

## Enforced cross-cuts

Floors, checked against the cumulative sample after every wave. A wave that
would push any floor below its threshold is rebalanced before research begins.

- Non-US primary career: >= 30%
- First hit before 1995: >= 25%
- Women: >= 20%

## Named source lists

Every roster entry cites the list it came from. No name enters by free recall.

- Forbes 400 (self-made score 6-10)
- Forbes World's Billionaires (self-made)
- Midas List; Midas List Europe
- Fortune 40 Under 40
- Nobel Prizes (Physics, Chemistry, Medicine, Economics)
- Turing Award
- Fields Medal
- Breakthrough Prize
- Time 100
- Y Combinator Top Companies
- Hurun Rich List (China, India)
- Nikkei / Toyo Keizai rankings (Japan)
- Maeil Business / Chosun Ilbo rankings (Korea)
- Sunday Times Rich List (UK)
- Pulitzer Prize, Academy Awards, Grammy Awards
- Endeavor Entrepreneur network (emerging markets)

## Hit criteria

Commercial buckets (`software_internet`, `hardware_deeptech`,
`consumer_retail_industrial`, `healthcare_biotech`, `trade_import_logistics`):

1. `rev10` — first year the person's own venture reached $10M annual revenue. Basis `primary`.
2. Only if revenue is never publicly documented: `ipo` or `acq50` (acquisition above $50M), whichever is earlier. Basis `fallback`.

Non-commercial buckets:

- `science_research` -> `prize` (Nobel, Turing, Fields, Breakthrough). Basis `equivalent`.
- `media_creators` -> `aud1m` (1M+ audience for their own work). Basis `equivalent`.
- `investors_finance` -> `fund100` (first fund closed above $100M). Basis `equivalent`.
