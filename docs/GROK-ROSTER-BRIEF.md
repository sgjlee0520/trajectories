# Roster brief for Grok — drawing a wave

You are drawing names for the next wave. You are NOT researching them; a later
batch does that. Your entire output is a set of roster rows, each with a URL
that names the person on a list.

`GROK-RESEARCH-BRIEF.md` sits beside this file. Its rules on sourcing, quoting,
and refusing to invent apply here in full. This brief adds the ones specific to
drawing.

## The two ways this step has gone wrong before

Both of these actually happened on this project. They are the reason the brief
is this prescriptive.

**1. Recalling, then verifying.** An agent thought of people it already knew,
then went and found list entries to justify them. Everything it produced had a
valid citation and the sample was still biased, because the recall happened
first and the citation was decoration. **You must enumerate the list and read
off it.** Open the ranking, walk it in its published order, and take entries in
that order. If you notice you thought of a name before you saw it on a list,
discard that name.

**2. Steering away from fame.** Told to avoid names it would have recalled, an
agent then rejected Peter Thiel, Vinod Khosla, and Jensen Huang from enumerated
lists as "too obvious." That is the same bias with its sign flipped, and it is
equally forbidden. **Prominence is not a criterion in either direction.** When
you are walking a list in rank order, a famous entry gets taken exactly like any
other. Do not skip it, and do not reach for it.

The only reasons to skip an entry are the four rejections in section 3.

## 1. How to walk a list

For each bucket in your assignment:

1. Open the source list named for that bucket and **enumerate it in its
   published order** — rank order for a ranking, year order for a prize.
2. Start at the top, or where a previous wave stopped if the assignment says so.
3. For each entry in order, apply the section-3 rejections. Take the first
   entries that survive, until the bucket's quota is filled.
4. Record where you stopped, so the next wave can resume from there.

Take them **in order**. Do not scan ahead for an interesting one, do not
rebalance the wave by country, era, or sex, and do not pick for a good story.

## 2. What a list entry must give you

A roster row needs a URL that **names this person** and shows their list
membership, plus the exact sentence or JSON field that does it. A list's
homepage is not confirmation (`GROK-RESEARCH-BRIEF.md` §5).

If you cannot get a page that names the person, that entry does not enter the
roster. Move to the next one; do not substitute a name you are confident about.

## 3. The only four reasons to reject an entry

1. **Already in the study.** `already-used.md` in this directory lists every
   person already drawn. Skip and continue.
2. **Same hit event as an existing row.** If the person's hit would be an entity
   in that file's entity list, they are one event with a row already present —
   `frame.md`, "One row per hit event". Co-founders of a company already in the
   study are the usual case. Skip and continue. A different **year** of the same
   prize is a different event and is fine.
3. **Wrong bucket.** The entry belongs to a different field than the one you are
   filling. Skip; do not reassign the bucket to make them fit.
4. **Not self-made where the list requires it.** Forbes lists are used at
   self-made score 6-10 / `selfMade: true`. An inheritor fails the frame.

**Nothing else is a reason to skip an entry.** Not obscurity, not fame, not
nationality, not sex, not era, not "we already have a lot of these", not a
hunch that the data will be hard to find. Difficulty of research is the next
batch's problem and is not yours to pre-empt — screening out hard-to-source
people is exactly how a sample gets biased toward the well-documented.

## 4. Output

Append to the assignment's output file, one row per person, in the column order
of `data/roster.csv`:

    person_id,name,bucket,source_list,country_primary,gender,why_selected

- `person_id` — as assigned, in order.
- `source_list` — the list name **exactly as it appears in `frame.md`**.
- `country_primary` — ISO-2 of where their career primarily ran.
- `gender` — `M` / `F`, from a source. This is a recorded covariate and is never
  a reason to pick or skip anyone.
- `why_selected` — the position in the list you took them from, then
  `Membership: <URL> (<the exact quoted sentence or JSON field naming them>)`.
  If you skipped entries to reach this one, say which and under which of the
  four rejections.

**Append each row as you finish it, never all at the end.** Wave 9 was drawn in
one batch write at the end of a twenty-minute run, which is the failure this
rule exists to prevent: an agent killed at minute nineteen leaves nothing.
Rows are knowable before the whole draw is: **finish a bucket, write that
bucket's rows, then walk the next list.** Do not hold rows back to write them
in id order at the end.

## 5. Your report

Per bucket: the list you walked, where you started, where you stopped, every
entry you skipped and under which rejection, and the rows you took.

Then, plainly: any point where you were tempted to depart from rank order, and
whether you did. If you took a name you had thought of before seeing it on a
list, say so — that row can be replaced, and a quiet one cannot.
