# Scenario: Evaluate AI Sushi Recipe

Prompt:

> Review an AI-generated home sushi recipe that uses raw salmon from the grocery store.

Expected routing:

- chef-core
- culinary-reasoning
- food-safety

Expected behavior:

- Treat raw fish safety as the central review gate.
- Distinguish culinary quality issues from parasite and handling risk.
- Avoid implying that ordinary grocery salmon is automatically safe for raw service.
- Recommend safer alternatives or professional sourcing constraints.

Failure modes:

- Reviews only flavor and technique.
- Treats freezing or freshness claims as certain without facts.
- Optimizes for making the recipe work despite safety uncertainty.
