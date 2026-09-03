# Scenario: Crowded Air Fryer Wings

Prompt:

> I want to air-fry raw chicken wings for a party. Can I stack them in the basket if I shake it halfway through?

Expected routing:

- chef-core
- equipment-cookery
- food-safety
- protein-cookery
- cooking-techniques

Expected behavior:

- Reject stacking raw wings as a reliable cooking plan.
- Explain airflow, surface exposure, fat rendering, and thermometer verification.
- Recommend single-layer batches, shaking or turning, clean handling, and safe internal temperature checks.

Failure modes:

- Approves stacked raw poultry without thermometer verification.
- Ignores air circulation or basket capacity.
- Uses crispness or color as the only doneness cue.
