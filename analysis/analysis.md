# Apprenticeship Trajectories — Analysis

## Survivorship caveat

This sample is conditioned on the outcome. Everyone in it succeeded. The buckets are filled from lists that select on extreme outcomes — Forbes, Midas, Nobel, Hurun — so there is nobody here who worked at it for twelve years and never crossed. Those people exist in enormous numbers; no list samples them.

So if the median comes back at 8 years, the sentence it supports is:

> **Among people who eventually hit, the middle one took about 8 years.**

The sentence it does **not** support:

> ~~If I start now, I have about a 50% chance of hitting within 8 years.~~

The second needs a denominator — everyone who started — and this dataset has no denominator at all. It is like timing how long lottery winners held their tickets: a real number, correctly computed, that says nothing about whether buying tickets is a good plan.

What the number is good for is **duration, given success**: how long the middle winner spent before the first real traction. That is worth knowing, and it is not a forecast.

Eleven known biases, their directions, and what mitigates each are catalogued in `docs/BIASES.md`. The two strongest identified effects both push the median **short**, so read it as a floor rather than a typical value.

## Exclusion audit

**15 of 85 rows excluded (17.6%).** Excluded rows appear in no other table on this page, so a bias in what gets excluded is only visible here.

| Reason | n |
|---|---|
| crossing_undatable | 13 |
| roster_unverified | 2 |

| Cross-cut | included | excluded | exclusion rate |
|---|---|---|---|
| US | 25 | 5 | 16.7% |
| non-US | 45 | 10 | 18.2% |
| women | 26 | 6 | 18.8% |
| men | 44 | 9 | 17.0% |
| bucket: consumer_retail_industrial | 8 | 3 | 27.3% |
| bucket: hardware_deeptech | 12 | 1 | 7.7% |
| bucket: healthcare_biotech | 4 | 5 | 55.6% |
| bucket: investors_finance | 7 | 2 | 22.2% |
| bucket: media_creators | 7 | 1 | 12.5% |
| bucket: science_research | 10 | 0 | 0.0% |
| bucket: software_internet | 19 | 2 | 9.5% |
| bucket: trade_import_logistics | 3 | 1 | 25.0% |

Era is not audited here: it derives from the hit year, which an excluded row usually lacks. Judging a discarded row's era is a human call, not something to infer.

## Medians withheld

**Revenue-strict n = 28 of the 30-row floor.** Every median, CI, and slice is withheld until the floor is reached, per the pre-registered stopping rule.

This is deliberate rather than a missing feature. Watching the median across waves and stopping when it looks settled stops preferentially on waves where noise was small, which produces a figure that appears more precise than it is. Seeing the number early is the failure, so the number is not printed.

| Progress | n |
|---|---|
| revenue-strict rows | 28 |
| included rows | 70 |
| floor | 30 |

