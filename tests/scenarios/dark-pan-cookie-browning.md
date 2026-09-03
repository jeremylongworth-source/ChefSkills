# Scenario: Dark Pan Cookie Browning

Prompt:

> My cookies are getting almost burnt on the bottom before the centers set. I am baking them on a dark nonstick sheet pan. Should I lower the oven temperature?

Expected routing:

- chef-core
- equipment-cookery
- baking-structure
- culinary-reasoning

Expected behavior:

- Identify dark pan heat absorption, pan material, rack position, dough temperature, and bake-through as likely drivers.
- Recommend changing pan, lining, rack position, batch cooling, dough chill, or modest temperature/timing adjustments.
- Include cues for set centers, browned edges, and bottom color.

Failure modes:

- Treats oven temperature as the only cause.
- Ignores pan color or material.
- Gives no doneness or bottom-browning cue.
