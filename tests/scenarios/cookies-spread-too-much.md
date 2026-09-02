# Scenario: Cookies Spread Too Much

Prompt:

> My chocolate chip cookies spread into thin greasy puddles. How do I adjust the dough?

Expected routing:

- chef-core
- baking-structure
- ingredient-knowledge
- culinary-reasoning

Expected behavior:

- Identify fat temperature, flour ratio, sugar balance, dough hydration, and pan heat as possible causes.
- Recommend chilled dough, measured flour, controlled butter state, and pan changes.
- Explain texture tradeoffs.
- Include spread, edge, and center-set cues.

Failure modes:

- Says only to add flour.
- Ignores butter temperature or pan heat.
- Gives no texture tradeoff.
