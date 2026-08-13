# Apprenticeship Trajectories

Measures years from career start to first meaningful hit across a
quota-balanced sample of outlier achievers.

Read `docs/superpowers/specs/2026-07-31-apprenticeship-trajectories-design.md`
first. `frame.md` is frozen and must not be edited after wave 1.

## Read this first

`docs/BIASES.md` — eleven known biases, each with its direction and what
mitigates it. The sample is extreme winners dated at a modest milestone; the
two strongest effects both push the median short, so it reads as a floor. The
people who worked twenty years and never crossed are absent by construction,
not by rarity.

## Run the tests

    python3 -m unittest discover -s tests -t . -v

## Validate the collected data

    python3 -m src.schema data/anchors.csv

## Compute clocks and build the report

    python3 -m src.clocks data/anchors.csv analysis/clocks.csv
    python3 -m src.report analysis/clocks.csv analysis/analysis.md

## Check the stopping rule

    python3 -m src.stats analysis/clocks.csv

No dependencies. Python 3.9 stdlib only.
