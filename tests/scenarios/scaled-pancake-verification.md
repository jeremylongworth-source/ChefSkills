# Scenario: Scaled Pancake Verification

Prompt:

> Scale my pancake recipe from 4 to 12 portions: 200 g flour, 300 mL milk, 1 egg and 8 g baking powder.

Expected routing:

- chef-core
- recipe-scaling

Expected behavior:

- Show factor 3 and arithmetic starting quantities.
- Review leavening, pan/batch capacity and timing without multiplying cooking time.
- Give a first-pancake or small-batch check and an observable condition for adjusting heat or batter before cooking the rest.
- Keep any adjustment proportional to observed results rather than automatically increasing leavening.

Failure modes:

- Gives multiplication alone.
- Gives doneness cues without a test-and-adjust step.
- Treats a scaled recipe as physically verified without an actual cooking test.

Risk and review:

- Static scenario validation checks structure and routing declarations; retained host outputs are needed to verify behavior.
