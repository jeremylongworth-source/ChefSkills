from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


REQUIRED_EVALUATION_FILES = {
    "README.md",
    "rubric.yaml",
    "scoring-schema.yaml",
    "safety-gates.yaml",
    "fixtures.yaml",
    "regression-suite.yaml",
    "report-template.md",
}

REQUIRED_CRITERIA = {
    "technical_accuracy",
    "culinary_reasoning",
    "ingredient_understanding",
    "workflow_quality",
    "sensory_reasoning",
    "safety",
    "constraint_handling",
    "communication",
}

REQUIRED_FIXTURE_FIELDS = {
    "id",
    "scenario",
    "task_type",
    "state_example",
    "safety_gate",
    "expected_route",
    "expected_state_surfaces",
    "required_behavior",
    "blockers",
}

ALLOWED_STATE_SURFACES = {
    "ingredient_state",
    "dish_state",
    "transformation_state",
    "equipment_state",
    "workflow_state",
    "observation_state",
    "recovery_state",
    "safety_state",
}

REQUIRED_SAFETY_BLOCKERS = {
    "unsafe_salvage",
    "raw_animal_product_overconfidence",
    "preservation_overconfidence",
    "allergen_or_medical_diet_certainty",
    "cross_contamination_ignored",
    "missing_facts_hidden",
}


def clean_scalar(value: str) -> str:
    value = value.strip()
    if (value.startswith('"') and value.endswith('"')) or (
        value.startswith("'") and value.endswith("'")
    ):
        return value[1:-1]
    return value


def parse_expected_routing(path: Path) -> dict[str, list[str]]:
    result: dict[str, list[str]] = {}
    current: str | None = None

    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.split("#", 1)[0].rstrip()
        if not line.strip():
            continue

        key = re.match(r"^([A-Za-z0-9_-]+)\s*:\s*$", line)
        if key:
            current = key.group(1)
            result[current] = []
            continue

        item = re.match(r"^\s*-\s*(.+?)\s*$", line)
        if item and current:
            result[current].append(clean_scalar(item.group(1)))

    return result


def parse_ids(path: Path, indent: int = 2) -> set[str]:
    pattern = rf"^\s{{{indent}}}- id:\s*(.+?)\s*$"
    return {
        clean_scalar(match.group(1))
        for raw in path.read_text(encoding="utf-8").splitlines()
        if (match := re.match(pattern, raw))
    }


def parse_minimum_fixtures(path: Path) -> int:
    text = path.read_text(encoding="utf-8")
    match = re.search(r"^minimum_fixtures:\s*(\d+)\s*$", text, re.M)
    if not match:
        return 12
    return int(match.group(1))


def parse_rubric_criteria(path: Path) -> dict[str, dict[str, str]]:
    criteria: dict[str, dict[str, str]] = {}
    current: str | None = None

    for raw in path.read_text(encoding="utf-8").splitlines():
        start = re.match(r"^\s{2}- id:\s*(.+?)\s*$", raw)
        if start:
            current = clean_scalar(start.group(1))
            criteria[current] = {}
            continue

        if current:
            scalar = re.match(r"^\s{4}([A-Za-z_][A-Za-z0-9_-]*):\s*(.*?)\s*$", raw)
            if scalar:
                criteria[current][scalar.group(1)] = clean_scalar(scalar.group(2))

    return criteria


def parse_fixtures(path: Path) -> list[dict[str, object]]:
    fixtures: list[dict[str, object]] = []
    current: dict[str, object] | None = None
    current_list: str | None = None

    list_keys = {"expected_route", "expected_state_surfaces", "required_behavior", "blockers"}

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
            if key in list_keys and not value:
                current_list = key
            else:
                current[key] = clean_scalar(value)
                current_list = None
            continue

        item = re.match(r"^\s{6}-\s*(.+?)\s*$", raw)
        if item and current_list:
            current[current_list].append(clean_scalar(item.group(1)))  # type: ignore[index]

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


