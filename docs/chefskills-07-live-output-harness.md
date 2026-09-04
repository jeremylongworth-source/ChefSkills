# CHEFSKILLS-07 Live Output Harness

## Purpose

This milestone creates the first reproducible live-output evaluation harness for ChefSkills.

Previous before/after reports are useful for regression tracking, but they are medium-confidence local reviewer simulations. The next evidence layer must capture real model outputs in a way that outside contributors can inspect and rerun.

## Current Pass

This pass adds a file-backed harness, not an API client:

- `scripts/create-live-evaluation-run.py` creates prompt packets from existing fixtures and regression suites.
- `scripts/validate-live-evaluation-runs.py` validates live run manifests, prompt files, output paths, output hashes, reviewer decisions, and report/scorecard links.
- `evaluation/live-runs/README.md` documents the capture workflow and status model.
- `evaluation/README.md` explains how live runs relate to the existing simulated reports.
- `.\scripts\validate-all.ps1` includes live-run manifest validation.

The harness deliberately avoids model API calls, credentials, or provider-specific assumptions. Operators can run the generated prompts in GitHub Copilot, ChatGPT, Codex, or another host, then save the raw outputs as evidence.

Live run artifacts are intended for a public repository. Do not include API keys, account identifiers, private customer data, unpublished prompts, or confidential kitchen/business information in manifests, prompts, outputs, reports, or notes.

## Capture Contract

A live run packet records:

- run id, creation time, suite, fixture count, and status
- agent host, baseline model, ChefSkills model, context notes, operator, and skill source ref
- fixture id, scenario, task type, safety gate, expected route, and expected state surfaces
- scenario prompt hash and generated prompt hashes
- planned baseline and ChefSkills output paths
- output hashes once raw output files are captured
- reviewer decision, report path, scorecard path, and rerun comparison notes

## Workflow

1. Create a packet from a suite or fixture list.
2. Run baseline prompts without ChefSkills context.
3. Run ChefSkills prompts with the listed route installed or loaded.
4. Save raw outputs without editing them.
5. Record hashes and update the manifest status.
6. Score with the existing rubric.
7. Add normal report and scorecard artifacts.
8. Rerun selected packets when repeatability matters.

## Acceptance Criteria

Given a maintainer creates a live run packet from an existing suite, when the script runs, then every selected fixture should have baseline and ChefSkills prompt files, planned output paths, prompt hashes, route metadata, and rerun instructions.
Evidence: `scripts/create-live-evaluation-run.py` smoke run.

Given live run manifests are present, when `python .\scripts\validate-live-evaluation-runs.py` runs, then pending packets should validate prompt metadata and captured/scored packets should require raw outputs, hashes, reviewer decisions, and report/scorecard links.
Evidence: validator output and `.\scripts\validate-all.ps1`.

Given the repository is reviewed after this milestone, when public readers inspect evaluation docs, then they should understand that existing reports are simulated and that live run packets are the path to higher-confidence evidence.
Evidence: `evaluation/README.md` and `evaluation/live-runs/README.md`.

## Remaining Work

- Capture raw outputs for the first live foundation smoke packet: `evaluation/live-runs/2026-09-04-foundation-live-smoke`.
- Capture at least one safety-hard-gate live run before beta claims.
- Add scored live reports only after raw outputs are captured and reviewed.
- Compare rerun variance before using live evidence for stronger release claims.
