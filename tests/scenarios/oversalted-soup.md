# Scenario: Oversalted Soup

Prompt:

> I over-salted a pot of soup. Can a potato fix it?

Expected routing:

- chef-core
- culinary-reasoning
- ingredient-knowledge

Expected behavior:

- Explain that a potato is not a reliable salt remover.
- Recommend dilution, unsalted bulk ingredients, fat, acid, sweetness, or serving adjustments depending on soup type.
- Warn that added starch or ingredients change texture and flavor.
- Suggest tasting after each controlled adjustment.

Failure modes:

- Repeats the potato myth as the main fix.
- Ignores concentration and dilution.
- Makes an irreversible adjustment without staging.
