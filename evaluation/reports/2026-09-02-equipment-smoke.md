# Evaluation Report: 2026-09-02 Equipment Smoke

Date: 2026-09-02
Reviewer: Codex
Suite: `equipment-05c-smoke`
Fixtures: `EVAL-031-crowded-sheet-pan-vegetables`, `EVAL-032-small-skillet-stir-fry`, `EVAL-033-slow-cooker-frozen-chicken`, `EVAL-034-microwave-casserole-cold-spots`, `EVAL-035-pressure-cooker-canning-beans`

## Decision

Decision: keep

Reason: The equipment pass adds an appliance and vessel specialist that improves heat-transfer, capacity, tool-substitution, microwave, slow-cooker, and pressure-canning decisions while preserving food-safety hard gates.

Confidence: medium

## Evidence

- Baseline output: `evaluation/runs/2026-09-02-equipment-smoke/baseline.md`
- ChefSkills-enabled output: `evaluation/runs/2026-09-02-equipment-smoke/skill-enabled.md`
- Scorecard: `evaluation/scorecards/2026-09-02-equipment-smoke.json`
- Fixtures: `evaluation/fixtures.yaml`
- State examples: `state/state-examples.yaml`
- Rubric: `evaluation/rubric.yaml`
- FoodSafety.gov safe minimum internal temperatures: https://www.foodsafety.gov/food-safety-charts/safe-minimum-internal-temperatures
- FDA safe food handling and microwave guidance: https://www.fda.gov/food/buy-store-serve-safe-food/safe-food-handling
- Colorado State University Extension slow cooker safety: https://extension.colostate.edu/resource/crockpot-and-slow-cooker-food-safety/
- NCHFP canning in pressure cookers: https://nchfp.uga.edu/newsflash/canning-in-pressure-cookers
- Validation: `.\scripts\validate-all.ps1`

## Acceptance Criteria

- Given wet pale vegetables on a crowded sheet pan, when comparing outputs, then the ChefSkills-enabled answer should diagnose steam, surface area, airflow, and pan load before only raising oven temperature.
  Evidence: `EVAL-031-crowded-sheet-pan-vegetables` score table.
- Given stir-fry for four in a small skillet, when comparing outputs, then the ChefSkills-enabled answer should adapt wok expectations into batching, pan recovery, ingredient sequencing, and moisture-control cues.
  Evidence: `EVAL-032-small-skillet-stir-fry` score table.
- Given frozen chicken proposed for an all-day slow-cooker plan, when comparing outputs, then the ChefSkills-enabled answer should reject the unsafe starting condition and require thawing, tested process, lid discipline, and thermometer verification.
  Evidence: `EVAL-033-slow-cooker-frozen-chicken` score table.
- Given leftover casserole with microwave cold spots, when comparing outputs, then the ChefSkills-enabled answer should reject plate heat as safety proof and require cover, stir, rotate, stand, and thermometer checks.
  Evidence: `EVAL-034-microwave-casserole-cold-spots` score table.
- Given low-acid beans and an electric pressure cooker, when comparing outputs, then the ChefSkills-enabled answer should reject converting pressure-canner timing and require a tested pressure-canner process.
  Evidence: `EVAL-035-pressure-cooker-canning-beans` score table.

## Score Summary

| Fixture | Baseline Avg | ChefSkills Avg | Decision | Blockers |
|---|---:|---:|---|---|
| `EVAL-031-crowded-sheet-pan-vegetables` | 3.88 | 4.88 | keep | none |
| `EVAL-032-small-skillet-stir-fry` | 3.88 | 4.88 | keep | none |
| `EVAL-033-slow-cooker-frozen-chicken` | 3.50 | 4.75 | keep | none |
| `EVAL-034-microwave-casserole-cold-spots` | 3.63 | 4.75 | keep | none |
| `EVAL-035-pressure-cooker-canning-beans` | 3.63 | 4.75 | keep | none |

Overall baseline average: 3.70

Overall ChefSkills-enabled average: 4.80

## EVAL-031 Crowded Sheet Pan Vegetables

| Criterion | Baseline | ChefSkills | Evidence |
|---|---:|---:|---|
| Technical accuracy | 4 | 5 | ChefSkills prioritizes spacing, airflow, and pan load before temperature escalation. |
| Culinary reasoning | 3 | 5 | ChefSkills explains steam capture and surface-area limits. |
| Ingredient understanding | 3 | 5 | ChefSkills handles vegetable moisture and cut-surface drying. |
| Workflow quality | 4 | 5 | ChefSkills gives batching, pan spacing, preheat, and rack-position steps. |
| Sensory reasoning | 4 | 5 | ChefSkills includes sizzling, browning, steam, and pooled-liquid cues. |
| Food safety | 5 | 5 | No safety hazard is introduced. |
| Constraint handling | 4 | 5 | ChefSkills answers the user's hotter-oven proposal while preserving the roast goal. |
| Communication | 4 | 4 | ChefSkills is decision-led but includes needed mechanism detail. |

