# CHEFSKILLS-05C Fermentation Expansion

## Purpose

This milestone adds `fermentation` as the next specialist domain after the first-wave 05C specialists stabilized.

Fermentation was selected because it stresses safety gates, preservation workflow, salt and pH assumptions, time-temperature reasoning, gas pressure, spoilage recognition, and source-check discipline.

## Skill Added

- `fermentation`: planning, adapting, troubleshooting, and safety-gating home fermentation for vegetables, sauces, kombucha, brines, pH, salt, acidity, gas pressure, spoilage, and storage.

## Routing Coverage

- `low-salt-sauerkraut` routes to `chef-core`, `fermentation`, `food-safety`, `ingredient-substitution`, and `ingredient-knowledge`.
- `soft-fermented-pickles` routes to `chef-core`, `fermentation`, `food-safety`, and `culinary-reasoning`.
- `kombucha-bottle-pressure` routes to `chef-core`, `fermentation`, `food-safety`, and `culinary-reasoning`.
- `hot-sauce-fermentation-plan` routes to `chef-core`, `fermentation`, `food-safety`, and `ingredient-knowledge`.

Existing catalog-only fermentation examples also route through `fermentation`.

## Evaluation Coverage

- Added fixtures `EVAL-022` through `EVAL-025`.
- Added the `fermentation-05c-smoke` regression suite.
- Added raw baseline and ChefSkills-enabled outputs under `evaluation/runs/2026-09-02-fermentation-smoke/`.
- Added the scored report `evaluation/reports/2026-09-02-fermentation-smoke.md`.
- Added the JSON scorecard `evaluation/scorecards/2026-09-02-fermentation-smoke.json`.

## Scorecard Result

The fermentation smoke report scored a baseline average of 3.7188, a ChefSkills-enabled average of 4.7813, and a delta of 1.0625 with no blockers.

After adding this report, the aggregate summary contains 6 reports, 22 fixtures, no blockers, a baseline average of 3.7727, a ChefSkills-enabled average of 4.8011, and a delta of 1.0284.

## Safety Sources

- NCHFP general fermenting guidance: https://nchfp.uga.edu/how/ferment/general-information-on-fermenting/
- NCHFP fermenting containers and brine coverage: https://nchfp.uga.edu/how/ferment/general-information-on-fermenting/suitable-containers-covers-and-weights-for-fermenting-food/
- NCHFP fermented-pickle troubleshooting: https://nchfp.uga.edu/how/ferment/general-information-on-fermenting/causes-and-possible-solutions-for-problems-with-fermented-pickles/
- NCHFP kombucha recipe and safety factors: https://nchfp.uga.edu/how/ferment/recipes/kombucha-tea/

The safety-gated fixtures use these sources for tested proportions, required salt boundaries, brine coverage, spoilage discard cues, kombucha pH/process controls, and sealed-bottle pressure warnings.

## Acceptance Criteria

Given the `fermentation` skill, when `python .\scripts\validate-skill-files.py` runs, then the skill should have valid frontmatter, references, output contract, and OpenAI interface metadata.
Evidence: command output.

Given the four fermentation scenarios, when `python .\scripts\validate-scenarios.py` and `python .\scripts\validate-router.py` run, then every scenario should have a catalog case, expected route, known skill folders, and no route above the hard ceiling.
Evidence: command output.

Given reduced-salt and spoilage fermentation fixtures, when scoring the skill-enabled outputs, then the answers should reject untested salt reduction, recommend discard for spoiled ferments, and avoid taste-testing or rinsing as safety fixes.
Evidence: `EVAL-022-low-salt-sauerkraut` and `EVAL-023-soft-fermented-pickles` score tables.

Given kombucha and hot-sauce fixtures, when scoring the skill-enabled outputs, then the answers should separate active fermentation from shelf-stable storage, identify pressure or spoilage hazards, and require tested proportions or source checks.
Evidence: `EVAL-024-kombucha-bottle-pressure` and `EVAL-025-hot-sauce-fermentation-plan` score tables.

Given the new fermentation scorecard, when `python .\scripts\validate-scorecards.py` and `python .\scripts\summarize-scorecards.py --check .\evaluation\scorecards\summary.json` run, then the scorecard and aggregate summary should be current.
Evidence: command output.

## Follow-On Status

Followed by `docs/chefskills-05c-fermentation-stabilization.md`, which adds lower-risk flavor, process, starter, temperature, and storage-boundary fixtures.

Recommended next candidate after fermentation stabilization: equipment. Fermentation already expanded the safety-heavy side of 05C, so the next domain should test heat-transfer and workflow breadth without adding as much preservation risk.
