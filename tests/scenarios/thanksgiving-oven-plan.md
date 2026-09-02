# Scenario: Thanksgiving Oven Plan

Prompt:

> Plan Thanksgiving oven timing for turkey, stuffing, green beans, rolls, and pie.

Expected routing:

- chef-core
- cooking-techniques
- recipe-scaling
- food-safety

Expected behavior:

- Build a staged oven and holding plan.
- Identify turkey and stuffing safety constraints.
- Account for oven temperature conflicts, resting, reheating, and service timing.
- Avoid exceeding the ordinary routing ceiling.

Failure modes:

- Treats the task as a simple recipe list.
- Ignores turkey or stuffing safety.
- Gives a timeline with impossible oven overlaps.
