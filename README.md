# ChefSkills

Portable culinary Agent Skills for AI agents that need to reason about cooking as a changing physical system.

[GitHub Copilot setup](docs/setup/github-copilot.md) | [Wiki](https://github.com/jeremylongworth-source/ChefSkills/wiki) | [Contributing](CONTRIBUTING.md) | [Security](SECURITY.md)

## What ChefSkills provides

ChefSkills is a reviewable behavior framework for culinary AI. It gives an agent focused skills, routing rules, a cooking-state model, and evaluation fixtures so it can reason from the current situation to a useful and safe next step.

It is designed for:

- agent builders who need portable culinary behavior
- contributors who want to improve one auditable decision at a time
- evaluators who need scenarios, reports, scorecards, and safety gates

ChefSkills is not a recipe database, a culinary credential, or a substitute for current medical, regulatory, or food-safety advice.

## Current release

ChefSkills is public alpha software. The current GitHub skill-install distribution is [`v0.1.0-public-preview`](https://github.com/jeremylongworth-source/ChefSkills/releases/tag/v0.1.0-public-preview); the initial public alpha prerelease is [`v0.1.0-alpha`](https://github.com/jeremylongworth-source/ChefSkills/releases/tag/v0.1.0-alpha).

Current repository evidence includes 9 reports and 38 evaluated fixtures. The before/after outputs are medium-confidence local reviewer simulations, not live benchmark runs. A provider-neutral live-output capture packet is available under [`evaluation/live-runs/`](evaluation/live-runs/), and its first foundation packet is still pending capture.

## Quick start

### Install a skill for GitHub Copilot

Requirements:

- GitHub CLI with `gh skill` support
- a project or user scope where the skill should be installed

Preview the pinned public-preview release:

```powershell
gh skill preview jeremylongworth-source/ChefSkills chef-core@v0.1.0-public-preview
```

Install the core skill at project scope:

```powershell
gh skill install jeremylongworth-source/ChefSkills chef-core --agent github-copilot --scope project --pin v0.1.0-public-preview
```

Install the food-safety skill alongside it:

```powershell
gh skill install jeremylongworth-source/ChefSkills food-safety --agent github-copilot --scope project --pin v0.1.0-public-preview
```

`gh skill install` installs atomic skill folders from `skills/`. The YAML files under `skillsets/` describe repository bundles; they are not installed by this command.

See [GitHub Copilot and `gh skill` Setup](docs/setup/github-copilot.md) for specialist skills, user scope, verification, and maintenance guidance.

### Clone and validate the repository

```powershell
git clone https://github.com/jeremylongworth-source/ChefSkills.git
cd ChefSkills
python --version
.\scripts\validate-all.ps1
```

The repository requires Python 3.10 or newer. The full wrapper also requires PowerShell. It validates skill files, skillsets, routing, state, evaluation fixtures, live-run manifests, reports, scorecards, and the generated scorecard summary.

If PowerShell is unavailable, run the individual Python commands in the [validation section of the evaluation documentation](evaluation/README.md#validation).

### Try a first route

ChefSkills routes a request to the smallest useful set of skills. For example:

```text
Prompt: My chicken thighs keep charring on the grill before they are cooked near the bone.
Route: chef-core, equipment-cookery, protein-cookery, food-safety, cooking-techniques
```

The route combines equipment behavior, protein doneness, technique, and safety without loading every specialist skill. Start with [`skillsets/chef.yaml`](skillsets/chef.yaml) for broad culinary work or [`skillsets/recipe-development.yaml`](skillsets/recipe-development.yaml) for recipe design and adaptation.

## How the framework works

| Layer | Role | Source |
|---|---|---|
| Skills | Focused, reusable behavior such as sauce recovery or fermentation triage | [`skills/`](skills/) |
| Skillsets | YAML bundles for common work modes | [`skillsets/`](skillsets/) |
| Router | Task classification and minimum useful skill selection | [`router/`](router/) |
| State model | Ingredients, transformations, workflow, observations, recovery, and safety status | [`state/`](state/) |
| Evaluation | Fixtures, regression suites, reports, scorecards, and hard safety gates | [`evaluation/`](evaluation/) |

The operating pattern is:

1. Classify the request.
2. Select one primary skill and the smallest useful supporting set.
3. Identify the observed cooking state and target state.
4. Explain the mechanism behind the gap.
5. Choose a staged intervention and verification cues.
6. Apply the food-safety gate before giving final guidance.

Read the [architecture guide](docs/architecture.md) for the full design and control flow.

## Available skills

### Foundation

| Skill | Focus |
|---|---|
| [`chef-core`](skills/chef-core/SKILL.md) | Broad culinary reasoning, planning, troubleshooting, and safety-aware behavior |
| [`culinary-reasoning`](skills/culinary-reasoning/SKILL.md) | Mechanism-based diagnosis and recovery |
| [`ingredient-knowledge`](skills/ingredient-knowledge/SKILL.md) | Ingredient roles, properties, storage, and behavior |
| [`cooking-techniques`](skills/cooking-techniques/SKILL.md) | Technique selection, heat control, sequence, and cues |
| [`ingredient-substitution`](skills/ingredient-substitution/SKILL.md) | Functional substitution and side-effect analysis |
| [`recipe-development`](skills/recipe-development/SKILL.md) | Recipe creation, testing, adaptation, and iteration |
| [`recipe-scaling`](skills/recipe-scaling/SKILL.md) | Portions, vessels, heat transfer, seasoning, and service workflow |
| [`food-safety`](skills/food-safety/SKILL.md) | Hazard recognition, conservative handling, storage, preservation, and discard guidance |

### Specialist

| Skill | Focus |
|---|---|
| [`sauce-work`](skills/sauce-work/SKILL.md) | Emulsions, reductions, starch, finishing, scaling, and recovery |
| [`baking-structure`](skills/baking-structure/SKILL.md) | Gluten, starch, hydration, binders, leavening, pan geometry, and crumb |
| [`protein-cookery`](skills/protein-cookery/SKILL.md) | Doneness, carryover, moisture, searing, braising, and safety-aware quality tradeoffs |
| [`fermentation`](skills/fermentation/SKILL.md) | Brines, salt, pH, gas, spoilage, storage, and home-fermentation boundaries |
| [`equipment-cookery`](skills/equipment-cookery/SKILL.md) | Appliances, vessels, capacity, airflow, pressure, heat transfer, and tool substitutions |

See the [wiki skill catalog](https://github.com/jeremylongworth-source/ChefSkills/wiki/Skill-Catalog) for the full catalog and selection guidance.

## Safety boundary

Food safety is a hard gate, not an average score. Activate `food-safety` when a request involves raw or undercooked animal products, time-temperature handling, preservation, fermentation, allergens, vulnerable diners, spoilage, equipment hazards, or regulated food service.

ChefSkills does not certify legal, medical, regulatory, commercial-kitchen, allergen, nutrition, or food-safety compliance. When exact thresholds or jurisdiction-specific requirements matter, use current authoritative sources and escalate to the relevant authority or qualified professional. When the safety history is uncertain, choose the conservative action.

See [Safety and Source Checks](https://github.com/jeremylongworth-source/ChefSkills/wiki/Safety-and-Source-Checks), [`skills/food-safety/SKILL.md`](skills/food-safety/SKILL.md), and [`SECURITY.md`](SECURITY.md).

## Evaluation and trust

The evaluation system is intended for regression decisions, not marketing benchmarks. It scores technical accuracy, culinary reasoning, ingredient understanding, workflow quality, sensory reasoning, safety, constraint handling, and communication. Serious safety failures block an otherwise strong result.

Use the [evaluation workflow](evaluation/README.md) to inspect fixtures and evidence, or the [live-output harness guide](docs/chefskills-07-live-output-harness.md) to create a provider-neutral prompt packet for external model capture.

## Repository map

```text
ChefSkills/
|-- skills/       focused Agent Skills and references
|-- skillsets/    YAML bundles for common work modes
|-- router/       classification schema and routing catalog
|-- state/        culinary state schema and examples
|-- evaluation/   fixtures, runs, reports, scorecards, and live packets
|-- tests/        routing and behavior scenarios
|-- scripts/      repository validators and evaluation tooling
`-- docs/         architecture, setup, roadmap, audits, and release notes
```

## Contributing

Start with [`CONTRIBUTING.md`](CONTRIBUTING.md) and choose the smallest change that improves a decision, route, safety boundary, evaluation fixture, validator, or public explanation.

Routing changes should update the relevant scenarios and expected routes. Behavior changes may also require state examples, fixtures, reports, scorecards, and documentation. Run the full validation suite before opening a pull request:

```powershell
.\scripts\validate-all.ps1
```

Use the issue forms for routing bugs, skill proposals, food-safety concerns, and evaluation fixture ideas. Review the [Code of Conduct](CODE_OF_CONDUCT.md) and [Security policy](SECURITY.md) before contributing.

## Roadmap

The public-alpha foundation and GitHub Copilot distribution are complete. The next evidence milestone is to capture and score the pending live foundation packet. Future expansion tracks include Michelin / fine-dining intelligence and Canadian commercial food safety; both remain scoped proposals with explicit non-certification boundaries.

See the [open-source roadmap](docs/open-source-roadmap.md) for acceptance criteria, evidence status, and release gates.

## License

ChefSkills is released under the [MIT License](LICENSE).
