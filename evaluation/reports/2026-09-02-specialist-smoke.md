# Evaluation Report: 2026-09-02 Specialist Smoke

Date: 2026-09-02
Reviewer: Codex
Suite: `specialist-05c-smoke`
Fixtures: `EVAL-013-split-pan-sauce`, `EVAL-014-dense-banana-bread`, `EVAL-015-dry-chicken-breast`

## Decision

Decision: keep

Reason: The first 05C specialist skills improved mechanism specificity and recovery structure while staying inside the existing routing ceiling. The strongest gains are in sauce emulsion recovery, baking structure diagnosis, and safety-aware protein troubleshooting.

Confidence: medium

## Evidence

- Baseline output: `evaluation/runs/2026-09-02-specialist-smoke/baseline.md`
- ChefSkills-enabled output: `evaluation/runs/2026-09-02-specialist-smoke/skill-enabled.md`
- Scorecard: `evaluation/scorecards/2026-09-02-specialist-smoke.json`
- Fixtures: `evaluation/fixtures.yaml`
- State examples: `state/state-examples.yaml`
- Rubric: `evaluation/rubric.yaml`
- Safety source for poultry endpoint: https://www.foodsafety.gov/food-safety-charts/safe-minimum-internal-temperatures
- Validation: `.\scripts\validate-all.ps1`

## Acceptance Criteria

- Given a split pan sauce fixture, when comparing outputs, then the ChefSkills-enabled answer should identify a broken butter emulsion, explain heat or water-phase causes, use staged liquid-and-whisk recovery, and include a glossy no-oil-pooling cue.
  Evidence: `EVAL-013-split-pan-sauce` score table.
- Given a dense banana bread fixture, when comparing outputs, then the ChefSkills-enabled answer should distinguish moisture, leavening, mixing, pan load, and bake-through causes before proposing next-batch changes.
  Evidence: `EVAL-014-dense-banana-bread` score table.
- Given a dry chicken breast fixture, when comparing outputs, then the ChefSkills-enabled answer should separate safe poultry doneness from juicy texture, require thermometer verification, and avoid color or juice-only safety tests.
  Evidence: `EVAL-015-dry-chicken-breast` score table.
- Given a registered specialist report, when `python .\scripts\validate-evaluation-reports.py` runs, then the report, raw outputs, fixture references, scorecard, and regression suite reference exist.
  Evidence: command output.

## Score Summary

| Fixture | Baseline Avg | ChefSkills Avg | Decision | Blockers |
|---|---:|---:|---|---|
| `EVAL-013-split-pan-sauce` | 3.75 | 4.88 | keep | none |
| `EVAL-014-dense-banana-bread` | 3.88 | 4.88 | keep | none |
| `EVAL-015-dry-chicken-breast` | 4.00 | 4.88 | keep | none |

Overall baseline average: 3.88

Overall ChefSkills-enabled average: 4.88

## EVAL-013 Split Pan Sauce

| Criterion | Baseline | ChefSkills | Evidence |
|---|---:|---:|---|
| Technical accuracy | 4 | 5 | Both give a valid recovery, but ChefSkills more clearly names the broken butter emulsion and water-phase rebuild. |
| Culinary reasoning | 3 | 5 | ChefSkills links observed greasiness to heat, fat load, and reduced water phase. |
| Ingredient understanding | 3 | 5 | ChefSkills separates butter fat, water phase, stock, wine, lemon, salt, and acid side effects. |
| Workflow quality | 4 | 5 | ChefSkills stages the recovery from off-heat whisking to clean-pan restart. |
| Sensory reasoning | 3 | 5 | ChefSkills uses gloss, spoon coating, and no oil pooling as stop cues. |
| Food safety | 5 | 5 | No safety issue introduced. |
| Constraint handling | 4 | 5 | ChefSkills provides alternative liquids and flavor-side-effect checks. |
| Communication | 4 | 4 | Both are direct; ChefSkills carries more state detail. |

## EVAL-014 Dense Banana Bread

| Criterion | Baseline | ChefSkills | Evidence |
|---|---:|---:|---|
| Technical accuracy | 4 | 5 | ChefSkills covers the main structural causes without overcommitting to one. |
| Culinary reasoning | 3 | 5 | ChefSkills orders hypotheses by moisture, bake-through, leavening, and gluten development. |
| Ingredient understanding | 4 | 5 | ChefSkills maps banana moisture, flour, leavener, egg set, and gluten structure. |
| Workflow quality | 4 | 5 | ChefSkills connects measured banana, pan fill, mixing, tenting, and pull cues. |
| Sensory reasoning | 3 | 5 | ChefSkills gives center spring-back, tester, wobble, and cooled-crumb cues. |
| Food safety | 5 | 5 | No safety issue introduced. |
| Constraint handling | 4 | 5 | ChefSkills distinguishes next-batch primary tests from lower-priority experiments. |
| Communication | 4 | 4 | ChefSkills is longer but still usable. |

## EVAL-015 Dry Chicken Breast

| Criterion | Baseline | ChefSkills | Evidence |
|---|---:|---:|---|
| Technical accuracy | 4 | 5 | ChefSkills separates lean-breast quality from safe poultry endpoint and carryover. |
| Culinary reasoning | 3 | 5 | ChefSkills names moisture loss, denaturation, uneven thickness, heat, and carryover. |
| Ingredient understanding | 4 | 5 | ChefSkills handles poultry form, thickness, salt, sauces, and repurposing. |
| Workflow quality | 4 | 5 | ChefSkills sequences thickness control, salting, gentler heat, thermometer check, rest, slicing, and service moisture. |
| Sensory reasoning | 3 | 5 | ChefSkills identifies dry fibrous texture and gives service recovery cues. |
| Food safety | 5 | 5 | ChefSkills keeps `food-safety` active and cites source-checked poultry endpoint guidance. |
| Constraint handling | 4 | 5 | ChefSkills avoids unsafe undercooking while still improving juiciness. |
| Communication | 5 | 4 | Baseline is shorter; ChefSkills is clear but denser because it includes safety and state framing. |

## Blockers

No safety blockers were triggered.

No promotion blockers were triggered.

## Gaps Found

- Specialist answers improve mechanism coverage but can become longer than the baseline.
- Protein cookery needs continued source-check discipline whenever exact safe endpoints are used.
- Existing foundation scenarios still serve as historical evidence; future specialist passes should add dedicated specialist fixtures rather than rewriting old report expectations.

## Follow-Up Changes

- Add a second 05C specialist pass for fermentation, pastry, or equipment once these first specialist routes remain stable.
- Consider a communication-tightening pass if specialist answers continue to lose concision points.
- Add independent run evidence when usage budget allows.
