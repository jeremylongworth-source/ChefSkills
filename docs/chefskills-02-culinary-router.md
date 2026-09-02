# CHEFSKILLS-02 Culinary Router

## Purpose

The culinary router makes ChefSkills behave like a bounded specialist system instead of loading every culinary instruction for every request.

The router is responsible for task classification, primary skill selection, supporting skill selection, safety preflight, ambiguity handling, and route validation.

It is not responsible for storing culinary knowledge. Culinary knowledge belongs in skills and references. Dish state belongs in `state/`.

## Task Taxonomy

ChefSkills uses seven top-level task classes:

- `MAKE`: create a dish, recipe, prep plan, menu, or workflow.
- `FIX`: diagnose and recover a failed or drifting dish.
- `JUDGE`: evaluate a recipe, plan, substitution, dish, or safety decision.
- `PLAN`: organize prep, shopping, timing, equipment, or service.
- `LEARN`: explain a culinary concept, mechanism, ingredient, or technique.
- `ADAPT`: modify a recipe or plan for constraints, scale, equipment, diet, or missing ingredients.
- `PRESERVE`: store, hold, reheat, freeze, cure, ferment, can, dehydrate, or assess leftovers.

## Routing Contract

A route should include `chef-core` plus one primary skill and only the supporting skills that materially change the answer.

Ordinary requests have a four-skill ceiling. The hard ceiling is five skills. Larger requests should be staged using the Extended Brigade Protocol described in `router/routing-rules.yaml`.

## Safety Preflight

Food-safety routing is triggered by plausible hazards, including raw or undercooked animal products, uncertain storage, reheating, preservation, allergens, vulnerable diners, spoilage, or time and temperature abuse.

When a food-safety issue is central, `food-safety` is the primary skill. When safety is relevant but not central, it is a supporting skill that can override the culinary recommendation.

## Ambiguity Handling

Ask a clarifying question only when missing facts change the safe or technically correct answer. Otherwise state assumptions and proceed.

Examples of clarifying triggers:

- missing time and temperature history for leftovers
- allergen or medical diet ambiguity
- substitution where the missing ingredient has multiple possible functions
- equipment constraints that determine feasibility

## Negative Routing

The router should avoid overloading context. Do not activate:

- `recipe-development` for a simple ingredient definition
- `recipe-scaling` for a normal serving suggestion with no yield change
- `food-safety` for a purely aesthetic plating question
- the full chef skillset for a narrow unit conversion

## Acceptance Criteria

- `router/task-types.yaml` defines all seven task classes.
- `router/classification-schema.yaml` describes a normalized router decision.
- `router/routing-rules.yaml` includes safety, ambiguity, confidence, negative routing, and extended-protocol rules.
- `router/routing-catalog.yaml` includes at least 60 examples.
- Each task class has at least five catalog examples.
- Safety-relevant catalog examples include `food-safety`.
- Catalog route length does not exceed the five-skill hard ceiling.
- Markdown scenarios continue to validate against `tests/expected-routing.yaml`.
- `scripts/validate-router.py` validates router data.
