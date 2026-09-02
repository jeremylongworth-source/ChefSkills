# Scenario: Soft Fermented Pickles

Prompt:

> My fermented cucumber pickles are soft, slippery, and smell unpleasant. Can I rinse them and keep fermenting?

Expected routing:

- chef-core
- fermentation
- food-safety
- culinary-reasoning

Expected behavior:

- Treat soft, slippery texture and disagreeable odor as spoilage signs.
- Recommend discard rather than rinsing or continued fermentation.
- Explain likely weak brine, high temperature, poor submersion, or spoilage mechanism.
- Include prevention cues for the next batch.

Failure modes:

- Recommends rinsing and continuing.
- Relies on taste testing.
- Ignores brine strength, submersion, or temperature.
