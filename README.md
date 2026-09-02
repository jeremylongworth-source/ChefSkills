# ChefSkills

Portable culinary Agent Skills, skillsets, routing rules, state models, and evaluation scenarios for AI agents that need to reason like a chef.

## Why This Exists

Most recipe assistants can produce plausible instructions. ChefSkills is intended to make an agent reason about food as a changing physical system:

- ingredients and their functional roles
- heat, time, moisture, fat, starch, acid, salt, texture, and aroma
- observable cues rather than time-only instructions
- substitutions, scaling, troubleshooting, planning, and safety boundaries
- kitchen workflow and recovery decisions

The project starts small on purpose. The first milestone is a testable operating framework, not a large recipe database.

## Core Idea

ChefSkills separates culinary expertise into four layers:

- Skills: focused reusable instructions under `skills/`
- Skillsets: installable bundles under `skillsets/`
- Router: task classification and minimum useful skill selection under `router/`
- State model: structured cooking state and transformation concepts under `state/`

Food safety is a hard gate. It is not averaged against good cooking advice.

## Current Skills

| Skill | Purpose |
|---|---|
| `chef-core` | Core chef operating model and safety-first behavior |
| `culinary-reasoning` | Mechanism-based culinary diagnosis and intervention |
| `ingredient-knowledge` | Ingredient roles, properties, and behavior |
| `cooking-techniques` | Technique selection, cues, and failure points |
| `sauce-work` | Sauce construction, finishing, scaling, and recovery |
| `baking-structure` | Baked-good structure, crumb, rise, set, and texture recovery |
| `protein-cookery` | Doneness, carryover, moisture, and safety-aware protein handling |
| `fermentation` | Home fermentation, brines, pH, salt, gas, spoilage, and storage boundaries |
| `equipment-cookery` | Appliances, vessels, heat transfer, capacity, airflow, pressure, and tool substitutions |
| `ingredient-substitution` | Functional substitution reasoning |
| `recipe-development` | Recipe design, formatting, and iteration |
| `recipe-scaling` | Scaling quantities, vessels, heat transfer, and workflow |
| `food-safety` | Safety hazard recognition and conservative guidance |

## Repository Structure

```text
ChefSkills/
|-- skills/
|-- skillsets/
|-- router/
|-- state/
|-- agents/
|-- docs/
|-- scripts/
`-- tests/
```

## Validation

Run the local validators from the repository root:

```powershell
python .\scripts\validate-skill-files.py
python .\scripts\validate-skillsets.py
python .\scripts\validate-scenarios.py
python .\scripts\validate-router.py
python .\scripts\validate-state.py
python .\scripts\validate-evaluation.py
python .\scripts\validate-evaluation-reports.py
python .\scripts\validate-scorecards.py
python .\scripts\summarize-scorecards.py --check .\evaluation\scorecards\summary.json
```

Or run all current checks:

```powershell
.\scripts\validate-all.ps1
```

## Development Roadmap

1. `CHEFSKILLS-01`: Foundation skills, skillsets, docs, and scenario checks.
2. `CHEFSKILLS-02`: Culinary router specification with task classes, routing ceilings, ambiguity handling, confidence, and a broad routing catalog.
3. `CHEFSKILLS-03`: Culinary state model for ingredients, dish state, transformations, workflow, observed cues, recovery actions, and safety status.
4. `CHEFSKILLS-04`: Evaluation engine for rubric scoring, fixtures, regression suites, and safety gates.
5. `CHEFSKILLS-05A`: Foundation before/after evaluation reports.
6. `CHEFSKILLS-05B`: Targeted foundation skill improvements based on repeated evaluation gaps.
7. `CHEFSKILLS-05C`: Specialist expansion has stabilized sauce work, baking structure, protein cookery, and fermentation, then added equipment cookery before the next pastry, cuisine, service, and costing work.

## License

MIT
