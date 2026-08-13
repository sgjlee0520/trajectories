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

**What "known" means here.** A qualitative claim in a source — that the venture
was already large, profitable, or industry-leading by a stated year — is enough
to establish that an earlier crossing occurred, even with no dollar figure
attached. Only the *year* needs pinning or bounding, not the crossing itself.
So a company that first disclosed revenue at IPO has a known earlier crossing
whenever any source describes it as substantial beforehand, and the fallback is
barred. Use the fallback only when no source suggests the venture reached
meaningful scale before the IPO or acquisition — which, for a company large
enough to list, is rare. Expect exclusion or a bounded date to be the normal
outcome, and the fallback to be the exception.

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

- `trade_import_logistics` → **`rev10` first, `rank1` where revenue is
  unavailable.** Basis `equivalent` for `rank1`.

  Private importers, exporters, and freight operators almost never publish
  revenue at any point in their history, and they rarely IPO. The second pilot
  excluded this bucket at **100%** on that alone — the whole bucket, gone, over
  a criterion it could not physically satisfy.

  What they do leave is a third-party, dated, public record of **volume**:
  customs and port-authority throughput tables, Journal of Commerce top-100
  importer and exporter rankings, and trade-press "largest X shipper of Y"
  designations. `rank1` fires on the first year the person's firm tops such a
  ranking. Zhang Yin's America Chung Nam, for instance, has been the largest
  US exporter of recovered paper to China by volume since about 2001 — a
  datable event, from a source that exists, for a company that never published
  a revenue figure before its 2006 listing.

  The ranking must be published by a third party and name a first year. A
  company's own claim to be "the largest" is not a ranking. Where no such
  ranking exists, the anchor is `unknown` and the row is excluded.

### Bounded dates

When sources establish that an event happened within a range but not which year,
record the anchor as `YYYY-YYYY` — low year first, at most 10 years wide (arithmetic
difference, so 1960-1970 is the widest permitted range), with a
source for the bound. Clocks use the midpoint; the report prints a sensitivity
run with bounded rows excluded so the uncertainty stays visible.

A bounded date is a real measurement, not a guess. `1960-1961` says the sources
place the event in those two years — whether that is two sources bracketing it
from either side, or one source stating the range directly. It is not licence
to widen a range until it contains a year you like.

**The founding year is a valid lower bound.** A company cannot earn revenue
before it exists, so the sourced founding (or first-production) year of the hit
entity brackets a crossing from below without inferring anything. Where the
earliest published figure is already above threshold, bound the crossing from
the entity's founding to that figure's year rather than excluding the row.
This only helps where the entity was young at the crossing: if the bracket
exceeds the ten-year span limit, or the hit entity is a going concern the
person inherited, the row is still `crossing_undatable`.
