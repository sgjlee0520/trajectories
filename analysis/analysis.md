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

**1 of 10 rows excluded (10.0%).** Excluded rows appear in no other table on this page, so a bias in what gets excluded is only visible here.

| Reason | n |
|---|---|
| crossing_undatable | 1 |

| Cross-cut | included | excluded | exclusion rate |
|---|---|---|---|
| US | 5 | 0 | 0.0% |
| non-US | 4 | 1 | 20.0% |
| women | 4 | 0 | 0.0% |
| men | 5 | 1 | 16.7% |
| bucket: consumer_retail_industrial | 1 | 1 | 50.0% |
| bucket: hardware_deeptech | 1 | 0 | 0.0% |
| bucket: investors_finance | 1 | 0 | 0.0% |
| bucket: media_creators | 1 | 0 | 0.0% |
| bucket: science_research | 1 | 0 | 0.0% |
| bucket: software_internet | 3 | 0 | 0.0% |
| bucket: trade_import_logistics | 1 | 0 | 0.0% |

Era is not audited here: it derives from the hit year, which an excluded row usually lacks. Judging a discarded row's era is a human call, not something to infer.

## Medians withheld

**Revenue-strict n = 4 of the 30-row floor.** Every median, CI, and slice is withheld until the floor is reached, per the pre-registered stopping rule.

This is deliberate rather than a missing feature. Watching the median across waves and stopping when it looks settled stops preferentially on waves where noise was small, which produces a figure that appears more precise than it is. Seeing the number early is the failure, so the number is not printed.

| Progress | n |
|---|---|
| revenue-strict rows | 4 |
| included rows | 9 |
| floor | 30 |

