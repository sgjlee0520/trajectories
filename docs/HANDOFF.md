# Handoff — continue this study anywhere

Written so this project can be picked up cold: a different Claude account, a
different machine, a different tool entirely. **No conversation history is
needed.** Everything below is in the repo.

Run everything from the repo root, `~/trajectories`, on branch `main`. Git identity is
already configured in the repo; `git push origin main` works.

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

## Current state (as of commit 95a1a41, wave 6 closed and pushed)

| | |
|---|---|
| people researched | 160 (`data/anchors.csv`) |
| included | 134 (26 excluded) |
| roster | 160 names (`data/roster.csv`) — fully researched, **wave 7 not yet drawn** |
| revenue-strict n | 60 |
| **median** | **9.2 yr, 95% CI [8.5, 13.0]**, half-width 2.25 |
| stopping rule | `STOP: False` — drift 0.80 and 0.60 yr, needs both < 0.50 |
| tests | `python -m unittest discover -s tests -t .` (207 tests) |

Waves completed: pilot (10), then waves 1-6 (25 each). Wave 6's audit came back at
**0.00 disagreement** on 10 drawn rows, with one second-only miss (p146).

Two data-quality facts worth knowing before reading any number: **64 of the 134
included rows carry a bounded `a5`**, so the bounded-row sensitivity run matters; and
**31 included rows have `a2_education_end = unknown`**, which means they contribute
nothing to the headline clock. `a2` is now the study's binding constraint, not `a5`.

## IMMEDIATE NEXT ACTION

Run wave 7. Nothing is half-finished — wave 6 is merged, validated, audited,
committed and pushed. Allocation for wave 7, already computed from the 160 rows:

    software_internet 6   hardware_deeptech 4   consumer_retail_industrial 3
    healthcare_biotech 3  investors_finance 3   science_research 3
    media_creators 2      trade_import_logistics 1

Draw p161-p185 into `data/roster.csv` from the enumerated lists in `frame.md`.

## Wave 6 lessons — read these before dispatching any agent

1. **This is Windows.** Use `python`, never `python3`. Set `PYTHONUTF8=1` before any
   python that handles the em dashes and non-ASCII names in the CSVs, or it dies on
   cp1252.
2. **`data/anchors.csv` is CRLF, UTF-8, QUOTE_MINIMAL.** APPEND to it. A full
   `csv.DictWriter` round-trip reflows quoting on every existing row and turns a
   25-row change into a 160-row diff. Same for `data/roster.csv`.
3. **Parallel agents leak the blind audit.** Wave 6 ran four concurrent research
   agents; all four shared one scratchpad and left 54 artifacts in it, including
   per-person JSON files with their finished answers. Any auditor spawned from that
   session would have started in that directory. Give each agent its own output file,
   and MOVE every first-pass artifact out of the shared scratchpad before dispatching
   a single auditor. See `docs/BIASES.md` 22.
4. **`docs/RESEARCH-RULES.md` breaks the blind if handed to an auditor unchanged.**
   It tells every agent to open `data/anchors.csv` for column style. Both wave-6
   auditors caught this themselves and declined. Audit prompts must carve it out
   explicitly.
5. **Roster membership URLs in the roster are not trustworthy until fetched.** Wave 6
   found three Endeavor entries citing directory paging URLs that name nobody, and one
   roster row that misdescribed the company (Ben & Frank is eyewear, not apparel).
6. **Fetch quirks, all verified in wave 6:** `sec.gov` needs
   `curl -H "User-Agent: research <contact>"`. `nobelprize.org`, `pulitzer.org` and
   `grammy.com` all 403 WebFetch but work fine with curl plus a browser UA — the
   roster's notes claiming otherwise were wrong. `oscars.org` genuinely 403s even with
   a full UA; use third-party named-person sources. `startupintros.com` is unreliable
   and misattributes foundings — do not use it.
7. **Serial founders are the dominant risk in commercial buckets.** Three of six rows
   in one wave-6 batch were serial founders and it changed the answer in all three.
   The hit is the FIRST venture to cross, not the famous one.
8. **Selection rule that worked, and is non-steering:** enumerate a list in published
   order and take the first entries whose hit entity appears nowhere in
   `data/anchors.csv` or `data/roster.csv`. The YC Top Companies list is machine-
   enumerable at `https://yc-oss.github.io/api/companies/top.json` (91 entries, YC's
   own top-company flag); entries 1-5 are used, the rest are not. Do NOT skip names
   for being famous — that is `BIASES.md` 24 and it is as much a bias as recalling them.

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

- **Palm pair** — p70 Dubinsky and p94 Hawkins both date to 1995 at Palm Computing. Same event, two rows. Needs a decision (`BIASES.md` 23). Wave 6 introduced no new shared hit events; a check for entity+year collisions across all 160 rows found only this pair.
- **`docs/OPEN-QUESTIONS.md` now has 7 questions, three added by wave 6.** Q5 (p141 Alpaca) and Q7 (p146 CookUnity/Sushi Pop) each decide whether a recorded row should be included or excluded — Q7 is the row where the blind audit's second pass reached a different verdict, invisible to the disagreement metric because the first pass returned `unknown`.
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
