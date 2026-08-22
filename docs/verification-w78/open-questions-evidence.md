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

---

# 2. Q5 — p141 Yoshi Yokokawa (Alpaca)

## 2.1 The question as written

> "In what year was Alpaca (the US brokerage-infrastructure company founded by
> Yoshi Yokokawa, legal entity AlpacaDB, Inc.) founded, and what was its revenue
> in any year before 2024? Four sources give four different founding years —
> 2013 (Ikkyo Technology, the Kobe predecessor), 2015 (AlpacaDB/Sacra), 2017
> (Keio) and 2018 (MEXT). Quote the figure or year and the source URL."

> "**On the 2013 lineage the span is 11 years and the row must instead be
> `crossing_undatable`.**"

That clause is mechanically true and I verified it in code rather than by
reading: `src/schema.parse_span` returns `(None, None)` when
`hi - lo > MAX_SPAN_YEARS`, so feeding p141 `2013-2024` yields `era=''`,
`clock_venture=None`, `clock_education=None` — the row silently contributes
nothing. The 10-year cap is enforced, not merely documented.

## 2.2 The founding year is now SETTLED by a primary regulator filing

**This is new evidence the first pass did not have.** AlpacaDB, Inc. has its own
EDGAR filer record — **CIK 0001689386** — separate from the broker-dealer
subsidiary (CIK 0001702580) the first pass checked. It filed two Form D notices.

Form D, filed 17 November 2016, accession 0001689386-16-000001,
<https://www.sec.gov/Archives/edgar/data/1689386/000168938616000001/primary_doc.xml>
(amended by D/A 0001689386-17-000001 filed 2 Feb 2017, identical on these
fields). Verbatim from the XML:

```xml
<entityName>AlpacaDB, Inc.</entityName>
<issuerAddress><street1>55 EAST 3RD AVE</street1><city>SAN MATEO</city>
  <stateOrCountry>CA</stateOrCountry></issuerAddress>
<jurisdictionOfInc>DELAWARE</jurisdictionOfInc>
<issuerPreviousNameList><value>None</value></issuerPreviousNameList>
<entityType>Corporation</entityType>
<yearOfInc>
    <withinFiveYears>true</withinFiveYears>
    <value>2015</value>
</yearOfInc>
<industryGroupType>Other Technology</industryGroupType>
<issuerSize><revenueRange>Not Applicable</revenueRange></issuerSize>
<dateOfFirstSale><value>2016-11-04</value></dateOfFirstSale>
<totalOfferingAmount>2500000</totalOfferingAmount>
<totalAmountSold>1221677</totalAmountSold>
<signatureName>/s/ Tsuyoshi Yokokawa</signatureName>
<signatureTitle>CEO and President</signatureTitle>
```

**What this establishes.** The company itself, signed by Yokokawa as CEO and
President, told the SEC in November 2016 that AlpacaDB, Inc. is a Delaware
corporation whose **year of incorporation is 2015**, and that it has had **no
previous names** (`issuerPreviousNameList: None`). That is a signed federal
filing, contemporaneous with the period in question, and for the question *when
was AlpacaDB, Inc. founded* it outranks Sacra, the Keio page (2017), the MEXT
page (2018) and the kigyotv interview (2013). **The 2015 lower bound the row
already uses now rests on a primary source rather than a data aggregator.**

What it does **not** settle: whether Ikkyo Technology Inc. (Kobe, Feb 2013) is
"the same venture" for `frame.md` purposes. `issuerPreviousNameList: None` shows
AlpacaDB was not a *renamed* Ikkyo, i.e. they are two distinct legal entities —
which weakens the 2013 lineage argument without killing it, because the frame
dates the person's venture rather than a legal entity, and Yokokawa himself says
Ikkyo "later evolved into AlpacaDB". Still a judgment call, but a better-informed
one.

`revenueRange = "Not Applicable"` is **not** a revenue statement. Form D's
issuer-size options for an operating company are "No Revenues" / "$1 -
$1,000,000" / … / "Decline to Disclose" / "Not Applicable"; the last is the
option intended for pooled funds. Its use here is a filing quirk and gives no
bound. Had they ticked "No Revenues" this row would be closed.

**No later Form D exists.** EDGAR full-text search for `"AlpacaDB"`
(`https://efts.sec.gov/LATEST/search-index?q=%22AlpacaDB%22&forms=D`) returns
exactly two hits — the 2016 D and the 2017 D/A. The 2021 Series B, 2023 SBI note
and 2024 Series C produced no further Form D under this CIK. I also enumerated
every EDGAR company matching "alpaca" (19 CIKs) to check for a renamed parent;
the only near-miss is "Alpaca, Inc." CIK 0001929936, an unrelated Omaha,
Nebraska corporation, year of incorporation 2021, Form D signed by Karen
Borchert. Ruled out.

