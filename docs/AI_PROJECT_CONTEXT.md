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

The `CHEFSKILLS-02 Culinary Router` now expands `router/` into a more complete decision layer with task confidence, ambiguity handling, negative routing, and a 60-case routing catalog.

The `CHEFSKILLS-03 Culinary State Model` now expands `state/` into a reusable representation of ingredients, transformations, dish state, equipment state, workflow stage, observed cues, recovery actions, and safety status.

The `CHEFSKILLS-04 Evaluation Engine` now turns routing and state-model expectations into stronger scoring, fixtures, safety gates, and regression checks.

The `CHEFSKILLS-05A Foundation Evaluation` now has three smoke before/after reports comparing baseline and ChefSkills-enabled outputs for troubleshooting, safety, scaling, raw-fish review, structural substitution, preservation storage, and state-reasoned failure recovery fixtures.

The next major artifact should be `CHEFSKILLS-05B Foundation Improvements`. The repeated concrete gap is consistent state framing across troubleshooting outputs, with secondary needs for machine-readable scorecards and source-checked safety evaluation.
