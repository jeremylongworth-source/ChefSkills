from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


LIST_KEYS = {
    "expected_route",
    "expected_state_surfaces",
    "required_behavior",
    "blockers",
}


def clean_scalar(value: str) -> str:
    value = value.strip()
    if (value.startswith('"') and value.endswith('"')) or (
        value.startswith("'") and value.endswith("'")
    ):
        return value[1:-1]
    return value


def parse_fixtures(path: Path) -> list[dict[str, Any]]:
    fixtures: list[dict[str, Any]] = []
    current: dict[str, Any] | None = None
    current_list: str | None = None

    for raw in path.read_text(encoding="utf-8").splitlines():
        if not raw.strip() or raw.lstrip().startswith("#"):
            continue

        start = re.match(r"^\s{2}- id:\s*(.+?)\s*$", raw)
        if start:
            if current:
                fixtures.append(current)
            current = {
                "id": clean_scalar(start.group(1)),
                "expected_route": [],
                "expected_state_surfaces": [],
                "required_behavior": [],
                "blockers": [],
            }
            current_list = None
            continue

        if current is None:
            continue

        scalar = re.match(r"^\s{4}([A-Za-z_][A-Za-z0-9_-]*):\s*(.*?)\s*$", raw)
        if scalar:
            key, value = scalar.group(1), scalar.group(2)
            if key in LIST_KEYS and not value:
                current_list = key
            else:
                current[key] = clean_scalar(value)
                current_list = None
            continue

        item = re.match(r"^\s{6}-\s*(.+?)\s*$", raw)
        if item and current_list:
            current[current_list].append(clean_scalar(item.group(1)))

    if current:
        fixtures.append(current)

    return fixtures


def parse_regression_suites(path: Path) -> dict[str, list[str]]:
    suites: dict[str, list[str]] = {}
    current_suite: str | None = None
    in_fixtures = False

    for raw in path.read_text(encoding="utf-8").splitlines():
        suite = re.match(r"^\s{2}- id:\s*(.+?)\s*$", raw)
        if suite:
            current_suite = clean_scalar(suite.group(1))
            suites[current_suite] = []
            in_fixtures = False
            continue

        if current_suite and re.match(r"^\s{4}fixtures:\s*$", raw):
            in_fixtures = True
            continue

        item = re.match(r"^\s{6}-\s*(.+?)\s*$", raw)
        if current_suite and in_fixtures and item:
            suites[current_suite].append(clean_scalar(item.group(1)))

        if in_fixtures and raw.strip() and not raw.startswith("      -") and not raw.startswith("    fixtures:"):
            in_fixtures = False

    return suites


def parse_scenario_prompt(path: Path) -> str:
    lines = path.read_text(encoding="utf-8").splitlines()
    collecting = False
    prompt_lines: list[str] = []

    for raw in lines:
        stripped = raw.strip()
        if stripped == "Prompt:":
            collecting = True
            continue
        if collecting and stripped in {"Expected routing:", "Expected behavior:", "Failure modes:"}:
            break
        if collecting and raw.lstrip().startswith(">"):
            prompt_lines.append(raw.lstrip()[1:].strip())

    prompt = "\n".join(prompt_lines).strip()
    if not prompt:
        raise ValueError(f"Unable to parse scenario prompt from {path}")
    return prompt


def git_head(repo_root: Path) -> str:
    try:
        result = subprocess.run(
            ["git", "rev-parse", "HEAD"],
            cwd=repo_root,
            check=True,
            capture_output=True,
            text=True,
        )
    except (OSError, subprocess.CalledProcessError):
        return "unknown"
    return result.stdout.strip() or "unknown"


