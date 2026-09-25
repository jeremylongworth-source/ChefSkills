# Scenario: Post-Scaling Recovery

Prompt:

> Follow-up to the stew plan: I doubled it and now the flavor is weak while the liquid is already low. What should I change first?

Expected routing:

- chef-core
- culinary-reasoning
- recipe-scaling

Expected behavior:

- Diagnose the changed batch using the observed liquid and flavor state.
- Choose a staged adjustment, explain side effects, and give verification cues.
- Ask for missing recipe details when they materially affect the intervention.

Failure modes:

- Blindly doubles seasoning or recommends reducing already-low liquid.
- Claims access to an earlier stew plan that was not supplied.

Risk and review:

- Static checks validate route registration; live response quality requires separate evaluation.
