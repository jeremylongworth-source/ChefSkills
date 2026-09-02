# Scenario: Thin Gravy

Prompt:

> My gravy is too thin. Should I just add flour?

Expected routing:

- chef-core
- culinary-reasoning
- cooking-techniques

Expected behavior:

- Diagnose possible causes before prescribing a fix.
- Distinguish reduction, starch gelatinization, roux quantity, slurry use, and excess liquid.
- Recommend a staged intervention that avoids lumps and raw flour taste.
- Include a spoon-coating or flow cue.

Failure modes:

- Says only "add flour".
- Ignores reduction and gelatinization.
- Provides no side effects.
