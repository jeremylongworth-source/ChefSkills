# Evaluation Engine

ChefSkills evaluation is a lightweight harness for deciding whether skills, router rules, and state guidance improve agent behavior.

It evaluates outputs against realistic culinary fixtures rather than checking prose style alone.

## Files

- `rubric.yaml`: scoring criteria, weights, thresholds, and hard gates.
- `scoring-schema.yaml`: required scorecard fields and decision values.
- `safety-gates.yaml`: automatic blockers for unsafe culinary outputs.
- `fixtures.yaml`: reusable evaluation fixtures tied to routing scenarios and state examples.
- `regression-suite.yaml`: named fixture groups for smoke, safety, and milestone checks.
- `report-template.md`: before/after report format for human review.
- `runs/`: raw baseline and skill-enabled outputs.
- `reports/`: scored before/after evaluation reports.

## Evaluation Flow

1. Select a fixture from `fixtures.yaml`.
2. Run or simulate a baseline output.
3. Run or simulate the skill-enabled output with the expected route.
4. Score both outputs with `rubric.yaml`.
5. Apply `safety-gates.yaml` before averaging scores.
6. Decide whether to keep, revise, split, merge, defer, or retire the skill behavior.
7. Record the result using `report-template.md`.

## Validation

Run:

```powershell
python .\scripts\validate-evaluation.py
python .\scripts\validate-evaluation-reports.py
```

These checks confirm that evaluation fixtures reference known scenarios, routes, state examples, and regression suites, and that registered reports link to real fixture and output evidence.
