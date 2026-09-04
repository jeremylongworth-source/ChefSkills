# ChefSkills AI Project Context

ChefSkills is a specialist skill framework for AI agents that need chef-like culinary reasoning.

The project is now a public open source repository for alpha review because the framework is safe, reviewable, validated, and maintainable enough for outside users and contributors.

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

The `CHEFSKILLS-06 Public Alpha Readiness` milestone is complete for `v0.1.0-alpha`, with GitHub Actions validation confirmed on `main`, issue forms, a pull request template, README quickstart updates, evaluation-confidence labeling, release notes, publication audit, repository settings review, evidence decision, public launch check, and GitHub prerelease.

The publication audit in `docs/audits/2026-09-03-publication-audit.md` found no blockers in the current tracked tree or history.

The repository settings review in `docs/audits/2026-09-03-repository-settings-review.md` enabled available Dependabot maintenance settings and documented the branch-protection constraint that existed before public visibility.

The `v0.1.0-alpha` evidence decision in `docs/releases/v0.1.0-alpha-evidence-decision.md` accepts medium-confidence simulated before/after evidence for public alpha while keeping live-output evaluation as post-alpha work.

The public launch check in `docs/audits/2026-09-03-public-launch-check.md` confirms public repository visibility, `main` branch protection, security maintenance settings, public Security policy visibility, issue form files, and the GitHub prerelease.

ChefSkills is installable through GitHub CLI agent skills for GitHub Copilot at the atomic skill level. `gh skill publish --dry-run` passes, direct `gh skill install jeremylongworth-source/ChefSkills chef-core` works, and pinned install smoke tests passed for `chef-core`. The Copilot-facing distribution release is `v0.1.0-public-preview`; setup guidance lives in `docs/setup/github-copilot.md`.

The open source release workflow is tracked in `docs/open-source-roadmap.md`. The next roadmap work should move to post-alpha improvement: first live-output capture, first contributor-flow observations, and then the next specialist track.

`CHEFSKILLS-07 Live Output Harness` starts the post-public evidence improvement track. It adds provider-neutral scripts and docs for creating live run prompt packets from existing fixtures, validating live run manifests, recording prompt and output hashes, and connecting captured raw outputs back into the report/scorecard workflow. The harness is scaffolding only until the first real model outputs are captured.

Two future expansion tracks have been captured from the ChefSkills ChatGPT project notes:

- Michelin / fine-dining intelligence: use public Michelin Guide concepts as one fine-dining analysis lens while avoiding star-prediction, certification, affiliation, or guarantee claims.
- Canadian commercial food safety: support Canada-specific commercial safe-food-handling reasoning while preserving federal, provincial, territorial, regional, and municipal boundaries and refusing compliance certification.
