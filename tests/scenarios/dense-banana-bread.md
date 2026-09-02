# Scenario: Dense Banana Bread

Prompt:

> My banana bread is dense and gummy in the middle. What should I change next batch?

Expected routing:

- chef-core
- baking-structure
- culinary-reasoning
- ingredient-knowledge

Expected behavior:

- Identify structural causes such as excess moisture, underbaking, weak leavening, pan load, or overmixing.
- Distinguish formula changes from process and doneness changes.
- Recommend measured next-batch adjustments.
- Include center-set and crumb cues.

Failure modes:

- Blames only oven time without considering structure.
- Gives a one-change answer with no confidence or cue.
- Ignores batter mixing, hydration, or leavening.
