# ChefSkills AI Project Context

ChefSkills is a specialist skill framework for AI agents that need chef-like culinary reasoning.

The project goal is to become a public open source repository when the framework is safe, reviewable, validated, and maintainable enough for outside users and contributors.

The project should not start by collecting recipes. It should start by proving a reusable decision system:

- classify culinary requests
- activate the smallest useful skill chain
- reason from current cooking state to target state
- use food safety as a hard gate
- explain mechanisms and observable cues
- validate behavior with scenarios

The first foundation contains eight skills:

- `chef-core`
- `culinary-reasoning`
- `ingredient-knowledge`
- `cooking-techniques`
- `ingredient-substitution`
- `recipe-development`
- `recipe-scaling`
- `food-safety`

The `CHEFSKILLS-02 Culinary Router` now expands `router/` into a more complete decision layer with task confidence, ambiguity handling, negative routing, and a 60-case routing catalog.

The `CHEFSKILLS-03 Culinary State Model` now expands `state/` into a reusable representation of ingredients, transformations, dish state, equipment state, workflow stage, observed cues, recovery actions, and safety status.

The `CHEFSKILLS-04 Evaluation Engine` now turns routing and state-model expectations into stronger scoring, fixtures, safety gates, and regression checks.

The `CHEFSKILLS-05A Foundation Evaluation` now has three smoke before/after reports comparing baseline and ChefSkills-enabled outputs for troubleshooting, safety, scaling, raw-fish review, structural substitution, preservation storage, and state-reasoned failure recovery fixtures.

The `CHEFSKILLS-05B Foundation Improvements` milestone tightens state-recovery expectations in the foundation skills, adds source-check expectations for precise high-risk safety guidance, and introduces validated JSON scorecards for report aggregation.

The `CHEFSKILLS-05C Readiness` artifact summarizes scorecard trends across 3 reports and 9 fixtures. The decision is ready for limited specialist expansion with medium confidence, starting with sauce work, baking structure, and protein cookery.

The `CHEFSKILLS-05C Specialist Expansion` milestone now begins that limited expansion with `sauce-work`, `baking-structure`, and `protein-cookery`, each backed by routing scenarios, state examples, fixtures, and a specialist smoke scorecard.

The `CHEFSKILLS-05C Specialist Stabilization` milestone adds two more fixtures per first-wave specialist and action-first communication guidance.

The `CHEFSKILLS-05C Fermentation Expansion` milestone adds `fermentation` as the next specialist domain, with source-checked preservation controls, routing scenarios, state examples, fixtures, and a fermentation smoke scorecard.

The `CHEFSKILLS-05C Fermentation Stabilization` milestone adds lower-risk fermentation quality, starter, brine, temperature, and storage-boundary fixtures. The aggregate evidence covers 7 reports and 27 fixtures with no blockers.

The `CHEFSKILLS-05C Equipment Expansion` milestone adds `equipment-cookery` as the next specialist domain, with source-checked safety handling for slow cookers, microwaves, and pressure canning plus lower-risk coverage for sheet-pan browning and skillet substitution.

The `CHEFSKILLS-05C Equipment Stabilization` milestone adds ovens, broilers, grills, induction, air fryers, damaged or incompatible cookware, thermometers, altitude, and capacity planning coverage. The aggregate evidence covers 9 reports and 38 fixtures with no blockers.

The next major artifact should start `CHEFSKILLS-06 Public Alpha Readiness Workflow` before moving to pastry, cuisine, service, costing, Michelin / fine-dining intelligence, or Canadian commercial food-safety work.

The open source release workflow is tracked in `docs/open-source-roadmap.md`. Public release should wait until evaluation credibility labeling, CI/templates, public docs, publication audits, and `v0.1.0-alpha` release notes are complete.

Two future expansion tracks have been captured from the ChefSkills ChatGPT project notes:

- Michelin / fine-dining intelligence: use public Michelin Guide concepts as one fine-dining analysis lens while avoiding star-prediction, certification, affiliation, or guarantee claims.
- Canadian commercial food safety: support Canada-specific commercial safe-food-handling reasoning while preserving federal, provincial, territorial, regional, and municipal boundaries and refusing compliance certification.
