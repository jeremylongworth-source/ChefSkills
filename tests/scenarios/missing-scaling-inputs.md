# Scenario: Missing Scaling Inputs

Prompt:

> Scale this recipe up for a party. I have not given you the original yield or party size.

Expected routing:

- chef-core
- recipe-scaling

Expected behavior:

- Read recipe-scaling before asking for the recipe and original and target yields.
- Keep clarification focused on the information needed to calculate and plan batches.

Failure modes:

- Invents quantities or a scale factor.
- Skips the scaling workflow because inputs are missing.

Risk and review:

- Static checks validate route registration; live skill-read and response evidence require a separate run.
