# Scenario: Buttermilk Substitution

Prompt:

> I do not have buttermilk for pancakes. Can I just use regular milk?

Expected routing:

- chef-core
- ingredient-knowledge
- ingredient-substitution

Expected behavior:

- Identify buttermilk's acidity, moisture, flavor, and leavening role.
- Explain what plain milk changes.
- Recommend an acidified milk substitute or recipe adjustment.
- Mention texture and browning tradeoffs.

Failure modes:

- Treats milk as a one-for-one equivalent without caveat.
- Ignores acidity and leavening.
- Gives no ratio or adjustment.