def sha256_text(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def serialize_path(path: Path, repo_root: Path) -> str:
    resolved = path.resolve()
    try:
        return resolved.relative_to(repo_root.resolve()).as_posix()
    except ValueError:
        return str(resolved)


def unique_items(values: list[str]) -> list[str]:
    seen: set[str] = set()
    result: list[str] = []
    for value in values:
        if value not in seen:
            result.append(value)
            seen.add(value)
    return result


def default_run_id(suite: str | None, fixtures: list[str]) -> str:
    stamp = datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S")
    suffix = suite or fixtures[0].lower()
    suffix = re.sub(r"[^A-Za-z0-9._-]+", "-", suffix).strip("-")
    return f"{stamp}-{suffix}"


def validate_run_id(run_id: str) -> None:
    if not re.match(r"^[A-Za-z0-9][A-Za-z0-9._-]*$", run_id):
        raise ValueError("run id must start with a letter or digit and contain only letters, digits, dots, underscores, or hyphens")


def baseline_prompt(fixture: dict[str, Any], scenario_prompt: str) -> str:
    return f"""# Baseline Prompt: {fixture['id']}

Capture role: baseline
Scenario: {fixture['scenario']}
Task type: {fixture['task_type']}

## Instructions

Answer the user as a capable general culinary assistant.

Do not use ChefSkills-specific skill files, router expectations, state model files, evaluation rubric, expected route, required behavior lists, or blocker lists.

If precise safety guidance would require a current authoritative source check, say what should be checked instead of inventing authority-specific precision.

Return only the user-facing answer.

## User Prompt

{scenario_prompt}
"""


def chefskills_prompt(fixture: dict[str, Any], scenario_prompt: str) -> str:
    route = fixture["expected_route"]
    route_text = "\n".join(f"- {skill}" for skill in route)
    source_files = "\n".join(f"- skills/{skill}/SKILL.md" for skill in route)
    return f"""# ChefSkills Prompt: {fixture['id']}

Capture role: ChefSkills-enabled
Scenario: {fixture['scenario']}
Task type: {fixture['task_type']}

## Instructions

Answer the user with ChefSkills enabled.

Use this expected ChefSkills route:

{route_text}

If your agent host can load local files, use these skill files as the behavioral source:

{source_files}

Preserve food safety as a hard gate. Do not use the evaluation rubric, expected behavior list, or blocker list as answer content.

Return only the user-facing answer.

## User Prompt

{scenario_prompt}
"""


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")


def build_run_readme(run_id: str, suite: str | None, fixture_ids: list[str]) -> str:
    fixture_list = "\n".join(f"- `{fixture_id}`" for fixture_id in fixture_ids)
    suite_text = f"`{suite}`" if suite else "custom fixture selection"
    return f"""# Live Evaluation Run: {run_id}

Status: pending capture

Suite: {suite_text}

Fixtures:

{fixture_list}

## Capture Workflow

1. Run each prompt under `prompts/baseline/` without loading ChefSkills.
2. Run each matching prompt under `prompts/chefskills/` with the listed ChefSkills route installed or loaded.
3. Save raw outputs under `outputs/baseline/` and `outputs/chefskills/` using the file names recorded in `manifest.json`.
4. Update `manifest.json` from `pending_capture` to `captured`, fill model/context notes, and record output SHA-256 hashes.
5. Score the captured outputs with `evaluation/rubric.yaml`.
6. Add the report and scorecard through the existing `evaluation/reports/` and `evaluation/scorecards/` workflow.

Do not edit model outputs after capture. Put reviewer notes in the report, not in the raw output files.
"""


def quote_arg(value: str) -> str:
    if re.match(r"^[A-Za-z0-9._:/\\-]+$", value):
        return value
    return "'" + value.replace("'", "''") + "'"


def build_rerun_command(
    suite: str | None,
    requested_fixtures: list[str],
    selected_fixtures: list[str],
    run_id: str,
    skill_source_ref: str,
    agent_host: str,
    baseline_model: str,
    chefskills_model: str,
) -> str:
    parts = ["python", "scripts/create-live-evaluation-run.py"]
    if suite:
        parts.extend(["--suite", suite])
    fixture_args = requested_fixtures if requested_fixtures else ([] if suite else selected_fixtures)
    for fixture_id in fixture_args:
        parts.extend(["--fixture", fixture_id])
    parts.extend(["--skill-source-ref", skill_source_ref])
    parts.extend(["--agent-host", agent_host])
    parts.extend(["--baseline-model", baseline_model])
    parts.extend(["--chefskills-model", chefskills_model])
    parts.extend(["--rerun-of", run_id])
    return " ".join(quote_arg(part) for part in parts)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Create a live ChefSkills evaluation capture packet.")
    parser.add_argument("--repo-root", default=Path(__file__).resolve().parents[1])
    parser.add_argument("--suite", help="Regression suite id from evaluation/regression-suite.yaml")
    parser.add_argument("--fixture", action="append", default=[], help="Fixture id from evaluation/fixtures.yaml; may be repeated")
    parser.add_argument("--run-id", help="Run id to create. Defaults to a UTC timestamp plus suite or fixture id.")
    parser.add_argument("--output-dir", help="Output directory. Defaults to evaluation/live-runs/<run-id>.")
    parser.add_argument("--agent-host", default=os.environ.get("CHEFSKILLS_AGENT_HOST", "manual"))
    parser.add_argument("--baseline-model", default=os.environ.get("CHEFSKILLS_BASELINE_MODEL", "unspecified"))
    parser.add_argument("--chefskills-model", default=os.environ.get("CHEFSKILLS_CHEFSKILLS_MODEL", "unspecified"))
    parser.add_argument("--operator", default="unspecified")
    parser.add_argument("--skill-source-ref", help="Git commit, tag, or branch used for skill-enabled runs. Defaults to HEAD.")
    parser.add_argument("--rerun-of", help="Prior live run id when this packet is a repeatability check.")
    parser.add_argument("--notes", default="")
    parser.add_argument("--force", action="store_true", help="Overwrite generated prompt and manifest files if the output directory already exists.")
    parser.add_argument("--dry-run", action="store_true", help="Print the planned run without writing files.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    repo_root = Path(args.repo_root).resolve()
    fixtures_path = repo_root / "evaluation" / "fixtures.yaml"
    suites_path = repo_root / "evaluation" / "regression-suite.yaml"
    scenarios_dir = repo_root / "tests" / "scenarios"

    fixtures = {fixture["id"]: fixture for fixture in parse_fixtures(fixtures_path)}
    suites = parse_regression_suites(suites_path)

    selected: list[str] = []
    if args.suite:
        if args.suite not in suites:
            print(f"Unknown suite: {args.suite}", file=sys.stderr)
            return 1
        selected.extend(suites[args.suite])

    for fixture_id in args.fixture:
        if fixture_id not in fixtures:
            print(f"Unknown fixture: {fixture_id}", file=sys.stderr)
            return 1
        selected.append(fixture_id)

    selected = unique_items(selected)
    if not selected:
        print("Select at least one fixture with --suite or --fixture.", file=sys.stderr)
        return 1

    run_id = args.run_id or default_run_id(args.suite, selected)
    try:
        validate_run_id(run_id)
    except ValueError as exc:
        print(str(exc), file=sys.stderr)
        return 1

    output_dir = Path(args.output_dir).resolve() if args.output_dir else repo_root / "evaluation" / "live-runs" / run_id
    if output_dir.exists() and any(output_dir.iterdir()) and not args.force:
        print(f"Output directory already exists and is not empty: {output_dir}", file=sys.stderr)
        return 1

    skill_source_ref = args.skill_source_ref or git_head(repo_root)
    created_utc = datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")

    manifest_fixtures: list[dict[str, Any]] = []
    prompt_writes: list[tuple[Path, str]] = []

    for fixture_id in selected:
        fixture = fixtures[fixture_id]
        scenario = str(fixture["scenario"])
        scenario_prompt = parse_scenario_prompt(scenarios_dir / f"{scenario}.md")

        baseline_prompt_path = output_dir / "prompts" / "baseline" / f"{fixture_id}.md"
        chefskills_prompt_path = output_dir / "prompts" / "chefskills" / f"{fixture_id}.md"
        baseline_output_path = output_dir / "outputs" / "baseline" / f"{fixture_id}.md"
        chefskills_output_path = output_dir / "outputs" / "chefskills" / f"{fixture_id}.md"

        baseline_text = baseline_prompt(fixture, scenario_prompt)
        chefskills_text = chefskills_prompt(fixture, scenario_prompt)
        prompt_writes.extend(
            [
                (baseline_prompt_path, baseline_text),
                (chefskills_prompt_path, chefskills_text),
            ]
        )

        manifest_fixtures.append(
            {
                "fixture_id": fixture_id,
                "scenario": scenario,
                "task_type": fixture["task_type"],
                "safety_gate": fixture["safety_gate"],
                "expected_route": fixture["expected_route"],
                "expected_state_surfaces": fixture["expected_state_surfaces"],
                "scenario_prompt_sha256": sha256_text(scenario_prompt),
                "prompt_files": {
                    "baseline": serialize_path(baseline_prompt_path, repo_root),
                    "chefskills": serialize_path(chefskills_prompt_path, repo_root),
                },
                "prompt_sha256": {
                    "baseline": sha256_text(baseline_text),
                    "chefskills": sha256_text(chefskills_text),
                },
                "output_files": {
                    "baseline": serialize_path(baseline_output_path, repo_root),
                    "chefskills": serialize_path(chefskills_output_path, repo_root),
                },
                "output_sha256": {
                    "baseline": None,
                    "chefskills": None,
                },
                "reviewer_decision": "pending",
                "scorecard": None,
            }
        )

    manifest = {
        "schema_version": "0.1",
        "run_id": run_id,
        "created_utc": created_utc,
        "status": "pending_capture",
        "suite": args.suite,
        "fixture_count": len(selected),
        "capture": {
            "agent_host": args.agent_host,
            "baseline_model": args.baseline_model,
            "chefskills_model": args.chefskills_model,
            "baseline_context": "No ChefSkills skill files, router expectations, state examples, evaluation rubric, expected route, required behavior list, or blocker list loaded.",
            "chefskills_context": "Expected ChefSkills route loaded from fixture metadata; skill files installed through gh skill or loaded from this repository.",
            "operator": args.operator,
            "skill_source_ref": skill_source_ref,
            "rerun_of": args.rerun_of,
            "notes": args.notes,
        },
        "review": {
            "reviewer": None,
            "decision": "pending",
            "report": None,
            "scorecard": None,
        },
        "fixtures": manifest_fixtures,
        "rerun": {
            "stable_inputs": [
                "fixture_id",
                "scenario_prompt_sha256",
                "expected_route",
                "skill_source_ref",
                "baseline_model",
                "chefskills_model",
            ],
            "rerun_command": build_rerun_command(
                args.suite,
                args.fixture,
                selected,
                run_id,
                skill_source_ref,
                args.agent_host,
                args.baseline_model,
                args.chefskills_model,
            ),
            "comparison": "Compare raw output hashes, rubric scores, safety blockers, reviewer decision, and report notes across runs.",
        },
    }

    if args.dry_run:
        print(json.dumps({"run_id": run_id, "output_dir": str(output_dir), "fixtures": selected}, indent=2))
        return 0

    for path, text in prompt_writes:
        write_text(path, text)

    write_text(output_dir / "README.md", build_run_readme(run_id, args.suite, selected))
    write_text(output_dir / "manifest.json", json.dumps(manifest, indent=2) + "\n")

    print(f"Created live evaluation run packet: {output_dir}")
    print(f"Fixtures: {', '.join(selected)}")
    print("Next: capture raw model outputs under outputs/baseline and outputs/chefskills, then update manifest.json.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
