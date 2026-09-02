# CHEFSKILLS-05C Specialist Expansion

## Purpose

This milestone starts limited specialist expansion after the foundation scorecards showed stable routing, no blockers, and consistent state-reasoning gains.

The first expansion intentionally adds a small set of high-value specialists rather than a broad cuisine or recipe corpus.

## Skills Added

- `sauce-work`: emulsions, reductions, pan sauces, gravies, starch thickening, finishing, scaling, holding, and sauce recovery.
- `baking-structure`: gluten, starch, hydration, binders, leavening, fat, pan geometry, doneness cues, and texture failure recovery.
- `protein-cookery`: doneness, carryover, searing, braising, moisture control, resting, and safety-aware protein handling.

## Routing Coverage

- `split-pan-sauce` routes to `chef-core`, `sauce-work`, `culinary-reasoning`, and `cooking-techniques`.
- `dense-banana-bread` routes to `chef-core`, `baking-structure`, `culinary-reasoning`, and `ingredient-knowledge`.
- `dry-chicken-breast` routes to `chef-core`, `protein-cookery`, `culinary-reasoning`, `cooking-techniques`, and `food-safety`.

The dry chicken case uses the hard five-skill ceiling because it spans protein texture, method, recovery, and poultry safety.

## Evaluation Coverage

- Added fixtures `EVAL-013` through `EVAL-015`.
- Added the `specialist-05c-smoke` regression suite.
- Added raw baseline and ChefSkills-enabled outputs under `evaluation/runs/2026-09-02-specialist-smoke/`.
- Added the scored report `evaluation/reports/2026-09-02-specialist-smoke.md`.
- Added the JSON scorecard `evaluation/scorecards/2026-09-02-specialist-smoke.json`.

## Scorecard Result

The specialist smoke report scored a baseline average of 3.8750, a ChefSkills-enabled average of 4.8750, and a delta of 1.0000 with no blockers.

After adding the specialist report, the aggregate summary contains 4 reports, 12 fixtures, no blockers, a baseline average of 3.7917, a ChefSkills-enabled average of 4.7813, and a delta of 0.9896.

## Safety Source

The protein fixture uses source-checked poultry endpoint guidance from FoodSafety.gov:

https://www.foodsafety.gov/food-safety-charts/safe-minimum-internal-temperatures

As of the source page reviewed on 2024-11-21, FoodSafety.gov lists chicken and other poultry at 165 F (74 C) by food thermometer.

## Acceptance Criteria

Given the new specialist skills, when `python .\scripts\validate-skill-files.py` runs, then all skill files should have valid frontmatter, references, output contracts, and OpenAI interface metadata.
Evidence: command output.

Given the specialist routing scenarios, when `python .\scripts\validate-scenarios.py` and `python .\scripts\validate-router.py` run, then the expected routes should match the routing catalog and remain within the hard skill ceiling.
Evidence: command output.

Given the new specialist fixtures, when `python .\scripts\validate-evaluation.py` runs, then each fixture should reference a known scenario, route, state example, and regression suite.
Evidence: command output.

Given the specialist scorecard, when `python .\scripts\validate-scorecards.py` and `python .\scripts\summarize-scorecards.py --check .\evaluation\scorecards\summary.json` run, then the report scorecard and aggregate summary should be current.
Evidence: command output.

## Follow-On Status

- Followed by `docs/chefskills-05c-specialist-stabilization.md`, which adds two more fixtures per first-wave specialist.
- Candidate next specialists: fermentation, pastry, equipment, service timing, costing, or cuisine-specific reasoning.
- Continue watching communication scores because specialist answers can become too dense, even after action-first guidance.
