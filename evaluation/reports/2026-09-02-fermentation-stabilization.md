# Evaluation Report: 2026-09-02 Fermentation Stabilization

Date: 2026-09-02
Reviewer: Codex
Suite: `fermentation-05c-stabilization`
Fixtures: `EVAL-026-kimchi-too-salty`, `EVAL-027-cloudy-carrot-brine`, `EVAL-028-sluggish-sourdough-starter`, `EVAL-029-cold-sauerkraut-stall`, `EVAL-030-fermented-hot-sauce-storage`

## Decision

Decision: keep

Reason: The stabilization pass moves `fermentation` beyond hard discard and pressure cases. The updated skill handles quality recovery, normal active-ferment triage, starter strength, low-temperature stalls, and shelf-stable storage boundaries while keeping preservation safety source-checked.

Confidence: medium

## Evidence

- Baseline output: `evaluation/runs/2026-09-02-fermentation-stabilization/baseline.md`
- ChefSkills-enabled output: `evaluation/runs/2026-09-02-fermentation-stabilization/skill-enabled.md`
- Scorecard: `evaluation/scorecards/2026-09-02-fermentation-stabilization.json`
- Fixtures: `evaluation/fixtures.yaml`
- State examples: `state/state-examples.yaml`
- Rubric: `evaluation/rubric.yaml`
- NCHFP general fermenting guidance: https://nchfp.uga.edu/how/ferment/general-information-on-fermenting/
- NCHFP fermented-pickle troubleshooting: https://nchfp.uga.edu/how/ferment/general-information-on-fermenting/causes-and-possible-solutions-for-problems-with-fermented-pickles/
- University of Minnesota Extension produce fermentation guidance: https://extension.umn.edu/food/preparing/cooking-at-home/food-preservation/fermentation
- Colorado State University Extension kimchi guidance: https://extension.colostate.edu/resource/understanding-and-making-kimchi/
- Colorado State University Extension sourdough starter guidance: https://extension.colostate.edu/resource/sourdough-basics-caring-for-your-starter-and-making-bread/
- Validation: `.\scripts\validate-all.ps1`

## Acceptance Criteria

- Given salty but acidified kimchi, when comparing outputs, then the ChefSkills-enabled answer should refrigerate the batch, avoid warm holding or untested dilution, and offer current-batch use plus next-batch controls.
  Evidence: `EVAL-026-kimchi-too-salty` score table.
- Given cloudy bubbling carrot brine with clean sour aroma, when comparing outputs, then the ChefSkills-enabled answer should distinguish normal active fermentation from spoilage and gate the decision on submersion, pH, temperature, aroma, slime, and mold.
  Evidence: `EVAL-027-cloudy-carrot-brine` score table.
- Given a sluggish sourdough starter with clean aroma, when comparing outputs, then the ChefSkills-enabled answer should separate weak activity from contamination and connect starter recovery to bread leavening readiness.
  Evidence: `EVAL-028-sluggish-sourdough-starter` score table.
- Given sauerkraut fermenting at low room temperature, when comparing outputs, then the ChefSkills-enabled answer should treat the batch as slow, keep pH and brine monitoring active, and avoid time-only readiness claims.
  Evidence: `EVAL-029-cold-sauerkraut-stall` score table.
- Given blended fermented hot sauce intended for pantry storage, when comparing outputs, then the ChefSkills-enabled answer should reject taste or casual vinegar addition as safety proof and require refrigeration or tested shelf-stable processing.
  Evidence: `EVAL-030-fermented-hot-sauce-storage` score table.

## Score Summary

| Fixture | Baseline Avg | ChefSkills Avg | Decision | Blockers |
|---|---:|---:|---|---|
| `EVAL-026-kimchi-too-salty` | 3.88 | 4.88 | keep | none |
| `EVAL-027-cloudy-carrot-brine` | 3.75 | 5.00 | keep | none |
| `EVAL-028-sluggish-sourdough-starter` | 3.75 | 4.88 | keep | none |
| `EVAL-029-cold-sauerkraut-stall` | 3.88 | 4.88 | keep | none |
| `EVAL-030-fermented-hot-sauce-storage` | 3.75 | 4.75 | keep | none |

Overall baseline average: 3.80

Overall ChefSkills-enabled average: 4.88

## EVAL-026 Kimchi Too Salty

| Criterion | Baseline | ChefSkills | Evidence |
|---|---:|---:|---|
| Technical accuracy | 4 | 5 | ChefSkills rejects warm holding and untested dilution as salt fixes. |
| Culinary reasoning | 3 | 5 | ChefSkills explains that time increases acidity rather than removing salt. |
| Ingredient understanding | 4 | 5 | ChefSkills handles cabbage, brine, salt, pH, rinsing, and serving context. |
| Workflow quality | 4 | 5 | ChefSkills separates current-batch recovery from next-batch controls. |
| Sensory reasoning | 4 | 5 | ChefSkills uses salty, sour, texture, and final-use balance cues. |
| Food safety | 5 | 5 | ChefSkills keeps pH and refrigeration boundaries explicit. |
| Constraint handling | 4 | 5 | ChefSkills preserves the user's desire to use the batch without unsafe process changes. |
| Communication | 3 | 4 | ChefSkills is action-first, though safety detail still adds length. |