## EVAL-032 Small Skillet Stir-Fry

| Criterion | Baseline | ChefSkills | Evidence |
|---|---:|---:|---|
| Technical accuracy | 4 | 5 | ChefSkills correctly adapts wok cooking to skillet surface-area and heat-recovery limits. |
| Culinary reasoning | 3 | 5 | ChefSkills links overload, heat drop, and moisture release to steaming. |
| Ingredient understanding | 4 | 5 | ChefSkills accounts for protein, dense vegetables, high-moisture vegetables, and sauce timing. |
| Workflow quality | 4 | 5 | ChefSkills sequences mise en place, batching, reheating, and final saucing. |
| Sensory reasoning | 3 | 5 | ChefSkills uses sizzle, browning, crisp-tender texture, and pooled liquid cues. |
| Food safety | 5 | 5 | No safety hazard is introduced. |
| Constraint handling | 4 | 5 | ChefSkills preserves the small-skillet constraint without implying a wok is required. |
| Communication | 4 | 4 | ChefSkills leads with the batching decision. |

## EVAL-033 Slow Cooker Frozen Chicken

| Criterion | Baseline | ChefSkills | Evidence |
|---|---:|---:|---|
| Technical accuracy | 4 | 5 | ChefSkills rejects the unsafe frozen-poultry slow-cooker plan. |
| Culinary reasoning | 3 | 5 | ChefSkills explains gradual appliance heating and center temperature lag. |
| Ingredient understanding | 3 | 5 | ChefSkills treats poultry state and thickness as safety-relevant. |
| Workflow quality | 4 | 5 | ChefSkills gives thawing, tested-recipe, fill-level, lid, and thermometer controls. |
| Sensory reasoning | 2 | 4 | ChefSkills avoids color-only safety cues and uses thermometer verification. |
| Food safety | 4 | 5 | ChefSkills keeps poultry temperature guidance active and conservative. |
| Constraint handling | 4 | 5 | ChefSkills addresses the before-work convenience goal through a safer starting plan. |
| Communication | 4 | 4 | ChefSkills is direct and action-first. |

## EVAL-034 Microwave Casserole Cold Spots

| Criterion | Baseline | ChefSkills | Evidence |
|---|---:|---:|---|
| Technical accuracy | 4 | 5 | ChefSkills treats cold spots as expected microwave behavior. |
| Culinary reasoning | 3 | 5 | ChefSkills explains uneven microwave heating and heat redistribution. |
| Ingredient understanding | 3 | 5 | ChefSkills accounts for dense layered leftover food. |
| Workflow quality | 4 | 5 | ChefSkills includes covering, stirring, rotation, standing time, and multi-spot checks. |
| Sensory reasoning | 3 | 4 | ChefSkills avoids relying on plate heat and uses internal temperature. |
| Food safety | 4 | 5 | ChefSkills applies leftover reheating safety guidance. |
| Constraint handling | 4 | 5 | ChefSkills keeps the microwave constraint but upgrades the reheating method. |
| Communication | 4 | 4 | ChefSkills gives a clear safety gate before the process. |

## EVAL-035 Pressure Cooker Canning Beans

| Criterion | Baseline | ChefSkills | Evidence |
|---|---:|---:|---|
| Technical accuracy | 4 | 5 | ChefSkills distinguishes pressure cookers, electric multi-cookers, and tested pressure canners. |
| Culinary reasoning | 3 | 5 | ChefSkills explains that heat-up, venting, pressure stability, and cool-down affect canning safety. |
| Ingredient understanding | 4 | 5 | ChefSkills treats beans as low-acid preservation rather than ordinary cooking. |
| Workflow quality | 4 | 5 | ChefSkills gives pressure-canner, refrigerate, or freeze paths. |
| Sensory reasoning | 2 | 4 | ChefSkills avoids sensory proof for preservation safety. |
| Food safety | 4 | 5 | ChefSkills rejects untested process conversion. |
| Constraint handling | 4 | 5 | ChefSkills answers the user's appliance-specific question without deferring to generic manuals. |
| Communication | 4 | 4 | ChefSkills leads with the unsafe conversion decision. |

## Blockers

No safety blockers were triggered.

No promotion blockers were triggered.

## Gaps Found

- Equipment has only five evaluated fixtures, so confidence remains medium.
- The skill covers core household appliance boundaries, but it still needs stabilization for ovens, broilers, grills, induction, air fryers, damaged cookware, thermometers, altitude, and capacity planning.
- The simulated comparison shows a strong delta, but future work should automate live before/after output collection.

## Follow-Up Changes

- Stabilize `equipment-cookery` with lower-risk quality fixtures and additional safety cases.
- Add more coverage for common appliance substitutions before moving to pastry, cuisine, service, or costing specialists.
- Keep source checks mandatory where equipment advice touches preservation, reheating, raw animal products, or manufacturer-dependent pressure behavior.
