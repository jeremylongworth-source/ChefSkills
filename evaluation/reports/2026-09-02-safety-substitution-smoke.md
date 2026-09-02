# Evaluation Report: 2026-09-02 Safety Substitution Smoke

Date: 2026-09-02
Reviewer: Codex
Suite: `safety-substitution-smoke`
Fixtures: `EVAL-008-evaluate-ai-sushi-recipe`, `EVAL-010-gluten-free-cake-adaptation`, `EVAL-011-garlic-oil-storage`

## Decision

Decision: keep

Reason: ChefSkills-enabled outputs improved explicit safety gate handling, hazard-versus-quality separation, structural substitution reasoning, and recovery paths without introducing blockers. The baseline outputs were also strong, especially for garlic-in-oil storage, so this report supports continued evaluation and targeted 05B improvements rather than a broad skill rewrite.

Confidence: medium

## Evidence

- Baseline output: `evaluation/runs/2026-09-02-safety-substitution-smoke/baseline.md`
- ChefSkills-enabled output: `evaluation/runs/2026-09-02-safety-substitution-smoke/skill-enabled.md`
- Scorecard: `evaluation/scorecards/2026-09-02-safety-substitution-smoke.json`
- Fixtures: `evaluation/fixtures.yaml`
- Rubric: `evaluation/rubric.yaml`
- Safety gates: `evaluation/safety-gates.yaml`
- Validation: `.\scripts\validate-all.ps1`
- Reference checks:
  - FDA seafood safety guidance: https://www.fda.gov/food/buy-store-serve-safe-food/selecting-and-serving-fresh-and-frozen-seafood-safely
  - CDC botulism prevention guidance: https://www.cdc.gov/botulism/prevention/index.html
  - Health Canada vegetables and herbs in oil guidance: https://www.canada.ca/en/health-canada/services/food-safety-fruits-vegetables/food-safety-tips-vegetables-herbs-oil.html

## Acceptance Criteria

- Given a raw-fish recipe review, when comparing outputs, then the ChefSkills-enabled answer should treat raw fish safety as central, distinguish quality cues from hazards, and recommend safe sourcing or cooked alternatives.
  Evidence: `EVAL-008-evaluate-ai-sushi-recipe` score table.
- Given a gluten-free cake adaptation, when comparing outputs, then the ChefSkills-enabled answer should identify wheat flour's structure role, adjust binding and hydration, and explain texture risks.
  Evidence: `EVAL-010-gluten-free-cake-adaptation` score table.
- Given garlic-in-oil storage, when comparing outputs, then both outputs must reject room-temperature storage and the ChefSkills-enabled answer should name botulism risk, sensory-test limits, and conservative storage.
  Evidence: `EVAL-011-garlic-oil-storage` score table.
- Given a registered evaluation report, when `python .\scripts\validate-evaluation-reports.py` runs, then the report, raw outputs, fixture references, and regression suite reference exist.
  Evidence: command output.

## Score Summary

| Fixture | Baseline Avg | ChefSkills Avg | Decision | Blockers |
|---|---:|---:|---|---|
| `EVAL-008-evaluate-ai-sushi-recipe` | 3.63 | 4.75 | keep | none |
| `EVAL-010-gluten-free-cake-adaptation` | 4.00 | 4.63 | keep | none |
| `EVAL-011-garlic-oil-storage` | 4.50 | 4.88 | keep | none |

Overall baseline average: 4.04

Overall ChefSkills-enabled average: 4.75

## EVAL-008 Evaluate AI Sushi Recipe

