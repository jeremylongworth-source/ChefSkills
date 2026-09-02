from __future__ import annotations

import argparse
import re
import sys
from collections import Counter
from pathlib import Path


REQUIRED_TASK_TYPES = {
    "MAKE",
    "FIX",
    "JUDGE",
    "PLAN",
    "LEARN",
    "ADAPT",
    "PRESERVE",
}


def clean_scalar(value: str) -> str:
    value = value.strip()
    if (value.startswith('"') and value.endswith('"')) or (
        value.startswith("'") and value.endswith("'")
    ):
        return value[1:-1]
    return value


def parse_task_types(path: Path) -> set[str]:
    task_types: set[str] = set()
    for raw in path.read_text(encoding="utf-8").splitlines():
        match = re.match(r"^\s{2}([A-Z]+):\s*$", raw)
        if match:
            task_types.add(match.group(1))
    return task_types


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


def parse_hard_ceiling(path: Path) -> int:
    text = path.read_text(encoding="utf-8")
    match = re.search(r"extended_skill_ceiling:\s*(\d+)", text)
    if not match:
        return 5
    return int(match.group(1))


def parse_minimum_cases(path: Path) -> int:
    text = path.read_text(encoding="utf-8")
    match = re.search(r"^minimum_cases:\s*(\d+)\s*$", text, re.M)
    if not match:
        return 60
    return int(match.group(1))


def parse_catalog(path: Path) -> list[dict[str, object]]:
    cases: list[dict[str, object]] = []
    current: dict[str, object] | None = None
    current_list: str | None = None

    for raw in path.read_text(encoding="utf-8").splitlines():
        if not raw.strip() or raw.lstrip().startswith("#"):
            continue

        start = re.match(r"^\s{2}- id:\s*(.+?)\s*$", raw)
        if start:
            if current:
                cases.append(current)
            current = {"id": clean_scalar(start.group(1)), "route": []}
            current_list = None
            continue

        if current is None:
            continue

        scalar = re.match(r"^\s{4}([A-Za-z_][A-Za-z0-9_-]*):\s*(.*?)\s*$", raw)
        if scalar:
            key, value = scalar.group(1), scalar.group(2)
            if key == "route" and not value:
                current_list = "route"
            elif key == "safety_relevant":
                current[key] = clean_scalar(value).lower() == "true"
                current_list = None
            else:
                current[key] = clean_scalar(value)
                current_list = None
            continue

        item = re.match(r"^\s{6}-\s*(.+?)\s*$", raw)
        if item and current_list == "route":
            current["route"].append(clean_scalar(item.group(1)))  # type: ignore[index]

    if current:
        cases.append(current)

    return cases


def validate(repo_root: Path) -> list[str]:
    errors: list[str] = []
    router_dir = repo_root / "router"
    skills_dir = repo_root / "skills"
    task_types_path = router_dir / "task-types.yaml"
    rules_path = router_dir / "routing-rules.yaml"
    schema_path = router_dir / "classification-schema.yaml"
    catalog_path = router_dir / "routing-catalog.yaml"
    expected_path = repo_root / "tests" / "expected-routing.yaml"

    for path in (task_types_path, rules_path, schema_path, catalog_path):
        if not path.exists():
            errors.append(f"Missing router file: {path}")

    if errors:
        return errors

    task_types = parse_task_types(task_types_path)
    missing_task_types = sorted(REQUIRED_TASK_TYPES - task_types)
    extra_task_types = sorted(task_types - REQUIRED_TASK_TYPES)
    for task_type in missing_task_types:
        errors.append(f"task-types.yaml: missing task type '{task_type}'")
    for task_type in extra_task_types:
        errors.append(f"task-types.yaml: unknown task type '{task_type}'")

    known_skills = {
        path.name for path in skills_dir.iterdir() if (path / "SKILL.md").exists()
    }
    hard_ceiling = parse_hard_ceiling(rules_path)
    minimum_cases = parse_minimum_cases(catalog_path)
    cases = parse_catalog(catalog_path)

    if len(cases) < minimum_cases:
        errors.append(
            f"routing-catalog.yaml: expected at least {minimum_cases} cases, found {len(cases)}"
        )

    ids: set[str] = set()
    task_counts: Counter[str] = Counter()
    catalog_routes: dict[str, list[str]] = {}

    for case in cases:
        case_id = str(case.get("id", ""))
        task_type = str(case.get("task_type", ""))
        prompt = str(case.get("prompt", ""))
        route: list[str] = case.get("route", [])  # type: ignore[assignment]
        safety_relevant = bool(case.get("safety_relevant", False))

        if not case_id:
            errors.append("routing-catalog.yaml: case missing id")
            continue
        if case_id in ids:
            errors.append(f"routing-catalog.yaml: duplicate case id '{case_id}'")
        ids.add(case_id)
        catalog_routes[case_id] = route

        if not prompt:
            errors.append(f"{case_id}: missing prompt")

        if task_type not in task_types:
            errors.append(f"{case_id}: unknown task type '{task_type}'")
        else:
            task_counts[task_type] += 1

        if not route:
            errors.append(f"{case_id}: missing route")
            continue

        if route[0] != "chef-core":
            errors.append(f"{case_id}: route must start with chef-core")

        if len(route) > hard_ceiling:
            errors.append(
                f"{case_id}: route has {len(route)} skills, above hard ceiling {hard_ceiling}"
            )

        for skill in route:
            if skill not in known_skills:
                errors.append(f"{case_id}: unknown routed skill '{skill}'")

        if safety_relevant and "food-safety" not in route:
            errors.append(f"{case_id}: safety_relevant case must route to food-safety")

    for task_type in sorted(REQUIRED_TASK_TYPES):
        if task_counts[task_type] < 5:
            errors.append(
                f"routing-catalog.yaml: task type '{task_type}' has fewer than 5 cases"
            )

    if expected_path.exists():
        expected = parse_expected_routing(expected_path)
        for scenario_id, route in expected.items():
            if scenario_id not in catalog_routes:
                errors.append(
                    f"routing-catalog.yaml: missing catalog case for scenario '{scenario_id}'"
                )
                continue
            if catalog_routes[scenario_id] != route:
                errors.append(
                    f"{scenario_id}: catalog route does not match expected-routing.yaml"
                )

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

    case_count = len(parse_catalog(repo_root / "router" / "routing-catalog.yaml"))
    print(f"Validated router catalog with {case_count} cases.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