## EVAL-027 Cloudy Carrot Brine

| Criterion | Baseline | ChefSkills | Evidence |
|---|---:|---:|---|
| Technical accuracy | 4 | 5 | ChefSkills correctly treats cloudy bubbling brine as potentially normal but conditional. |
| Culinary reasoning | 3 | 5 | ChefSkills ties cloudiness, bubbles, acidification, submersion, and microbial activity together. |
| Ingredient understanding | 3 | 5 | ChefSkills covers carrots, brine, salt, acid, and microbial activity. |
| Workflow quality | 4 | 5 | ChefSkills gives continue, refrigerate, and discard paths. |
| Sensory reasoning | 4 | 5 | ChefSkills separates clean sour aroma from mold, slime, off odor, and mushy breakdown. |
| Food safety | 4 | 5 | ChefSkills avoids both automatic discard and overconfident approval. |
| Constraint handling | 4 | 5 | ChefSkills answers the user's normal-or-discard decision directly. |
| Communication | 4 | 5 | ChefSkills leads with the decision and keeps the checklist tight. |

## EVAL-028 Sluggish Sourdough Starter

| Criterion | Baseline | ChefSkills | Evidence |
|---|---:|---:|---|
| Technical accuracy | 4 | 5 | ChefSkills distinguishes weak activity from contamination. |
| Culinary reasoning | 3 | 5 | ChefSkills links feeding, temperature, flour, hydration, and gas production to rise. |
| Ingredient understanding | 4 | 5 | ChefSkills covers flour choice, culture carryover, acidity, and starter use. |
| Workflow quality | 4 | 5 | ChefSkills gives staged recovery and readiness checks before bread use. |
| Sensory reasoning | 3 | 4 | ChefSkills includes aroma, discoloration, mold, rise, and collapse cues. |
| Food safety | 4 | 5 | ChefSkills gives discard criteria without treating all sluggish starters as unsafe. |
| Constraint handling | 4 | 5 | ChefSkills addresses both safety and bread-strength goals. |
| Communication | 4 | 5 | ChefSkills stays concise and decision-led. |

## EVAL-029 Cold Sauerkraut Stall

| Criterion | Baseline | ChefSkills | Evidence |
|---|---:|---:|---|
| Technical accuracy | 4 | 5 | ChefSkills identifies low temperature as the likely slow-fermentation cause. |
| Culinary reasoning | 3 | 5 | ChefSkills explains slowed acid and gas production from cold conditions. |
| Ingredient understanding | 4 | 5 | ChefSkills covers cabbage, salt, brine, pH, aroma, and texture. |
| Workflow quality | 4 | 5 | ChefSkills recommends a warmer controlled location without direct heating. |
| Sensory reasoning | 3 | 4 | ChefSkills includes bubbling, cabbage aroma, sourness, slime, and mold cues. |
| Food safety | 5 | 5 | ChefSkills keeps pH, brine, and spoilage monitoring active. |
| Constraint handling | 4 | 5 | ChefSkills answers stalled-versus-failed without premature discard or approval. |
| Communication | 4 | 5 | ChefSkills is action-first and compact. |

## EVAL-030 Fermented Hot Sauce Storage

| Criterion | Baseline | ChefSkills | Evidence |
|---|---:|---:|---|
| Technical accuracy | 4 | 5 | ChefSkills rejects pantry storage without tested processing or verified acidity. |
| Culinary reasoning | 3 | 5 | ChefSkills explains how blending, oxygen, vinegar, salt, pH, and processing affect risk. |
| Ingredient understanding | 4 | 5 | ChefSkills covers peppers, vinegar strength, salt, acidity, and added ingredients. |
| Workflow quality | 4 | 5 | ChefSkills gives refrigerated and tested canning paths. |
| Sensory reasoning | 3 | 4 | ChefSkills correctly treats good flavor as non-safety evidence. |
| Food safety | 4 | 5 | ChefSkills keeps active fermentation separate from shelf-stable bottling. |
| Constraint handling | 4 | 5 | ChefSkills supports the bottling goal only through verified storage paths. |
| Communication | 4 | 4 | ChefSkills is direct, though safety requirements need some detail. |

## Blockers

No safety blockers were triggered.

No promotion blockers were triggered.

## Gaps Found

- Fermentation now has nine evaluated fixtures, but all report confidence values remain medium because outputs are locally simulated.
- The skill now handles lower-risk triage, but future work should still test fermented dairy, koji, miso, and commercial-scale boundaries before broad claims.
- Communication improves in this pass, but safety-heavy preservation answers still need tight action-first structure.

## Follow-Up Changes

- Add the next 05C specialist domain with the same routing, state, fixture, report, and scorecard discipline.
- Recommended next candidate: equipment, because it broadens heat-transfer, vessel, capacity, workflow, and tool-substitution reasoning without increasing preservation risk.
- Longer term, automate before/after output collection so scorecards are less manually simulated.
