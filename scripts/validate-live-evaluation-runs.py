from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path
from typing import Any


LIST_KEYS = {
    "expected_route",
    "expected_state_surfaces",
    "required_behavior",
    "blockers",
}
ALLOWED_STATUS = {"pending_capture", "captured", "reviewed", "scored"}
ALLOWED_DECISIONS = {"pending", "keep", "revise", "split", "merge", "defer", "retire"}
CAPTURED_STATUS = {"captured", "reviewed", "scored"}
REQUIRED_MANIFEST_FIELDS = {
    "schema_version",
    "run_id",
    "created_utc",
    "status",
    "suite",
    "fixture_count",
    "capture",
    "review",
    "fixtures",
    "rerun",
}
REQUIRED_CAPTURE_FIELDS = {
    "agent_host",
    "baseline_model",
    "chefskills_model",
    "baseline_context",
    "chefskills_context",
    "operator",
    "skill_source_ref",
    "rerun_of",
    "notes",
}
REQUIRED_REVIEW_FIELDS = {"reviewer", "decision", "report", "scorecard"}
REQUIRED_FIXTURE_FIELDS = {
    "fixture_id",
    "scenario",
    "task_type",
    "safety_gate",
    "expected_route",
    "expected_state_surfaces",
    "scenario_prompt_sha256",
    "prompt_files",
    "prompt_sha256",
    "output_files",
    "output_sha256",
    "reviewer_decision",
    "scorecard",
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

    return "\n".join(prompt_lines).strip()


def sha256_text(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def resolve_path(value: Any, repo_root: Path) -> Path | None:
    if not isinstance(value, str) or not value:
        return None
    path = Path(value)
    if path.is_absolute():
        return path
    return repo_root / path


def is_within(path: Path, parent: Path) -> bool:
    try:
        path.resolve().relative_to(parent.resolve())
    except ValueError:
        return False
    return True


def validate_mapping_keys(
    report_id: str,
    field_name: str,
    value: Any,
    required_keys: set[str],
) -> list[str]:
    if not isinstance(value, dict):
        return [f"{report_id}: {field_name} must be an object"]
    errors: list[str] = []
    for key in sorted(required_keys - set(value)):
        errors.append(f"{report_id}: {field_name} missing '{key}'")
    return errors


def validate_prompt_file(
    manifest_path: Path,
    repo_root: Path,
    fixture_id: str,
    prompt_kind: str,
    prompt_files: dict[str, Any],
    prompt_hashes: dict[str, Any],
) -> list[str]:
    errors: list[str] = []
    prompt_path = resolve_path(prompt_files.get(prompt_kind), repo_root)
    if prompt_path is None:
        return [f"{manifest_path}: {fixture_id}: missing prompt_files.{prompt_kind}"]
    if not is_within(prompt_path, manifest_path.parent):
        errors.append(f"{manifest_path}: {fixture_id}: prompt_files.{prompt_kind} must be inside the live run directory")
    if not prompt_path.exists():
        return errors + [f"{manifest_path}: {fixture_id}: missing prompt file '{prompt_files.get(prompt_kind)}'"]
    text = prompt_path.read_text(encoding="utf-8")
    if not text.strip():
        errors.append(f"{manifest_path}: {fixture_id}: prompt file '{prompt_files.get(prompt_kind)}' is empty")
    expected_hash = prompt_hashes.get(prompt_kind)
    if not isinstance(expected_hash, str) or not expected_hash:
        errors.append(f"{manifest_path}: {fixture_id}: prompt_sha256.{prompt_kind} must be a non-empty string")
    elif expected_hash != sha256_text(text):
        errors.append(f"{manifest_path}: {fixture_id}: prompt_sha256.{prompt_kind} does not match prompt file")
    return errors


def validate_output_file(
    manifest_path: Path,
    repo_root: Path,
    fixture_id: str,
    output_kind: str,
    output_files: dict[str, Any],
    output_hashes: dict[str, Any],
    status: str,
) -> list[str]:
    errors: list[str] = []
    output_path = resolve_path(output_files.get(output_kind), repo_root)
    if output_path is None:
        return [f"{manifest_path}: {fixture_id}: missing output_files.{output_kind}"]
    if not is_within(output_path, manifest_path.parent):
        errors.append(f"{manifest_path}: {fixture_id}: output_files.{output_kind} must be inside the live run directory")

    if status not in CAPTURED_STATUS and not output_path.exists():
        return errors

    if not output_path.exists():
        return errors + [f"{manifest_path}: {fixture_id}: missing output file '{output_files.get(output_kind)}'"]
    if output_path.stat().st_size == 0:
        errors.append(f"{manifest_path}: {fixture_id}: output file '{output_files.get(output_kind)}' is empty")

    expected_hash = output_hashes.get(output_kind)
    if status in CAPTURED_STATUS and not expected_hash:
        errors.append(f"{manifest_path}: {fixture_id}: output_sha256.{output_kind} is required when status is {status}")
    if expected_hash and expected_hash != sha256_file(output_path):
        errors.append(f"{manifest_path}: {fixture_id}: output_sha256.{output_kind} does not match output file")
    return errors


def validate_manifest(
    manifest_path: Path,
    repo_root: Path,
    known_fixtures: dict[str, dict[str, Any]],
    suites: dict[str, list[str]],
) -> list[str]:
    errors: list[str] = []
    try:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        return [f"{manifest_path}: invalid JSON: {exc}"]

    if not isinstance(manifest, dict):
        return [f"{manifest_path}: manifest must be a JSON object"]

    for field in sorted(REQUIRED_MANIFEST_FIELDS - set(manifest)):
        errors.append(f"{manifest_path}: missing manifest field '{field}'")

    if manifest.get("schema_version") != "0.1":
        errors.append(f"{manifest_path}: schema_version must be 0.1")

    run_id = manifest.get("run_id")
    if not isinstance(run_id, str) or not re.match(r"^[A-Za-z0-9][A-Za-z0-9._-]*$", run_id):
        errors.append(f"{manifest_path}: run_id is invalid")

    status = str(manifest.get("status", ""))
    if status not in ALLOWED_STATUS:
        errors.append(f"{manifest_path}: invalid status '{status}'")

    suite = manifest.get("suite")
    if suite is not None and suite not in suites:
        errors.append(f"{manifest_path}: unknown suite '{suite}'")

    errors.extend(validate_mapping_keys(str(manifest_path), "capture", manifest.get("capture"), REQUIRED_CAPTURE_FIELDS))
    capture = manifest.get("capture")
    if isinstance(capture, dict):
        for field in sorted(REQUIRED_CAPTURE_FIELDS - {"rerun_of", "notes"}):
            if not isinstance(capture.get(field), str) or not capture.get(field):
                errors.append(f"{manifest_path}: capture.{field} must be a non-empty string")

    errors.extend(validate_mapping_keys(str(manifest_path), "review", manifest.get("review"), REQUIRED_REVIEW_FIELDS))
    review = manifest.get("review")
    if isinstance(review, dict):
        decision = str(review.get("decision", ""))
        if decision not in ALLOWED_DECISIONS:
            errors.append(f"{manifest_path}: review.decision is invalid")
        if status in {"reviewed", "scored"} and decision == "pending":
            errors.append(f"{manifest_path}: review.decision cannot be pending when status is {status}")
        for path_field in ("report", "scorecard"):
            value = review.get(path_field)
            if status == "scored" and not value:
                errors.append(f"{manifest_path}: review.{path_field} is required when status is scored")
            if value:
                path = resolve_path(value, repo_root)
                if path is None or not path.exists():
                    errors.append(f"{manifest_path}: missing review.{path_field} path '{value}'")

    rerun = manifest.get("rerun")
    errors.extend(validate_mapping_keys(str(manifest_path), "rerun", rerun, {"stable_inputs", "rerun_command", "comparison"}))
    if isinstance(rerun, dict):
        if not isinstance(rerun.get("stable_inputs"), list) or not rerun.get("stable_inputs"):
            errors.append(f"{manifest_path}: rerun.stable_inputs must be a non-empty list")
        for field in ("rerun_command", "comparison"):
            if not isinstance(rerun.get(field), str) or not rerun.get(field):
                errors.append(f"{manifest_path}: rerun.{field} must be a non-empty string")

    fixtures = manifest.get("fixtures")
    if not isinstance(fixtures, list) or not fixtures:
        errors.append(f"{manifest_path}: fixtures must be a non-empty list")
        return errors

    if manifest.get("fixture_count") != len(fixtures):
        errors.append(f"{manifest_path}: fixture_count does not match fixtures length")

    actual_fixture_ids: list[str] = []
    for fixture in fixtures:
        if not isinstance(fixture, dict):
            errors.append(f"{manifest_path}: fixture entry must be an object")
            continue

        for field in sorted(REQUIRED_FIXTURE_FIELDS - set(fixture)):
            errors.append(f"{manifest_path}: fixture entry missing '{field}'")

        fixture_id = str(fixture.get("fixture_id", ""))
        actual_fixture_ids.append(fixture_id)
        expected = known_fixtures.get(fixture_id)
        if expected is None:
            errors.append(f"{manifest_path}: unknown fixture '{fixture_id}'")
            continue

        for field in ("scenario", "task_type", "safety_gate"):
            if fixture.get(field) != expected.get(field):
                errors.append(f"{manifest_path}: {fixture_id}: {field} does not match evaluation/fixtures.yaml")
        if fixture.get("expected_route") != expected.get("expected_route"):
            errors.append(f"{manifest_path}: {fixture_id}: expected_route does not match evaluation/fixtures.yaml")
        if fixture.get("expected_state_surfaces") != expected.get("expected_state_surfaces"):
            errors.append(f"{manifest_path}: {fixture_id}: expected_state_surfaces does not match evaluation/fixtures.yaml")

        scenario_prompt = parse_scenario_prompt(repo_root / "tests" / "scenarios" / f"{expected['scenario']}.md")
        if not isinstance(fixture.get("scenario_prompt_sha256"), str) or not fixture.get("scenario_prompt_sha256"):
            errors.append(f"{manifest_path}: {fixture_id}: scenario_prompt_sha256 must be a non-empty string")
        elif fixture.get("scenario_prompt_sha256") != sha256_text(scenario_prompt):
            errors.append(f"{manifest_path}: {fixture_id}: scenario_prompt_sha256 does not match scenario prompt")

        prompt_files = fixture.get("prompt_files")
        prompt_hashes = fixture.get("prompt_sha256")
        errors.extend(validate_mapping_keys(f"{manifest_path}: {fixture_id}", "prompt_files", prompt_files, {"baseline", "chefskills"}))
        errors.extend(validate_mapping_keys(f"{manifest_path}: {fixture_id}", "prompt_sha256", prompt_hashes, {"baseline", "chefskills"}))
        if isinstance(prompt_files, dict) and isinstance(prompt_hashes, dict):
            for prompt_kind in ("baseline", "chefskills"):
                errors.extend(validate_prompt_file(manifest_path, repo_root, fixture_id, prompt_kind, prompt_files, prompt_hashes))

        output_files = fixture.get("output_files")
        output_hashes = fixture.get("output_sha256")
        errors.extend(validate_mapping_keys(f"{manifest_path}: {fixture_id}", "output_files", output_files, {"baseline", "chefskills"}))
        errors.extend(validate_mapping_keys(f"{manifest_path}: {fixture_id}", "output_sha256", output_hashes, {"baseline", "chefskills"}))
        if isinstance(output_files, dict) and isinstance(output_hashes, dict):
            for output_kind in ("baseline", "chefskills"):
                errors.extend(validate_output_file(manifest_path, repo_root, fixture_id, output_kind, output_files, output_hashes, status))

        decision = str(fixture.get("reviewer_decision", ""))
        if decision not in ALLOWED_DECISIONS:
            errors.append(f"{manifest_path}: {fixture_id}: reviewer_decision is invalid")
        if status in {"reviewed", "scored"} and decision == "pending":
            errors.append(f"{manifest_path}: {fixture_id}: reviewer_decision cannot be pending when status is {status}")

        scorecard = fixture.get("scorecard")
        if status == "scored" and not scorecard:
            errors.append(f"{manifest_path}: {fixture_id}: scorecard is required when status is scored")
        if scorecard:
            scorecard_path = resolve_path(scorecard, repo_root)
            if scorecard_path is None or not scorecard_path.exists():
                errors.append(f"{manifest_path}: {fixture_id}: missing scorecard path '{scorecard}'")

    if suite is not None and suite in suites:
        suite_fixtures = suites[suite]
        if actual_fixture_ids[: len(suite_fixtures)] != suite_fixtures:
            errors.append(f"{manifest_path}: fixtures do not preserve regression suite order")

    return errors


def find_manifests(repo_root: Path, run_dir: str | None) -> list[Path]:
    if run_dir:
        path = Path(run_dir)
        manifest = path if path.name == "manifest.json" else path / "manifest.json"
        return [manifest]
    live_runs_dir = repo_root / "evaluation" / "live-runs"
    if not live_runs_dir.exists():
        return []
    return sorted(live_runs_dir.rglob("manifest.json"))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo-root", default=Path(__file__).resolve().parents[1])
    parser.add_argument("--run-dir", help="Validate one live run directory or manifest file.")
    args = parser.parse_args()

    repo_root = Path(args.repo_root).resolve()
    known_fixtures = {
        fixture["id"]: fixture
        for fixture in parse_fixtures(repo_root / "evaluation" / "fixtures.yaml")
    }
    suites = parse_regression_suites(repo_root / "evaluation" / "regression-suite.yaml")
    manifests = find_manifests(repo_root, args.run_dir)

    errors: list[str] = []
    for manifest in manifests:
        if not manifest.exists():
            errors.append(f"Missing live run manifest: {manifest}")
            continue
        errors.extend(validate_manifest(manifest.resolve(), repo_root, known_fixtures, suites))

    if errors:
        for error in errors:
            print(error, file=sys.stderr)
        return 1

    print(f"Validated {len(manifests)} live evaluation run manifests.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
