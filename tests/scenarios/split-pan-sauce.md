# Scenario: Split Pan Sauce

Prompt:

> My pan sauce looked glossy, then turned greasy after I whisked in butter. Can I fix it?

Expected routing:

- chef-core
- sauce-work
- culinary-reasoning
- cooking-techniques

Expected behavior:

- Identify the sauce as a broken butter emulsion.
- Explain likely heat, fat-load, or low-water-phase causes.
- Recommend a lower-heat staged recovery using liquid and whisking.
- Include a glossy spoon-coating cue with no oil pooling.

Failure modes:

- Treats the sauce as simply too oily without explaining emulsion failure.
- Adds more fat as the main recovery.
- Gives no stop cue or stability cue.
