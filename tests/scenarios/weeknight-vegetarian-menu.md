# Scenario: Weeknight Vegetarian Menu

Prompt:

> Build a simple vegetarian dinner menu for four using lentils, carrots, yogurt, rice, lemons, and herbs.

Expected routing:

- chef-core
- recipe-development
- ingredient-knowledge

Expected behavior:

- Propose a coherent menu from available ingredients.
- Use ingredient roles to balance protein, starch, acidity, herbs, and texture.
- Include a practical prep sequence.
- Avoid unnecessary extra ingredients.

Failure modes:

- Produces disconnected dishes.
- Ignores available ingredients.
- Gives no prep order.
