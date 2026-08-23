# Open for PI

Collector stopped at `STOP: True`. These are not collection tasks. They need a
methodology call before or during the paper.

## 1. Is ARR calendar-year revenue?

p211 Alex Solomon / PagerDuty is dated 2013-2014 from ARR. The wave 9 second
pass refused ARR, used GAAP, and bounded 2009-2017. The spans overlap, so the
audit did not contradict and the row was not rewritten.

If ARR is not `rev10`, several SaaS rows in this study may be dated the same
way. Collector did not sweep them.

## 2. Rescue the miss rows, or leave them?

Standing rescue candidates, first pass stands in the data:

- p183 Neal O'Mara / HelloSign `2011-2019` (wave 7–8 miss)
- p214 Bill Clerico / WePay `2008-2017` (wave 9 miss)
- p233 Olivia Dean / Reason to Stay `2018-2019` (wave 9 miss)

None of these can un-fire the stopping rule: p183 and p214 are already in the
revenue-strict set; p233 is `aud1m`. Rescue would only tighten or drop them.

## 3. `docs/OPEN-QUESTIONS.md` Q1–Q7

Still unanswered. Q1 (Alfred Mann) and Q5 (Alpaca founding year) can change
whether a row is in or out. Q5 in particular: on a 2013 founding p141's
2015-2024 bound exceeds ten years and the row should have been excluded.

## 4. The stopping rule fired on the boundary

CI half-width is **exactly 1.00**. The test is `ci_half_width > 1.0`, so 1.00
stops. Collector has no authority to keep going because the number looks
exactly-on-the-line.
