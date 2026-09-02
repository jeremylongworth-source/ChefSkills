# CHEFSKILLS-05C Fermentation Stabilization

## Purpose

This milestone stabilizes `fermentation` after the initial smoke pass.

The goal is to prove that fermentation guidance handles quality recovery and ordinary process triage, not only hard safety rejections, while preserving source-checked preservation boundaries.

## Scope

- Added five fermentation depth scenarios.
- Added matching routing catalog entries, expected routes, state examples, fixtures, and a regression suite.
- Tightened `fermentation` guidance for action-first answers, normal-versus-spoilage triage, sourdough starter recovery, low-temperature stalls, and shelf-stable storage boundaries.
- Added a registered before/after report, raw outputs, JSON scorecard, and regenerated aggregate scorecard summary.

## Scenario Coverage

- `kimchi-too-salty`: acidified but overly salty kimchi, with current-batch recovery and next-batch controls.
- `cloudy-carrot-brine`: normal active vegetable fermentation signs versus spoilage cues.
- `sluggish-sourdough-starter`: weak starter activity separated from contamination and bread leavening readiness.
- `cold-sauerkraut-stall`: low-temperature fermentation slowdown without premature discard or time-only approval.
- `fermented-hot-sauce-storage`: refrigerator storage versus shelf-stable bottling after blending fermented pepper mash.

## Scorecard Result

The fermentation stabilization report scored a baseline average of 3.8000, a ChefSkills-enabled average of 4.8750, and a delta of 1.0750 with no blockers.

After adding this report, the aggregate summary contains 7 reports, 27 fixtures, no blockers, a baseline average of 3.7778, a ChefSkills-enabled average of 4.8148, and a delta of 1.0370.

## Safety Sources

- NCHFP general fermenting guidance: https://nchfp.uga.edu/how/ferment/general-information-on-fermenting/
- NCHFP fermented-pickle troubleshooting: https://nchfp.uga.edu/how/ferment/general-information-on-fermenting/causes-and-possible-solutions-for-problems-with-fermented-pickles/
- University of Minnesota Extension produce fermentation guidance: https://extension.umn.edu/food/preparing/cooking-at-home/food-preservation/fermentation
- Colorado State University Extension kimchi guidance: https://extension.colostate.edu/resource/understanding-and-making-kimchi/
- Colorado State University Extension sourdough starter guidance: https://extension.colostate.edu/resource/sourdough-basics-caring-for-your-starter-and-making-bread/

The safety-gated fixtures use these sources for pH readiness, brine coverage, temperature, finished-ferment refrigeration, kimchi pH and storage expectations, sourdough starter storage and activity, spoilage discard cues, and tested shelf-stable processing boundaries.

## Acceptance Criteria

Given the five fermentation stabilization scenarios, when `python .\scripts\validate-scenarios.py` and `python .\scripts\validate-router.py` run, then every scenario should have a catalog case, expected route, known skill folders, and no route above the hard ceiling.
Evidence: command output.

Given the new fermentation state examples and fixtures, when `python .\scripts\validate-state.py` and `python .\scripts\validate-evaluation.py` run, then every fixture should reference a known scenario, state example, expected route, and regression suite.
Evidence: command output.

Given salty kimchi, clean cloudy brine, sluggish sourdough starter, cold sauerkraut, and blended hot sauce storage cases, when scoring the skill-enabled outputs, then the answers should distinguish quality recovery from safety gates and avoid both premature discard and overconfident preservation claims.
Evidence: `EVAL-026` through `EVAL-030` score tables.

Given the communication watch item, when reviewing the updated fermentation skill, then answers should lead with the decision or next action before mechanism detail.
Evidence: `skills/fermentation/SKILL.md`.

Given the new report scorecard, when `python .\scripts\validate-scorecards.py` and `python .\scripts\summarize-scorecards.py --check .\evaluation\scorecards\summary.json` run, then the scorecard and aggregate summary should be current.
Evidence: command output.

## Follow-On Status

Fermentation now has nine evaluated fixtures across smoke and stabilization reports.

Recommended next milestone: `CHEFSKILLS-05C Equipment Specialist Expansion`, because it can test heat-transfer, vessel capacity, appliance constraints, workflow, and tool-substitution reasoning without adding another high-preservation-risk domain.
