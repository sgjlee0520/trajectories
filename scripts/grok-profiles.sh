#!/bin/bash
# Build data/profiles.csv from anchors notes plus gap research.
#   scripts/grok-profiles.sh <out.csv> <start_id> <end_id>
set -u
cd "$(dirname "$0")/.."
OUT="$1"; A="$2"; B="$3"
[ -f "$OUT" ] || echo "person_id,name,hit_entity,bucket,nationality,sex,highest_degree,field_of_study,institution,expertise,basis,source" > "$OUT"
PROMPT="$(cat docs/GROK-PROFILE-BRIEF.md)

---

# YOUR ASSIGNMENT

Working directory: $(pwd)
Write only to: $OUT  (header already present)

Do people **$A through $B inclusive**, in person_id order, from
\`data/anchors.csv\`. Read each person's \`notes\` column FIRST — most of what
you need is already there and was sourced when it was written.

Append each row as you finish it."
grok -p "$PROMPT" --always-approve --max-turns 300 2>&1 | tail -40
echo "=== DONE $OUT ==="
python3 -c "
import csv
r=list(csv.DictReader(open('$OUT')))
print('rows: %d' % len(r))
import collections
print('degree:', collections.Counter(x['highest_degree'] for x in r).most_common())
print('basis :', collections.Counter(x['basis'] for x in r).most_common())
"
