#!/bin/bash
# Blind second pass over already-researched people, for the wave audit.
#   scripts/grok-audit.sh <output-file> <assignment-file>
# The assignment file is one line per person:
#   person_id|Name|hit_entity|hit_criterion
# and must NOT contain the first pass's dates.
#
# Runs in a scratch directory outside the repo holding only the two briefs and
# src/cpi.py, so the auditor cannot read the first pass's scraped files or
# answers (docs/BIASES.md 22).
set -u
cd "$(dirname "$0")/.."
REPO="$(pwd)"
OUT="$1"; ASSIGN="$2"
[ -s "$ASSIGN" ] || { echo "FATAL: $ASSIGN missing or empty"; exit 1; }
grep -qE '^[a-z0-9]+\|' "$ASSIGN" || { echo "FATAL: $ASSIGN has no person lines"; exit 1; }
grep -qE '\|(1[89]|20)[0-9]{2}(-|$|\|)' "$ASSIGN" && {
  echo "FATAL: $ASSIGN looks like it contains dates. An audit assignment must be blind."; exit 1; }

CLEAN="$(mktemp -d "${TMPDIR:-/tmp}/trajectories-audit.XXXXXX")"
mkdir -p "$CLEAN/src"
cp src/cpi.py src/__init__.py "$CLEAN/src/"
cp docs/GROK-RESEARCH-BRIEF.md docs/GROK-AUDIT-BRIEF.md "$CLEAN/"
echo "person_id,second_pass,evidence" > "$CLEAN/out.csv"

PROMPT="$(cat "$CLEAN/GROK-AUDIT-BRIEF.md")

The research brief this refers to is GROK-RESEARCH-BRIEF.md in this directory.
Read it now, before anything else.

---

# YOUR ASSIGNMENT

Working directory: $CLEAN
Write only to: $CLEAN/out.csv  (header row is already there)

\`python3 -m src.cpi <year>\` works here. Nothing else from the study is
present, by design — do not go looking for it.

Date \`a5_first_hit\` for each of these people. The entity and the criterion
are given; they are settled and you do not re-open them. Your job is the year.

$(cat "$ASSIGN")

Append one row per person as you finish them, never all at the end."

grok -p "$PROMPT" --always-approve --max-turns 200 2>&1 | tail -80
echo "=== AUDIT DONE ==="
cp "$CLEAN/out.csv" "$REPO/$OUT"
echo "scratch dir kept for inspection: $CLEAN"
python3 -c "
import csv
rows=list(csv.DictReader(open('$REPO/$OUT')))
print('rows written: %d' % len(rows))
for r in rows:
    d=r['second_pass'].strip()
    ok='OK' if (d=='unknown' or d.replace('-','').isdigit()) else 'MALFORMED'
    cpi='cpi-pasted' if 'src.cpi' in r['evidence'] or 'bar' in r['evidence'].lower() else 'NO-CPI'
    print('  %-6s %-12s %-10s %s' % (r['person_id'], d, ok, cpi))
"
