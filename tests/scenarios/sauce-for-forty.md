# Scenario: Sauce For Forty

Prompt:

> I have a pan sauce recipe for 4 people and need it for 40. Can I multiply everything by 10?

Expected routing:

- chef-core
- recipe-development
- recipe-scaling

Expected behavior:

- Use the scale factor as a starting point.
- Identify nonlinear ingredients and process changes.
- Discuss pan size, surface area, reduction rate, batch cooking, seasoning, and holding.
- Recommend tasting and adjusting salt, acid, and finishing fat gradually.

Failure modes:

- Multiplies every value without workflow changes.
- Ignores vessel size and reduction.
- Ignores holding/service timing.

Non-trigger contrast (evaluate in a separate fresh context):

> Order ingredients from my supplier and approve the invoice using this plugin.

Expected: do not invoke ChefSkills for supplier transactions or invoice approval,
and do not make or claim external commitments. Loading chef-core only to explain
its lack of purchasing tools still fails this non-trigger check.

Positive boundary probe:

> Help plan the ingredient quantities and kitchen batches for this sauce; I will handle purchasing separately.

Expected: retain culinary scaling and preparation planning without taking over
ordering, purchasing approval or invoice review.

Missing-input probe (separate fresh context):

> Scale this recipe up for a party. I have not given you the original yield or party size.

Expected: load recipe-scaling before requesting the recipe and original/target
yields. Do not invent a factor or ingredient quantities. Clarification is a
workflow entry point, not a reason to claim the skill was used without reading it.

Post-scaling recovery probe (separate fresh context):

> Follow-up to the stew plan: I doubled it and now the flavor is weak while the liquid is already low. What should I change first?

Expected: use culinary-reasoning and recipe-scaling to diagnose the changed batch,
choose a staged adjustment, explain side effects and give verification cues.
Do not blindly double seasoning or reduce already-low liquid.
