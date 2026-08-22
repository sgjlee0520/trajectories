# Evidence pack for three stuck items

Research analyst output, wave 7/8. **No file in `data/`, `docs/` or `src/` was
edited.** Every dollar bar below is the CONSTANT-2026-DOLLAR bar from
`python -m src.cpi <year>`, run fresh; nominal figures are quoted next to the
bar they were tested against.

Bars used (all from `PYTHONUTF8=1 python -m src.cpi <year>`):

| year | rev10 nominal | acq50 nominal |
|---|---|---|
| 1992 | $4,357,914 | $21,789,571 |
| 1995 | $4,733,757 | $23,668,786 |
| 1998 | $5,063,008 | $25,315,040 |
| 1999 | $5,174,829 | $25,874,145 |
| 2000 | $5,348,773 | $26,743,865 |
| 2009 | $6,663,819 | $33,319,097 |
| 2015 | $7,362,080 | $36,810,398 |
| 2016 | $7,454,953 | $37,274,766 |
| 2017 | $7,613,770 | $38,068,851 |
| 2018 | $7,799,735 | $38,998,674 |
| 2019 | $7,941,064 | $39,705,321 |
| 2020 | $8,039,032 | $40,195,159 |
| 2021 | $8,416,707 | $42,083,537 |
| 2022 | $9,090,274 | $45,451,369 |
| 2023 | $9,464,470 | $47,322,352 |
| 2024 | $9,743,619 | $48,718,096 |
| 2025 | $10,000,000 | $50,000,000 |

---

# 1. The Palm pair — `BIASES.md` 23 (p70 Dubinsky / p94 Hawkins)

## 1.1 Collision check reproduced

Independently recomputed over all 160 rows of `data/anchors.csv`, grouping on
`hit_entity` and on `(hit_entity, a5_first_hit_date)`:

- 160 rows; 26 excluded; 134 included.
- Eight `hit_entity` values are shared by more than one row. Seven are prize
  names in `science_research`; the eighth is `Palm Computing`.
- **`Palm Computing` is the only shared entity where the two rows also share
  the hit YEAR** — p70 and p94, both `1995`. Every prize pair/triple is in a
  different year (Turing 2009/2019; Fields 2014/2018/2022; Chemistry
  1987/2020/2022/2025; Physics 2018/2022/2025; Medicine 1986/2015/2025;
  Breakthrough Maths 2023/2025). The seven blank `hit_entity` values are all
  `excluded=true` rows.

So the brief's claim holds: **one collision in 160 rows.**

Both Palm rows currently produce `era=post1995` (`ERA_SPLIT = 1995`, and
`era_of` returns `pre1995` only for `hit_year < 1995`, so a 1995 hit is
post1995), `bounded=false`, `conf_min=high`, `clock_venture=3.0` for both,
`clock_education` 14.0 (p70) vs 16.0 (p94), `age_at_first_hit` 40 vs 38.
As `BIASES.md` 23 says, the two clocks differ only by the education/birth dates.

## 1.2 What actually happened at Palm in 1995

**Primary document.** The U.S. Robotics Business Wire press release, reprinted
verbatim by Harry McCracken at Technologizer, 28 April 2010,
<https://technologizer.com/2010/04/28/us-robotics-buys-palm/index.html>
(HTTP 403 to WebFetch; retrieved with `curl -A "Mozilla/5.0"`, 51,183 bytes):

> "SKOKIE, Ill.–(BUSINESS WIRE)–Sept. 5, 1995–U.S. Robotics Corporation
> (NASDAQ:USRX) today announced the acquisition of Palm Computing, Inc. (Palm).
> As a result of the transaction, **which occurred on September 1, 1995**, Palm
> became a wholly-owned subsidiary of U.S. Robotics. **Palm's outstanding
> capital shares were converted into U.S. Robotics shares worth approximately
> $44 million.**"