## 2.3 Revenue: what exists, checked against constant-2026-dollar bars

**Upper end (confirmed, unchanged).** Sacra, <https://sacra.com/c/alpaca/>:
$100M annualised as of September 2025, "up from **$60M at the end of 2024**".
$60,000,000 vs the **2024 rev10 bar of $9,743,619** = **615.8% of bar, +515.8%
margin** — decisively above. The 2025 $100M vs the 2025 bar of $10,000,000 =
1,000% of bar.

Sacra also gives the funding history: Series B $50M led by Tribe Capital (2021,
$215M post), Series B-2 $50M led by Unbound (2021, $475M post), $15M SBI
convertible note (2023, $250M cap), Series C $50M from Tencent (2024, $461M
post), $115M raised in total. **No source gives a revenue figure for any year
before 2024.** Valuation is not revenue, and `frame.md` forbids inferring one
from the other.

**The regulator route is now exhausted, one filing further than the first pass
went.** The row's `notes` list four X-17A-5 filings (2021-02-12, 2022-02-14,
2023-04-19, 2024-06-12). EDGAR CIK 0001702580 actually holds **eight**:

| filed | period | format |
|---|---|---|
| 2019-01-29 | 2018-11-30 | paper (placeholder stub only) |
| 2020-01-31 | 2019-11-30 | paper stub + FOCUSN |
| 2021-02-12 | 2020-11-30 | electronic |
| 2022-02-14 (+ /A 2022-02-18) | 2021-11-30 | electronic |
| 2023-04-19 (+ /A 2023-05-25) | 2022-12-31 | electronic |
| 2024-06-12 | 2023-12-31 | electronic |
| 2025-03-25 | 2024-12-31 | paper (placeholder stub only) |
| **2026-02-27** | **2025-12-31** | **electronic — not checked by the first pass** |

I downloaded and text-extracted the newest one,
<https://www.sec.gov/Archives/edgar/data/1702580/000170258026000007/AlpacaSec2025Public.pdf>
(811,570 bytes, 18 pages). Its financial statement is titled "Statement of
Financial Condition" and its notes "Notes to Statement of Financial Condition".
**No income statement, no revenue line** — the same confidential-treatment
posture as 2020-2023. The three paper filings resolve to `9999999997-*.paper`
placeholder stubs with no document behind them. **The regulator gives no revenue
for any year, 2018 through 2025.**

The 2025 filing does confirm the entity structure the row assumes:

> "Alpaca Securities LLC (the 'Company') is a **wholly owned subsidiary of
> AlpacaDB, Inc. (the 'Parent')**. The Company is a registered broker-dealer with
> the Securities and Exchange Commission ('SEC') and is a member of the Financial
> Industry Regulatory Authority ('FINRA'), and the Securities Investor Protection
> Corporation ('SIPC')."

