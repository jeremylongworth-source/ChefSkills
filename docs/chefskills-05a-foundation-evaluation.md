# CHEFSKILLS-05A Foundation Evaluation

## Purpose

This milestone starts the roadmap after the core framework by evaluating whether the current ChefSkills foundation improves real culinary outputs.

The first evaluation is intentionally small: three smoke fixtures covering troubleshooting, safety, and scaling.

## Evidence Created

- `evaluation/runs/2026-09-02-foundation-smoke/baseline.md`
- `evaluation/runs/2026-09-02-foundation-smoke/skill-enabled.md`
- `evaluation/reports/2026-09-02-foundation-smoke.md`
- `evaluation/reports/index.yaml`
- `scripts/validate-evaluation-reports.py`

## Findings

The baseline outputs were competent. ChefSkills still improved the evaluated answers by adding:

- clearer mechanism reasoning
- stronger observable cues
- better workflow sequencing
- more explicit food-safety gates
- better scaling logic around vessel geometry and reduction behavior

## Acceptance Criteria

Given a registered evaluation report, when `python .\scripts\validate-evaluation-reports.py` runs, then every report, raw output, fixture, and regression suite reference exists.
Evidence: command output.

Given the foundation smoke report, when a reviewer reads the score summary, then baseline and ChefSkills-enabled averages are present for every fixture.
Evidence: `evaluation/reports/2026-09-02-foundation-smoke.md`.

Given a safety fixture in the report, when reviewing blockers, then unsafe salvage blockers are reported before score averages.
Evidence: report blocker section.

Given the full validation command, when `.\scripts\validate-all.ps1` runs, then evaluation report validation runs with the existing checks.
Evidence: command output.

## Next Work

Continue `CHEFSKILLS-05A` with at least three more before/after reports:

- raw fish safety review
- gluten-free cake adaptation
- garlic-in-oil storage

After the repeated reports identify concrete gaps, begin `CHEFSKILLS-05B` by patching only the affected foundation skills.
