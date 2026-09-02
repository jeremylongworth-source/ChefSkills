# Culinary Router

The ChefSkills router is the decision layer that determines which culinary skills should be loaded for a user request.

It should stay smaller than the knowledge layer. Its job is classification and routing, not teaching culinary content.

## Decision Output

A router decision should include:

- `task_type`: one of `MAKE`, `FIX`, `JUDGE`, `PLAN`, `LEARN`, `ADAPT`, or `PRESERVE`
- `primary_skill`: the skill responsible for the main decision
- `supporting_skills`: skills that materially change the answer
- `safety_preflight`: whether safety review is required
- `confidence`: high, medium, or low
- `assumptions`: facts inferred from the request
- `clarifying_questions`: only when the answer would change materially

## Routing Ceiling

Ordinary requests should use one primary skill and up to three supporting skills.

The hard ceiling is five skills. When a request needs more than five skills, write a staged brief first and handle it as an extended culinary project.

## Task Classes

- `MAKE`: create a dish, recipe, prep plan, menu, or workflow.
- `FIX`: diagnose and recover a failed or drifting dish.
- `JUDGE`: evaluate a recipe, plan, substitution, dish, or safety decision.
- `PLAN`: organize prep, shopping, timing, equipment, or service.
- `LEARN`: explain a culinary concept, technique, ingredient, or mechanism.
- `ADAPT`: modify a recipe or plan for constraints, scale, equipment, diet, or missing ingredients.
- `PRESERVE`: store, hold, reheat, freeze, cure, ferment, can, dehydrate, or assess leftovers.

## Files

- `task-types.yaml`: task class definitions and default primary skills.
- `classification-schema.yaml`: normalized router decision shape.
- `routing-rules.yaml`: precedence, safety, ambiguity, and ceiling rules.
- `routing-catalog.yaml`: broad machine-checked routing examples.
- `routing-examples.yaml`: short illustrative examples for humans.

## Validation

Run:

```powershell
python .\scripts\validate-router.py
```

The validator checks that catalog routes use existing skills, known task types, the configured skill ceiling, and safety requirements.