**One genuinely new hard date, from the SEC header of the 2019 paper filing**
(<https://www.sec.gov/Archives/edgar/data/1702580/999999999719000303/9999999997-19-000303.txt>):

```
CONFORMED SUBMISSION TYPE:  X-17A-5
CONFORMED PERIOD OF REPORT: 20181130
FILED AS OF DATE:           20190129
PERIOD START:               20180326
COMPANY CONFORMED NAME:     ALPACA SECURITIES LLC
STATE OF INCORPORATION:     DE
SEC FILE NUMBER:            008-69928
```

**`PERIOD START: 2018-03-26`** is the first day of Alpaca Securities LLC's first
reported fiscal period. The brokerage business — the business that earns the
revenue Sacra measures — did not exist as a reporting broker-dealer before
26 March 2018.

**Still negative after this pass:** TechCrunch (Oct 2023) reports revenue grew
17x since the Aug-2021 Series B but "the company declined to provide the
baseline"; the Endeavor entrepreneur profile
(<https://endeavor.org/entrepreneurs/yoshi-yokokawa/>) carries only "Alpaca is an
API provider and self-clearing broker-dealer that enables developers and
entrepreneurs to launch and scale products for trading assets" and **no**
founding year, revenue, AUC, customer count or dated scale claim; Latka's $5.7M
for 2024 contradicts Sacra by an order of magnitude and is unusable either way.

## 2.4 What the decision actually costs the study — the decisive number

p141 has `a1_birth_date = unknown` and `a2_education_end_date = unknown`.
**It therefore contributes to `clock_venture` only.** Recomputed with
`src.clocks` + `src.stats.bootstrap_median_ci` (seed 0, 10,000 iters):

| scenario | clock_education n / med / half | clock_venture n / med / half |
|---|---|---|
| status quo, hit `2015-2024` | 103 / 14.00 / **2.500** | 114 / 5.00 / **1.250** |
| hit `2018-2024` | 103 / 14.00 / 2.500 | 114 / 5.00 / 1.375 |
| hit `2022-2023` | 103 / 14.00 / 2.500 | 114 / 5.00 / 1.375 |
| **excluded** | 103 / 14.00 / **2.500** | 113 / 5.00 / **1.250** |

**Excluding p141 changes the headline education clock by exactly nothing — same
n, same median, same interval — and leaves the venture median at 5.00 with an
identical interval.** Whatever is decided, no reported number moves. That is the
most useful single fact for a one-sitting decision: this is a data-integrity
call, not a results call.

p141's own `clock_venture` under each span (a4 = 2013): `2015-2024` → **6.5**;
`2018-2024` → 8.0; `2022-2023` → 9.5; `2013-2024` → `None` (span rejected).

## 2.5 Options and consequences

### Option 1 — keep as recorded, `2015-2024`, re-sourced to the Form D

- Span 9, inside the cap. **The lower bound upgrades from Sacra (an aggregator)
  to a signed SEC Form D**, so `a5_first_hit_src` would gain
  `https://www.sec.gov/Archives/edgar/data/1689386/000168938616000001/primary_doc.xml`.
  A strict improvement in provenance, and arguably grounds to lift
  `a5_first_hit_conf` above `low` on the *bound* (though not on the crossing).
- **The known defect survives it.** The row's own notes concede: "the 17x growth
  since 2021 makes it likely that the true crossing sits late in the bracket,
  around 2022-2023, so the bracket midpoint of 2019-2020 that the clocks will use
  is probably several years early." Under `frame.md` that is not fatal — the
  founding year is an explicitly sanctioned lower bound ("**The founding year is
  a valid lower bound.** A company cannot earn revenue before it exists…") — but
  the row dates the hit early by an unknown amount, in the direction `BIASES.md`
  already says the study leans (short).
- Sample: 134 included, no reported figure changes.

### Option 2 — narrow to `2018-2024`, on Alpaca Securities' `PERIOD START`

- Span 6, comfortably inside the cap; **halves the residual dating error** and
  moves the midpoint from 2019/2020 to 2021, much closer to the 2022-2023 the
  17x claim implies.
- **Rule it leans on:** `frame.md` allows the bound to start at "the sourced
  founding **(or first-production)** year of the hit entity". 26 March 2018 is
  the SEC-recorded first day of the broker-dealer's first reporting period.
- **Its weakness, stated plainly:** the hit entity of record is AlpacaDB, Inc.,
  not Alpaca Securities LLC, and AlpacaDB *was* in production before 2018 —
  Labellio shipped June 2015 and was sold to Kyocera Communication Systems in
  January 2016 (terms undisclosed), and Capitalico existed. So "first production"
  for the *entity* is 2015, and 2018 is first production only for the *current
  revenue line*. Choosing 2018 is a defensible reading but it is a reading, and
  it makes the bound tighter than the frame compels — the mirror image of the
  failure mode `frame.md` names: "It is not licence to widen a range until it
  contains a year you like." The same caution cuts against narrowing to one.
- Effect: p141's `clock_venture` 6.5 → 8.0; sample venture half-width 1.250 →
  1.375, an honest slight widening. No other number moves.

### Option 3 — exclude, `crossing_undatable`, on the 2013 Ikkyo lineage

- The reading the first-pass researcher raised against its own row. Requires
  holding that Yokokawa's venture began with Ikkyo Technology (Kobe, Feb 2013),
  making the bracket 2013-2024 = span 11 > cap.
- **The Form D weakens this option.** `issuerPreviousNameList: None` shows
  AlpacaDB, Inc. was a fresh Delaware incorporation in 2015, not a renamed Ikkyo.
  Two distinct entities. The lineage argument now rests solely on Yokokawa's own
  interview language that Ikkyo "later evolved into AlpacaDB" — a
  self-description, the evidentiary class `BIASES.md` 4b ("The self-description
  trap") already flags as weak.
- Effect: 133 included; **`clock_education` completely unchanged** (n 103, median
  14.00, half 2.500); `clock_venture` n 114 → 113, median and interval unchanged.
  The discard pile gains one `crossing_undatable`, marginally worsening the
  exclusion-rate statistics `BIASES.md` 4/4c track — and note `BIASES.md` 4
  says exclusion already correlates with era and geography, so adding a
  non-US row to the discard pile pushes that bias very slightly further.

### Option 4 — pin to `2022-2023` on the 17x claim

- **Not permitted.** It requires deriving an absolute from a relative whose
  baseline was withheld, which is inference. `OPEN-QUESTIONS.md` states the
  standard: "the frame's rule is that no year is ever inferred, and a confident
  paraphrase is exactly how an inferred year gets laundered into data." Recorded
  only so the author can see it was considered and rejected.

## 2.6 What is still genuinely unresolved

1. **No revenue figure for Alpaca in any year before 2024 exists in any source I
   could reach.** Eight SEC broker-dealer filings (one of which the first pass
   never saw), two Form Ds, Sacra, Endeavor and TechCrunch all fail to produce
   one. The crossing is **boundable but not datable**, and every option above is
   a choice of bound, not the discovery of a year.
2. **The Ikkyo-lineage question is a definitional judgment `frame.md` does not
   adjudicate.** The Form D makes the two-entity reading stronger; it cannot make
   it certain.
3. **The residual early-dating error is real under every non-excluding option**
   and is unquantifiable without the 2021 baseline TechCrunch was refused.
4. **Budget note:** the session's WebSearch allowance (200/200) was exhausted
   partway through this section. Everything above came from direct WebFetch and
   `curl` against SEC EDGAR and named URLs, so no finding depends on a search
   engine — but a further keyword sweep for a 2021-2023 Alpaca revenue figure
   could not be run.

---

# 3. Q7 — p146 Mateo Marietti (CookUnity / Sushi Pop)

## 3.1 The question as written, and why it is the interesting one

> "What was the annual revenue of POP / Sushi Pop (the Argentine restaurant group
> co-founded by Mateo Marietti and Diego Araujo in 2007/08, which grew to eight
> brands in four countries) in any year between 2010 and 2021? **Group revenue,
> not the Sushi Pop brand alone.** Quote the figure, the year and the source URL."

> "this is the one row where the blind audit's second pass reached a different
> verdict than the first, and the disagreement metric could not see it because
> the first pass returned `unknown`."

The audit-visibility point is worth restating for the author because it
generalises: the disagreement metric compares recorded values, and `unknown`
compares equal to `unknown`. **A first pass that excludes a row and a second pass
that includes it with a dated bound score as agreement.** That is a defect in the
metric, not in either pass, and it is a close cousin of `BIASES.md` 22's
complaint that "a blind audit that has silently stopped being blind looks exactly
like a blind audit that passed."

## 3.2 The governing rule, quoted

`frame.md`, commercial buckets:

> "1. `rev10` — first year **the person's own venture** reached the
> constant-dollar $10M threshold. Basis `primary`."

and on what counts as knowing a crossing happened:

> "A qualitative claim in a source — that the venture was already large,
> profitable, or industry-leading by a stated year — is enough to establish that
> an earlier crossing occurred, even with no dollar figure attached. **Only the
> *year* needs pinning or bounding, not the crossing itself.**"

and on bounds:

> "record the anchor as `YYYY-YYYY` — low year first, **at most 10 years wide
> (arithmetic difference, so 1960-1970 is the widest permitted range)**"

> "A bounded date is a real measurement, not a guess. … **It is not licence to
> widen a range until it contains a year you like.**"

The serial-founder consequence: POP (2007/08) precedes CookUnity on any reading,
so **POP must be settled before CookUnity is even reached.**

## 3.3 The Sushi Pop / POP evidence, re-verified from source

### Currency basis, re-derived

World Bank indicator `PA.NUS.FCRF`, official annual-average ARS/USD, fetched
directly from
<https://api.worldbank.org/v2/country/ARG/indicator/PA.NUS.FCRF?date=2007:2022&format=json>:

| year | ARS per USD |
|---|---|
| 2009 | 3.71010683052328 |
| 2010 | 3.89629515447050 |
| 2011 | 4.11013957621326 |
| 2018 | 28.0949916666667 |
| 2021 | 94.9907416666667 |

These match the row's `notes` exactly (2009: 3.7101, 2018: 28.0950). No error
there.

### The 2009 figure — confirmed, and it carries a SECOND figure the row does not use

El Cronista, "Un sushi barato para competir con la pizza y las empanadas"
(8 March 2010),
<https://www.cronista.com/impresa-general/un-sushi-barato-para-competir-con-la-pizza-y-las-empanadas/>.
Verbatim:

> "Hace apenas un año y medio estos dos emprendedores sub-30 fundaron Sushi Pop"

> "cerró 2009 con una **facturación de $ 3 millones**"

> "Durante este año, **tienen previsto triplicar esa cifra**"

> "ya cuenta con **tres sucursales**"

> "Hoy la cadena responde unos **500 pedidos diarios**"

> "la cantidad de empleados –**ya suman 200**–"

> "van de menos de $ 1 a $ 2 por pieza" (competitors "arrancan en los $ 3 por
> pieza")

Against the constant-2026-dollar bars:

| year | ARS | rate | USD | rev10 bar | % of bar |
|---|---|---|---|---|---|
| 2009 (actual) | 3,000,000 | 3.71011 | **$808,602** | $6,663,819 | **12.1%** |
| 2010 (founders' projection, "triplicar") | 9,000,000 | 3.89630 | **$2,309,887** | $6,773,124 | **34.1%** |
| 2018 (projection, La Nación) | 200,000,000 | 28.09499 | **$7,118,707** | $7,799,735 | **91.3%** |

**The 2010 projection is new to this file and it matters.** At 34.1% of bar it
sits nowhere near the threshold — a 66% margin, far outside the 20% flag zone
that disqualified the 2018 figure. If the author is willing to treat a founder
projection reported by a national business daily as a below-bar anchor at all,
2010 is a far safer instance of that class than 2018 is. **It moves the lower end
of the bracket from 2009 to 2010 — and 2010-2021 is 11 years, still one year over
the cap.** So it improves the bracket without rescuing it.

### The 2018 figure — why it cannot decide, quantified both ways

The row's `notes` reject the La Nación April 2018 figure (350 employees, five
Izakaya restaurants, "la compañía proyecta facturar $200 millones") as too close
to the bar. I could not re-fetch the La Nación article — the URL I attempted
returned 404 and, with WebSearch budget exhausted (see 3.6), I could not locate
the live one. Taking the figure as the row records it, the arithmetic is:

- **ARS needed to reach the 2018 bar: 219,133,490 — i.e. 109.6% of the ARS 200M
  projection.** POP had to beat its own April projection by 9.6% to cross.
- Argentine CPI inflation in 2018 ran roughly 47.6%, so a projection struck at
  Q1-2018 menu prices would very likely be beaten in nominal pesos.
- **But the peso fell harder than prices rose**: the annual-average rate went
  16.5627 (2017) → 28.0950 (2018), a 69.6% depreciation against 47.6% inflation.
  So the USD figure would tend to fall even as the ARS figure rose.

**These two effects run in opposite directions and neither is sourced.** The
honest conclusion is the first pass's: a projection sitting within 9.6% of the
bar, in a currency that lost 41% of its value inside the measurement year, cannot
serve as either end of a bound. `frame.md`'s "not licence to widen a range until
it contains a year you like" applies symmetrically to narrowing one.

### The qualitative scale claim — re-verified, and it is genuinely dated 2021

Endeavor Argentina's entrepreneur profile,
<https://www.endeavor.org.ar/emprendedores/mateo-marietti/>, verbatim:

> "cofundó POP y le dio a los clientes la oportunidad de elegir diferentes
> estilos de comida a través de **8 marcas**, una de ellas, la conocida Sushi POP"

> "En pocos años, su modelo innovador escaló a **4 países de la región** y **hoy
> emplea a más de 1000 personas** en Sudamérica"

and the announcement item of 21 April 2021,
<https://www.endeavor.org.ar/mateo-marietti-argentino-escalo-cookunity-estados-unidos-se-suma-la-red-endeavor/>,
repeats "8 marcas", "4 países de la región", "más de 1000 personas en
Sudamérica", gives his age as "36", and dates the CookUnity Series A: "ronda de
inversión Serie A de 15,5 millones de dólares" raised "**A finales de 2020**".

**I tried and failed to date the eight-brand / four-country / 1,000-employee
state to any year earlier than 2021, and the surrounding evidence says it really
does belong to ~2021 rather than earlier:**

- March 2010 (El Cronista): **three** sucursales, **200** employees, one brand.
- April 2018 (La Nación, per the row's notes): **350** employees, **five**
  Izakaya restaurants.
- April 2021 (Endeavor): **8** brands, **4** countries, **1,000+** employees.

So the "already large" claim `frame.md` accepts attaches to 2021, not to 2016 or
2018. **This is the finding that most strengthens the first pass's exclusion**,
and it is the opposite of what I expected to find when I went looking: had any
source dated the 4-country footprint to 2016 or earlier, the bracket would have
closed at 2009-2016 (7 years) and the row would be rescued as a POP hit. No such
source surfaced.

### An internal inconsistency in the source base, flagged not used

The employee-to-revenue ratios in these sources do not reconcile:

- 2018: 350 employees ↔ US$7.12M = **~US$20,300 revenue per employee** —
  plausible for Argentine restaurants.
- 2009: 200 employees ↔ US$0.81M = **~US$4,040 revenue per employee** —
  implausible. Argentina's minimum wage in 2009 was around ARS 1,400/month;
  200 employees at that wage with the statutory 13th month is roughly ARS 3.6M of
  payroll alone, i.e. **more than the ARS 3M of revenue reported for the same
  period.**

At least one of the two 2010-article numbers is measuring something other than
what it appears to (franchisee headcount counted in, or ARS 3M being a
company-level rather than system-wide figure). **I record this as a caution
against leaning on headcount as a revenue proxy anywhere in this row — including
against reading the 1,000-employee 2021 claim as a quantitative statement.** It
is not evidence for any year and I have not used it as such.

## 3.4 The CookUnity leg — a primary-source finding that changes the second pass's arithmetic

**CookUnity Inc. is an EDGAR filer: CIK 0001766491**, Delaware, 630 Flushing
Avenue, Brooklyn NY. It has filed **twelve** Form D / D/A notices. Parsed
directly from the XML:

| filed | accession | year of incorporation | previous name | revenue range | total sold | date of first sale | signed |
|---|---|---|---|---|---|---|---|
| 2019-02-06 | 0001766491-19-000001 | **2014** (`withinFiveYears: true`) | None | **Decline to Disclose** | $3,157,807 | 2019-01-15 | **Mateo Marietti** |
| 2019-02-15 | 0001766491-19-000002 | **2014** | None | Decline to Disclose | $1,400,000 | — | Mateo Marietti |
| 2020-01-03 | 0001766491-20-000001 | `overFiveYears: true` | **Cookunity LLC** | Decline to Disclose | $2,537,388 | 2019-12-20 | Mateo Marietti |
| 2020-02-25 (D/A) | 0001766491-20-000002 | overFiveYears | — | Decline to Disclose | $1,846,799 | — | Mateo Marietti |
| 2020-09-22 (D/A) | 0001766491-20-000003 | overFiveYears | — | Decline to Disclose | $4,699,999 | — | Mateo Marietti |
| 2021-01-07 | 0001766491-21-000001 | overFiveYears | None | Decline to Disclose | $4,034,794 | 2020-12-24 | Mateo Marietti |
| 2021-04-06 | 0001766491-21-000002 | overFiveYears | — | Decline to Disclose | $141,012 | — | Mateo Marietti |
| 2022-12-08 | 0001766491-22-000002 | overFiveYears | Cookunity LLC | Decline to Disclose | $4,540,529 | 2022-11-28 | Mateo Marietti |
| 2023-04-27 | 0001766491-23-000001 | overFiveYears | Cookunity LLC | Decline to Disclose | **$46,999,985** | **2021-06-16** | Mateo Marietti |
| 2024-10-30 | 0000950123-24-010019 | overFiveYears | None | Decline to Disclose | $11,250,000 | 2024-10-15 | /s/ James Cosgrove |
| 2024-11-14 | 0000950123-24-011668 | overFiveYears | — | Decline to Disclose | $12,999,990 | — | /s/ James Cosgrove |
| 2025-04-08 | 0000950123-25-003383 | overFiveYears | — | Decline to Disclose | $24,162 | — | /s/ James Cosgrove |

Verbatim from the first one,
<https://www.sec.gov/Archives/edgar/data/1766491/000176649119000001/primary_doc.xml>:

```xml
<entityName>CookUnity Inc.</entityName>
<jurisdictionOfInc>DELAWARE</jurisdictionOfInc>
<yearOfInc>
    <withinFiveYears>true</withinFiveYears>
    <value>2014</value>
</yearOfInc>
<issuerSize><revenueRange>Decline to Disclose</revenueRange></issuerSize>
<signatureName>Mateo Marietti</signatureName>
```

**Three consequences.**

1. **CookUnity's founding year of record with the SEC is 2014, not 2018**, signed
   by Marietti himself, and the entity previously existed as "Cookunity LLC".
   Every secondary source the row relies on — Endeavor's infobox ("Founded:
   2018"), the row's own note that CookUnity was "founded after he moved to the
   United States in 2016" — is contradicted by the company's own federal filing.
   This is the same class of correction as the Alpaca Form D in section 2.
2. **The second pass's proposed bound of `2018-2025` does not survive it.** If
   the lower bound is the hit entity's founding year, that is 2014, and
   **2014-2025 is 11 years — over the cap.** I verified this in code: feeding
   p146 `2014-2025` yields `era=''` and all three clocks `None`, exactly as
   `2013-2024` does for p141. The second pass's verdict was reached without this
   filing.
   *However*, `2014-2024` is exactly 10 and **is** admissible (`frame.md`:
   "at most 10 years wide (arithmetic difference…)"), so the second pass's
   conclusion can be rescued by moving the upper end to the sourced 2024 revenue
   rather than the 2025 ARR.
3. **All twelve filings say "Decline to Disclose" on revenue range.** The trick
   that settled Alpaca's founding year gives nothing on CookUnity's revenue. The
   regulator route is closed here too.

**The CookUnity below-bar anchor the row already holds is better than the
founding year anyway.** The row's `notes` record CookUnity's "own revenue was
only about US$2M at its 2018 peak before he shut that line down". US$2M vs the
2018 bar of $7,799,735 = **25.6% of bar** — comfortably below, outside the flag
zone. Paired with the sourced US$350M for 2024 (**3,592% of the 2024 bar**), that
gives **2018-2024, span 6**, which is tighter and better-founded than either
`2018-2025` or `2014-2024`.

Datable further? The $47M round with **date of first sale 16 June 2021** (the row
records this as "September 2021"; the SEC says June) and the 2022 Series C make a
2021 or 2022 crossing very likely, but **no revenue figure for CookUnity in any
year between 2019 and 2023 was found**, so the upper end cannot honestly move
below 2024.

## 3.5 Options and consequences

Recomputed with `src.clocks` + `src.stats.bootstrap_median_ci` (seed 0, 10,000
iters). p146's own clocks, for `a2 = 2007`, `a4 = 2007-2008`:

| hit span | entity | clock_education | clock_venture | age_at_hit | admissible? |
|---|---|---|---|---|---|
| `2009-2021` | POP | — | — | — | **no** (12 > 10) |
| `2010-2021` | POP | — | — | — | **no** (11 > 10) |
| `2018-2021` | POP | 12.5 | 12.0 | 35.0 | yes (3) |
| `2014-2025` | CookUnity | — | — | — | **no** (11 > 10) |
| `2014-2024` | CookUnity | 12.0 | 11.5 | 34.5 | yes (10, at the cap) |
| `2018-2025` | CookUnity | 14.5 | 14.0 | 37.0 | yes (7) |
| `2018-2024` | CookUnity | 14.0 | 13.5 | 36.5 | yes (6) |

Sample effect:

| scenario | education n / med / half | venture n / med / half | age n / med / half |
|---|---|---|---|
| **status quo — p146 excluded** | 103 / **14.00** / **2.500** | 114 / 5.00 / 1.250 | 121 / **38.00** / 2.500 |
| in as `2018-2025` | 104 / **14.00** / 2.750 | 115 / 5.00 / 1.250 | 122 / 37.50 / 2.000 |
| in as `2018-2024` | 104 / **14.00** / 2.750 | 115 / 5.00 / 1.250 | 122 / 37.50 / 2.000 |
| in as `2014-2024` | 104 / **14.00** / 2.750 | 115 / 5.00 / 1.250 | 122 / 37.50 / 2.250 |
| in as `2018-2021` | 104 / **14.00** / 2.750 | 115 / 5.00 / 1.250 | 122 / 37.50 / 2.250 |

**One correction to the framing in `OPEN-QUESTIONS.md`.** It says "including it
would add a clock of roughly 14 years, which is long, and the study's two
strongest known biases both push the median short." The first half is confirmed
(14.5 / 14.0 under `2018-2025`). **The second half does not follow: the median
does not move.** It is 14.00 in every scenario above, because a single 14-year
observation added at the median cannot shift a 103-observation median. What
changes is the interval (half-width 2.500 → 2.750, correctly widening) and the
age median (38.00 → 37.50). So the "it would help correct a short bias" argument
for inclusion is **not supported by the arithmetic** — inclusion is a
data-completeness question, not a bias-correction lever.

### Option 1 — keep excluded, `crossing_undatable` (status quo, first-pass verdict)

- **The rule:** `frame.md` says a qualitative scale claim establishes an earlier
  crossing; Endeavor's 2021 claim does that for POP; the best sourced below-bar
  year for POP is 2009 (or 2010 on the projection), and 2009-2021 = 12 /
  2010-2021 = 11, both over the cap. `frame.md` then requires
  `excluded = true, crossing_undatable`.
- **Strengthened by this pass**, not weakened: the 3 → 5 → 8 brand and 200 → 350
  → 1,000 employee progression shows the scale claim genuinely belongs to 2021,
  closing the one route that could have rescued POP as a dated hit.
- **Cost:** 133 included; the discard pile keeps a fully-researched row; the
  Argentine / non-US row count stays one lower, feeding `BIASES.md` 4
  ("Exclusion correlates with era and geography") and 4c.

### Option 2 — include as CookUnity `2018-2024` (span 6) — second pass, repaired

- **The rule:** hold that POP never *demonstrably* crossed, on the ground that
  every dated POP figure is below bar (12.1%, 34.1%, 91.3%) and the only
  above-bar evidence is a headcount claim the 2009 arithmetic shows is an
  unreliable revenue proxy (3.3). Then CookUnity is the first venture with a
  sourced crossing, bounded from its sourced below-bar 2018 (US$2M, 25.6% of bar)
  to its sourced above-bar 2024 (US$350M, 3,592% of bar).
- **Better than the second pass's own `2018-2025`**: span 6 rather than 7, and it
  sidesteps the 2014 founding-year problem by using a below-bar year rather than
  the founding year as the lower end — which `frame.md` prefers anyway, since the
  founding-year rule is offered as a fallback ("Where the earliest published
  figure is already above threshold, bound the crossing from the entity's
  founding to that figure's year").
- **What it costs:** it requires overriding `frame.md`'s explicit instruction
  that a qualitative claim suffices — "A qualitative claim … is enough to
  establish that an earlier crossing occurred, even with no dollar figure
  attached." Choosing this option is choosing to disbelieve Endeavor's own
  description of a company its network vetted. That is a defensible call but it
  is a call *against* the frame's text, and it should be recorded as such.
- Sample: 134 included; education half-width 2.500 → 2.750; median unchanged.

### Option 3 — include as CookUnity `2014-2024` (span 10, at the cap)

- Uses the SEC founding year as the lower bound instead of the US$2M 2018 figure.
  Strictly more conservative about the lower end, at the price of sitting exactly
  on the 10-year limit and pulling the midpoint back to 2019 — which is almost
  certainly too early, since CookUnity had ~US$2M of revenue in 2018 and was
  still raising $2-5M tranches through 2020.
- Recommended against on the evidence: where a sourced below-bar year exists, it
  dominates the founding-year fallback. Recorded for completeness because the
  2014 filing is real and an author who distrusts the US$2M figure may want it.

### Option 4 — include as POP `2018-2021` (span 3)

- The bound the first pass explicitly refused: "Using it as a lower end would
  produce a tidy 2018-2021 bound that is exactly the kind of stretched bound
  frame.md forbids." I agree, and section 3.3 quantifies why — the 2018 figure is
  a pre-year projection sitting 9.6% under the bar in a year the currency lost
  41%.
- Recorded only so the author can see it was tested, not overlooked.

### Option 5 — record the audit-metric defect regardless of the row decision

Independent of which of 1-4 is chosen, the fact that a first-pass `unknown` and a
second-pass dated bound score as *agreement* is a live measurement problem for
`BIASES.md` 18/19, which calibrate the audit rule against a measured
disagreement rate. Costs nothing and changes no data.

## 3.6 What is still genuinely unresolved

1. **No group-level revenue figure for POP exists in any source I could reach**,
   for any year. Q7 asks exactly the right question and it is still open. Every
   number in the record describes the Sushi Pop brand (2009, 2018) rather than
   the eight-brand group, which is precisely the ambiguity `OPEN-QUESTIONS.md`
   identifies: "the dated figures describe the Sushi Pop *brand*, while the
   qualitative claim describes the eight-brand *group*".
2. **The La Nación April 2018 article could not be re-fetched** (404 on the URL I
   tried; WebSearch budget exhausted). Its figures are taken as the row records
   them and were not independently re-verified in this pass. Everything that
   turns on the 91.3%-of-bar number therefore rests on the first pass's
   transcription.
3. **No CookUnity revenue figure for 2019-2023 was found**, so the upper end of
   any CookUnity bound cannot honestly move below 2024 even though the funding
   pattern strongly suggests a 2021-2022 crossing.
4. **Whether "1,000+ employees across 8 brands in 4 countries" is a claim about
   Marietti's *own venture* is itself unexamined.** He moved to the US in 2016
   and founded CookUnity; POP's 2021 scale may postdate his operational
   involvement. `frame.md` does not say the founder must still be present at the
   crossing, so this does not change the analysis — but nobody has checked
   whether he still owned POP in 2021, and it is the kind of thing that would
   matter if the frame were ever tightened.
5. **Budget note:** WebSearch was exhausted during section 2 and both
   DuckDuckGo HTML endpoints returned JS challenges to `curl`, so section 3 was
   researched entirely by direct URL fetch and SEC EDGAR. Targeted keyword
   searching for a POP group revenue figure and for CookUnity 2021-2022 revenue
   was **not possible** and is the obvious next step for whoever picks this up.

---

## Cross-cutting note for the author

Two of the three items turned on the same trick: **the company's own SEC Form D
carries a signed `yearOfInc`, and in both cases it contradicted the secondary
sources the rows were built on** (AlpacaDB → 2015, confirming the row; CookUnity
Inc. → 2014, contradicting every source that says 2016 or 2018). Neither pass
checked for a parent-company EDGAR filer, only for the operating subsidiary or
not at all. **For any US-incorporated private venture in this study, a Form D
lookup is a cheap, primary-source founding-year check** — and the founding year
is load-bearing under `frame.md`'s bounded-date rule, because it sets the lower
end of a great many brackets. Worth a sweep across the existing US rows,
independent of these three decisions.