def validate(repo_root: Path) -> list[str]:
    errors: list[str] = []
    evaluation_dir = repo_root / "evaluation"
    scenarios_dir = repo_root / "tests" / "scenarios"
    expected_path = repo_root / "tests" / "expected-routing.yaml"
    state_examples_path = repo_root / "state" / "state-examples.yaml"

    if not evaluation_dir.exists():
        return [f"Missing evaluation directory: {evaluation_dir}"]

    for file_name in sorted(REQUIRED_EVALUATION_FILES):
        if not (evaluation_dir / file_name).exists():
            errors.append(f"Missing evaluation file: evaluation/{file_name}")

    if errors:
        return errors

    criteria = parse_rubric_criteria(evaluation_dir / "rubric.yaml")
    missing_criteria = sorted(REQUIRED_CRITERIA - set(criteria))
    for criterion in missing_criteria:
        errors.append(f"rubric.yaml: missing criterion '{criterion}'")

    safety = criteria.get("safety", {})
    if safety.get("hard_gate") != "true":
        errors.append("rubric.yaml: safety criterion must be a hard gate")

    safety_blockers = parse_ids(evaluation_dir / "safety-gates.yaml", indent=2)
    missing_blockers = sorted(REQUIRED_SAFETY_BLOCKERS - safety_blockers)
    for blocker in missing_blockers:
        errors.append(f"safety-gates.yaml: missing blocker '{blocker}'")

    expected_routes = parse_expected_routing(expected_path)
    state_examples = parse_ids(state_examples_path, indent=2)
    fixtures = parse_fixtures(evaluation_dir / "fixtures.yaml")
    minimum_fixtures = parse_minimum_fixtures(evaluation_dir / "fixtures.yaml")

    if len(fixtures) < minimum_fixtures:
        errors.append(
            f"fixtures.yaml: expected at least {minimum_fixtures} fixtures, found {len(fixtures)}"
        )

    fixture_ids: set[str] = set()
    for fixture in fixtures:
        fixture_id = str(fixture.get("id", ""))
        if not fixture_id:
            errors.append("fixtures.yaml: fixture missing id")
            continue
        if fixture_id in fixture_ids:
            errors.append(f"fixtures.yaml: duplicate fixture id '{fixture_id}'")
        fixture_ids.add(fixture_id)

        for field in sorted(REQUIRED_FIXTURE_FIELDS):
            if field not in fixture:
                errors.append(f"{fixture_id}: missing fixture field '{field}'")

        scenario = str(fixture.get("scenario", ""))
        if scenario:
            if not (scenarios_dir / f"{scenario}.md").exists():
                errors.append(f"{fixture_id}: unknown scenario '{scenario}'")
            if scenario not in expected_routes:
                errors.append(f"{fixture_id}: scenario missing expected routing '{scenario}'")

        expected_route: list[str] = fixture.get("expected_route", [])  # type: ignore[assignment]
        if scenario in expected_routes and expected_route != expected_routes[scenario]:
            errors.append(f"{fixture_id}: expected route does not match tests/expected-routing.yaml")

        surfaces: list[str] = fixture.get("expected_state_surfaces", [])  # type: ignore[assignment]
        for surface in sorted(set(surfaces) - ALLOWED_STATE_SURFACES):
            errors.append(f"{fixture_id}: unknown state surface '{surface}'")
        if not surfaces:
            errors.append(f"{fixture_id}: missing expected state surfaces")

        state_example = str(fixture.get("state_example", ""))
        if state_example and state_example != "none" and state_example not in state_examples:
            errors.append(f"{fixture_id}: unknown state example '{state_example}'")

        safety_gate = str(fixture.get("safety_gate", ""))
        blockers: list[str] = fixture.get("blockers", [])  # type: ignore[assignment]
        if safety_gate != "not_required":
            if "food-safety" not in expected_route:
                errors.append(f"{fixture_id}: safety-gated fixture must route to food-safety")
            if not blockers:
                errors.append(f"{fixture_id}: safety-gated fixture must include blockers")
        if "food-safety" in expected_route and safety_gate == "not_required":
            errors.append(f"{fixture_id}: food-safety route must have a safety gate")

    suites = parse_regression_suites(evaluation_dir / "regression-suite.yaml")
    if not suites:
        errors.append("regression-suite.yaml: missing suites")
    for suite_id, suite_fixtures in suites.items():
        if not suite_fixtures:
            errors.append(f"{suite_id}: regression suite has no fixtures")
        for fixture_id in suite_fixtures:
            if fixture_id not in fixture_ids:
                errors.append(f"{suite_id}: unknown fixture '{fixture_id}'")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo-root", default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()

    repo_root = Path(args.repo_root).resolve()
    errors = validate(repo_root)
    if errors:
        for error in errors:
            print(error, file=sys.stderr)
        return 1

    fixture_count = len(parse_fixtures(repo_root / "evaluation" / "fixtures.yaml"))
    suite_count = len(parse_regression_suites(repo_root / "evaluation" / "regression-suite.yaml"))
    print(f"Validated evaluation engine with {fixture_count} fixtures and {suite_count} suites.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
