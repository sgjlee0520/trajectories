# Handoff — continue this study anywhere

Written so this project can be picked up cold: a different Claude account, a
different machine, a different tool entirely. **No conversation history is
needed.** Everything below is in the repo.

Run everything from the repo root, `~/trajectories`, on branch `main`.

---

## What this project is

It measures the median number of years from the end of formal education to a
person's "first hit" — the first year a venture of theirs crossed **$10 million
in constant 2026 dollars**, or a per-bucket equivalent. Data is collected in
waves of 25 people. The purpose is to answer how long an apprenticeship
actually takes among people who succeeded.

**Read these, in order:**

1. `frame.md` — the sampling frame. Buckets, hit criteria, source lists. The authority on every rule.
2. `docs/RESEARCH-RULES.md` — the standing brief handed to every research agent, verbatim.
3. `docs/BIASES.md` — 24 recorded biases, several discovered the hard way. Read before quoting any number.
4. `docs/superpowers/RUNBOOK.md` — the 8-step wave procedure.

## Current state (as of commit d6b4940)

| | |
|---|---|
| people researched | 135 (`data/anchors.csv`) |
| included | 113 |
| roster | 160 names (`data/roster.csv`) — wave 6 drawn, not researched |
| revenue-strict n | 52 |
| **median** | **9.8 yr, 95% CI [8.0, 13.0]** |
| stopping rule | `STOP: False` — drift 0.80 yr, needs < 0.50 |
| tests | `python3 -m unittest discover -s tests -t .` |

Waves completed: pilot (10), then waves 1–5 (25 each). Wave 6's roster exists;
none of it is researched.

## IMMEDIATE NEXT ACTION

**Five wave-6 roster rows must be replaced before any research begins:**
`p136, p137, p138, p140, p142`.

Each is a co-founder of a company already in the sample (Razorpay, Zepto,
Meesho, Auth0, Palm). A company crosses the threshold once, so co-founders
share one hit event and are not independent observations. Because the stopping
rule keys off the bootstrap CI half-width, correlated rows narrow the interval
without adding information — the study could stop early on precision it has not
earned. See `docs/BIASES.md` 23.

Replace them with people whose hit entity appears **nowhere** in
`data/anchors.csv` (`hit_entity` column) or `data/roster.csv`. Same buckets:
four `software_internet`, one `hardware_deeptech`.

Then research all 25 (p136–p160) using `docs/RESEARCH-RULES.md` as the brief.

## The rules that matter most

1. **Never infer a year.** Every anchor is a sourced date, a sourced bounded range `YYYY-YYYY` (max 10 years, BOTH ends sourced), or the literal `unknown`.
2. **Every dollar threshold is constant 2026 dollars, never nominal.** `python3 -m src.cpi <year>` gives that year's real bar. The 1960 bar is **$919,417**, not $10M. Getting this wrong dated one row eleven years late in the first pilot and another six.
3. **Fix the data, never the validator.** Do not edit anything under `src/`.
4. **An honest exclusion beats a fabricated date.** 22 rows are excluded and every one has survived independent re-checking.
5. **Selection is money-only.** Country, era, and sex are recorded covariates, reported every wave, and must never steer who is drawn — in either direction. Avoiding famous names is as much a bias as recalling them (`BIASES.md` 24).
6. **Append rows incrementally**, never in one batch. Several agents have died mid-task; only incremental writers kept their work.
7. **Roster membership needs a URL that NAMES the person.** A link to a list's homepage is not confirmation. Four names so far were credited to lists that do not contain them.

## Running a wave

    # 1. allocate
    python3 -m src.allocate 25 <bucket>=<cumulative count> ...
    # 2. build roster (names only, confirmed memberships)
    # 3. research with agents, using docs/RESEARCH-RULES.md
    # 4. validate — must be 0 errors
    python3 -m src.schema data/anchors.csv
    # 5. blind audit: second pass must NOT see data/anchors.csv
    python3 -c "import csv; from src import stats; \
      ids=[r['person_id'] for r in csv.DictReader(open('data/anchors.csv'))][-25:]; \
      print(stats.audit_sample(ids))"
    # write data/audit.csv (person_id,first_pass,second_pass), then:
    python3 -c "from src import stats; \
      print(stats.audit_disagreement(stats.read_audit_pairs('data/audit.csv')))"
    # over 0.10 = contradictions, wave voids. Misses are NOT contradictions:
    python3 -c "from src import stats; \
      print(stats.audit_misses(stats.read_audit_pairs('data/audit.csv')))"
    # 6. close
    python3 -m src.clocks data/anchors.csv analysis/clocks.csv
    python3 -m src.report analysis/clocks.csv analysis/analysis.md
    python3 -m src.stats analysis/clocks.csv --history analysis/wave_medians.txt

The median is withheld below 30 revenue-strict rows, by design, in both the CLI
and `analysis.md`. That floor is now passed, so the number prints.

## Known open items

- **Palm pair** — p70 Dubinsky and p94 Hawkins both date to 1995 at Palm Computing. Same event, two rows. Needs a decision (`BIASES.md` 23).
- **Blind audits are not environment-enforced** (`BIASES.md` 22). A wave-5 auditor found the first pass's scraped files in its scratchpad. It declined to open them and disclosed it, but the isolation depends on agents honouring an instruction. Run second passes in a clean directory.
- **`investors_finance` and `trade_import_logistics` have no dedicated sampling list** (`BIASES.md` 12).
- **`docs/OPEN-QUESTIONS.md`** — stuck factual questions worth a search-first tool.
- **`docs/CROSSCHECK-PROMPT.md`** — a portable, self-contained prompt for verifying rows on any platform with no repo access. This produced the strongest reliability evidence in the study: six platforms, 60 comparisons, zero conflicts.

## How far there is to go

The stopping rule needs median drift under 0.5 yr across two consecutive waves
AND a CI half-width at or under 1.0 yr. Currently drift is 0.80 and half-width
2.50. Median precision improves roughly with the square root of n, so reaching
1.0 implies **n ≈ 230 revenue-strict rows, or roughly 500 people researched** —
several hundred more.

That is the pre-registered rule refusing to call the number settled, which is
correct behaviour. But stopping early and reporting the median with its actual
interval, plus the honest statement that it has not converged, is a legitimate
scientific outcome. That is a decision for the study author, not a default.

## What the number means

Whatever median this produces describes **time-to-hit among people who made
it**. It says nothing about the odds of making it. The sample is conditioned on
the outcome and has no denominator — the people who worked twenty years and
never crossed are absent by construction, not by rarity. The two strongest
measured biases both push the figure **short**, so read it as a floor.

`analysis/analysis.md` states this above every table, and it should stay there.
