# Evaluation Report: 2026-09-02 Foundation Smoke

Date: 2026-09-02
Reviewer: Codex
Suite: `chefskills-04-smoke`
Fixtures: `EVAL-002-thin-gravy`, `EVAL-006-chicken-counter-overnight`, `EVAL-005-sauce-for-forty`

## Decision

Decision: keep

Reason: ChefSkills-enabled outputs improved mechanism reasoning, workflow specificity, verification cues, and safety boundary expression without introducing blockers. Baseline outputs were already competent, so this report is evidence for refinement value rather than proof that the foundation is uniquely sufficient.

Confidence: medium

## Evidence

- Baseline output: `evaluation/runs/2026-09-02-foundation-smoke/baseline.md`
- Skill-enabled output: `evaluation/runs/2026-09-02-foundation-smoke/skill-enabled.md`
- Scorecard: `evaluation/scorecards/2026-09-02-foundation-smoke.json`
- Fixtures: `evaluation/fixtures.yaml`
- Rubric: `evaluation/rubric.yaml`
- Validation: `.\scripts\validate-all.ps1`

## Acceptance Criteria

- Given a troubleshooting fixture, when comparing outputs, then the ChefSkills-enabled answer should identify mechanism, intervention, side effects, and verification cues.
  Evidence: `EVAL-002-thin-gravy` score table.
- Given a safety fixture, when comparing outputs, then both outputs must avoid unsafe salvage and the ChefSkills-enabled answer should make the safety gate explicit.
  Evidence: `EVAL-006-chicken-counter-overnight` score table.
- Given a scaling fixture, when comparing outputs, then the ChefSkills-enabled answer should account for scale factor, vessel geometry, batching, nonlinear seasoning, and service state.
  Evidence: `EVAL-005-sauce-for-forty` score table.

## Score Summary

| Fixture | Baseline Avg | ChefSkills Avg | Decision | Blockers |
|---|---:|---:|---|---|
| `EVAL-002-thin-gravy` | 3.25 | 4.50 | keep | none |
| `EVAL-006-chicken-counter-overnight` | 4.00 | 4.75 | keep | none |
| `EVAL-005-sauce-for-forty` | 3.50 | 4.88 | keep | none |

Overall baseline average: 3.58

Overall ChefSkills-enabled average: 4.71

## EVAL-002 Thin Gravy

| Criterion | Baseline | ChefSkills | Evidence |
|---|---:|---:|---|
| Technical accuracy | 4 | 5 | Both avoid dry flour; ChefSkills distinguishes reduction from starch thickening. |
| Culinary reasoning | 3 | 5 | Baseline gives fixes; ChefSkills diagnoses watery flavor vs texture gap. |
| Ingredient understanding | 2 | 4 | ChefSkills names flour taste, slurry, roux, and beurre manie behavior. |
| Workflow quality | 3 | 4 | ChefSkills stages additions and simmer time. |
| Sensory reasoning | 2 | 5 | ChefSkills uses spoon-coating and nappage cues. |
| Food safety | 5 | 5 | No safety issue introduced. |
| Constraint handling | 3 | 4 | ChefSkills handles flavor-good vs flavor-watery branches. |
| Communication | 4 | 4 | Both are clear; ChefSkills is longer but still practical. |

## EVAL-006 Chicken Counter Overnight

| Criterion | Baseline | ChefSkills | Evidence |
|---|---:|---:|---|
| Technical accuracy | 5 | 5 | Both recommend discard and mention reheating limitations. |
| Culinary reasoning | 4 | 5 | ChefSkills explains time-abused food and toxin uncertainty more explicitly. |
| Ingredient understanding | 3 | 4 | ChefSkills is more specific to cooked chicken handling. |
| Workflow quality | 3 | 4 | ChefSkills adds bagging, surface cleanup, and future shallow-container storage. |
| Sensory reasoning | 3 | 5 | ChefSkills explicitly rejects smell, taste, and appearance tests. |
| Food safety | 5 | 5 | Both pass the safety hard gate. |
| Constraint handling | 4 | 5 | ChefSkills handles current discard and future safe storage. |
| Communication | 5 | 5 | Both are direct. |

## EVAL-005 Sauce For Forty

| Criterion | Baseline | ChefSkills | Evidence |
|---|---:|---:|---|
| Technical accuracy | 4 | 5 | Both warn against blind multiplication; ChefSkills adds evaporation and surface-area mechanics. |
| Culinary reasoning | 3 | 5 | ChefSkills explains why scale changes reduction behavior. |
| Ingredient understanding | 3 | 4 | ChefSkills calls out salt, acid, spices, alcohol, thickeners, butter, herbs, lemon, and aromatics. |
| Workflow quality | 3 | 5 | ChefSkills gives batching, wide-vessel, holding, and service guidance. |
| Sensory reasoning | 2 | 5 | ChefSkills includes glossy, balanced, spoon-coating cues. |
| Food safety | 5 | 5 | No safety issue introduced. |
| Constraint handling | 4 | 5 | ChefSkills handles target yield, equipment geometry, and finishing adjustments. |
| Communication | 4 | 5 | ChefSkills remains direct while adding useful operational detail. |

## Blockers

No safety blockers were triggered.

No promotion blockers were triggered.

## Gaps Found

- The baseline was already strong on straightforward safety and basic scaling, so future evaluations should use harder edge cases.
- This report covers only three fixtures and does not yet prove the full eight-skill foundation.
- Current reports are manually scored; a future tool could produce scorecard JSON for easier aggregation.

## Follow-Up Changes

- Add more before/after reports for `EVAL-008-evaluate-ai-sushi-recipe`, `EVAL-010-gluten-free-cake-adaptation`, and `EVAL-011-garlic-oil-storage`.
- Patch foundation skills only after repeated reports show the same concrete gap.
- Add `CHEFSKILLS-05B` improvements after at least one safety, one substitution, one scaling, and one troubleshooting report are reviewed.
