from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


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


def parse_scenario_routing(path: Path) -> list[str]:
    routes: list[str] = []
    in_routing = False

    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.rstrip()
        if line.strip() == "Expected routing:":
            in_routing = True
            continue

        if in_routing:
            item = re.match(r"^\s*-\s*(.+?)\s*$", line)
            if item:
                routes.append(clean_scalar(item.group(1)))
                continue
            if line.strip() and not line.startswith(">"):
                break

    return routes


def validate(repo_root: Path) -> list[str]:
    errors: list[str] = []
    scenarios_dir = repo_root / "tests" / "scenarios"
    expected_path = repo_root / "tests" / "expected-routing.yaml"
    skills_dir = repo_root / "skills"

    if not expected_path.exists():
        return [f"Missing expected routing file: {expected_path}"]
    if not scenarios_dir.exists():
        return [f"Missing scenarios directory: {scenarios_dir}"]

    expected = parse_expected_routing(expected_path)
    scenario_paths = sorted(scenarios_dir.glob("*.md"))
    scenario_keys = {path.stem for path in scenario_paths}

    for key in expected:
        if key not in scenario_keys:
            errors.append(f"expected-routing.yaml: missing scenario file '{key}.md'")

    for path in scenario_paths:
        key = path.stem
        routes = parse_scenario_routing(path)

        if key not in expected:
            errors.append(f"{path.name}: missing expected-routing.yaml entry")
            continue

        if not routes:
            errors.append(f"{path.name}: missing Expected routing list")
            continue

        if routes != expected[key]:
            errors.append(f"{path.name}: Expected routing does not match routing map")

        for skill in routes:
            if not (skills_dir / skill / "SKILL.md").exists():
                errors.append(f"{path.name}: unknown routed skill '{skill}'")

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

    count = len(list((repo_root / "tests" / "scenarios").glob("*.md")))
    print(f"Validated {count} routing scenarios.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
