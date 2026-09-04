# Evaluation Engine

ChefSkills evaluation is a lightweight harness for deciding whether skills, router rules, and state guidance improve agent behavior.

It evaluates outputs against realistic culinary fixtures rather than checking prose style alone.

## Current Evidence Confidence

Current before/after outputs are medium-confidence local reviewer simulations. They are useful for regression tracking and roadmap decisions, but they are not live captured model outputs from a reproducible harness.

Public-alpha documentation should keep this caveat visible until a live-output harness records route, prompt, model/context notes, output path, scorecard, reviewer decision, and rerun behavior.

The `v0.1.0-alpha` release decision accepts this evidence class for public alpha only. It should not be described as a live benchmark, external validation, certification, or guarantee of future model behavior.

## Live Output Harness

Live output capture packets live under `evaluation/live-runs/`.

Create a packet from an existing regression suite:

```powershell
python .\scripts\create-live-evaluation-run.py --suite state-reasoning --run-id 2026-09-04-state-reasoning-live
```

The generated packet contains baseline prompts, ChefSkills-enabled prompts, planned raw output paths, hashes for stable inputs, model/context fields, reviewer decision fields, and rerun instructions.

The harness is provider-neutral and does not call a model API. Run the prompts in the target host, save the raw outputs without rewriting them, update the manifest hashes and status, then score the captured outputs through the normal report and scorecard workflow.

## Files

- `rubric.yaml`: scoring criteria, weights, thresholds, and hard gates.
- `scoring-schema.yaml`: required scorecard fields and decision values.
- `safety-gates.yaml`: automatic blockers for unsafe culinary outputs.
- `fixtures.yaml`: reusable evaluation fixtures tied to routing scenarios and state examples.
- `regression-suite.yaml`: named fixture groups for smoke, safety, and milestone checks.
- `report-template.md`: before/after report format for human review.
- `runs/`: raw baseline and skill-enabled outputs.
- `live-runs/`: reproducible prompt packets and manifests for live model-output capture.
- `reports/`: scored before/after evaluation reports.
- `scorecards/`: machine-readable JSON summaries of registered reports.

## Evaluation Flow

1. Select a fixture from `fixtures.yaml`.
2. Run or simulate a baseline output.
3. Run or simulate the skill-enabled output with the expected route.
4. Score both outputs with `rubric.yaml`.
5. Apply `safety-gates.yaml` before averaging scores.
6. Decide whether to keep, revise, split, merge, defer, or retire the skill behavior.
7. Record the result using `report-template.md`.
8. Add a JSON scorecard under `evaluation/scorecards/` and register it in `evaluation/reports/index.yaml`.
9. Regenerate `evaluation/scorecards/summary.json` when report scorecards change.

## Validation

Run:

```powershell
python .\scripts\validate-evaluation.py
python .\scripts\validate-live-evaluation-runs.py
python .\scripts\validate-evaluation-reports.py
python .\scripts\validate-scorecards.py
python .\scripts\summarize-scorecards.py --check .\evaluation\scorecards\summary.json
```

These checks confirm that evaluation fixtures reference known scenarios, routes, state examples, and regression suites, that registered reports link to real fixture and output evidence, and that scorecards match the report index and rubric criteria.
