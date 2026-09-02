# Routing Model

The router answers three questions:

1. What kind of culinary task is this?
2. Which primary skill owns the decision?
3. Which supporting skills are necessary?

## Task Classes

- `MAKE`: create a dish, recipe, prep plan, or menu.
- `FIX`: diagnose and recover a dish, process, flavor, or texture problem.
- `JUDGE`: evaluate a recipe, substitution, plan, dish, or safety decision.
- `PLAN`: organize prep, shopping, workflow, timing, or service.
- `LEARN`: explain a technique, ingredient, mechanism, or culinary concept.
- `ADAPT`: modify for constraints, dietary needs, equipment, scale, or ingredient availability.
- `PRESERVE`: store, hold, reheat, ferment, cure, can, freeze, or assess leftovers.

## Skill Ceiling

Use one primary skill and up to three supporting skills for ordinary requests.

Use up to five skills only when the request genuinely spans recipe design, scale, safety, workflow, and troubleshooting.

For larger work, write a brief first and stage the work.

## Safety Preflight

Before giving cooking instructions, check whether the request includes:

- raw or undercooked animal products
- time and temperature abuse
- canning, curing, fermenting, dehydration, sous vide, or vacuum storage
- allergens or medically relevant diet constraints
- vulnerable diners
- spoilage, mold, off odors, or uncertain storage

Activate `food-safety` when any of those are plausible.
