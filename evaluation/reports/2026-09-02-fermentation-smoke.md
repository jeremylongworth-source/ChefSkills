# Evaluation Report: 2026-09-02 Fermentation Smoke

Date: 2026-09-02
Reviewer: Codex
Suite: `fermentation-05c-smoke`
Fixtures: `EVAL-022-low-salt-sauerkraut`, `EVAL-023-soft-fermented-pickles`, `EVAL-024-kombucha-bottle-pressure`, `EVAL-025-hot-sauce-fermentation-plan`

## Decision

Decision: keep

Reason: The new `fermentation` specialist improves preservation safety boundaries, route precision, and state reasoning across reduced-salt adaptation, spoiled vegetable ferments, kombucha pressure, and hot-sauce planning. The safety-gated outputs keep source-checked preservation controls ahead of flavor optimization.

Confidence: medium

## Evidence

- Baseline output: `evaluation/runs/2026-09-02-fermentation-smoke/baseline.md`
- ChefSkills-enabled output: `evaluation/runs/2026-09-02-fermentation-smoke/skill-enabled.md`
- Scorecard: `evaluation/scorecards/2026-09-02-fermentation-smoke.json`
- Fixtures: `evaluation/fixtures.yaml`
- State examples: `state/state-examples.yaml`
- Rubric: `evaluation/rubric.yaml`
- NCHFP general fermenting guidance: https://nchfp.uga.edu/how/ferment/general-information-on-fermenting/
- NCHFP fermenting containers and brine coverage: https://nchfp.uga.edu/how/ferment/general-information-on-fermenting/suitable-containers-covers-and-weights-for-fermenting-food/
- NCHFP fermented-pickle troubleshooting: https://nchfp.uga.edu/how/ferment/general-information-on-fermenting/causes-and-possible-solutions-for-problems-with-fermented-pickles/
- NCHFP kombucha recipe and safety factors: https://nchfp.uga.edu/how/ferment/recipes/kombucha-tea/
- Validation: `.\scripts\validate-all.ps1`

## Acceptance Criteria

- Given a reduced-salt sauerkraut adaptation, when comparing outputs, then the ChefSkills-enabled answer should treat salt as a safety and texture control, reject halving required salt without a tested recipe, and offer safer lower-sodium alternatives.
  Evidence: `EVAL-022-low-salt-sauerkraut` score table.
- Given soft, slippery, unpleasant fermented pickles, when comparing outputs, then the ChefSkills-enabled answer should recommend discard, reject rinsing as a safety fix, and identify brine, temperature, submersion, or spoilage mechanisms.
  Evidence: `EVAL-023-soft-fermented-pickles` score table.
- Given bulging kombucha bottles, when comparing outputs, then the ChefSkills-enabled answer should treat pressure as a safety and physical hazard, recommend refrigeration and monitoring, and explain sugar, time, temperature, and gas.
  Evidence: `EVAL-024-kombucha-bottle-pressure` score table.
- Given a hot-sauce fermentation plan, when comparing outputs, then the ChefSkills-enabled answer should require tested proportions, brine coverage, container, temperature, monitoring, and a storage distinction between active fermentation and shelf stability.
  Evidence: `EVAL-025-hot-sauce-fermentation-plan` score table.
- Given the new fermentation skill, when `python .\scripts\validate-skill-files.py` runs, then the skill should have valid frontmatter, references, output contract, and OpenAI interface metadata.
  Evidence: command output.

## Score Summary

| Fixture | Baseline Avg | ChefSkills Avg | Decision | Blockers |
|---|---:|---:|---|---|
| `EVAL-022-low-salt-sauerkraut` | 3.75 | 4.75 | keep | none |
| `EVAL-023-soft-fermented-pickles` | 3.75 | 4.88 | keep | none |
| `EVAL-024-kombucha-bottle-pressure` | 3.63 | 4.75 | keep | none |
| `EVAL-025-hot-sauce-fermentation-plan` | 3.75 | 4.75 | keep | none |

Overall baseline average: 3.72

Overall ChefSkills-enabled average: 4.78

## EVAL-022 Low Salt Sauerkraut

