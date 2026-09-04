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

The project started in private development and is now public for alpha review after validation, safety, documentation, and contribution workflow gates.

## Status

ChefSkills is public. The current GitHub skill-install distribution release is `v0.1.0-public-preview`; the initial public alpha prerelease is `v0.1.0-alpha`. The current readiness state is `ready_for_public_alpha_readiness_work`.

Current evidence: 9 reports, 38 evaluated fixtures, 0 blockers, a baseline average of 3.7599, a ChefSkills-enabled average of 4.8059, and a delta of 1.0461.

Current caveat: before/after outputs are medium-confidence local reviewer simulations, not live captured model runs from a reproducible harness. The `v0.1.0-alpha` evidence decision accepts this for public alpha only because the limitation is visible and the release is not framed as a benchmark or certification claim.

## Core Idea

ChefSkills separates culinary expertise into four layers:

- Skills: focused reusable instructions under `skills/`
- Skillsets: installable bundles under `skillsets/`
- Router: task classification and minimum useful skill selection under `router/`
- State model: structured cooking state and transformation concepts under `state/`

Food safety is a hard gate. It is not averaged against good cooking advice.

ChefSkills does not certify legal, medical, regulatory, commercial kitchen, allergen, or food-safety compliance. Safety-sensitive work should use current authoritative sources and conservative uncertainty wording.

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

## Quick Start

Requirements:

- Python 3.10 or newer.
- PowerShell for the wrapper script, or a shell that can run the individual Python validators.

After cloning the repository, run:

```powershell
.\scripts\validate-all.ps1
```

If PowerShell is unavailable, run the individual Python commands listed in the validation section.

## GitHub Skill Install

ChefSkills can be previewed and installed through GitHub CLI agent skills for GitHub Copilot.

Preview a skill:

```powershell
gh skill preview jeremylongworth-source/ChefSkills chef-core
```

Install a skill for GitHub Copilot at project scope:

```powershell
gh skill install jeremylongworth-source/ChefSkills chef-core
```

Pin the public-preview release when reproducibility matters:

```powershell
gh skill install jeremylongworth-source/ChefSkills chef-core --agent github-copilot --scope project --pin v0.1.0-public-preview
```

Install the food-safety skill:

```powershell
gh skill install jeremylongworth-source/ChefSkills food-safety --agent github-copilot --scope project --pin v0.1.0-public-preview
```

`gh skill install` installs atomic skill folders from `skills/`, not YAML skillsets from `skillsets/`.

See [GitHub Copilot and `gh skill` Setup](docs/setup/github-copilot.md) for examples, scope guidance, and verification prompts.

## First Use

Start with a skillset:

- `skillsets/chef.yaml` for broad culinary reasoning.
- `skillsets/recipe-development.yaml` for recipe design, adaptation, testing, and scaling.

Then route a prompt through the smallest useful skill chain. Example:

```text
Prompt: My chicken thighs keep charring on the grill before they are cooked near the bone.
Route: chef-core, equipment-cookery, protein-cookery, food-safety, cooking-techniques
```

That route keeps equipment behavior, protein doneness, and food safety active without loading unrelated specialist skills.

## Repository Structure

```text
ChefSkills/
|-- .github/
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
python .\scripts\validate-live-evaluation-runs.py
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
7. `CHEFSKILLS-05C`: Specialist expansion has stabilized sauce work, baking structure, protein cookery, fermentation, and equipment cookery before the next pastry, cuisine, service, and costing work.
8. `CHEFSKILLS-06`: Open source readiness, public alpha launch, GitHub Copilot skill-install docs, and `v0.1.0-public-preview` distribution.
9. `CHEFSKILLS-07`: Live-output harness scaffold for reproducible prompt packets, manifests, captured outputs, and rerun review.
10. Future expansion tracks: Michelin / fine-dining intelligence and Canadian commercial food-safety support after current roadmap gates are complete.

See `docs/open-source-roadmap.md` for the public-release workflow and tracked future expansion ideas.

## Contributing

Use the GitHub issue templates for routing bugs, skill proposals, food-safety concerns, and evaluation fixture ideas. Pull requests should run `.\scripts\validate-all.ps1` and update scorecards, docs, or release notes when reader expectations change.

## License

MIT
