#!/bin/bash
# Merge batch files into anchors.csv, with pre-flight checks.
#   scripts/merge-batches.sh data/w9-*.csv
set -u
cd "$(dirname "$0")/.."
python3 - "$@" <<'PY'
import csv, sys, os
files=sys.argv[1:]
cols=list(csv.DictReader(open('data/anchors.csv')).fieldnames)
main=list(csv.DictReader(open('data/anchors.csv')))
existing={r['person_id'] for r in main}
incoming=[]; bad=[]
for f in files:
    if not os.path.exists(f): bad.append('%s MISSING' % f); continue
    rd=csv.DictReader(open(f))
    if list(rd.fieldnames)!=cols:
        bad.append('%s COLUMN MISMATCH' % f); continue
    incoming += list(rd)
ids=[r['person_id'] for r in incoming]
dupes=[i for i in set(ids) if ids.count(i)>1]
clash=[i for i in ids if i in existing]
if bad or dupes or clash:
    print('REFUSING TO MERGE'); print(' problems:', bad or '-')
    print(' duplicates within incoming:', dupes or '-')
    print(' clashes with anchors.csv:', clash or '-')
    sys.exit(1)
incoming.sort(key=lambda r:int(r['person_id'][1:]))
merged=main+incoming
with open('data/anchors.csv','w',newline='') as h:
    w=csv.DictWriter(h,fieldnames=cols); w.writeheader(); w.writerows(merged)
print('merged %d + %d = %d rows' % (len(main),len(incoming),len(merged)))
PY
python3 -m src.schema data/anchors.csv
