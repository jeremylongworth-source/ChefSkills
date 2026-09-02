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
