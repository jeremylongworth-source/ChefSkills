from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


REQUIRED_BUNDLE_BRIEF_HEADINGS = (
    "## Problem",
    "## Target User",
    "## Included Skills",
    "## Context Files",
    "## Safety Rules",
    "## Pilot Metrics",
    "## Acceptance Criteria",
)


def clean_scalar(value: str) -> str:
    value = value.strip()
    if (value.startswith('"') and value.endswith('"')) or (
        value.startswith("'") and value.endswith("'")
    ):
        return value[1:-1]
    return value


def parse_manifest(path: Path) -> dict[str, object]:
    result: dict[str, object] = {
        "name": None,
        "description": None,
        "skills": [],
        "agents_file": None,
    }
    current: str | None = None

    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.split("#", 1)[0].rstrip()
        if not line.strip():
            continue

        scalar = re.match(r"^([A-Za-z_][A-Za-z0-9_-]*)\s*:\s*(.*)$", line)
        if scalar:
            key, value = scalar.group(1), scalar.group(2).strip()
            if key == "skills" and not value:
                current = key
            elif key in ("name", "description", "agents_file"):
                result[key] = clean_scalar(value)
                current = None
            else:
                current = None
            continue

        item = re.match(r"^\s*-\s*(.+?)\s*$", line)
        if item and current == "skills":
            result[current].append(clean_scalar(item.group(1)))  # type: ignore[index]

    return result


def find_duplicates(items: list[str]) -> list[str]:
    seen: set[str] = set()
    duplicates: list[str] = []
    for item in items:
        if item in seen and item not in duplicates:
            duplicates.append(item)
        seen.add(item)
    return duplicates


def validate(repo_root: Path) -> list[str]:
    errors: list[str] = []
    skillsets_dir = repo_root / "skillsets"
    skills_dir = repo_root / "skills"
    bundle_docs_dir = repo_root / "docs" / "bundles"

    manifests = sorted(skillsets_dir.glob("*.yaml"))
    if not manifests:
        return [f"No skillset manifests found: {skillsets_dir}"]

    for manifest_path in manifests:
        manifest = parse_manifest(manifest_path)
        label = manifest_path.name
        name = manifest["name"]
        description = manifest["description"]
        skills: list[str] = manifest["skills"]  # type: ignore[assignment]
        agents_file = manifest["agents_file"]

        if not name:
            errors.append(f"{label}: missing name")
        elif name != manifest_path.stem:
            errors.append(f"{label}: name '{name}' does not match filename")

        if not description:
            errors.append(f"{label}: missing description")

        if not skills:
            errors.append(f"{label}: missing skills")

        for duplicate in find_duplicates(skills):
            errors.append(f"{label}: duplicate skill '{duplicate}'")

        for skill in skills:
            if not (skills_dir / skill / "SKILL.md").exists():
                errors.append(f"{label}: unknown skill '{skill}'")

        if agents_file and not (repo_root / str(agents_file)).exists():
            errors.append(f"{label}: unknown agents_file '{agents_file}'")

        if name:
            brief_path = bundle_docs_dir / f"{name}.md"
            if not brief_path.exists():
                errors.append(f"{label}: missing bundle brief '{brief_path}'")
            else:
                brief_text = brief_path.read_text(encoding="utf-8")
                for heading in REQUIRED_BUNDLE_BRIEF_HEADINGS:
                    if heading not in brief_text:
                        errors.append(f"{label}: bundle brief missing heading '{heading}'")

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

    count = len(list((repo_root / "skillsets").glob("*.yaml")))
    print(f"Validated {count} skillsets.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
