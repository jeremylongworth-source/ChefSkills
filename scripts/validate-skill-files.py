from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


PLACEHOLDER_PATTERNS = (
    r"\[TODO",
    r"TODO:",
    r"Structuring This Skill",
    r"Examples from other skills",
)


def clean_scalar(value: str) -> str:
    value = value.strip()
    if (value.startswith('"') and value.endswith('"')) or (
        value.startswith("'") and value.endswith("'")
    ):
        return value[1:-1]
    return value


def parse_frontmatter(text: str) -> dict[str, str]:
    match = re.match(r"\A---\s*\n(.*?)\n---\s*\n", text, re.S)
    if not match:
        return {}

    fields: dict[str, str] = {}
    for raw in match.group(1).splitlines():
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        scalar = re.match(r"^([A-Za-z_][A-Za-z0-9_-]*)\s*:\s*(.+?)\s*$", line)
        if scalar:
            fields[scalar.group(1)] = clean_scalar(scalar.group(2))
    return fields


def validate_skill(skill_dir: Path) -> list[str]:
    errors: list[str] = []
    skill_md = skill_dir / "SKILL.md"
    agent_yaml = skill_dir / "agents" / "openai.yaml"
    refs_dir = skill_dir / "references"

    if not skill_md.exists():
        return [f"{skill_dir.name}: missing SKILL.md"]

    text = skill_md.read_text(encoding="utf-8")
    fields = parse_frontmatter(text)

    if fields.get("name") != skill_dir.name:
        errors.append(f"{skill_dir.name}: frontmatter name must match folder name")
    if not fields.get("description"):
        errors.append(f"{skill_dir.name}: missing frontmatter description")
    if fields.get("license") != "MIT":
        errors.append(f"{skill_dir.name}: missing or non-MIT license")

    if "## References" not in text:
        errors.append(f"{skill_dir.name}: missing References section")
    if not re.search(r"## (Output Contract|Deliverable Shape)", text):
        errors.append(f"{skill_dir.name}: missing output contract/deliverable shape")

    for pattern in PLACEHOLDER_PATTERNS:
        if re.search(pattern, text):
            errors.append(f"{skill_dir.name}: scaffold placeholder remains")
            break

    if not agent_yaml.exists():
        errors.append(f"{skill_dir.name}: missing agents/openai.yaml")
    else:
        agent_text = agent_yaml.read_text(encoding="utf-8")
        for required in (
            "interface:",
            "display_name:",
            "short_description:",
            "default_prompt:",
        ):
            if required not in agent_text:
                errors.append(f"{skill_dir.name}: agents/openai.yaml missing {required}")

    if not refs_dir.exists():
        errors.append(f"{skill_dir.name}: missing references/")
    elif not any(path.is_file() for path in refs_dir.iterdir()):
        errors.append(f"{skill_dir.name}: references/ has no files")

    return errors


def validate(repo_root: Path) -> list[str]:
    skills_dir = repo_root / "skills"
    if not skills_dir.exists():
        return [f"Missing skills directory: {skills_dir}"]

    errors: list[str] = []
    for skill_dir in sorted(path for path in skills_dir.iterdir() if path.is_dir()):
        errors.extend(validate_skill(skill_dir))
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

    count = len([path for path in (repo_root / "skills").iterdir() if path.is_dir()])
    print(f"Validated {count} skill files.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
