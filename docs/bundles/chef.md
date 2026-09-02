# Chef Bundle Brief

## Problem

General-purpose agents can produce recipes, but they often miss culinary mechanisms, process cues, substitution side effects, scaling problems, and safety boundaries.

## Target User

Home cooks, recipe developers, culinary educators, operators, and agent builders who need practical chef-like reasoning.

## Included Skills

- `chef-core`: core culinary operating model.
- `culinary-reasoning`: mechanism-based diagnosis and intervention.
- `ingredient-knowledge`: ingredient roles and properties.
- `cooking-techniques`: technique selection and process control.
- `sauce-work`: sauce construction, finishing, scaling, and recovery.
- `baking-structure`: baked-good structure, crumb, rise, set, and texture recovery.
- `protein-cookery`: doneness, carryover, texture, moisture, and safety-aware protein handling.
- `ingredient-substitution`: substitutions and adaptations.
- `recipe-development`: recipe design and iteration.
- `recipe-scaling`: scaling and batch workflow.
- `food-safety`: safety hazard recognition and conservative guidance.

## Context Files

- `router/task-types.yaml`
- `router/routing-rules.yaml`
- `state/culinary-state.yaml`
- `docs/state-model.md`
- `tests/expected-routing.yaml`

## Safety Rules

- Activate `food-safety` for plausible hazards.
- Do not optimize for saving food when safety is uncertain.
- Distinguish safety requirements from quality preferences.
- Do not invent exact safety thresholds when conditions are missing.

## Pilot Metrics

- Correct skill routing on foundation scenarios.
- Fewer unsafe or overconfident food-safety answers.
- Better troubleshooting through mechanism, intervention, side effect, and verification.
- Better recipe scaling through workflow and vessel reasoning, not linear multiplication alone.
- Better specialist coverage for sauces, baking structure, and protein cookery without loading the full culinary library.

## Acceptance Criteria

- The skillset validates with `scripts/validate-skillsets.py`.
- Foundation scenarios route to the expected skills.
- Safety scenarios activate `food-safety`.
- Troubleshooting outputs identify current state, target state, cause, intervention, side effects, and verification cues.
- Specialist scenarios activate the relevant specialist skill while staying inside the routing ceiling.
