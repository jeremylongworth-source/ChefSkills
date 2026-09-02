from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


REQUIRED_STATE_FILES = {
    "culinary-state.yaml",
    "ingredient-state.yaml",
    "dish-state.yaml",
    "transformation-state.yaml",
    "equipment-state.yaml",
    "workflow-state.yaml",
    "observation-state.yaml",
    "recovery-state.yaml",
    "safety-state.yaml",
    "state-examples.yaml",
}

REQUIRED_SCHEMA_SECTIONS = {
    "required_state_files",
    "required_top_level_sections",
    "controlled_vocabularies",
    "example_requirements",
}

REQUIRED_EXAMPLE_SURFACES = {
    "ingredient_state",
    "dish_state",
    "transformation_state",
    "equipment_state",
    "workflow_state",
    "observation_state",
    "recovery_state",
    "safety_state",
}

REQUIRED_EXAMPLE_FIELDS = {
    "id",
    "surface",
    "safety_relevant",
    "task_context",
    "workflow_stage",
    "current_observation",
    "target_state",
    "intervention",
    "verification_cue",
}

REQUIRED_TOP_LEVEL = {
    "culinary-state.yaml": "culinary_state",
    "ingredient-state.yaml": "ingredient_state",
    "dish-state.yaml": "dish_state",
    "transformation-state.yaml": "transformation_state",
    "equipment-state.yaml": "equipment_state",
    "workflow-state.yaml": "workflow_state",
    "observation-state.yaml": "observation_state",
    "recovery-state.yaml": "recovery_state",
    "safety-state.yaml": "safety_state",
}


def clean_scalar(value: str) -> str:
    value = value.strip()
    if (value.startswith('"') and value.endswith('"')) or (
        value.startswith("'") and value.endswith("'")
    ):
        return value[1:-1]
    return value


def top_level_keys(text: str) -> set[str]:
    keys: set[str] = set()
    for raw in text.splitlines():
        match = re.match(r"^([A-Za-z_][A-Za-z0-9_-]*):\s*", raw)
        if match:
            keys.add(match.group(1))
    return keys


def second_level_keys(text: str, top_key: str) -> set[str]:
    keys: set[str] = set()
    in_section = False
    for raw in text.splitlines():
        if re.match(rf"^{re.escape(top_key)}:\s*$", raw):
            in_section = True
            continue
        if in_section and re.match(r"^[A-Za-z_][A-Za-z0-9_-]*:\s*", raw):
            break
        if in_section:
            match = re.match(r"^\s{2}([A-Za-z_][A-Za-z0-9_-]*):\s*", raw)
            if match:
                keys.add(match.group(1))
    return keys


def parse_schema_required_sections(schema_text: str) -> dict[str, list[str]]:
    result: dict[str, list[str]] = {}
    current_top: str | None = None
    current_state: str | None = None

    for raw in schema_text.splitlines():
        top = re.match(r"^([A-Za-z_][A-Za-z0-9_-]*):\s*$", raw)
        if top:
            current_top = top.group(1)
            current_state = None
            continue

        state = re.match(r"^\s{2}([A-Za-z_][A-Za-z0-9_-]*):\s*$", raw)
        if state and current_top == "required_top_level_sections":
            current_state = state.group(1)
            result[current_state] = []
            continue

        item = re.match(r"^\s{4}-\s*(.+?)\s*$", raw)
        if item and current_state:
            result[current_state].append(clean_scalar(item.group(1)))

    return result


def parse_minimum_examples(schema_text: str) -> int:
    match = re.search(r"minimum_examples:\s*(\d+)", schema_text)
    if not match:
        return 12
    return int(match.group(1))


