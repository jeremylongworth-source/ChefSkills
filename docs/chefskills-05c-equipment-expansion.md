# CHEFSKILLS-05C Equipment Expansion

## Purpose

This milestone adds `equipment-cookery` as the next specialist domain after fermentation stabilization.

Equipment was selected because it stresses heat transfer, vessel geometry, surface area, appliance behavior, batch sizing, airflow, microwave unevenness, slow-cooker heating, pressure equipment boundaries, and tool substitutions without moving immediately into another broad cuisine or service domain.

## Skill Added

- `equipment-cookery`: planning, adapting, troubleshooting, and safety-gating cooking around kitchen equipment, appliances, vessels, heat transfer, capacity, airflow, pressure, microwaves, slow cookers, and tool substitutions.

## Routing Coverage

- `crowded-sheet-pan-vegetables` routes to `chef-core`, `equipment-cookery`, `culinary-reasoning`, and `cooking-techniques`.
- `small-skillet-stir-fry` routes to `chef-core`, `equipment-cookery`, `cooking-techniques`, and `ingredient-knowledge`.
- `slow-cooker-frozen-chicken` routes to `chef-core`, `equipment-cookery`, `food-safety`, and `protein-cookery`.
- `microwave-casserole-cold-spots` routes to `chef-core`, `equipment-cookery`, `food-safety`, and `cooking-techniques`.
- `pressure-cooker-canning-beans` routes to `chef-core`, `equipment-cookery`, and `food-safety`.

## Evaluation Coverage

- Added fixtures `EVAL-031` through `EVAL-035`.
- Added the `equipment-05c-smoke` regression suite.
- Added raw baseline and ChefSkills-enabled outputs under `evaluation/runs/2026-09-02-equipment-smoke/`.
- Added the scored report `evaluation/reports/2026-09-02-equipment-smoke.md`.
- Added the JSON scorecard `evaluation/scorecards/2026-09-02-equipment-smoke.json`.

## Scorecard Result

The equipment smoke report scored a baseline average of 3.7000, a ChefSkills-enabled average of 4.8000, and a delta of 1.1000 with no blockers.

After adding this report, the aggregate summary contains 8 reports, 32 fixtures, no blockers, a baseline average of 3.7656, a ChefSkills-enabled average of 4.8125, and a delta of 1.0469.

## Safety Sources

- FoodSafety.gov safe minimum internal temperatures: https://www.foodsafety.gov/food-safety-charts/safe-minimum-internal-temperatures
- FDA safe food handling and microwave guidance: https://www.fda.gov/food/buy-store-serve-safe-food/safe-food-handling
- Colorado State University Extension slow cooker safety: https://extension.colostate.edu/resource/crockpot-and-slow-cooker-food-safety/
- NCHFP canning in pressure cookers: https://nchfp.uga.edu/newsflash/canning-in-pressure-cookers

The safety-gated fixtures use these sources for thermometer endpoints, leftover reheating expectations, microwave cold-spot controls, slow-cooker thawing and lid/fill guidance, and pressure-cooker versus pressure-canner boundaries.

## Acceptance Criteria

Given the `equipment-cookery` skill, when `python .\scripts\validate-skill-files.py` runs, then the skill should have valid frontmatter, references, output contract, and OpenAI interface metadata.
Evidence: command output.

Given the five equipment scenarios, when `python .\scripts\validate-scenarios.py` and `python .\scripts\validate-router.py` run, then every scenario should have a catalog case, expected route, known skill folders, and no route above the hard ceiling.
Evidence: command output.

Given equipment state examples and fixtures, when `python .\scripts\validate-state.py` and `python .\scripts\validate-evaluation.py` run, then every fixture should reference a known scenario, state example, expected route, and regression suite.
Evidence: command output.

Given slow-cooker, microwave, and pressure-canning fixtures, when scoring the skill-enabled outputs, then the answers should keep food safety active, reject unsafe equipment substitutions, and verify with thermometer or tested-process guidance where required.
Evidence: `EVAL-033` through `EVAL-035` score tables.

Given sheet-pan and skillet fixtures, when scoring the skill-enabled outputs, then the answers should explain heat transfer, surface area, airflow, moisture, capacity, and batch sequencing rather than giving time-only or temperature-only advice.
Evidence: `EVAL-031` and `EVAL-032` score tables.

Given the new equipment scorecard, when `python .\scripts\validate-scorecards.py` and `python .\scripts\summarize-scorecards.py --check .\evaluation\scorecards\summary.json` run, then the scorecard and aggregate summary should be current.
Evidence: command output.

## Follow-On Status

Followed by `CHEFSKILLS-05C Equipment Specialist Stabilization`.

That pass added lower-risk equipment quality fixtures and additional safety cases for ovens, broilers, grills, induction, air fryers, damaged cookware, thermometer use, altitude, and capacity planning before moving the roadmap to public-alpha readiness work.
