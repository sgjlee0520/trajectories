# Apprenticeship Trajectories

Measures years from career start to first meaningful hit across a
quota-balanced sample of outlier achievers.

Read `docs/superpowers/specs/2026-07-31-apprenticeship-trajectories-design.md`
first. `frame.md` is frozen and must not be edited after wave 1.

## Run the tests

    python3 -m unittest discover -s tests -t . -v

## Validate the collected data

    python3 -m src.schema data/anchors.csv

## Compute clocks and build the report

    python3 -m src.clocks data/anchors.csv analysis/clocks.csv
    python3 -m src.report data/anchors.csv analysis/clocks.csv analysis/analysis.md

## Check the stopping rule

    python3 -m src.stats analysis/clocks.csv

No dependencies. Python 3.9 stdlib only.