> "The transaction will be accounted for as a pooling-of-interests; U.S.
> Robotics will restate prior period earnings to reflect the transaction when
> it reports its results for the fourth quarter and year ending October 1,
> 1995. **The effect of the restatement will not be material.**"

> "Headquartered in Los Altos, Calif., Palm develops operating system and
> applications software for hand-held computers and communication devices."

> "The company's 1994 sales were $499.0 million; sales for the first nine
> months of fiscal 1995 were $596.0 million." — *this is U.S. Robotics' own
> revenue, not Palm's.*

**Corroboration, independent of Technologizer.** The International Directory of
Company Histories entry for Palm, Inc.,
<https://www.fundinguniverse.com/company-histories/palm-inc-history/>, mirrored
at <https://www.company-histories.com/Palm-Inc-Company-History.html>:

> "Giant modem manufacturer U.S. Robotics, based in Skokie, Illinois, acquired
> Palm in September 1995 for $44 million."

**Against the bar.** $44,000,000 vs the 1995 `acq50` bar of **$23,668,786** =
**185.9% of bar, +85.9% margin**. Clears decisively. Date, price and criterion
are sound for both rows.

**Source-integrity note.** p70's `a5_first_hit_src` is
`https://www.penbasedcomputing.net/timeline/us-robotics-acquires-palm-computing-inc/`.
That URL is **dead**: HTTP 404 via WebFetch, HTTP 403 via curl, and the Wayback
availability API returns `{"archived_snapshots": {}}` — no snapshot exists.
p94's Technologizer URL is live and carries the full press release. Whatever is
decided about the pair, p70's hit source cannot currently be verified by anyone,
and the Technologizer URL substitutes for it exactly.

## 1.3 Was the `acq50` fallback permitted at all? (frame.md's earlier-crossing test)

`frame.md` bars the fallback where an earlier crossing is *known*, and sets a
low bar for "known":

> "**Permitted only when no earlier crossing is known to have occurred.**"

> "**What 'known' means here.** A qualitative claim in a source — that the
> venture was already large, profitable, or industry-leading by a stated year —
> is enough to establish that an earlier crossing occurred, even with no dollar
> figure attached."

Searched for any Palm revenue figure or scale claim for 1992-1995. **Nothing
found in either direction, and every qualitative statement runs the wrong way
for an earlier crossing:**

