# CHEFSKILLS-05C Equipment Stabilization

## Purpose

This milestone stabilizes `equipment-cookery` after the initial equipment smoke pass.

The goal is to make equipment guidance broad enough for public-alpha readiness without opening another large specialist track. The pass adds coverage for ovens, broilers, grills, induction, air fryers, damaged or incompatible cookware, thermometers, altitude, and capacity planning.

## Scope

- Strengthen `equipment-cookery` for direct heat, radiant heat, vessel compatibility, thin-pan scorching, airflow limits, grill flare-ups, and high-altitude pressure cooking.
- Expand the equipment checklist with source-backed safety boundaries for glass under broilers, damaged vessels, air-fryer poultry, grill poultry, high-elevation cooking, and pressure-cooker max-fill behavior.
- Add `damaged_or_incompatible_cookware` to safety preflight routing so physical equipment hazards can activate `food-safety`.
- Keep Michelin / fine-dining intelligence and Canadian commercial food safety as future tracks until public-alpha gates are in place.

## Scenario Coverage

- `dark-pan-cookie-browning` routes to `chef-core`, `equipment-cookery`, `baking-structure`, and `culinary-reasoning`.
- `glass-broiler-lasagna` routes to `chef-core`, `equipment-cookery`, `food-safety`, and `cooking-techniques`.
- `crowded-air-fryer-wings` routes to `chef-core`, `equipment-cookery`, `food-safety`, `protein-cookery`, and `cooking-techniques`.
- `induction-thin-pan-scorching` routes to `chef-core`, `equipment-cookery`, `sauce-work`, `culinary-reasoning`, and `cooking-techniques`.
- `high-altitude-pressure-cooker-beans` routes to `chef-core`, `equipment-cookery`, `ingredient-knowledge`, and `cooking-techniques`.
- `grill-flare-up-chicken-thighs` routes to `chef-core`, `equipment-cookery`, `protein-cookery`, `food-safety`, and `cooking-techniques`.

## Evaluation Coverage

- Added fixtures `EVAL-036` through `EVAL-041`.
- Added the `equipment-05c-stabilization` regression suite.
- Added raw baseline and ChefSkills-enabled outputs under `evaluation/runs/2026-09-03-equipment-stabilization/`.
- Added the scored report `evaluation/reports/2026-09-03-equipment-stabilization.md`.
- Added the JSON scorecard `evaluation/scorecards/2026-09-03-equipment-stabilization.json`.

## Scorecard Result

The equipment stabilization report scored a baseline average of 3.7292, a ChefSkills-enabled average of 4.7708, and a delta of 1.0417 with no blockers.

After adding this report, the aggregate summary contains 9 reports, 38 fixtures, no blockers, a baseline average of 3.7599, a ChefSkills-enabled average of 4.8059, and a delta of 1.0461.

The aggregate readiness status is now `ready_for_public_alpha_readiness_work`.

## Safety Sources

- FoodSafety.gov safe minimum internal temperatures: https://www.foodsafety.gov/food-safety-charts/safe-minimum-internal-temperatures
- USDA FSIS air fryers and food safety: https://www.fsis.usda.gov/food-safety/safe-food-handling-and-preparation/food-safety-basics/air-fryers-and-food-safety
- USDA FSIS grilling and food safety: https://www.fsis.usda.gov/food-safety/safe-food-handling-and-preparation/food-safety-basics/grilling-and-food-safety
- Colorado State University Extension high elevation food preparation: https://extension.colostate.edu/resource/high-elevation-food-preparation-guide/
- Colorado State University Extension high-elevation pressure-cooker beans: https://extension.colostate.edu/resource/cooking-beans-at-high-elevation-using-an-electric-pressure-cooker-2/
- Pyrex use and care FAQ for glass direct heat and damaged glassware: https://pyrexhome.com/pages/frequently-asked-questions

The safety-gated fixtures use these sources for poultry thermometer endpoints, direct broiler heat on glass, damaged glassware, air-fryer airflow limits, grill flare-up handling, high-elevation cooking adjustments, pressure-cooker foaming food limits, and post-cooking handling.

## Acceptance Criteria

Given the six equipment stabilization scenarios, when `python .\scripts\validate-scenarios.py` and `python .\scripts\validate-router.py` run, then every scenario should have an expected route, catalog case, known skill folders, and no route above the hard ceiling.
Evidence: command output.

Given the new equipment state examples and fixtures, when `python .\scripts\validate-state.py` and `python .\scripts\validate-evaluation.py` run, then every fixture should reference a known scenario, state example, expected route, and regression suite.
Evidence: command output.

Given broiler glassware, raw poultry, air-fryer crowding, grill flare-ups, and high-altitude pressure-cooker cases, when scoring the skill-enabled outputs, then the answers should activate safety where required, reject unsafe equipment use, and distinguish quality cues from thermometer or manufacturer-dependent safety checks.
Evidence: `EVAL-037`, `EVAL-038`, `EVAL-040`, and `EVAL-041` score tables.

Given lower-risk equipment quality cases, when scoring the skill-enabled outputs, then the answers should explain heat transfer, pan material, rack position, airflow, induction response, and verification cues rather than giving time-only fixes.
Evidence: `EVAL-036` and `EVAL-039` score tables.

Given the new equipment stabilization scorecard, when `python .\scripts\validate-scorecards.py` and `python .\scripts\summarize-scorecards.py --check .\evaluation\scorecards\summary.json` run, then the scorecard and aggregate summary should be current and the readiness state should advance to public-alpha readiness work.
Evidence: command output.

## Follow-On Status

Recommended next milestone: `CHEFSKILLS-06 Public Alpha Readiness Workflow`.

The next pass should add repository operations, public documentation, evaluation credibility labeling, publication audits, and release notes before changing repository visibility.
