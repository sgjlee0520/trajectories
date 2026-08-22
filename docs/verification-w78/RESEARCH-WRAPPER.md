# Research wrapper — waves 7 and 8

`~/trajectories/docs/RESEARCH-RULES.md` is your brief. Read it and follow it verbatim.
This file only states the four places your run differs from it, plus the emphases that
cost wave 6 the most time.

## Differences from RESEARCH-RULES.md

1. **You do NOT write to `data/anchors.csv`.** You write to YOUR OWN output file, named
   in your assignment. It already exists with the correct 30-column header. Ten agents
   are running concurrently; two agents writing `anchors.csv` would destroy the wave.
   Still read `data/anchors.csv` for column order and `notes` style, as the brief says
   (rows p25-p35 are good templates) — read only, never write.
2. **Windows.** `python`, never `python3`. Set `PYTHONUTF8=1` before any python that
   touches the CSVs, or it dies on cp1252 with the em dashes and non-ASCII names.
   `PYTHONUTF8=1 python -m src.cpi 1994`
3. **Validate your own file, not anchors.csv**: `python -m src.schema data/<your-file>`
   must report 0 errors before you report back. Fix DATA errors; never edit `src/`.
4. **Do not write temp files into the session scratchpad.** Use
   `C:\Users\measu\AppData\Local\Temp\claude\C--Users-measu\41ce67f7-9b18-4415-8c7a-86e35fc72cfc\w78work\<your-letter>\`.
   A blind audit runs from the shared scratchpad afterwards and wave 6 leaked 54 files
   into it (`docs/BIASES.md` 22).

## Emphases — these are where wave 6 lost time and nearly lost rows

- **Constant 2026 dollars, never nominal.** `PYTHONUTF8=1 python -m src.cpi <year>` prints
  that year's real bar for rev10, acq50 and fund100. The 1960 rev10 bar is $919,417, not
  $10M. Check every figure against the bar for THAT year. This defect dated one pilot row
  eleven years late.
- **Serial founders are the dominant risk.** Three of six rows in one wave-6 batch were
  serial founders and it changed the answer in all three. The hit is the FIRST venture to
  cross, not the famous one. Before you record a hit entity, ask explicitly: did this
  person run anything earlier that crossed the bar first? Write the answer in `notes`
  even when it is "no earlier venture found".
- **The IPO/acquisition fallback is barred whenever an earlier crossing is *known*** —
  and frame.md is explicit that a purely qualitative claim ("already the industry leader
  by 1994", "profitable and growing fast") counts as knowing. Only the year needs pinning
  or bounding, not the crossing. Expect a bounded date or an exclusion to be the normal
  outcome and the fallback to be rare.
- **Founding year is a valid lower bound.** A company cannot earn before it exists. Try
  the bracket `founding..first sourced above-bar figure` before giving up — but only if
  the span is <= 10 years and the entity is not a going concern the person inherited.
- **An honest exclusion beats a fabricated date.** 26 rows are excluded and every one has
  survived independent re-checking. Do not stretch a bound to avoid an exclusion.
- **`a2_education_end` matters more than the other anchors** — the headline clock counts
  from it, and 31 included rows currently have it as `unknown`, which makes it the study's
  binding constraint, not `a5`. Give it a genuine second attempt. For a dropout, the
  anchor is the last credential actually COMPLETED.
- **Roster membership URLs are not trustworthy until fetched.** The roster row cites one.
  Confirm it names the person. If you cannot after two attempts, put
  `LIST MEMBERSHIP UNCONFIRMED` in that row's notes and say so in your report; do not drop
  the row. If the person appears not to exist in the described role, say
  `SUSPECTED FABRICATED ROSTER ENTRY` and invent nothing.

## Fetch quirks, all verified in wave 6
- `sec.gov`: WebFetch 403s; `curl -H "User-Agent: research gpm434@gmail.com"` works.
- `nobelprize.org`, `pulitzer.org`, `grammy.com`: 403 WebFetch, fine with `curl` + a
  browser User-Agent.
- `oscars.org`: genuinely 403s even with a full UA — use third-party named-person sources.
- `startupintros.com`: unreliable, misattributes foundings — do not use it.

## Tool budget — report a failure immediately
The WebSearch budget is shared across ten concurrent agents and is finite; wave 6 burned
~200 calls on 25 people. **Prefer WebFetch and curl over WebSearch.** If WebSearch starts
erroring, rate-limiting, or returning nothing, STOP and say so at the top of your report.
Do not fall back to guessing URLs — a guessed URL that happens to 200 is how a fabricated
citation gets in.

## Write as you go
Append each completed row to your output file the moment you finish that person, never in
one batch at the end. Agents have died mid-task here; the survivors wrote as they went.

## Report back
Per person: anchors, `hit_entity`, `hit_criterion`, `hit_basis`, the figure vs THAT year's
bar, anyone excluded and why, list-membership verdict, and anything uncertain.
**Flag any margin under 20%**, every serial-founder call you made, and every row where a
qualitative scale claim ("already large", "industry leader") is doing the dating work —
those three are being re-checked by adversarial agents afterwards.
