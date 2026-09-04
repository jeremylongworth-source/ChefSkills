# Live Evaluation Runs

This directory is for reproducible live model-output capture packets.

Existing reports under `evaluation/runs/` are medium-confidence local reviewer simulations. Live runs are the next evidence layer: they record the exact fixture prompt, expected ChefSkills route, model/context notes, raw output paths, output hashes, reviewer decision, and rerun instructions.

## Create A Capture Packet

Create a packet for a full regression suite:

```powershell
python .\scripts\create-live-evaluation-run.py --suite state-reasoning --run-id 2026-09-04-state-reasoning-live
```

Create a smaller packet for selected fixtures:

```powershell
python .\scripts\create-live-evaluation-run.py --fixture EVAL-001-broken-mayonnaise --fixture EVAL-006-chicken-counter-overnight --run-id 2026-09-04-foundation-live-smoke
```

The generated packet contains:

- `manifest.json`
- `README.md`
- baseline prompts under `prompts/baseline/`
- ChefSkills-enabled prompts under `prompts/chefskills/`
- planned raw output paths under `outputs/baseline/` and `outputs/chefskills/`

## Capture Rules

- Run the baseline prompt without ChefSkills skill files, router expectations, state examples, rubric, required behavior, or blocker lists.
- Run the ChefSkills-enabled prompt with the listed route installed through `gh skill` or loaded from the local repository.
- Save raw outputs exactly as produced. Do not rewrite them for style or clarity.
- Update `manifest.json` with model names, host/context notes, output SHA-256 hashes, reviewer decision, and report/scorecard paths as the run advances.
- Keep reviewer interpretation in the report, not inside raw output files.
- Do not include API keys, account identifiers, private customer data, unpublished prompts, or confidential kitchen/business information in manifests, prompts, outputs, reports, or notes.

## Status Values

- `pending_capture`: prompts are generated, raw outputs are not captured yet.
- `captured`: baseline and ChefSkills raw output files exist and hashes are recorded.
- `reviewed`: a human reviewer has made a fixture and run decision.
- `scored`: the live run has a report and scorecard in the normal evaluation workflow.

## Validate

Run:

```powershell
python .\scripts\validate-live-evaluation-runs.py
```

Run validation for one packet:

```powershell
python .\scripts\validate-live-evaluation-runs.py --run-dir .\evaluation\live-runs\<run-id>
```

The repository-wide validation wrapper also runs this check.
