# Contributing

ChefSkills prioritizes small, reviewable culinary skills over bulk-generated content.

The project is preparing for a public alpha. Contributions should make behavior easier to inspect, route, validate, or safely decline.

Good contributions:

- improve a skill's decision criteria, workflow, or output contract
- add a focused reference that changes agent behavior
- add realistic scenarios with expected routing
- tighten safety guidance with cited, reviewable reasoning
- improve validators or documentation

Avoid:

- large recipe dumps
- unreviewed food-safety claims
- generic cooking advice that does not improve agent decisions
- adding a new skill when an existing skill can be improved

## Skill Quality Bar

Each skill should include:

- concise frontmatter with `name`, `description`, and `license`
- a clear core workflow
- an output contract or deliverable shape
- at least one focused reference file
- `agents/openai.yaml` metadata

Run validation before submitting changes:

```powershell
.\scripts\validate-all.ps1
```

## Contribution Flow

1. Open or link an issue when the change affects routing, safety, evaluation scope, or a new specialist skill.
2. Keep changes small enough to review against one behavior or milestone.
3. Add or update scenarios in `tests/scenarios/` and `tests/expected-routing.yaml` when routing changes.
4. Add or update catalog cases, state examples, fixtures, reports, and scorecards when behavior expectations change.
5. Regenerate `evaluation/scorecards/summary.json` when scorecards change.
6. Update README, roadmap, changelog, or release notes when public expectations change.

## Safety And Sources

Use current authoritative sources for safety-sensitive guidance. This includes raw animal products, time-temperature handling, preservation, allergens, vulnerable diners, equipment hazards, and jurisdiction-specific commercial food-service claims.

ChefSkills should not certify legal, medical, regulatory, commercial kitchen, allergen, or food-safety compliance.
