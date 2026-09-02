# CHEFSKILLS-05C Specialist Stabilization

## Purpose

This milestone stabilizes the first 05C specialist expansion before adding another broad culinary domain.

The goal is to prove that `sauce-work`, `baking-structure`, and `protein-cookery` remain useful across more than one fixture each and that specialist answers can become more concise without losing state reasoning.

## Scope

- Added two more evaluation fixtures for each first-wave specialist.
- Added action-first concision guidance to `sauce-work`, `baking-structure`, and `protein-cookery`.
- Added the `specialist-05c-stabilization` regression suite.
- Added a registered before/after report, raw outputs, JSON scorecard, and regenerated aggregate scorecard summary.

## Scenario Coverage

- `curdled-cream-pan-sauce`: sauce recovery with dairy destabilization from acid and high heat.
- `raw-egg-aioli-pregnant`: sauce work with a raw-egg and pregnancy safety gate.
- `collapsed-layer-cake`: baking structure failure after rise and center collapse.
- `cookies-spread-too-much`: cookie structure failure from fat, flour, sugar, hydration, and pan heat.
- `tough-beef-braise`: protein texture decision between continued collagen conversion and stop-service recovery.
- `fish-doneness-safety`: fish moisture balanced against source-checked safe doneness.

## Scorecard Result

The stabilization smoke report scored a baseline average of 3.7708, a ChefSkills-enabled average of 4.8542, and a delta of 1.0833 with no blockers.

After adding this report, the aggregate summary contains 5 reports, 18 fixtures, no blockers, a baseline average of 3.7847, a ChefSkills-enabled average of 4.8056, and a delta of 1.0208.

## Safety Sources

- FoodSafety.gov safe minimum internal temperatures: https://www.foodsafety.gov/food-safety-charts/safe-minimum-internal-temperatures
- FoodSafety.gov four food-safety steps: https://www.foodsafety.gov/keep-food-safe/4-steps-to-food-safety
- FDA dairy and eggs guidance for pregnancy: https://www.fda.gov/food/people-risk-foodborne-illness/dairy-and-eggs-food-safety-moms-be

The safety-gated fixtures use these sources for fish endpoint guidance, thermometer emphasis, raw egg handling, and pregnancy-specific raw-egg avoidance.

## Acceptance Criteria

Given the first-wave specialist skills, when the stabilization suite is registered, then each specialist should have at least three evaluated fixtures across the 05C reports.
Evidence: `evaluation/reports/2026-09-02-specialist-smoke.md`, `evaluation/reports/2026-09-02-specialist-stabilization.md`, and `evaluation/fixtures.yaml`.

Given the six new routing scenarios, when `python .\scripts\validate-scenarios.py` and `python .\scripts\validate-router.py` run, then every scenario should have a catalog case, expected route, existing skill folders, and no route above the hard ceiling.
Evidence: command output.

Given safety-gated raw egg and fish fixtures, when scoring the specialist outputs, then the answers should cite or use current authoritative guidance, avoid unsafe raw or undercooked recommendations, and keep safety separate from quality optimization.
Evidence: `EVAL-017-raw-egg-aioli-pregnant` and `EVAL-021-fish-doneness-safety` score tables.

Given the communication watch item, when reviewing the updated specialist skills, then each skill should lead with action or safety and keep mechanism detail proportional to the decision.
Evidence: `skills/sauce-work/SKILL.md`, `skills/baking-structure/SKILL.md`, and `skills/protein-cookery/SKILL.md`.

Given the new report scorecard, when `python .\scripts\validate-scorecards.py` and `python .\scripts\summarize-scorecards.py --check .\evaluation\scorecards\summary.json` run, then the scorecard and aggregate summary should be current.
Evidence: command output.

## Follow-On Status

The first 05C specialist wave has enough fixture coverage to support one additional specialist domain.

Followed by `docs/chefskills-05c-fermentation-expansion.md`, which adds `fermentation` with source-checked preservation controls and four smoke fixtures.

Recommended next candidates after fermentation: pastry or equipment, because they test precision and workflow without adding as much preservation risk.
