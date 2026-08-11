# Sampling Frame — FROZEN

Frozen 2026-07-31; revised 2026-08-11 after the 10-person pilot. Do not edit
after wave 1 begins. Changing the frame mid-collection invalidates the stopping
rule, because the sample composition would no longer be stable across waves.

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

Revised 2026-08-11 after the 10-person pilot. See `docs/PILOT-REVIEW.md`.

### The threshold is in constant 2026 dollars

`rev10` means **$10M in constant 2026 US dollars**, not $10M nominal. A nominal
threshold would demand that a 1960 founder build a business roughly eleven times
larger in real terms than a 2020 founder to trigger the same "first hit", which
inflates every pre-1995 apprenticeship — and the frame requires at least 25% of
those.

Look up the nominal threshold for a revenue year with:

    python3 -m src.cpi 1960

For non-USD accounts, convert at the **spot rate for the revenue year**, then
compare against that year's nominal threshold.

### Commercial buckets

`software_internet`, `hardware_deeptech`, `consumer_retail_industrial`,
`healthcare_biotech`, `trade_import_logistics`:

1. `rev10` — first year the person's own venture reached the constant-dollar
   $10M threshold. Basis `primary`.
2. `ipo` or `acq50` (acquisition above $50M constant 2026 dollars), whichever is
   earlier. Basis `fallback`. **Permitted only when no earlier crossing is known
   to have occurred.** If sources establish that the venture passed the threshold
   in an earlier year that cannot be pinned exactly, record a bounded `rev10`
   date instead — see below. If it cannot even be bounded, the row is
   `excluded = true` with reason `crossing_undatable`. Dating such a row by a
   later IPO is forbidden: it produces a confidently sourced answer that is years
   wrong.

### Non-commercial buckets

- `science_research` → `prize` (Nobel, Turing, Fields, or Breakthrough). Basis
  `equivalent`. **Record the announcement year**, not the prize's official
  designated year, because the announcement is when recognition actually landed.
  Karikó's Breakthrough Prize is officially the 2022 prize but was announced
  9 September 2021, so the anchor is 2021.
- `media_creators` → `aud1m` (1M+ audience for their own work). Basis
  `equivalent`.
- `investors_finance` → **two criteria, chosen by career type**:
  - Fund managers: `fund100` — first fund closed above $100M constant 2026
    dollars where the person was a named general partner. Basis `equivalent`.
  - Analysts, economists, and other non-fund finance careers: `rank1` — the
    first year the person topped a recognized industry ranking, such as the
    Institutional Investor All-America Research Team. Basis `equivalent`.

  `fund100` alone mis-dates analysts badly: Mary Meeker was among the most
  influential people in technology investing roughly 23 years before Bond
  Capital's 2019 debut fund. Where no recognized ranking exists for a person,
  the anchor is `unknown` and the row is excluded — that is honest, and better
  than dating a career by an event that came decades late.

### Bounded dates

When sources establish that an event happened within a range but not which year,
record the anchor as `YYYY-YYYY` — low year first, at most 10 years wide, with a
source for the bound. Clocks use the midpoint; the report prints a sensitivity
run with bounded rows excluded so the uncertainty stays visible.

A bounded date is a real measurement, not a guess. `1960-1961` says two sources
bracket the event. It is not licence to widen a range until it contains a year
you like.
