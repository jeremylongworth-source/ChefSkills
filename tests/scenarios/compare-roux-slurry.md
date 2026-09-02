# Scenario: Compare Roux Slurry

Prompt:

> Should I thicken this sauce with roux or a cornstarch slurry?

Expected routing:

- chef-core
- culinary-reasoning
- cooking-techniques

Expected behavior:

- Compare the two thickeners by mechanism, texture, opacity, flavor, timing, and reheating behavior.
- Ask for sauce context only if needed to choose definitively.
- Recommend a default based on the described target if enough context exists.
- Include failure points such as raw flour flavor or slurry clumping.

Failure modes:

- Treats thickeners as interchangeable.
- Gives no mechanism or texture tradeoff.
- Routes to ingredient substitution unnecessarily.
