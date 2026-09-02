# Scenario: Broken Mayonnaise

Prompt:

> My mayonnaise broke and looks oily and separated. How do I fix it?

Expected routing:

- chef-core
- culinary-reasoning
- cooking-techniques

Expected behavior:

- Identify emulsion failure.
- Explain likely causes such as adding oil too quickly, insufficient water phase, or temperature mismatch.
- Give a staged recovery method using a fresh yolk, water, or mustard base as appropriate.
- Include cues for when the emulsion is stable again.

Failure modes:

- Tells the user to throw it out without attempting normal recovery.
- Adds dry ingredients without addressing emulsion mechanics.
- Gives no observable cue.
