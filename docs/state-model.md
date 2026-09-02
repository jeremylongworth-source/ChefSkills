# Culinary State Model

ChefSkills treats cooking as movement from observed state to target state.

## State Categories

- Ingredient state: raw, trimmed, cut, soaked, salted, marinated, cooked, cooled, stored.
- Heat state: cold, room temperature, warming, simmering, boiling, searing, baking, holding, cooling.
- Moisture state: dry, hydrated, wet, reduced, evaporating, waterlogged.
- Texture state: crisp, tender, tough, dry, gummy, grainy, emulsified, broken.
- Flavor state: under-seasoned, balanced, salty, acidic, bitter, sweet, flat, concentrated.
- Workflow state: shopping, prep, active cooking, holding, service, storage, recovery.
- Safety state: safe, time-limited, uncertain, unsafe, discard.

## Reasoning Pattern

1. Identify the user's goal.
2. Identify current observable state.
3. Identify target state.
4. Explain the mechanism behind the gap.
5. Choose the lowest-risk intervention.
6. Predict side effects.
7. Give verification cues.

This pattern matters most for troubleshooting and adaptation.
