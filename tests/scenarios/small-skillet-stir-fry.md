# Scenario: Small Skillet Stir-Fry

Prompt:

> I do not own a wok, only a small skillet. How should I cook a stir-fry for four without everything steaming?

Expected routing:

- chef-core
- equipment-cookery
- cooking-techniques
- ingredient-knowledge

Expected behavior:

- Adapt wok cooking to a small skillet instead of implying the dish requires a wok.
- Use batching, high preheat, pan recovery, ingredient sequencing, and late saucing to control moisture.
- Include cues that distinguish searing from steaming.

Failure modes:

- Tells the user to cook everything together in the small skillet.
- Ignores surface area, heat retention, or moisture release.
- Gives no batch workflow.
