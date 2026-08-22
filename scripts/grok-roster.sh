#!/bin/bash
# Draw a wave's roster with Grok.
#   scripts/grok-roster.sh <assignment.md> <output-csv>
# The assignment names the buckets, ids, and the list to walk for each.
# Regenerates the already-used exclusion list next to the assignment first, so
# a candidate already in the study or sharing an existing hit event is rejected
# from data rather than from memory.
set -u
cd "$(dirname "$0")/.."
ASSIGN="$1"; OUT="$2"
[ -s "$ASSIGN" ] || { echo "FATAL: $ASSIGN missing or empty"; exit 1; }
DIR="$(dirname "$ASSIGN")"

python3 - "$DIR/already-used.md" <<'PY'
import csv, sys
ros=list(csv.DictReader(open('data/roster.csv')))
anc=list(csv.DictReader(open('data/anchors.csv')))
names=sorted({r['name'].strip() for r in ros} | {r['name'].strip() for r in anc})
ents=sorted({r['hit_entity'].strip() for r in anc if r['hit_entity'].strip()})
with open(sys.argv[1],'w') as f:
    f.write("# Already in the study — reject any candidate matching these\n\n")
    f.write("Generated from `data/roster.csv` and `data/anchors.csv`.\n\n")
    f.write("## %d people already drawn\n\n" % len(names))
    for n in names: f.write("- %s\n" % n)
    f.write("\n## %d hit entities already used\n\n" % len(ents))
    f.write("A candidate whose hit would be one of these is the SAME EVENT as an\n")
    f.write("existing row and must be rejected (`frame.md`, One row per hit event).\n")
    f.write("Prizes are per-year: a different year of the same prize is a different\n")
    f.write("event and is allowed.\n\n")
    for e in ents: f.write("- %s\n" % e)
print("exclusions: %d names, %d entities" % (len(names), len(ents)))
PY

[ -f "$OUT" ] || head -1 data/roster.csv > "$OUT"

PROMPT="$(cat docs/GROK-ROSTER-BRIEF.md)

---

$(cat "$ASSIGN")

---

# MECHANICS

Working directory: $(pwd)
Write only to: $OUT  (header row is already there)

Read \`$DIR/already-used.md\` before you start — that is rejections 1 and 2.
Read \`frame.md\` for the named source lists and the one-row-per-hit-event rule.
You may read \`data/roster.csv\` for column order and note style.

Do not write to \`data/roster.csv\`, do not touch \`src/\`, do not run git."

grok -p "$PROMPT" --always-approve --max-turns 300 2>&1 | tail -100
echo "=== ROSTER DRAW DONE: $OUT ==="
python3 - "$OUT" <<'PY'
import csv, sys, collections
rows=list(csv.DictReader(open(sys.argv[1])))
print("rows: %d" % len(rows))
print("by bucket:", dict(collections.Counter(r['bucket'] for r in rows)))
bad=[r['person_id'] for r in rows if 'http' not in r['why_selected']]
print("rows with NO membership URL:", bad or "none")
seen=collections.Counter(r['name'].strip() for r in rows)
print("duplicate names in draw:", [n for n,c in seen.items() if c>1] or "none")
PY
