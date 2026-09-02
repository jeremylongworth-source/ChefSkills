# Architecture

ChefSkills is a vertical specialist framework modeled on AgentSkills, but focused on culinary reasoning in a physical domain.

## Layers

1. Skills define focused agent behavior.
2. Skillsets group skills for common work modes.
3. Router rules classify requests and select the minimum useful skills.
4. State models describe ingredients, transformations, workflow, and observable cues.
5. Evaluation reports and scorecards validate routing and behavior.

## Design Principles

- Build a chef reasoning system, not a recipe library.
- Keep skills atomic enough to inspect and test.
- Put reusable culinary facts in references when they materially improve decisions.
- Treat food safety as a gate, not a score component.
- Prefer observable cues over time-only instructions.
- Keep host-specific setup at the edge.

## Initial Milestones

`CHEFSKILLS-01` creates the foundation structure.

`CHEFSKILLS-02` formalizes the router with task classes, routing ceilings, ambiguity handling, and negative routing.

`CHEFSKILLS-03` expands the state model so agents can reason from current state to target state.

`CHEFSKILLS-04` adds stronger evaluation around routing, reasoning, and safety.

`CHEFSKILLS-05A` records before/after evidence for the foundation.

`CHEFSKILLS-05B` applies targeted foundation improvements and adds scorecards for aggregate evaluation.

`CHEFSKILLS-05C` begins and stabilizes limited specialist expansion with sauce work, baking structure, protein cookery, and fermentation, each backed by routing, state, fixture, and scorecard coverage. The next specialist candidate is equipment.
