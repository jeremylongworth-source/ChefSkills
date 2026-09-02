# CHEFSKILLS-05B Foundation Improvements

## Purpose

This milestone applies the repeated findings from `CHEFSKILLS-05A` without broadly rewriting the foundation.

The evidence showed that ChefSkills improves outputs most consistently when it forces a clear state transition: current observable state, target state, mechanism, staged intervention, side effects, and verification cue.

## Changes

- Added a `State Recovery Pattern` to `chef-core`.
- Tightened `culinary-reasoning` so troubleshooting includes target state, staged adjustments, side effects, and stop cues.
- Updated `ingredient-knowledge` and `cooking-techniques` to support state-aware recovery when they are part of a troubleshooting route.
- Added a source-check expectation to `food-safety` for precise high-risk or evaluation-critical safety guidance.
- Added machine-readable JSON scorecards for the three existing evaluation reports.
- Added scorecard validation and wired it into `.\scripts\validate-all.ps1`.

## Acceptance Criteria

Given a troubleshooting or recovery request, when `chef-core` and `culinary-reasoning` are active, then the answer should make the state transition visible enough to identify current state, target state, mechanism, staged intervention, side effects, and verification cue.
Evidence: `skills/chef-core/SKILL.md`, `skills/culinary-reasoning/SKILL.md`, and skill checklist updates.

Given an ingredient-driven or technique-driven recovery request, when `ingredient-knowledge` or `cooking-techniques` supports the route, then the answer should connect ingredient or technique behavior to the state gap and stop condition instead of listing generic facts.
Evidence: `skills/ingredient-knowledge/SKILL.md`, `skills/cooking-techniques/SKILL.md`, and checklist updates.

Given a safety-gated evaluation output with precise high-risk guidance, when the guidance depends on current limits or public rules, then the output should include a source-check note or use conservative uncertainty wording.
Evidence: `skills/food-safety/SKILL.md` and `skills/food-safety/references/food-safety-checklist.md`.

Given a registered evaluation report, when `python .\scripts\validate-scorecards.py` runs, then its JSON scorecard should match the report index, reference known fixtures and rubric criteria, and have valid averages and deltas.
Evidence: command output.

Given the full validation command, when `.\scripts\validate-all.ps1` runs, then scorecard validation runs with the existing checks.
Evidence: command output.

## Validation

Run:

```powershell
.\scripts\validate-all.ps1
```

## Follow-On Status

- Scorecard trends are summarized in `evaluation/scorecards/summary.json`.
- The readiness decision is documented in `docs/chefskills-05c-readiness.md`.
- `CHEFSKILLS-05C` should start with a small specialist scope and require routing cases, fixtures, and scorecards for each new specialist skill.
