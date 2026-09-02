# Recipe Development Bundle Brief

## Problem

Recipe work needs more than a plausible ingredient list. Agents must handle intent, constraints, ingredient function, technique, scaling, testing notes, and safety.

## Target User

Recipe developers, content creators, home cooks, culinary educators, and teams building cooking assistants.

## Included Skills

- `chef-core`: baseline chef behavior and quality bar.
- `culinary-reasoning`: technique and mechanism tradeoffs.
- `ingredient-knowledge`: ingredient behavior and function.
- `cooking-techniques`: process selection and cues.
- `ingredient-substitution`: swaps and adaptations.
- `recipe-development`: recipe structure, iteration, and testing.
- `sauce-work`: sauce design, texture, finishing, and recovery.
- `baking-structure`: baked-good structure, hydration, leavening, and crumb troubleshooting.
- `protein-cookery`: protein doneness, method choice, carryover, and safety-aware quality tradeoffs.
- `fermentation`: fermented foods, brines, pH, salt, spoilage, gas pressure, and storage controls.
- `recipe-scaling`: portions, batch size, and workflow.
- `food-safety`: safety review for risky ingredients or processes.

## Context Files

- `skills/recipe-development/SKILL.md`
- `skills/recipe-development/references/recipe-development-checklist.md`
- `router/routing-rules.yaml`
- `state/culinary-state.yaml`
- `tests/scenarios/sauce-for-forty.md`

## Safety Rules

- Review raw animal products, holding, reheating, preservation, and vulnerable diners.
- Mark missing safety-critical facts instead of guessing.
- Keep medical nutrition and regulated food-service claims subject to professional review.

## Pilot Metrics

- Recipes include quantities, prep state, sequence, heat, timing, cues, failure points, and serving assumptions.
- Scaling changes workflow and vessel assumptions where needed.
- Substitutions preserve functional role or explain tradeoffs.
- Specialist work on sauces, baked structure, and proteins includes mechanism and verification cues.
- Fermentation work uses tested proportions and source-checked safety boundaries.

## Acceptance Criteria

- The bundle installs as a focused recipe-development profile.
- Generated recipes include sensory cues and critical failure points.
- Scaling and substitutions are not treated as pure arithmetic.
- Safety review is triggered when relevant.
- Sauce, baking, and protein cases route to the relevant specialist skill.
- Fermentation cases route to `fermentation` and keep `food-safety` active when preservation or spoilage risks exist.
