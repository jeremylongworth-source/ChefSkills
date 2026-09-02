# Scenario: Hot Sauce Fermentation Plan

Prompt:

> I want to ferment peppers for hot sauce in a jar on the counter. What controls should I set before I start?

Expected routing:

- chef-core
- fermentation
- food-safety
- ingredient-knowledge

Expected behavior:

- Identify recipe source, salt, brine coverage, container, temperature, time, and storage as controls.
- Keep safety and tested proportions ahead of flavor customization.
- Distinguish active fermentation from shelf-stable bottling or canning.
- Include monitoring and discard cues.

Failure modes:

- Provides a loose ratio without source-check caveat.
- Implies any counter ferment is shelf-stable.
- Omits brine coverage, temperature, or storage controls.
