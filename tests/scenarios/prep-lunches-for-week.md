# Scenario: Prep Lunches For Week

Prompt:

> Plan five days of chicken and rice lunches with safe storage and reheating.

Expected routing:

- chef-core
- recipe-development
- food-safety

Expected behavior:

- Produce a prep plan with storage and reheating constraints.
- Treat rice and chicken storage as safety-relevant.
- Separate quality tips from safety requirements.
- Include a practical batching sequence.

Failure modes:

- Plans only recipes and macros.
- Ignores storage and reheating.
- Gives unsafe long holding assumptions.
