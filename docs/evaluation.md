# Evaluation

ChefSkills evaluates culinary competence through scenarios, expected routing, and behavior checks.

`CHEFSKILLS-04` expands evaluation into a validated engine. See `evaluation/README.md`, `evaluation/rubric.yaml`, `evaluation/fixtures.yaml`, and `evaluation/safety-gates.yaml`.

## Rubric

Score outputs from 0 to 5 on:

- technical accuracy
- culinary reasoning
- ingredient understanding
- workflow quality
- sensory reasoning
- safety
- constraint handling
- communication

Food safety is a hard gate. A serious unsafe answer fails even if other dimensions are strong.

## Scenario Expectations

Each scenario should include:

- prompt
- expected routing
- expected behavior
- safety gate, if relevant
- failure modes

Scenarios should test decisions, not just prose style.

## Promotion Decisions

Use evaluation results to decide whether to keep, revise, split, merge, defer, or retire skill behavior.

Do not promote an output when a food-safety blocker is triggered, even if the average score is otherwise high.

## Reports

Store raw before/after outputs under `evaluation/runs/` and scored summaries under `evaluation/reports/`.

Register each report in `evaluation/reports/index.yaml` so `scripts/validate-evaluation-reports.py` can verify fixture, suite, scorecard, and evidence links.

Store machine-readable report summaries under `evaluation/scorecards/`. `scripts/validate-scorecards.py` verifies that scorecards match the report index, use known rubric criteria, reference known fixtures, and calculate averages and deltas correctly.