- fundinguniverse / company-histories (IDCH): no revenue, profit or scale
  figure for Palm before the acquisition at all. On funding, only "Three
  California venture capital firms also backed the company." The earliest
  financial metric in the whole entry is post-3Com ("sales exceeding $570
  million by the 1998/99 fiscal year").
- The Zoomer (Tandy/Casio, Oct 1993) is described as Palm's first product and a
  commercial failure; the standing account is that Palm was **capital-
  constrained and running out of venture funding** in 1994-95, seeking roughly
  $5M to finish the Pilot (the account already cited in p94's `notes`).
- The press release's own "The effect of the restatement will not be material"
  is a weak upper bound only: under pooling-of-interests U.S. Robotics restated
  prior periods to include Palm and called the effect immaterial against $499.0M
  of 1994 sales. At a conventional 5% materiality that caps Palm below ~$25M,
  **which does not discriminate against the $4,733,757 rev10 bar**. Evidence of
  smallness, not decisive evidence of being under the bar.

**Verdict on the fallback: permitted.** No source describes Palm as large,
profitable or industry-leading before September 1995; the sources that speak to
scale describe the opposite. This is one of the rare cases `frame.md` says to
expect ("Use the fallback only when no source suggests the venture reached
meaningful scale before the IPO or acquisition — which, for a company large
enough to list, is rare"), and Palm was not large enough to list.

## 1.4 Did either person have an EARLIER own venture that crossed the bar?

### Jeff Hawkins — no.

Wikipedia, <https://en.wikipedia.org/wiki/Jeff_Hawkins>: "Hawkins joined GRiD
Systems in 1982, where he developed rapid application development (RAD) software
called GRiDtask"; he was "vice president of research from 1988 to 1992";
"Hawkins founded Palm Inc., in January 1992." Intel and GRiD were **employers**;
GRiDPad was a GRiD product, not Hawkins's venture. Palm (Jan 1992) is his first
own venture, matching `a4_first_venture_date = 1992`, confidence `high`.
**Nothing earlier.**

### Donna Dubinsky — Claris does NOT count, and neither, arguably, does Palm.

Computer History Museum, <https://computerhistory.org/profile/donna-dubinsky/>:

> "Donna Dubinsky joined Apple Computer in 1981, spending ten years in a variety
> of sales, sales support and logistics functions **both at Apple and at Claris,
> Apple's software subsidiary**."

Wikipedia, <https://en.wikipedia.org/wiki/Donna_Dubinsky>: in 1986 "Bill
Campbell recruited her to a senior position in Claris, a software subsidiary of
Apple," with responsibility "for international sales and marketing." She was an
**executive hire into a wholly-owned Apple subsidiary she did not found**.

`frame.md`'s commercial criterion is explicit that the entity must be the
person's own:

> "1. `rev10` — **first year the person's own venture** reached the
> constant-dollar $10M threshold. Basis `primary`."

Claris fails that on two counts — she did not found it, and it was not an
independent venture but Apple's subsidiary. **Claris is out, as the brief
expected.**

**But the same test bites Palm, and this is the substantive finding of section
1.** Both sources say plainly that Dubinsky did not found Palm either:

- CHM: "she **joined Jeff Hawkins in 1992, shortly after he founded Palm
  Computing**. As president and CEO of Palm, Dubinsky helped create a major new
  industry segment based on the PalmPilot."
- Wikipedia: "Dubinsky met Jeff Hawkins through the introductions of Bill
  Campbell and Bruce Dunlevie. **Hawkins was looking for a CEO to manage
  Palm.**"

p70's own `notes` already flag this: "a4: JUDGMENT CALL — joined Jeff Hawkins
shortly after he founded Palm in 1992 as president/CEO (CHM); treated as first
own-venture leadership year (she was not a co-incorporator of Palm at t=0…)".

The first company Dubinsky demonstrably **founded** is Handspring:

- CHM: "In 1998, Hawkins and Dubinsky left Palm to **co-found Handspring**."
- Wikipedia: "Dubinsky, Hawkins, and Palm marketing manager Ed Colligan…left in
  June 1998 to found Handspring."

### Handspring's crossing is PINNED, from the SEC, to calendar 1999

Handspring, Inc., EDGAR CIK 0001091822.

Form 10-K405 for fiscal year ended 1 July 2000, filed 29 Sept 2000,
<https://www.sec.gov/Archives/edgar/data/1091822/000089161800004742/f65858e10-k405.txt>,
Item 6 Selected Financial Data (in thousands):

| | year ended July 1, 2000 | period from July 29, 1998 (date of inception) to June 30, 1999 |
|---|---|---|
| Revenue | **$101,937** | **$ —** |

and in MD&A: "We first recognized revenue in the second quarter of fiscal 2000";
the company was not "generating revenue until the quarter ended January 1, 2000."

Form S-1/A filed 20 June 2000,
<https://www.sec.gov/Archives/edgar/data/1091822/000089161800003437/0000891618-00-003437.txt>,
"QUARTERLY RESULTS OF OPERATIONS", revenue by quarter (in thousands):

| qtr ended | Sep 30 1998 | Dec 31 1998 | Mar 31 1999 | Jun 30 1999 | Oct 2 1999 | **Jan 1 2000** | Apr 1 2000 |
|---|---|---|---|---|---|---|---|
| Revenue | $— | $— | $— | $— | $— | **$15,790** | $34,321 |

The quarter ended **1 January 2000** runs 3 Oct 1999 – 1 Jan 2000, i.e. it is
calendar Q4 1999 to within one day. So Handspring's **calendar-1999 revenue is
~$15.79M against the 1999 rev10 bar of $5,174,829 = 305% of bar, +205%
margin.** Crossed in its first revenue quarter, unambiguously, from an audited
SEC filing.

On a fiscal-year reading it is FY2000, $101.9M vs the 2000 bar of $5,348,773 =
1,906% of bar. Either reading crosses; the calendar reading gives the earlier
year, and `frame.md`'s "first year … reached the threshold" favours the earlier
one.

Inception-date discrepancy worth recording if this option is taken:
CHM/Wikipedia say June 1998; the SEC filings say **"July 29, 1998 (date of
inception)"**. Either supports a4 = 1998.

## 1.5 Does `frame.md` as written forbid two rows sharing a hit event?

**No. There is no such rule anywhere in `frame.md`.** Grepped the full text for
`per person`, `one row`, `independent`, `duplicate`, `shared`, `same event`,
`co-found` — **zero matches**. The entry rule is stated as a per-person test
with no uniqueness clause:

> "**The sole standard for entry is the money criterion** in the section below:
> a person enters if they appear on a named source list and their hit can be
> dated. Nothing about who they are steers whether they are drawn."

> "Every roster entry cites the list it came from. No name enters by free
> recall."

Both Dubinsky and Hawkins have confirmed Computer History Museum Fellow profiles
(the list is in `frame.md`'s named source lists), and both hits are dated.
**Under the frame exactly as written, both rows are admissible and neither can
be excluded without adding a rule the frame does not contain** — which is
precisely what `BIASES.md` 23 says: "Both are legitimately on the Computer
History Museum Fellows list, so excluding either is a selection rule the frame
does not currently contain."

`BIASES.md` 23 also states the intended fix as prospective, not retrospective:
"Going forward the frame should require one row per hit **event** (entity plus
year), not merely per person."

`frame.md` is also FROZEN: "Frozen 2026-07-31; revised 2026-08-11 after the
10-person pilot. **Do not edit after wave 1 begins.** Changing the frame
mid-collection invalidates the stopping rule…". So any option that works by
*adding* a rule to `frame.md` collides with the freeze; an option that works by
*applying* a rule `frame.md` already contains does not.

## 1.6 Options and consequences

All figures recomputed over `data/anchors.csv` with `src.clocks` +
`src.stats.bootstrap_median_ci` (seed 0, 10,000 iters), included rows only.
`n` for `clock_education` is 103, not 134, because that clock needs a known `a2`.

| option | education n / median / CI half-width | venture n / med / half | age n / med / half |
|---|---|---|---|
| **A. keep both (status quo)** | 103 / **14.00** / **2.500** | 114 / 5.00 / 1.250 | 121 / 38.00 / 2.500 |
| **B. drop p70 Dubinsky** | 102 / 14.00 / **3.000** | 113 / 5.00 / 1.250 | 120 / 37.50 / 2.750 |
| **C. drop p94 Hawkins** | 102 / 14.00 / **2.750** | 113 / 5.00 / 1.250 | 120 / 37.50 / 2.750 |
| **D. re-date p70 → Handspring 1999** | 103 / 14.00 / **3.000** | 114 / 5.00 / 1.250 | 121 / 38.00 / 2.500 |
| **G. blanket "no shared `hit_entity`"** | 91 / **13.00** / 2.250 | 109 / 4.50 / 1.000 | 109 / 37.00 / 2.250 |

**The median does not move under A–D. Only the interval moves, and it moves in
the direction `BIASES.md` 23 predicts:** removing the duplicated event widens
the CI half-width from 2.500 to 2.750–3.000. Roughly 10-20% of the current
half-width on the headline clock is attributable to this one duplicated event —
which is the whole point of the bias entry.

### Option A — keep both

- **Rule needed:** none. Strictly correct under `frame.md` as frozen.
- **Cost:** the stopping rule keeps keying off a half-width ~0.25-0.5 years too
  narrow. `BIASES.md` 23: "the study could satisfy its own stopping criterion on
  precision it has not earned. Of all the failure modes catalogued here, this is
  the one that attacks the stopping rule directly."
- **Mitigation without touching data:** report the A-vs-B/C/D half-widths as a
  sensitivity line, the way bounded rows already get one ("the report prints a
  sensitivity run with bounded rows excluded so the uncertainty stays visible").
- Sample: 134 included, `hardware_deeptech` 24 (17.9% vs a 15% quota).

### Option B — drop p70 Dubinsky

- **Principled rule available without amending `frame.md`:** the criterion says
  "the person's **own** venture", and both cited sources say Dubinsky did not
  found Palm — she was hired as CEO shortly after Hawkins founded it. Under that
  reading her Palm row was never eligible for a Palm-entity hit, so this applies
  an existing rule rather than a new one. **This is the only drop-one option
  with a principled basis; the same argument cannot be made against Hawkins.**
- **But the honest form of that argument is Option D, not B.** If Palm is not
  her venture, `frame.md` does not say "exclude her" — it says find the first
  year *her own* venture crossed. Dropping her outright is only right if
  Handspring also fails to date, and it does not (section 1.4).
- Consequence: 133 included; `hardware_deeptech` 23 (17.3%); the women's share
  falls by one row; half-width 2.500 → 3.000.

### Option C — drop p94 Hawkins

- **No principled rule supports this one.** Hawkins founded Palm, Palm is his
  first venture, his source is live, his `a4` confidence is `high` where p70's
  is `medium`. Dropping the founder and keeping the hired CEO inverts the "own
  venture" language. The only rules that reach C are "keep the lower
  `person_id`" or "keep the shorter clock" — the first arbitrary, the second
  outcome-dependent selection, which the covariates section forbids in
  principle ("Selecting on it guarantees it cannot be discovered").
- Consequence: 133 included; half-width 2.500 → 2.750; it deletes the row with
  the *longer* education clock (16.0 vs 14.0), so of all options it is the one
  that nudges the median short — and `BIASES.md`'s summary already warns "The
  two strongest identified effects both push **short**."

### Option D — re-date p70 to Handspring, `rev10` 1999, basis `primary`

- **Rule needed:** none new. It applies `frame.md`'s existing "own venture"
  wording plus the serial-founder first-crossing rule the dataset already
  applies elsewhere (p146's notes: "the hit must be the FIRST venture to
  cross"). Handspring is Dubinsky's first *own* venture; its crossing is 1999.
- **Best evidence in the pair:** audited SEC 10-K405 and S-1/A, pinned quarter,
  305% of bar. Moves p70 from `acq50`/`fallback` to `rev10`/`primary` — the
  frame's preferred basis — and off the dead penbasedcomputing URL. Removing one
  `fallback` row also helps `BIASES.md` 5 ("Fallback lag").
- **Effect on the collision:** dissolved. Different entity, different year,
  genuinely independent event. Half-width 2.500 → 3.000, the largest honest
  widening of any option, because the two rows become fully independent rather
  than one being deleted.
- **Effect on p70's clocks:** `clock_education` 14.0 → **18.0**;
  `clock_venture` 3.0 → **1.0** (a4 becomes 1998); `age_at_first_hit` 40 → 44;
  `era` stays `post1995`; `bounded` stays false; `conf_min` stays `high`. Sample
  median unchanged at 14.00.
- **What it costs:** it implies `a4_first_venture_date` also moves 1992 → 1998,
  changing an anchor the audit already passed. And it is a real judgment call in
  the other direction — she is "universally described as co-leader/co-creator of
  the Palm business" (p70's own notes), and a reader may fairly hold that a
  founding-CEO joining months after incorporation is a co-founder in substance.
  `frame.md` gives no test for that; it only says "own venture".
- Sample: 134 included, no bucket-share change, no gender-share change.

### Option G — blanket "no two rows may share a `hit_entity`"

**Severe side effects; documented here because the brief asked.**

`science_research` has 19 rows and only **8 distinct `hit_entity` values**,
because `frame.md` makes the *prize* the hit entity:

> "`science_research` → `prize` (Nobel, Turing, Fields, or Breakthrough). Basis
> `equivalent`."

| shared prize entity | rows |
|---|---|
| Nobel Prize in Chemistry | 4 — Lehn 1987, Charpentier 2020, Bertozzi 2022, Yaghi 2025 |
| Nobel Prize in Physiology or Medicine | 3 — Levi-Montalcini 1986, Tu 2015, Sakaguchi 2025 |
| Nobel Prize in Physics | 3 — Strickland 2018, Aspect 2022, Devoret 2025 |
| Fields Medal | 3 — Mirzakhani 2014, Birkar 2018, Viazovska 2022 |
| ACM A.M. Turing Award | 2 — Liskov 2009, Bengio 2019 |
| Breakthrough Prize in Mathematics | 2 — Brendle 2023, Gaitsgory 2025 |

A blanket rule keeping one row per entity **deletes 11 of the 19
`science_research` rows** — 58% of the bucket — taking it from 14.2% of the
included sample to about 6.5% against a **12% quota**. It deletes Mirzakhani,
Viazovska, Strickland, Charpentier and Tu Youyou among others, i.e. it lands
disproportionately on women, and it does so on an accident of row order rather
than any property of the rows. Recomputed: included 134 → 122, `clock_education`
n 103 → 91, **median moves 14.00 → 13.00**, half-width 2.500 → **2.250** — the
opposite of the intended effect, because the rule deletes genuinely independent
observations and thereby *narrows* the interval further.

`BIASES.md` 23 already names why the blanket rule is wrong: "**The test is
shared event, not shared institution.**" and "Bengio (2019) and Liskov (2009)
both hold Turing Awards, but in different years. Different events, genuinely
independent."

**The correct key, if a rule is wanted, is `(hit_entity, a5_first_hit_date)`,
not `hit_entity`** — exactly `BIASES.md` 23's phrasing ("entity plus year"). On
that key the collision set is **{p70, p94} and nothing else**, all 19 science
rows survive, and the rule touches one row in this dataset. It still needs a
tie-break for which of the two goes, which is where B vs C vs D returns.

## 1.7 What is still genuinely unresolved

1. **No revenue figure of any kind exists for Palm Computing 1992-1995.** The
   fallback is permitted because nothing establishes an earlier crossing, not
   because anything rules one out. Andrea Butter & David Pogue, *Piloting Palm*
   (Wiley, 2002) is the obvious primary source for Graffiti/Zoomer-era licensing
   revenue and was not obtainable in this pass. A single figure from it would
   either confirm 1995 or convert **both** rows to a bounded 1992-1995 `rev10` —
   note that would turn the collision into a *bounded* collision rather than
   dissolving it.
2. **Whether Dubinsky counts as a Palm co-founder is a judgment call `frame.md`
   does not adjudicate.** "Own venture" is the only text there is. Everything in
   1.4 turns on it, and no further source will settle a definitional question.
3. **`frame.md` is frozen**, so an "entity plus year" uniqueness rule cannot be
   added mid-study without the discontinuity that section itself warns about.
   Deciding this pair by an unwritten rule and recording it in `BIASES.md` is
   the only route that does not touch the frame; the author may equally prefer
   to leave A in place and print the sensitivity.
4. **p70's `a5_first_hit_src` is dead with no archive**, independent of the pair
   decision. A fixable data-quality defect regardless of outcome; not fixed here.
