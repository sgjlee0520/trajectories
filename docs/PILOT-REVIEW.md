# Pilot Review — 10 stress-case rows

**Date:** 2026-08-11
**Data:** `data/roster.csv`, `data/anchors.csv` (validator: `10 rows checked, 0 errors`)
**Verdict up front:** **Revise the spec first.** Three specific defects, all fixable
in the spec text without re-researching anyone. Do not begin wave 1 until they are
fixed, because two of them silently move `a5_first_hit` by 5–11 years.

---

## 1. Did `a3_first_domain_job` have a defensible answer for the career-switcher?

**No. It required a judgment call, and the call is not mechanical yet.**

The career-switcher is **p01 Sara Blakely** (`consumer_retail_industrial`, Forbes
World's Billionaires). She spent roughly seven years at Danka selling fax machines
door to door, was promoted to national sales trainer, and then founded a shapewear
company. She has **no prior employment in apparel, hosiery, retail, or product
design of any kind.** The definition — "first full-time paid work in the field of
the eventual hit" — has no referent in her life history.

**The call made:** `a3_first_domain_job = 2000`, identical to `a4_first_venture`,
confidence `low`, with the reasoning written into the row's `notes`.

**The proposed rule, stated so it is mechanical for the next 400 people:**

> **R1.** If no employer-paid work in the hit's field precedes `a4_first_venture`,
> set `a3_first_domain_job = a4_first_venture` and confidence `low`. Founding
> counts as entering the domain. Only record `unknown` when domain employment
> plausibly existed but could not be sourced.

R1 is worth adopting, but adopt it knowing what it costs, because the pilot shows
the cost is real:

- **It makes `a3` non-independent.** Under R1, every founder-first career gets
  `a3 == a4`. In this pilot that is p01. In a wave of 25 software founders it will
  be a large minority of rows, and `a3` will silently stop being a separate
  measurement for exactly the people whose careers are most interesting.
- **It overloads `unknown`.** The schema has two states per anchor: a sourced year,
  or `unknown`/`none`. There is no third state for *"this event did not occur."*
  Blakely's true answer is "there was never a first domain job," which is a fact
  about her career, not a failure of research. Recording it as `unknown` would put
  it in the same bucket as **p10 Zhang Yin**, whose bookkeeping and paper-trading
  jobs certainly existed and simply have no published dates. Those two are not the
  same thing and should not be counted together.

**Recommendation:** adopt R1, and add a fourth confidence value `na` (or an
`a3_is_own_venture` boolean) so that "no such job existed" is distinguishable from
"not sourced." Without that, the `unknown` rate reported in §3 conflates two
different phenomena and cannot be used to judge sourcing quality.

`a3` is descriptive only — no clock in `src/clocks.py` consumes it — so this defect
does not corrupt any median. It is a data-quality problem, not a measurement one.
Fix it, but it is not the reason to hold wave 1.

---

## 2. Did any bucket's hit criterion fail to fire?

**Every criterion fired at least once. But two of them fired at demonstrably wrong
years, and that is worse than not firing.**

| Bucket | Criterion | Fired? | Notes |
|---|---|---|---|
| `consumer_retail_industrial` | `rev10` (p01) / `ipo` (p03) | yes | p03's date is late — see below |
| `hardware_deeptech` | `ipo` (p04) | yes | ~11 years late — see below |
| `science_research` | `prize` (p02) | yes | convention ambiguity — see below |
| `media_creators` | `aud1m` (p05) | yes | clean |
| `investors_finance` | `fund100` (p06) | yes | large judgment call — see below |
| `software_internet` | `acq50` (p07), `rev10` (p09) | yes | p07 is the cleanest row in the set |
| `trade_import_logistics` | `ipo` (p10) | yes | late, same defect as p03/p04 |
| `software_internet` (p08) | none | **no** | excluded — see §4 |

### Defect A — the fallback lags the true hit, and nothing records that it did

This is the most damaging finding in the pilot. **3 of 10 rows** (p03 Yanai,
p04 Moore, p10 Zhang Yin) hit the same failure:

> The person's venture is *known* to have passed $10M revenue years before the
> recorded hit, but the specific crossing year is not documented, so the `ipo`
> fallback fires at a much later date.

The worst case is **p04 Gordon Moore**. He co-founded Fairchild Semiconductor in
1957; Fairchild was a multi-million-dollar business by 1959 and a very large one by
1961. Its `rev10` crossing is therefore somewhere in 1960–61, but no citable source
pins the year, and Fairchild Camera's 1959 buyout of the founders was about $3M —
below the `acq50` threshold. So the row records **Intel's 1971 IPO**: a real,
well-sourced, legal date that is roughly **11 years later than his actual first
hit**. His `clock_education` is recorded as 17 years; the true value is closer to 6.

p03 Yanai (Uniqlo opened 1984, hit recorded at the 1994 Hiroshima listing) and p10
Zhang Yin (paper-trading business from 1985, hit recorded at the 2006 HKEX listing)
carry the same distortion at smaller magnitude.

The frame's wording is the root cause. It says the fallback applies "only if revenue
is **never publicly documented**." That is not the failure mode that actually occurs.
The real failure mode is **"revenue is documented, but only from a year well after
the crossing"** — which is what happens to every company that discloses financials
for the first time at IPO. That is most of them.

**This biases the headline median upward, and the bias is invisible.** `hit_basis =
fallback` marks these rows, so a fallback-vs-primary comparison will show *a*
difference — but it will be read as "companies that exit look different," when part
of it is simply this dating error. At 3 of 10 rows in the pilot, it is not a corner
case.

**What would have to change** — pick one before wave 1:

- **B1 (recommended).** Add a rule: if a criterion is known to have fired at an
  undatable earlier year, the row is `excluded = true` with reason
  `crossing_undatable`, rather than being dated by a later fallback. This keeps the
  median honest and makes the loss visible in the exclusion rate. It would have
  excluded p04, and probably p03 and p10.
- **B2.** Keep the fallback but add a `hit_date_is_upper_bound` boolean, and report
  a third median with those rows dropped.
- **B3.** Restrict `ipo`/`acq50` to ventures where no earlier venture of the same
  person is known to have passed $10M. This fixes Moore, not Yanai.

Doing nothing is not an option. As written, the frame produces confidently sourced
dates that are a decade wrong, which is precisely the failure the cite-or-flag
standard was built to prevent — it just arrives through the definition rather than
through a guessed year.

### Defect B — `prize` and `fund100` need tie-breaking conventions

- **p02 Katalin Karikó.** The frame lists Breakthrough alongside Nobel, and
  §4 says take the **earliest**. So her hit is the Breakthrough Prize, not the 2023
  Nobel. The Breakthrough Prize is officially the *2022* prize but was **announced
  9 September 2021**. Recorded as 2021. **The spec never says whether prize year or
  announcement year governs.** One year, every science row, systematically.
- **p06 Mary Meeker.** `fund100` = "first fund closed above $100M." Read as
  *the first fund she raised as a principal*, that is Bond Capital's $1.25B debut
  fund, April **2019** — at age 60, twenty-three years after she was already one of
  the most influential people in technology investing. Read as *the first $100M+
  fund she was a named partner on*, it is Kleiner Perkins' digital growth fund
  around **2010–11**. **That is an 8–9 year swing on a single word.** The spec must
  say which.
- **p09 Daniel Ek.** `rev10` is a **dollar** threshold, but Spotify Ltd's accounts
  are in **pounds** (£11.3M, 2009). Baidu's are in RMB, Fast Retailing's in yen.
  The spec specifies no conversion rule — spot rate in the revenue year, or PPP, or
  a fixed rate. At 30%+ non-US quota this affects a large fraction of every wave.

---

## 3. What fraction of anchors came back `unknown`?

**5 of 60 anchors = 8.3%.** Below the 10% line, so on its face the sourcing
standard holds.

**Do not take comfort from that number.** It is 8.3% only because judgment calls
were resolved rather than abandoned. The breakdown:

| Confidence | Count | Share |
|---|---|---|
| `high` | 34 | 56.7% |
| `medium` | 17 | 28.3% |
| `low` | 4 | 6.7% |
| `none` (unknown) | 5 | 8.3% |

The five genuine unknowns:

| Row | Anchor | Why |
|---|---|---|
| p08 Robin Li | `a5_first_hit` | crossing year bounded to 2003–2004, not pinnable (see §4) |
| p09 Daniel Ek | `a3_first_domain_job` | year he joined the SEO firm Jajja is in no source found |
| p09 Daniel Ek | `a6_scale_hit` | no sourced scale marker after two attempts |
| p10 Zhang Yin | `a2_education_end` | "attended a trade school for accounting" — no year, anywhere |
| p10 Zhang Yin | `a3_first_domain_job` | bookkeeper, then a Shenzhen paper trader — no years, anywhere |

Two observations that matter more than the headline rate:

1. **The unknowns concentrate.** Three of five fall on one non-US, pre-internet,
   thin-bucket career (p10) and two on another (p09). If the 30% non-US floor and
   the 5% `trade_import_logistics` quota are honoured, wave 1 will produce a
   materially higher unknown rate than this pilot did — the pilot is 50% non-US but
   only 10% `trade_import_logistics`. Expect 12–18%, not 8%.
2. **One of the five is a tooling failure, not a documentation failure.** See §4.

**Recommendation:** the sourcing standard itself is fine. What needs revising is the
expectation: budget for a higher unknown rate in thin buckets, and re-check the rate
after wave 1 rather than treating 8.3% as the baseline.

---

## 4. Did any real career fail to fit the schema at all?

**Yes — p08 Robin Li, and it failed in the most embarrassing way possible: he was
selected *because* his revenue is exceptionally well documented.**

Baidu filed an SEC F-1 in 2005 with audited revenue for 2002, 2003 and 2004. This
should have been the easiest `rev10` row in the pilot. Two things went wrong:

1. **The summary table skips the year that matters.** The F-1's summary line quotes
   2002 (RMB 10.5M ≈ $1.3M) and 2004 (RMB 110.9M = **US$13.4M**) but not 2003. So
   the $10M crossing is bounded to **2003 or 2004** and cannot be pinned from the
   summary alone.
2. **The full statement of operations was unreachable.** `sec.gov` returned HTTP 403
   to the fetch tool on every attempt, as did Baidu's IR host (timeouts) and a
   Britannica page and a CNBC page elsewhere in this pilot. Five attempts, no route.

So the row is `excluded = true`, contributing to no median, over one missing table
cell in a document that unambiguously contains the answer.

Two distinct schema failures are visible here:

- **The schema cannot represent a bounded date.** "2003 or 2004" is far more
  information than `unknown`, and it is enough to compute a median with a ±1 year
  uncertainty. The three-column anchor format forces it to be discarded entirely.
  Consider `<anchor>_date` accepting `2003-2004` and clocks taking the midpoint, or
  an explicit `_date_max` column.
- **The `ipo` fallback is blocked where it is most needed.** Baidu's revenue *is*
  publicly documented, so under the frame's literal wording the fallback is illegal
  — and the 2005 NASDAQ IPO would in any case be later than the true crossing. The
  row falls between the two rules and lands nowhere. This is Defect A viewed from
  the other side.

**A tooling prerequisite for wave 1:** a working route to SEC EDGAR. Primary
financial filings are the single best `rev10` source that exists, and right now the
research tooling cannot open them. Fixing this is probably worth more to data
quality than any wording change in this document.

---

## 5. Other things worth the spec author's attention

- **Cross-cut floors.** Pilot composition: women 4/10 = 40% (floor 20%, met);
  non-US 5/10 = 50% (floor 30%, met); **first hit before 1995 = 2/10 = 20%, below
  the 25% floor.** The pilot is not quota-bound, but the near-miss is a signal:
  pre-1995 hits are the hardest to source (see p04), so the era floor will be the
  binding constraint on every wave, and rebalancing toward it will import Defect A.
- **The stopping rule can be satisfied by noise.** `analysis.md` reports the
  revenue-strict CI half-width as **0.50 yr at n = 2**, already inside the 1.0-year
  threshold. Only the N=30 hard floor and the three-wave history requirement prevent
  a stop. The rule is safe as implemented, but the CI is meaningless at this n and
  the report prints it without a caveat next to the stopping-rule line.
- **`hit_basis` distribution is 2 primary / 4 fallback / 3 equivalent / 1 excluded.**
  Spec §6 forecasts `primary` at roughly half of all rows. The pilot came in at
  **20%**, and the shortfall is entirely Defect A. If wave 1 reproduces this, the
  stopping rule — which tracks the revenue-strict subset — will need a total N far
  above the 350–500 forecast to reach a revenue-strict n of 200.
- **Spec §8 requires a `conf = high`-only sensitivity run printed beside the
  all-rows medians. `src/report.py` does not implement one.** With 6.7% of anchors
  at `low` confidence and 28.3% at `medium`, this run is not decorative. (Flagged,
  not fixed — `src/` was out of scope for this task.)
- **The cleanest row is p07 Kevin Systrom**, and it is worth noticing why: US,
  English-language, post-2005, one venture, a headline-grabbing acquisition, and
  six anchors all at `high`. Wave rows that look like this will be cheap and
  accurate. Every quota in the frame exists to stop the sample from becoming
  entirely this person, and every finding above is a cost of that decision. The
  quotas are still right.

---

## Verdict

**Revise the spec first. Do not start wave 1.**

The pilot did its job: `a5_first_hit` broke in three of ten rows and `a3_first_domain_job`
broke in one, and all four breaks are cheap to fix now and expensive to fix at N=400.

Blocking changes, in priority order:

1. **Fix the fallback-lag defect** (§2, Defect A) — pick B1, B2, or B3. This one
   moves the headline median by years and is invisible without the fix.
2. **Pin the `prize` and `fund100` conventions and the currency-conversion rule**
   (§2, Defect B) — three sentences of spec text, each worth 1–9 years per row.
3. **Get a working route to SEC EDGAR** (§4) — a tooling task, not a spec task, but
   it gates the `primary` share and therefore the stopping rule.

Non-blocking, do them anyway:

4. Adopt rule R1 for `a3` and add a `na` state distinct from `unknown` (§1).
5. Allow a bounded date, or accept that bounded-but-unpinned rows are excluded (§4).
6. Implement the §8 `conf = high` sensitivity run in `src/report.py` (§5).

Nothing here requires re-researching the ten people. All six anchors are stored per
person, so every change above can be applied in post — which is exactly the property
§10.3 of the design was built to have, and it held.
