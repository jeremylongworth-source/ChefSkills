# Live Evaluation Run: 2026-09-04-foundation-live-smoke

Status: pending capture

Suite: `chefskills-04-smoke`

Fixtures:

- `EVAL-001-broken-mayonnaise`
- `EVAL-002-thin-gravy`
- `EVAL-005-sauce-for-forty`
- `EVAL-006-chicken-counter-overnight`
- `EVAL-008-evaluate-ai-sushi-recipe`

## Capture Workflow

1. Run each prompt under `prompts/baseline/` without loading ChefSkills.
2. Run each matching prompt under `prompts/chefskills/` with the listed ChefSkills route installed or loaded.
3. Save raw outputs under `outputs/baseline/` and `outputs/chefskills/` using the file names recorded in `manifest.json`.
4. Update `manifest.json` from `pending_capture` to `captured`, fill model/context notes, and record output SHA-256 hashes.
5. Score the captured outputs with `evaluation/rubric.yaml`.
6. Add the report and scorecard through the existing `evaluation/reports/` and `evaluation/scorecards/` workflow.

Do not edit model outputs after capture. Put reviewer notes in the report, not in the raw output files.

Do not include API keys, account identifiers, private customer data, unpublished prompts, or confidential kitchen/business information in manifests, prompts, outputs, reports, or notes.
