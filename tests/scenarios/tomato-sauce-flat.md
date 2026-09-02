# Scenario: Tomato Sauce Tastes Flat

Prompt:

> My tomato sauce tastes flat even after simmering. What should I adjust?

Expected routing:

- chef-core
- culinary-reasoning
- ingredient-knowledge

Expected behavior:

- Diagnose salt, acidity, sweetness, umami, aromatics, fat, and concentration separately.
- Recommend small staged adjustments.
- Explain how each adjustment changes perception.
- Include tasting checkpoints.

Failure modes:

- Adds sugar as the only answer.
- Ignores salt or acid.
- Makes multiple large changes at once.
