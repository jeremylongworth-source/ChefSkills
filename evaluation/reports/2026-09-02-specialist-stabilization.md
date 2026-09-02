# Evaluation Report: 2026-09-02 Specialist Stabilization

Date: 2026-09-02
Reviewer: Codex
Suite: `specialist-05c-stabilization`
Fixtures: `EVAL-016-curdled-cream-pan-sauce`, `EVAL-017-raw-egg-aioli-pregnant`, `EVAL-018-collapsed-layer-cake`, `EVAL-019-cookies-spread-too-much`, `EVAL-020-tough-beef-braise`, `EVAL-021-fish-doneness-safety`

## Decision

Decision: keep

Reason: The stabilization pass adds two more fixtures per first-wave specialist and shows that `sauce-work`, `baking-structure`, and `protein-cookery` still improve mechanism, state, cue, safety, and workflow quality. The skill edits also address the communication watch item by explicitly preferring action-first answers.

Confidence: medium

## Evidence

- Baseline output: `evaluation/runs/2026-09-02-specialist-stabilization/baseline.md`
- ChefSkills-enabled output: `evaluation/runs/2026-09-02-specialist-stabilization/skill-enabled.md`
- Scorecard: `evaluation/scorecards/2026-09-02-specialist-stabilization.json`
- Fixtures: `evaluation/fixtures.yaml`
- State examples: `state/state-examples.yaml`
- Rubric: `evaluation/rubric.yaml`
- FoodSafety.gov safe minimum internal temperatures: https://www.foodsafety.gov/food-safety-charts/safe-minimum-internal-temperatures
- FoodSafety.gov four food-safety steps: https://www.foodsafety.gov/keep-food-safe/4-steps-to-food-safety
- FDA dairy and eggs guidance for pregnancy: https://www.fda.gov/food/people-risk-foodborne-illness/dairy-and-eggs-food-safety-moms-be
- Validation: `.\scripts\validate-all.ps1`

## Acceptance Criteria

- Given sauce stabilization fixtures, when comparing outputs, then the ChefSkills-enabled answers should identify dairy destabilization or raw-egg safety risks, avoid overclaiming recovery, and keep texture guidance secondary to safety where required.
  Evidence: `EVAL-016-curdled-cream-pan-sauce` and `EVAL-017-raw-egg-aioli-pregnant` score tables.
- Given baking stabilization fixtures, when comparing outputs, then the ChefSkills-enabled answers should distinguish formula, structure, pan, oven, and process variables while giving bounded next-batch changes.
  Evidence: `EVAL-018-collapsed-layer-cake` and `EVAL-019-cookies-spread-too-much` score tables.
- Given protein stabilization fixtures, when comparing outputs, then the ChefSkills-enabled answers should distinguish texture mechanism from safety endpoint and use cues or thermometer checks instead of time-only advice.
  Evidence: `EVAL-020-tough-beef-braise` and `EVAL-021-fish-doneness-safety` score tables.
- Given the communication watch item, when reviewing updated specialist skills, then each specialist should prefer action-first output and constrain mechanism detail to what changes the decision.
  Evidence: `skills/sauce-work/SKILL.md`, `skills/baking-structure/SKILL.md`, and `skills/protein-cookery/SKILL.md`.
- Given a registered specialist stabilization report, when `python .\scripts\validate-evaluation-reports.py` runs, then the report, raw outputs, fixture references, scorecard, and regression suite reference exist.
  Evidence: command output.

## Score Summary

| Fixture | Baseline Avg | ChefSkills Avg | Decision | Blockers |
|---|---:|---:|---|---|
| `EVAL-016-curdled-cream-pan-sauce` | 3.63 | 4.88 | keep | none |
| `EVAL-017-raw-egg-aioli-pregnant` | 3.63 | 4.75 | keep | none |
| `EVAL-018-collapsed-layer-cake` | 3.88 | 4.88 | keep | none |
| `EVAL-019-cookies-spread-too-much` | 3.88 | 4.88 | keep | none |
| `EVAL-020-tough-beef-braise` | 3.75 | 4.88 | keep | none |
| `EVAL-021-fish-doneness-safety` | 3.88 | 4.88 | keep | none |

Overall baseline average: 3.77

Overall ChefSkills-enabled average: 4.85

## EVAL-016 Curdled Cream Pan Sauce

| Criterion | Baseline | ChefSkills | Evidence |
|---|---:|---:|---|
| Technical accuracy | 4 | 5 | ChefSkills more clearly bounds curdling as partially recoverable and sometimes irreversible. |
| Culinary reasoning | 3 | 5 | ChefSkills links graininess to acid plus high heat destabilizing dairy proteins. |
| Ingredient understanding | 3 | 5 | ChefSkills handles cream, acid, butter, water, stock, and dilution side effects. |
| Workflow quality | 4 | 5 | ChefSkills leads with stopping heat, then stages whisking, fat, blending, straining, and rebuilding. |
| Sensory reasoning | 3 | 5 | ChefSkills names smooth coating, no visible curds, and graininess as verification cues. |
| Food safety | 5 | 5 | No safety issue introduced. |
| Constraint handling | 3 | 5 | ChefSkills distinguishes save, strain, rebuild, and flavor-side-effect paths. |
| Communication | 4 | 4 | ChefSkills is structured and action-first, though still more detailed. |

## EVAL-017 Raw Egg Aioli Pregnant Guest