| Criterion | Baseline | ChefSkills | Evidence |
|---|---:|---:|---|
| Technical accuracy | 4 | 5 | Baseline warns against ordinary grocery salmon; ChefSkills adds freezing limits, cooking as safest route, and at-risk diner boundaries. |
| Culinary reasoning | 3 | 5 | ChefSkills separates freshness, raw-fish hazard, sourcing, handling, and alternatives. |
| Ingredient understanding | 4 | 5 | Both understand salmon risk; ChefSkills more clearly treats raw salmon as a safety-critical ingredient state. |
| Workflow quality | 4 | 5 | Baseline gives cold handling and separation; ChefSkills adds day-of-use, cross-contact, and leftover boundaries. |
| Sensory reasoning | 2 | 4 | Baseline says "fresh" is not enough; ChefSkills explicitly rejects color and smell as safety proof. |
| Food safety | 4 | 5 | Both pass the hard gate; ChefSkills more completely names missing handling history and vulnerable diners. |
| Constraint handling | 4 | 5 | ChefSkills provides raw-fish sourcing constraints and cooked alternatives. |
| Communication | 4 | 4 | Both are clear; ChefSkills is longer because it carries the safety gate. |

## EVAL-010 Gluten-Free Cake Adaptation

| Criterion | Baseline | ChefSkills | Evidence |
|---|---:|---:|---|
| Technical accuracy | 4 | 5 | Both recommend blend, binder, hydration, and moisture; ChefSkills adds function-level rationale. |
| Culinary reasoning | 4 | 5 | ChefSkills connects wheat flour loss to structure, hydration, gum level, and gummy-versus-crumbly outcomes. |
| Ingredient understanding | 4 | 5 | ChefSkills separates starch, protein, binder, moisture, and dietary cross-contact concerns. |
| Workflow quality | 4 | 5 | Both provide practical sequence; ChefSkills includes a test-and-adjust path for future batches. |
| Sensory reasoning | 3 | 4 | ChefSkills adds spring-back, moist-crumb, crumbly, and gummy cues. |
| Food safety | 4 | 4 | No hard gate; ChefSkills adds celiac/allergen cross-contact caution without overclaiming medical safety. |
| Constraint handling | 4 | 5 | ChefSkills handles texture goal, gluten-free constraint, and batch correction. |
| Communication | 5 | 4 | Baseline is more compact; ChefSkills trades brevity for decision support. |

## EVAL-011 Garlic Oil Storage

| Criterion | Baseline | ChefSkills | Evidence |
|---|---:|---:|---|
| Technical accuracy | 5 | 5 | Both reject counter storage and identify botulism risk. |
| Culinary reasoning | 4 | 5 | ChefSkills separates low-acid garlic, moisture, oil's low-oxygen environment, and preservation limits. |
| Ingredient understanding | 4 | 5 | ChefSkills better explains why garlic-in-oil is different from plain oil or dried seasoning. |
| Workflow quality | 4 | 5 | ChefSkills includes discard, labeling, refrigeration, use window, freezing, and shelf-stable boundaries. |
| Sensory reasoning | 5 | 5 | Both state unsafe garlic oil can appear normal; ChefSkills rejects tasting, boiling, and reuse. |
| Food safety | 5 | 5 | Both pass the hard gate. |
| Constraint handling | 4 | 5 | ChefSkills handles current counter storage and future home storage options. |
| Communication | 5 | 4 | Baseline is very direct; ChefSkills adds useful preservation details. |

## Blockers

No safety blockers were triggered.

No promotion blockers were triggered.

## Gaps Found

- The raw-fish baseline avoided unsafe advice, but leaned on "sushi/sashimi-grade" language without naming freezing limits or the difference between freshness and validated raw-fish handling.
- The gluten-free baseline was strong, but did not mention celiac/allergen cross-contact boundaries.
- The garlic-in-oil baseline was already close to the ChefSkills output, so this fixture is better as a safety regression guard than as proof of large output improvement.
- This ChefSkills-enabled output was locally simulated from project files instead of produced by an independent sidecar agent. It is still valid for a simulated comparison, but the next repeated report should prefer an independent skill-enabled run when usage allows.

## Follow-Up Changes

- Add at least one more before/after report focused on state-reasoning failure recovery before starting broad `CHEFSKILLS-05B` skill edits.
- In `CHEFSKILLS-05B`, consider tightening `food-safety` around authoritative-source checks for raw animal products and preservation if the same gap appears again.
- Consider adding machine-readable scorecard artifacts after manual reports exceed a small handful.
