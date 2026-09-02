# Scenario: Tough Beef Braise

Prompt:

> My chuck roast braise is still tough and dry after hours. Should I keep cooking or stop?

Expected routing:

- chef-core
- protein-cookery
- culinary-reasoning
- cooking-techniques

Expected behavior:

- Distinguish under-converted collagen from overcooked lean dryness.
- Use cut, liquid, heat level, and fork-tender cues to decide whether to keep cooking.
- Recommend a covered gentle braise or service recovery.
- Avoid time-only advice.

Failure modes:

- Says always cook longer.
- Ignores cut and connective tissue.
- Gives no tenderness cue.
