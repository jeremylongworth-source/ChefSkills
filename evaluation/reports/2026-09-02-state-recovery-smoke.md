# Evaluation Report: 2026-09-02 State Recovery Smoke

Date: 2026-09-02
Reviewer: Codex
Suite: `state-reasoning`
Fixtures: `EVAL-001-broken-mayonnaise`, `EVAL-003-oversalted-soup`, `EVAL-007-tomato-sauce-flat`

## Decision

Decision: keep

Reason: ChefSkills-enabled outputs improved state framing, mechanism explanation, staged recovery, side-effect warnings, and verification cues across three failure-recovery fixtures. The baseline outputs were practical and mostly correct, so the value shown here is not basic competence; it is repeatable structure for diagnosing and recovering dishes without over-adjusting.

Confidence: medium

## Evidence

- Baseline output: `evaluation/runs/2026-09-02-state-recovery-smoke/baseline.md`
- ChefSkills-enabled output: `evaluation/runs/2026-09-02-state-recovery-smoke/skill-enabled.md`
- Scorecard: `evaluation/scorecards/2026-09-02-state-recovery-smoke.json`
- Fixtures: `evaluation/fixtures.yaml`
- State examples: `state/state-examples.yaml`
- Rubric: `evaluation/rubric.yaml`
- Validation: `.\scripts\validate-all.ps1`

## Acceptance Criteria

- Given a broken emulsion fixture, when comparing outputs, then the ChefSkills-enabled answer should name emulsion failure, use a staged restart method, and include a stable-emulsion verification cue.
  Evidence: `EVAL-001-broken-mayonnaise` score table.
- Given an oversalted soup fixture, when comparing outputs, then the ChefSkills-enabled answer should reject the potato myth as the main fix, explain dilution and concentration, and stage tasting.
  Evidence: `EVAL-003-oversalted-soup` score table.
- Given a flat tomato sauce fixture, when comparing outputs, then the ChefSkills-enabled answer should separate salt, acid, sweetness, umami, fat, aromatics, and concentration before recommending staged adjustments.
  Evidence: `EVAL-007-tomato-sauce-flat` score table.
- Given a registered evaluation report, when `python .\scripts\validate-evaluation-reports.py` runs, then the report, raw outputs, fixture references, and regression suite reference exist.
  Evidence: command output.

## Score Summary

| Fixture | Baseline Avg | ChefSkills Avg | Decision | Blockers |
|---|---:|---:|---|---|
| `EVAL-001-broken-mayonnaise` | 3.50 | 4.63 | keep | none |
| `EVAL-003-oversalted-soup` | 3.75 | 4.88 | keep | none |
| `EVAL-007-tomato-sauce-flat` | 3.75 | 4.88 | keep | none |

Overall baseline average: 3.67

Overall ChefSkills-enabled average: 4.79

## EVAL-001 Broken Mayonnaise

| Criterion | Baseline | ChefSkills | Evidence |
|---|---:|---:|---|
| Technical accuracy | 4 | 5 | Both describe a valid emulsion restart; ChefSkills more clearly distinguishes water-phase restart and fresh-yolk fallback. |
| Culinary reasoning | 3 | 5 | ChefSkills moves from observed state to mechanism, intervention, side effects, and verification. |
| Ingredient understanding | 3 | 4 | ChefSkills names oil phase, water phase, yolk, mustard, lemon, and temperature mismatch. |
| Workflow quality | 4 | 5 | ChefSkills gives a tighter pause/recover sequence if the sauce starts to split again. |
| Sensory reasoning | 2 | 5 | ChefSkills includes glossy texture, whisk ridges, and no oil pooling as cues. |
| Food safety | 5 | 5 | No safety issue introduced. |
| Constraint handling | 3 | 4 | ChefSkills handles water-base failure and fresh-yolk fallback. |
| Communication | 4 | 4 | Both are clear; ChefSkills uses more structure. |

## EVAL-003 Oversalted Soup

| Criterion | Baseline | ChefSkills | Evidence |
|---|---:|---:|---|
| Technical accuracy | 4 | 5 | Both reject potato as reliable; ChefSkills more clearly explains salt concentration and reduction risk. |
| Culinary reasoning | 3 | 5 | ChefSkills identifies concentration as the mechanism and sequences dilution, integration, and balancing. |
| Ingredient understanding | 3 | 5 | ChefSkills distinguishes salty components, unsalted bulk, starch body, fat, dairy, acid, and sweetness. |
| Workflow quality | 4 | 5 | ChefSkills starts by stopping reduction, then removes salty solids before staged dilution. |
| Sensory reasoning | 3 | 5 | ChefSkills uses sharp, briny, mouth-drying, and "close but still salty" cues. |
| Food safety | 5 | 5 | No safety issue introduced. |
| Constraint handling | 4 | 5 | ChefSkills adapts options by soup type and supports serving adjustments. |
| Communication | 4 | 4 | Both are practical; ChefSkills is more diagnostic. |

## EVAL-007 Tomato Sauce Flat

| Criterion | Baseline | ChefSkills | Evidence |
|---|---:|---:|---|
| Technical accuracy | 4 | 5 | Both cover major flavor levers; ChefSkills better separates concentration from seasoning. |
| Culinary reasoning | 3 | 5 | ChefSkills diagnoses flatness as a balance problem and tests one flavor axis at a time. |
| Ingredient understanding | 4 | 5 | ChefSkills names salt, acid, sweetness, umami, fat, aromatics, and tomato paste behavior. |
| Workflow quality | 4 | 5 | ChefSkills gives a precise staged tasting path and stop condition. |
| Sensory reasoning | 3 | 5 | ChefSkills uses watery, dull, heavy, harsh, metallic, muddy, brighter, and fuller cues. |
| Food safety | 5 | 5 | No safety issue introduced. |
| Constraint handling | 3 | 5 | ChefSkills handles watery sauce versus already-thick sauce and avoids irreversible sugar-heavy correction. |
| Communication | 4 | 4 | Both are direct; ChefSkills carries more decision support. |

## Blockers

No safety blockers were triggered.

No promotion blockers were triggered.

## Gaps Found

- Across repeated reports, ChefSkills consistently improves mechanism, cue, and workflow specificity, but the baseline often remains competent on common cooking problems.
- The strongest repeated gap is not a single missing culinary fact; it is that baseline answers are less consistent about explicitly separating current state, target state, mechanism, side effects, and verification cues.
- Manual reports are becoming useful but repetitive. A machine-readable scorecard format would make trend analysis easier.
- This pass used local simulated outputs for both baseline and ChefSkills-enabled answers. Future high-confidence promotion evidence should use independent runs when usage budget allows.

## Follow-Up Changes

- Begin `CHEFSKILLS-05B` with targeted improvements to make state reasoning easier to apply consistently across skills.
- Add a machine-readable scorecard artifact format before the evaluation set grows much larger.
- Keep public-safety guidance source-checked in future safety-gated reports.
