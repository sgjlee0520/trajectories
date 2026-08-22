#!/bin/bash
# Run one Grok research batch.
#   scripts/grok-batch.sh <output-file> <id> [<id> ...]
# Example: scripts/grok-batch.sh data/w9-a.csv p211 p212 p213 p214 p215
set -u
cd "$(dirname "$0")/.."
OUT="$1"; shift
IDS="$*"
BRIEF=docs/GROK-RESEARCH-BRIEF.md
[ -s "$BRIEF" ] || { echo "FATAL: $BRIEF missing or empty"; exit 1; }
[ -n "$IDS" ]   || { echo "FATAL: no ids given"; exit 1; }

# Seed the output file with the exact header of anchors.csv
if [ ! -f "$OUT" ]; then head -1 data/anchors.csv > "$OUT"; fi

PROMPT="$(cat "$BRIEF")

---

# YOUR ASSIGNMENT

Working directory: $(pwd)

Research these people: $IDS

Look each one up in data/roster.csv for their name, bucket, and source list.
You may READ data/anchors.csv to copy its column order and note style, but you
must WRITE only to: $OUT

$OUT already contains the correct header row. Append one line per person as you
finish them — never all at the end.

Follow every rule in the brief above literally. When you are done, run the
self-check in section 8 and paste the schema output."

grok -p "$PROMPT" --always-approve --max-turns 200 2>&1 | tail -60
echo "=== BATCH DONE: $OUT ==="
python3 -c "
import csv,sys
rows=list(csv.DictReader(open('$OUT')))
print('rows written: %d' % len(rows))
for r in rows:
    d=r['a5_first_hit_date'].strip()
    ok='OK' if (d=='unknown' or d.replace('-','').isdigit()) else 'MALFORMED'
    print('  %-6s %-24s a5=%-12s %s' % (r['person_id'], r['name'][:24], d, ok))
"
