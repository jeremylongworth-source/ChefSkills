# ChefSkills AI Project Context

ChefSkills is a specialist skill framework for AI agents that need chef-like culinary reasoning.

The project should not start by collecting recipes. It should start by proving a reusable decision system:

- classify culinary requests
- activate the smallest useful skill chain
- reason from current cooking state to target state
- use food safety as a hard gate
- explain mechanisms and observable cues
- validate behavior with scenarios

The first foundation contains eight skills:

- `chef-core`
- `culinary-reasoning`
- `ingredient-knowledge`
- `cooking-techniques`
- `ingredient-substitution`
- `recipe-development`
- `recipe-scaling`
- `food-safety`

The active architectural artifact is `CHEFSKILLS-02 Culinary Router`, expanding `router/` into a more complete decision layer with task confidence, ambiguity handling, negative routing, and a 60-case routing catalog.

The `CHEFSKILLS-03 Culinary State Model` now expands `state/` into a reusable representation of ingredients, transformations, dish state, equipment state, workflow stage, observed cues, recovery actions, and safety status.

The next evaluation artifact should be `CHEFSKILLS-04 Evaluation Engine`, turning routing and state-model expectations into stronger scoring, fixtures, and regression checks.

Future work should expand specialist culinary knowledge only after the router, state model, and evaluation engine are testable.
