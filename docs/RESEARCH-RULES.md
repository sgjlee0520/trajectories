# Research brief — the standing rules

This file is the brief handed to every research agent. It lives in the repo on
purpose: an earlier version lived in a temp directory, got swept between
sessions, and a research batch ran with an EMPTY brief before anyone noticed.

---

Research task in ~/trajectories. Read `frame.md` FIRST (hit criteria, sourcing rules, bounded dates), then `data/roster.csv` for your assigned ids, then `data/anchors.csv` to match its column order and `notes` style exactly (rows p25-p35 are good templates). Do NOT edit anything under `src/`.

THE RULE YOU MUST NOT GET WRONG: every dollar threshold is in CONSTANT 2026 DOLLARS, never nominal. Run `python3 -m src.cpi <year>` for that year's real bar (it prints rev10, acq50, fund100). The 1960 rev10 bar is $919,417, not $10M. Check every figure against the bar for THAT year. Applying $10M nominally to an old company is the defect that wrecked this study's first pilot, dating one row eleven years late. Convert non-USD at the spot rate for the revenue year and state the rate in `notes`.

SOURCING DISCIPLINE:
- NEVER infer a year. Each anchor is a sourced date, a sourced bounded range YYYY-YYYY (max 10-year span, BOTH ends sourced), or the literal `unknown` with empty _src and _conf=none.
- Two genuine source attempts per anchor, then `unknown`. That is an honest outcome.
- A bounded date needs a source for BOTH ends: below the bar in the earlier year, at/above it in the later year. The hit entity's FOUNDING YEAR is a valid lower bound (a company cannot earn before it exists) — try this before giving up.
- The IPO/acquisition fallback is BARRED whenever revenue is documented from after the crossing. If a crossing cannot be dated or bounded within 10 years: excluded=true, exclusion_reason=crossing_undatable.
- CALIBRATION: rows in this study are honestly excluded as crossing_undatable and every one has held up under independent re-checking. Do NOT stretch a bound or accept a weak source to avoid an exclusion. A fabricated date is the worst outcome available to you; an exclusion is a fine one.
- For a serial founder, the hit is the FIRST company to cross, not the famous one.
- An appointment or a single-winner prize is NOT a `rank1` ranking. `rank1` needs a published third-party ranking naming them at the top in a datable year. An informal magazine poll does not qualify.
- SEC EDGAR: WebFetch/browser gets 403, but `curl -H "User-Agent: research contact@example.com"` works on sec.gov.

LIST MEMBERSHIP: the roster credits each person to a source list. Confirm it with a URL that NAMES THE PERSON (or their company, where the list ranks companies). A link to the list's homepage or a generic blog post is NOT confirmation. If you cannot confirm after two attempts, put `LIST MEMBERSHIP UNCONFIRMED` in that row's notes and say so in your report. Do not drop the row yourself. If the person appears not to exist in the role the roster describes, say `SUSPECTED FABRICATED ROSTER ENTRY` and do not invent data for them.

a2_education_end MATTERS MORE THAN THE OTHER ANCHORS. The headline clock counts from it, so a row without it contributes nothing to the study's main number. Give it a genuine second attempt before recording unknown. For a dropout, the anchor is the last credential actually COMPLETED.

APPEND EACH COMPLETED ROW to data/anchors.csv AS YOU FINISH IT, never in one batch at the end. Agents have died mid-task here; the survivors wrote as they went.

When your assigned ids are done run `python3 -m src.schema data/anchors.csv` and fix any DATA errors (never the validator). Do not commit. Do not run clocks/report/stats. Then print a short per-person summary: anchors, hit_criterion, hit_basis, the figure vs that year's bar, anyone excluded and why, list-membership verdicts, and anything uncertain — flag any margin under 20%.
