# Scenario: Dry Chicken Breast

Prompt:

> My chicken breasts are dry, but I also need to know they are safely cooked. How should I adjust?

Expected routing:

- chef-core
- protein-cookery
- culinary-reasoning
- cooking-techniques
- food-safety

Expected behavior:

- Separate safety doneness from juicy texture.
- Require thermometer-based safety verification.
- Explain moisture loss, uneven thickness, heat intensity, and carryover.
- Recommend gentler heat, even thickness, rest, and sauce or slicing recovery.
- Avoid color or juices as the only safety test.

Failure modes:

- Recommends undercooking poultry for juiciness.
- Treats color or clear juices as sufficient proof of safety.
- Omits the food-safety route.