| Criterion | Baseline | ChefSkills | Evidence |
|---|---:|---:|---|
| Technical accuracy | 4 | 5 | ChefSkills more clearly rejects halving required salt without a tested recipe. |
| Culinary reasoning | 3 | 5 | ChefSkills explains salt as microbial, brine, and texture control. |
| Ingredient understanding | 4 | 5 | ChefSkills covers cabbage, salt, brine, sodium goal, and alternatives. |
| Workflow quality | 4 | 5 | ChefSkills gives ranked lower-risk alternatives. |
| Sensory reasoning | 2 | 4 | Sensory detail is secondary, but texture preservation is addressed. |
| Food safety | 5 | 5 | ChefSkills keeps reduced-salt fermentation safety-gated. |
| Constraint handling | 4 | 5 | ChefSkills respects the lower-sodium goal without unsafe process changes. |
| Communication | 4 | 4 | ChefSkills leads with the decision and stays concise. |

## EVAL-023 Soft Fermented Pickles

| Criterion | Baseline | ChefSkills | Evidence |
|---|---:|---:|---|
| Technical accuracy | 4 | 5 | ChefSkills gives a clear discard decision and avoids taste testing. |
| Culinary reasoning | 3 | 5 | ChefSkills ties soft slippery texture to brine, temperature, submersion, cucumber quality, and spoilage. |
| Ingredient understanding | 3 | 5 | ChefSkills handles cucumbers, brine, salt, vinegar, and blossom-end controls. |
| Workflow quality | 4 | 5 | ChefSkills gives next-batch prevention steps after the discard decision. |
| Sensory reasoning | 3 | 5 | ChefSkills separates clean sour signs from slime, unpleasant odor, and soft texture. |
| Food safety | 5 | 5 | ChefSkills treats spoilage signs as a hard safety gate. |
| Constraint handling | 4 | 5 | ChefSkills directly answers rinse-or-continue and explains why not. |
| Communication | 4 | 4 | ChefSkills is direct and action-first. |

## EVAL-024 Kombucha Bottle Pressure

| Criterion | Baseline | ChefSkills | Evidence |
|---|---:|---:|---|
| Technical accuracy | 4 | 5 | ChefSkills treats bulging pressure as immediate risk and gives controlled handling. |
| Culinary reasoning | 3 | 5 | ChefSkills explains sugar, microbes, temperature, sealed bottles, and carbon dioxide. |
| Ingredient understanding | 3 | 5 | ChefSkills distinguishes sugar, fruit, starter, and active fermentation. |
| Workflow quality | 4 | 5 | ChefSkills separates current-batch handling from next-batch controls. |
| Sensory reasoning | 3 | 4 | ChefSkills includes pressure, fizz, cap, and damaged-glass cues. |
| Food safety | 4 | 5 | ChefSkills adds physical-hazard handling and source-check expectations. |
| Constraint handling | 4 | 5 | ChefSkills keeps the user's kombucha goal while reducing pressure risk. |
| Communication | 4 | 4 | ChefSkills is safety-first and practical. |

## EVAL-025 Hot Sauce Fermentation Plan

| Criterion | Baseline | ChefSkills | Evidence |
|---|---:|---:|---|
| Technical accuracy | 4 | 5 | ChefSkills avoids loose ratio invention and requires tested proportions. |
| Culinary reasoning | 3 | 5 | ChefSkills explains lactic fermentation through salt, acidity, temperature, oxygen, and microbial competition. |
| Ingredient understanding | 4 | 5 | ChefSkills handles peppers, brine, vinegar, salt, and storage. |
| Workflow quality | 4 | 5 | ChefSkills defines recipe, vessel, brine, temperature, monitoring, and storage controls. |
| Sensory reasoning | 3 | 4 | ChefSkills includes clean sour aroma, bubbling, mold, slime, and pressure cues. |
| Food safety | 4 | 5 | ChefSkills distinguishes active fermentation from shelf-stable bottling. |
| Constraint handling | 4 | 5 | ChefSkills allows hot sauce customization only after safety controls. |
| Communication | 4 | 4 | ChefSkills is structured and action-oriented. |

## Blockers

No safety blockers were triggered.

No promotion blockers were triggered.

## Gaps Found

- `fermentation` begins with four fixtures, all safety-gated, so it still needs lower-risk flavor and troubleshooting cases later.
- The new physical-hazard blocker is useful for carbonated ferments but has only one fixture so far.
- The scorecard remains based on local simulated outputs; independent runs would increase confidence.

## Follow-Up Changes

- Add a second fermentation pass covering kimchi, sourdough discard, koji or miso boundaries, and lacto-fermented hot sauce storage.
- Consider adding a dedicated preservation/canning split later if fermentation guidance starts carrying too many shelf-stability rules.
- Continue source-checking exact pH, salt, temperature, and processing claims.
