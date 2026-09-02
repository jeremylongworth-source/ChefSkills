# Scenario: Explain Searing Vs Braising

Prompt:

> Explain when to sear, simmer, roast, or braise meat and what each method changes.

Expected routing:

- chef-core
- culinary-reasoning
- cooking-techniques

Expected behavior:

- Classify as a learning request, not a recipe request.
- Explain technique differences through heat transfer, moisture, browning, connective tissue, and texture.
- Include decision criteria for choosing a method.
- Avoid unnecessary recipe-development routing.

Failure modes:

- Produces recipes instead of explaining technique selection.
- Omits why each method works.
- Gives time-only guidance without cues.
