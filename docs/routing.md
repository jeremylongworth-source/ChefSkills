# Routing Model

The router answers three questions:

1. What kind of culinary task is this?
2. Which primary skill owns the decision?
3. Which supporting skills are necessary?

`CHEFSKILLS-02` promotes the router from prose guidance into a validated data layer. See `router/README.md`, `router/classification-schema.yaml`, and `router/routing-catalog.yaml`.

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

## Confidence

- High confidence: task class and primary skill are clear, with no safety-critical gaps.
- Medium confidence: the task class is clear, but the answer needs stated assumptions.
- Low confidence: missing facts would change safety, feasibility, or the selected route; ask a concise clarifying question.

## Safety Preflight

Before giving cooking instructions, check whether the request includes:

- raw or undercooked animal products
- time and temperature abuse
- canning, curing, fermenting, dehydration, sous vide, or vacuum storage
- allergens or medically relevant diet constraints
- vulnerable diners
- spoilage, mold, off odors, or uncertain storage

Activate `food-safety` when any of those are plausible.