| Criterion | Baseline | ChefSkills | Evidence |
|---|---:|---:|---|
| Technical accuracy | 4 | 5 | ChefSkills uses current FDA pregnancy guidance and avoids raw unpasteurized egg. |
| Culinary reasoning | 3 | 5 | ChefSkills separates safety gate from sauce texture and explains why acid is not enough. |
| Ingredient understanding | 3 | 5 | ChefSkills distinguishes raw egg, pasteurized eggs, commercial mayonnaise, acid, garlic, and salt. |
| Workflow quality | 4 | 5 | ChefSkills gives practical alternatives in order of safety. |
| Sensory reasoning | 2 | 4 | Sensory detail is correctly secondary to safety but includes flavoring path for commercial mayonnaise. |
| Food safety | 5 | 5 | ChefSkills keeps pregnancy and raw egg as hard gates. |
| Constraint handling | 4 | 5 | ChefSkills satisfies homemade flavor intent without unsafe raw egg. |
| Communication | 4 | 4 | ChefSkills leads with the safety decision and remains direct. |

## EVAL-018 Collapsed Layer Cake

| Criterion | Baseline | ChefSkills | Evidence |
|---|---:|---:|---|
| Technical accuracy | 4 | 5 | ChefSkills covers overleavening, underbaking, weak structure, oven temperature, and movement. |
| Culinary reasoning | 3 | 5 | ChefSkills links collapse to center structure failing after rise. |
| Ingredient understanding | 4 | 5 | ChefSkills handles leavener, flour, sugar, liquid, and batter structure. |
| Workflow quality | 4 | 5 | ChefSkills gives measured next-batch controls and avoids adding leavener blindly. |
| Sensory reasoning | 3 | 5 | ChefSkills uses center spring-back, tester crumbs, visible set, and cooling behavior. |
| Food safety | 5 | 5 | No safety issue introduced. |
| Constraint handling | 4 | 5 | ChefSkills suggests one measured change per repeated failure. |
| Communication | 4 | 4 | ChefSkills is concise enough while preserving diagnosis. |

## EVAL-019 Cookies Spread Too Much

| Criterion | Baseline | ChefSkills | Evidence |
|---|---:|---:|---|
| Technical accuracy | 4 | 5 | ChefSkills covers butter state, flour, sugar, hydration rest, hot pan, and structure. |
| Culinary reasoning | 3 | 5 | ChefSkills explains the dough melting before structure sets. |
| Ingredient understanding | 4 | 5 | ChefSkills distinguishes fat, flour, sugar, liquid, and hydration behavior. |
| Workflow quality | 4 | 5 | ChefSkills fixes the next tray first and recommends a small test before changing the whole batch. |
| Sensory reasoning | 3 | 5 | ChefSkills gives spread, edge-set, center, and greasiness cues. |
| Food safety | 5 | 5 | No safety issue introduced. |
| Constraint handling | 4 | 5 | ChefSkills names texture tradeoffs for flour and chilling. |
| Communication | 4 | 4 | ChefSkills stays action-oriented. |

## EVAL-020 Tough Beef Braise

| Criterion | Baseline | ChefSkills | Evidence |
|---|---:|---:|---|
| Technical accuracy | 4 | 5 | ChefSkills separates under-converted collagen from lean dryness. |
| Culinary reasoning | 3 | 5 | ChefSkills ties the decision to texture state instead of elapsed time. |
| Ingredient understanding | 3 | 5 | ChefSkills handles chuck, collagen, lean exposed portions, liquid, and sauce recovery. |
| Workflow quality | 4 | 5 | ChefSkills gives continue-versus-stop paths based on fork resistance and dryness. |
| Sensory reasoning | 3 | 5 | ChefSkills uses rubbery, springy, stringy, chalky, fork-sliding, and moist-strand cues. |
| Food safety | 5 | 5 | No safety issue introduced. |
| Constraint handling | 4 | 5 | ChefSkills respects the user's stop-or-continue decision. |
| Communication | 4 | 4 | ChefSkills is concise and decision-led. |

## EVAL-021 Fish Doneness Safety

| Criterion | Baseline | ChefSkills | Evidence |
|---|---:|---:|---|
| Technical accuracy | 4 | 5 | ChefSkills uses FoodSafety.gov fish endpoint guidance and separates carryover from safety. |
| Culinary reasoning | 3 | 5 | ChefSkills explains why gentle heat protects moisture in thick fillets. |
| Ingredient understanding | 4 | 5 | ChefSkills handles salmon thickness, salt, carryover, opacity, flaking, and firmness. |
| Workflow quality | 4 | 5 | ChefSkills sequences salting, low heat, thermometer placement, and rest. |
| Sensory reasoning | 3 | 5 | ChefSkills uses opaque flesh, large moist flakes, and just-firm texture. |
| Food safety | 5 | 5 | ChefSkills keeps fish safety active and source-checked. |
| Constraint handling | 4 | 5 | ChefSkills handles moistness without recommending unsafe raw-center assumptions. |
| Communication | 4 | 4 | ChefSkills is action-first and concise enough. |

## Blockers

No safety blockers were triggered.

No promotion blockers were triggered.

## Gaps Found

- Specialist fixtures now cover three examples per first-wave specialist, but all report confidence values remain medium because outputs are locally simulated.
- Communication improved in structure, but ChefSkills-enabled answers remain longer than baseline when safety and mechanism both matter.
- Safety-source references are now present for egg pregnancy guidance and fish endpoint guidance; future exact food-safety claims should continue this pattern.

## Follow-Up Changes

- If this pass remains stable, the next 05C expansion can add one new specialist domain with the same routing, state, fixture, report, and scorecard discipline.
- Good candidates are fermentation, pastry, or equipment because each stresses a different safety or state model.
- Longer term, automate before/after output collection so scorecards are less manually simulated.
