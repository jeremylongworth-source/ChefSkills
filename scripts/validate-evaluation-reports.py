from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


REQUIRED_REPORT_FIELDS = {
    "id",
    "report",
    "scorecard",
    "run_dir",
    "baseline_output",
    "skill_enabled_output",
    "suite",
    "decision",
    "confidence",
    "fixtures",
    "blockers",
}

REQUIRED_REPORT_SECTIONS = {
    "## Decision",
    "## Evidence",
    "## Acceptance Criteria",
    "## Score Summary",
    "## Blockers",
    "## Gaps Found",
    "## Follow-Up Changes",
}

ALLOWED_DECISIONS = {"keep", "revise", "split", "merge", "defer", "retire"}
ALLOWED_CONFIDENCE = {"high", "medium", "low"}


def clean_scalar(value: str) -> str:
    value = value.strip()
    if (value.startswith('"') and value.endswith('"')) or (
        value.startswith("'") and value.endswith("'")
    ):
        return value[1:-1]
    return value


def parse_fixture_ids(path: Path) -> set[str]:
    return {
        clean_scalar(match.group(1))
        for raw in path.read_text(encoding="utf-8").splitlines()
        if (match := re.match(r"^\s{2}- id:\s*(.+?)\s*$", raw))
    }


def parse_suite_ids(path: Path) -> set[str]:
    return {
        clean_scalar(match.group(1))
        for raw in path.read_text(encoding="utf-8").splitlines()
        if (match := re.match(r"^\s{2}- id:\s*(.+?)\s*$", raw))
    }


def parse_report_index(path: Path) -> list[dict[str, object]]:
    reports: list[dict[str, object]] = []
    current: dict[str, object] | None = None
    current_list: str | None = None

    for raw in path.read_text(encoding="utf-8").splitlines():
        if not raw.strip() or raw.lstrip().startswith("#"):
            continue

        start = re.match(r"^\s{2}- id:\s*(.+?)\s*$", raw)
        if start:
            if current:
                reports.append(current)
            current = {"id": clean_scalar(start.group(1)), "fixtures": [], "blockers": []}
            current_list = None
            continue

        if current is None:
            continue

        scalar = re.match(r"^\s{4}([A-Za-z_][A-Za-z0-9_-]*):\s*(.*?)\s*$", raw)
        if scalar:
            key, value = scalar.group(1), scalar.group(2)
            if key in {"fixtures", "blockers"} and not value:
                current_list = key
            elif key == "blockers" and value == "[]":
                current[key] = []
                current_list = None
            else:
                current[key] = clean_scalar(value)
                current_list = None
            continue

        item = re.match(r"^\s{6}-\s*(.+?)\s*$", raw)
        if item and current_list:
            current[current_list].append(clean_scalar(item.group(1)))  # type: ignore[index]

    if current:
        reports.append(current)

    return reports


def parse_minimum_reports(path: Path) -> int:
    text = path.read_text(encoding="utf-8")
    match = re.search(r"^minimum_reports:\s*(\d+)\s*$", text, re.M)
    if not match:
        return 1
    return int(match.group(1))


def validate(repo_root: Path) -> list[str]:
    errors: list[str] = []
    reports_dir = repo_root / "evaluation" / "reports"
    index_path = reports_dir / "index.yaml"
    fixtures_path = repo_root / "evaluation" / "fixtures.yaml"
    suites_path = repo_root / "evaluation" / "regression-suite.yaml"

    if not index_path.exists():
        return [f"Missing report index: {index_path}"]

    known_fixtures = parse_fixture_ids(fixtures_path)
    known_suites = parse_suite_ids(suites_path)
    reports = parse_report_index(index_path)
    minimum_reports = parse_minimum_reports(index_path)

    if len(reports) < minimum_reports:
        errors.append(
            f"evaluation/reports/index.yaml: expected at least {minimum_reports} reports, found {len(reports)}"
        )

    ids: set[str] = set()
    for report in reports:
        report_id = str(report.get("id", ""))
        if not report_id:
            errors.append("evaluation/reports/index.yaml: report missing id")
            continue
        if report_id in ids:
            errors.append(f"evaluation/reports/index.yaml: duplicate report id '{report_id}'")
        ids.add(report_id)

        for field in sorted(REQUIRED_REPORT_FIELDS):
            if field not in report:
                errors.append(f"{report_id}: missing report index field '{field}'")

        decision = str(report.get("decision", ""))
        if decision and decision not in ALLOWED_DECISIONS:
            errors.append(f"{report_id}: invalid decision '{decision}'")

        confidence = str(report.get("confidence", ""))
        if confidence and confidence not in ALLOWED_CONFIDENCE:
            errors.append(f"{report_id}: invalid confidence '{confidence}'")

        suite = str(report.get("suite", ""))
        if suite and suite not in known_suites:
            errors.append(f"{report_id}: unknown regression suite '{suite}'")

        for key in ("report", "scorecard", "run_dir", "baseline_output", "skill_enabled_output"):
            value = str(report.get(key, ""))
            if value and not (repo_root / value).exists():
                errors.append(f"{report_id}: missing {key} path '{value}'")

        fixtures: list[str] = report.get("fixtures", [])  # type: ignore[assignment]
        if not fixtures:
            errors.append(f"{report_id}: report must reference at least one fixture")
        for fixture in fixtures:
            if fixture not in known_fixtures:
                errors.append(f"{report_id}: unknown fixture '{fixture}'")

        report_path = repo_root / str(report.get("report", ""))
        if report_path.exists():
            text = report_path.read_text(encoding="utf-8")
            for section in sorted(REQUIRED_REPORT_SECTIONS):
                if section not in text:
                    errors.append(f"{report_id}: report missing section '{section}'")
            for fixture in fixtures:
                if fixture not in text:
                    errors.append(f"{report_id}: report does not mention fixture '{fixture}'")
            if "Baseline" not in text or "ChefSkills" not in text:
                errors.append(f"{report_id}: report must compare baseline and ChefSkills outputs")

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

    report_count = len(parse_report_index(repo_root / "evaluation" / "reports" / "index.yaml"))
    print(f"Validated {report_count} evaluation reports.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
