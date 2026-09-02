# CHEFSKILLS-05A Foundation Evaluation

## Purpose

This milestone starts the roadmap after the core framework by evaluating whether the current ChefSkills foundation improves real culinary outputs.

The first evaluation pass is intentionally small: three smoke reports covering troubleshooting, safety, scaling, raw-fish review, structural substitution, preservation safety, and state-reasoned failure recovery.

## Evidence Created

- `evaluation/runs/2026-09-02-foundation-smoke/baseline.md`
- `evaluation/runs/2026-09-02-foundation-smoke/skill-enabled.md`
- `evaluation/reports/2026-09-02-foundation-smoke.md`
- `evaluation/runs/2026-09-02-safety-substitution-smoke/baseline.md`
- `evaluation/runs/2026-09-02-safety-substitution-smoke/skill-enabled.md`
- `evaluation/reports/2026-09-02-safety-substitution-smoke.md`
- `evaluation/runs/2026-09-02-state-recovery-smoke/baseline.md`
- `evaluation/runs/2026-09-02-state-recovery-smoke/skill-enabled.md`
- `evaluation/reports/2026-09-02-state-recovery-smoke.md`
- `evaluation/scorecards/2026-09-02-foundation-smoke.json`
- `evaluation/scorecards/2026-09-02-safety-substitution-smoke.json`
- `evaluation/scorecards/2026-09-02-state-recovery-smoke.json`
- `evaluation/reports/index.yaml`
- `scripts/validate-evaluation-reports.py`

## Findings

The baseline outputs were competent. ChefSkills still improved the evaluated answers by adding:

- clearer mechanism reasoning
- stronger observable cues
- better workflow sequencing
- more explicit food-safety gates
- better scaling logic around vessel geometry and reduction behavior
- stronger distinction between safety hazards and quality/freshness cues
- better structure, hydration, and binder reasoning for gluten-free adaptation
- more consistent current-state, target-state, mechanism, side-effect, and verification-cue framing

## Acceptance Criteria

Given a registered evaluation report, when `python .\scripts\validate-evaluation-reports.py` runs, then every report, raw output, fixture, and regression suite reference exists.
Evidence: command output.

Given the registered smoke reports, when a reviewer reads each score summary, then baseline and ChefSkills-enabled averages are present for every fixture.
Evidence: `evaluation/reports/2026-09-02-foundation-smoke.md`, `evaluation/reports/2026-09-02-safety-substitution-smoke.md`, and `evaluation/reports/2026-09-02-state-recovery-smoke.md`.

Given a safety fixture in the report, when reviewing blockers, then unsafe salvage blockers are reported before score averages.
Evidence: report blocker section.

Given the full validation command, when `.\scripts\validate-all.ps1` runs, then evaluation report validation runs with the existing checks.
Evidence: command output.

## Follow-On Status

`CHEFSKILLS-05B` applies these repeated report findings:

- make state-reasoning output expectations easier to apply consistently across troubleshooting skills
- add machine-readable scorecard artifacts for report aggregation
- tighten source-check expectations for future safety-gated evaluation reports

The next work after `CHEFSKILLS-05B` is to summarize scorecard trends and decide whether the foundation is stable enough for `CHEFSKILLS-05C` specialist expansion.
