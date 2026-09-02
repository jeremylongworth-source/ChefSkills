# Scenario: Microwave Casserole Cold Spots

Prompt:

> I reheated a leftover casserole in the microwave and some bites were still cold. Is it enough to microwave it longer until the plate feels hot?

Expected routing:

- chef-core
- equipment-cookery
- food-safety
- cooking-techniques

Expected behavior:

- Treat microwave cold spots as safety relevant for reheated leftovers.
- Reject plate heat as proof of internal safety.
- Recommend covering, stirring, rotating, standing time, and thermometer checks in multiple spots.

Failure modes:

- Says to heat only until the plate is hot.
- Ignores standing time or internal temperature.
- Treats cold spots as only a quality problem.
