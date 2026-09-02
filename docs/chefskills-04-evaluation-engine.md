# CHEFSKILLS-04 Evaluation Engine

## Purpose

The evaluation engine makes ChefSkills measurable. It defines how maintainers judge whether a skill, router rule, or state model actually improves culinary agent behavior.

The engine is intentionally lightweight: YAML fixtures, a rubric, safety gates, regression suites, and a validator. It does not require a live model provider or private trace system.

## Artifacts

- `evaluation/rubric.yaml`: weighted 0-5 rubric with food safety as a hard gate.
- `evaluation/scoring-schema.yaml`: normalized scorecard shape.
- `evaluation/safety-gates.yaml`: automatic blockers for unsafe culinary outputs.
- `evaluation/fixtures.yaml`: reusable evaluation fixtures tied to existing scenarios, routes, and state examples.
- `evaluation/regression-suite.yaml`: grouped fixture suites for smoke, safety, state reasoning, and adaptation checks.
- `evaluation/report-template.md`: human-readable report template.
- `scripts/validate-evaluation.py`: structural validation for evaluation files.

## Evaluation Contract

Each fixture must connect four layers:

1. A realistic scenario prompt under `tests/scenarios/`.
2. An expected route from `tests/expected-routing.yaml`.
3. A state example from `state/state-examples.yaml` when state reasoning applies.
4. Required behavior and blockers for scoring.

## Safety Gate

Food safety cannot be averaged away. If a fixture triggers a safety blocker, the output fails promotion regardless of total score.

Common blockers include unsafe salvage, raw-animal-product overconfidence, preservation overconfidence, allergen or medical diet certainty, ignored cross-contamination, and hidden safety-critical missing facts.

## Acceptance Criteria

Given the evaluation engine, when a maintainer runs `python .\scripts\validate-evaluation.py`, then rubric criteria, safety gates, fixtures, routes, state examples, and regression suites validate.
Evidence: command output.

Given a safety-relevant fixture, when the validator reads `evaluation/fixtures.yaml`, then the fixture routes to `food-safety`, has a non-`not_required` safety gate, and includes blockers.
Evidence: `scripts/validate-evaluation.py`.

Given a fixture with an expected route, when the validator compares it to `tests/expected-routing.yaml`, then the route must match exactly.
Evidence: `scripts/validate-evaluation.py`.

Given a regression suite, when the validator reads `evaluation/regression-suite.yaml`, then every fixture id must exist in `evaluation/fixtures.yaml`.
Evidence: `scripts/validate-evaluation.py`.

Given the full repository validation command, when a maintainer runs `.\scripts\validate-all.ps1`, then evaluation validation runs with the other checks.
Evidence: command output.

## Next Work

Future work should add before/after reports from actual model outputs, broaden fixture coverage, and introduce a repeatable scoring workflow for proposed new culinary skills.
