# Culinary State Model

The state model describes what is happening in the food, workflow, equipment, and safety context before the agent recommends an action.

It is not a recipe format. It is a reasoning aid for moving from observed state to target state.

## Core Files

- `state-schema.yaml`: required sections and allowed vocabularies.
- `culinary-state.yaml`: normalized top-level state envelope.
- `ingredient-state.yaml`: ingredient identity, function, preparation, and safety state.
- `dish-state.yaml`: dish-level target, observed, and quality state.
- `transformation-state.yaml`: physical and chemical transformations.
- `equipment-state.yaml`: equipment capacity, heat behavior, and constraints.
- `workflow-state.yaml`: prep, active cooking, holding, service, and storage stages.
- `observation-state.yaml`: sensory and measured cues.
- `recovery-state.yaml`: interventions, side effects, verification, and stop conditions.
- `safety-state.yaml`: safety status, hazards, missing facts, and conservative decisions.
- `state-examples.yaml`: example state records used by validation and design review.

## Reasoning Contract

For troubleshooting and adaptation, state should support this path:

```text
goal -> current state -> observed cue -> mechanism -> intervention -> side effect -> verification cue -> safety gate
```

## Validation

Run:

```powershell
python .\scripts\validate-state.py
```

The validator checks that required state files exist, schema sections are present, examples cover the required reasoning surfaces, and safety-relevant examples include a safety gate.