def parse_examples(path: Path) -> list[dict[str, object]]:
    examples: list[dict[str, object]] = []
    current: dict[str, object] | None = None
    current_list: str | None = None

    for raw in path.read_text(encoding="utf-8").splitlines():
        if not raw.strip() or raw.lstrip().startswith("#"):
            continue

        start = re.match(r"^\s{2}- id:\s*(.+?)\s*$", raw)
        if start:
            if current:
                examples.append(current)
            current = {"id": clean_scalar(start.group(1)), "surface": []}
            current_list = None
            continue

        if current is None:
            continue

        scalar = re.match(r"^\s{4}([A-Za-z_][A-Za-z0-9_-]*):\s*(.*?)\s*$", raw)
        if scalar:
            key, value = scalar.group(1), scalar.group(2)
            if key == "surface" and not value:
                current_list = "surface"
            elif key == "safety_relevant":
                current[key] = clean_scalar(value).lower() == "true"
                current_list = None
            else:
                current[key] = clean_scalar(value)
                current_list = None
            continue

        item = re.match(r"^\s{6}-\s*(.+?)\s*$", raw)
        if item and current_list == "surface":
            current["surface"].append(clean_scalar(item.group(1)))  # type: ignore[index]

    if current:
        examples.append(current)

    return examples


def validate(repo_root: Path) -> list[str]:
    errors: list[str] = []
    state_dir = repo_root / "state"
    schema_path = state_dir / "state-schema.yaml"
    examples_path = state_dir / "state-examples.yaml"

    if not state_dir.exists():
        return [f"Missing state directory: {state_dir}"]

    for file_name in sorted(REQUIRED_STATE_FILES):
        if not (state_dir / file_name).exists():
            errors.append(f"Missing state file: state/{file_name}")

    if not schema_path.exists():
        return errors

    schema_text = schema_path.read_text(encoding="utf-8")
    schema_top = top_level_keys(schema_text)
    for section in sorted(REQUIRED_SCHEMA_SECTIONS):
        if section not in schema_top:
            errors.append(f"state-schema.yaml: missing section '{section}'")

    required_sections = parse_schema_required_sections(schema_text)
    for file_name, top_key in sorted(REQUIRED_TOP_LEVEL.items()):
        path = state_dir / file_name
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        if top_key not in top_level_keys(text):
            errors.append(f"{file_name}: missing top-level key '{top_key}'")
            continue
        actual_sections = second_level_keys(text, top_key)
        for section in required_sections.get(top_key, []):
            if section not in actual_sections:
                errors.append(f"{file_name}: missing section '{section}'")

    if examples_path.exists():
        examples = parse_examples(examples_path)
        minimum_examples = parse_minimum_examples(schema_text)
        if len(examples) < minimum_examples:
            errors.append(
                f"state-examples.yaml: expected at least {minimum_examples} examples, found {len(examples)}"
            )

        ids: set[str] = set()
        covered_surfaces: set[str] = set()
        for example in examples:
            example_id = str(example.get("id", ""))
            surfaces: list[str] = example.get("surface", [])  # type: ignore[assignment]
            safety_relevant = bool(example.get("safety_relevant", False))

            if not example_id:
                errors.append("state-examples.yaml: example missing id")
                continue
            if example_id in ids:
                errors.append(f"state-examples.yaml: duplicate example id '{example_id}'")
            ids.add(example_id)

            for field in sorted(REQUIRED_EXAMPLE_FIELDS):
                if field not in example:
                    errors.append(f"{example_id}: missing example field '{field}'")

            if not surfaces:
                errors.append(f"{example_id}: missing surface coverage")
            covered_surfaces.update(surfaces)
            unknown_surfaces = sorted(set(surfaces) - REQUIRED_EXAMPLE_SURFACES)
            for surface in unknown_surfaces:
                errors.append(f"{example_id}: unknown surface '{surface}'")

            if safety_relevant and "safety_gate" not in example:
                errors.append(f"{example_id}: safety-relevant example missing safety_gate")

        for surface in sorted(REQUIRED_EXAMPLE_SURFACES - covered_surfaces):
            errors.append(f"state-examples.yaml: no example covers '{surface}'")

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

    case_count = len(parse_examples(repo_root / "state" / "state-examples.yaml"))
    print(f"Validated culinary state model with {case_count} examples.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
