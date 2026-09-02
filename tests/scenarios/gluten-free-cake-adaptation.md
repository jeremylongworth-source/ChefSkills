# Scenario: Gluten-Free Cake Adaptation

Prompt:

> Adapt a simple chocolate cake recipe to be gluten-free without making it crumbly.

Expected routing:

- chef-core
- ingredient-substitution
- recipe-development
- cooking-techniques

Expected behavior:

- Identify wheat flour's structural role.
- Recommend a substitute strategy with binding, hydration, and texture considerations.
- Explain likely technique or mixing changes.
- Avoid treating gluten-free flour as a guaranteed one-for-one replacement.

Failure modes:

- Makes a direct flour swap with no structural adjustment.
- Ignores moisture and binding.
- Routes only to recipe development.
