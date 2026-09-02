# Scenario: Collapsed Layer Cake

Prompt:

> My layer cake rose in the oven, then sank and left a dense ring near the center. What should I change?

Expected routing:

- chef-core
- baking-structure
- culinary-reasoning
- cooking-techniques

Expected behavior:

- Identify possible overleavening, underbaking, weak structure, oven temperature, or early movement.
- Separate formula changes from process changes.
- Recommend bounded next-batch adjustments.
- Include center-set and cooling cues.

Failure modes:

- Blames only oven temperature.
- Suggests adding more leavener without caveat.
- Gives no structural or doneness cue.
