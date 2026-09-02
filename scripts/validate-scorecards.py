from __future__ import annotations

import argparse
import json
import re
import sys
from decimal import Decimal, ROUND_HALF_UP
from pathlib import Path
from typing import Any


REQUIRED_SCORECARD_FIELDS = {
    "scorecard_version",
    "report_id",
    "report",
    "date",
    "reviewer",
    "suite",
    "decision",
    "confidence",
    "blockers",
    "overall",
    "fixtures",
    "validation",
}

REQUIRED_OVERALL_FIELDS = {
    "baseline_average",
    "chefskills_average",
    "delta",
}

REQUIRED_FIXTURE_FIELDS = {
    "fixture_id",
    "decision",
    "blockers",
    "baseline_average",
    "chefskills_average",
    "delta",
    "scores",
    "evidence_summary",
}

REQUIRED_VALIDATION_FIELDS = {"command", "result"}
ALLOWED_DECISIONS = {"keep", "revise", "split", "merge", "defer", "retire"}
ALLOWED_CONFIDENCE = {"high", "medium", "low"}
ALLOWED_VALIDATION_RESULTS = {"pass", "fail", "not_run"}


def clean_scalar(value: str) -> str:
    value = value.strip()
    if (value.startswith('"') and value.endswith('"')) or (
        value.startswith("'") and value.endswith("'")
    ):
        return value[1:-1]
    return value


def parse_ids(path: Path, indent: int = 2) -> set[str]:
    pattern = rf"^\s{{{indent}}}- id:\s*(.+?)\s*$"
    return {
        clean_scalar(match.group(1))
        for raw in path.read_text(encoding="utf-8").splitlines()
        if (match := re.match(pattern, raw))
    }


def parse_report_index(path: Path) -> list[dict[str, Any]]:
    reports: list[dict[str, Any]] = []
    current: dict[str, Any] | None = None
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
            current[current_list].append(clean_scalar(item.group(1)))

    if current:
        reports.append(current)

    return reports


def parse_rubric_criteria(path: Path) -> set[str]:
    return {
        clean_scalar(match.group(1))
        for raw in path.read_text(encoding="utf-8").splitlines()
        if (match := re.match(r"^\s{2}- id:\s*(.+?)\s*$", raw))
    }


def round_score(value: Decimal) -> Decimal:
    return value.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)


def decimal_from_number(value: Any) -> Decimal | None:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        return None
    return Decimal(str(value))


def validate_scores(
    report_id: str,
    fixture: dict[str, Any],
    criterion_ids: set[str],
) -> list[str]:
    errors: list[str] = []
    fixture_id = str(fixture.get("fixture_id", ""))
    scores = fixture.get("scores")

    if not isinstance(scores, dict):
        return [f"{report_id}/{fixture_id}: scores must be an object"]

    for source in ("baseline", "chefskills"):
        source_scores = scores.get(source)
        if not isinstance(source_scores, dict):
            errors.append(f"{report_id}/{fixture_id}: missing scores.{source}")
            continue

        score_keys = set(source_scores)
        missing = sorted(criterion_ids - score_keys)
        extra = sorted(score_keys - criterion_ids)
        for criterion in missing:
            errors.append(f"{report_id}/{fixture_id}: scores.{source} missing '{criterion}'")
        for criterion in extra:
            errors.append(f"{report_id}/{fixture_id}: scores.{source} has unknown criterion '{criterion}'")

        total = Decimal("0")
        for criterion, score in source_scores.items():
            value = decimal_from_number(score)
            if value is None or value < 0 or value > 5:
                errors.append(
                    f"{report_id}/{fixture_id}: scores.{source}.{criterion} must be a number from 0 to 5"
                )
                continue
            total += value

        if len(source_scores) == len(criterion_ids):
            expected_average = round_score(total / Decimal(len(criterion_ids)))
            average_key = f"{source}_average" if source == "baseline" else "chefskills_average"
            actual_average = decimal_from_number(fixture.get(average_key))
            if actual_average is None:
                errors.append(f"{report_id}/{fixture_id}: {average_key} must be numeric")
            elif round_score(actual_average) != expected_average:
                errors.append(
                    f"{report_id}/{fixture_id}: {average_key} expected {expected_average}, found {actual_average}"
                )

    baseline_average = decimal_from_number(fixture.get("baseline_average"))
    chefskills_average = decimal_from_number(fixture.get("chefskills_average"))
    delta = decimal_from_number(fixture.get("delta"))
    if baseline_average is not None and chefskills_average is not None and delta is not None:
        expected_delta = round_score(chefskills_average - baseline_average)
        if round_score(delta) != expected_delta:
            errors.append(f"{report_id}/{fixture_id}: delta expected {expected_delta}, found {delta}")

    return errors


def validate_scorecard(
    repo_root: Path,
    report: dict[str, Any],
    criterion_ids: set[str],
    fixture_ids: set[str],
) -> list[str]:
    errors: list[str] = []
    report_id = str(report.get("id", ""))
    scorecard_path = repo_root / str(report.get("scorecard", ""))

    if not scorecard_path.exists():
        return [f"{report_id}: missing scorecard path '{report.get('scorecard', '')}'"]

    try:
        scorecard = json.loads(scorecard_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        return [f"{report_id}: invalid scorecard JSON: {exc}"]

    if not isinstance(scorecard, dict):
        return [f"{report_id}: scorecard must be a JSON object"]

    missing_fields = sorted(REQUIRED_SCORECARD_FIELDS - set(scorecard))
    for field in missing_fields:
        errors.append(f"{report_id}: scorecard missing field '{field}'")

    if scorecard.get("report_id") != report_id:
        errors.append(f"{report_id}: scorecard report_id does not match report index")
    if scorecard.get("report") != report.get("report"):
        errors.append(f"{report_id}: scorecard report path does not match report index")
    if scorecard.get("suite") != report.get("suite"):
        errors.append(f"{report_id}: scorecard suite does not match report index")
    if scorecard.get("decision") != report.get("decision"):
        errors.append(f"{report_id}: scorecard decision does not match report index")
    if scorecard.get("confidence") != report.get("confidence"):
        errors.append(f"{report_id}: scorecard confidence does not match report index")

    decision = str(scorecard.get("decision", ""))
    if decision and decision not in ALLOWED_DECISIONS:
        errors.append(f"{report_id}: invalid scorecard decision '{decision}'")
    confidence = str(scorecard.get("confidence", ""))
    if confidence and confidence not in ALLOWED_CONFIDENCE:
        errors.append(f"{report_id}: invalid scorecard confidence '{confidence}'")

    blockers = scorecard.get("blockers")
    if not isinstance(blockers, list):
        errors.append(f"{report_id}: blockers must be a list")
    elif blockers != report.get("blockers", []):
        errors.append(f"{report_id}: scorecard blockers do not match report index")

    overall = scorecard.get("overall")
    if not isinstance(overall, dict):
        errors.append(f"{report_id}: overall must be an object")
    else:
        for field in sorted(REQUIRED_OVERALL_FIELDS - set(overall)):
            errors.append(f"{report_id}: overall missing '{field}'")
        for field in REQUIRED_OVERALL_FIELDS:
            if field in overall and decimal_from_number(overall[field]) is None:
                errors.append(f"{report_id}: overall.{field} must be numeric")

    validation = scorecard.get("validation")
    if not isinstance(validation, dict):
        errors.append(f"{report_id}: validation must be an object")
    else:
        for field in sorted(REQUIRED_VALIDATION_FIELDS - set(validation)):
            errors.append(f"{report_id}: validation missing '{field}'")
        result = str(validation.get("result", ""))
        if result and result not in ALLOWED_VALIDATION_RESULTS:
            errors.append(f"{report_id}: invalid validation result '{result}'")

    fixtures = scorecard.get("fixtures")
    if not isinstance(fixtures, list) or not fixtures:
        errors.append(f"{report_id}: fixtures must be a non-empty list")
        return errors

    expected_fixtures = list(report.get("fixtures", []))
    actual_fixtures: list[str] = []
    baseline_total = Decimal("0")
    chefskills_total = Decimal("0")

    for fixture in fixtures:
        if not isinstance(fixture, dict):
            errors.append(f"{report_id}: fixture entry must be an object")
            continue

        for field in sorted(REQUIRED_FIXTURE_FIELDS - set(fixture)):
            errors.append(f"{report_id}: fixture entry missing '{field}'")

        fixture_id = str(fixture.get("fixture_id", ""))
        actual_fixtures.append(fixture_id)
        if fixture_id not in fixture_ids:
            errors.append(f"{report_id}: unknown fixture '{fixture_id}'")

        decision = str(fixture.get("decision", ""))
        if decision and decision not in ALLOWED_DECISIONS:
            errors.append(f"{report_id}/{fixture_id}: invalid decision '{decision}'")
        if not isinstance(fixture.get("blockers"), list):
            errors.append(f"{report_id}/{fixture_id}: blockers must be a list")
        if not isinstance(fixture.get("evidence_summary"), str) or not fixture.get("evidence_summary"):
            errors.append(f"{report_id}/{fixture_id}: evidence_summary must be non-empty")

        errors.extend(validate_scores(report_id, fixture, criterion_ids))

        baseline_average = decimal_from_number(fixture.get("baseline_average"))
        chefskills_average = decimal_from_number(fixture.get("chefskills_average"))
        if baseline_average is not None:
            baseline_total += baseline_average
        if chefskills_average is not None:
            chefskills_total += chefskills_average

    if actual_fixtures != expected_fixtures:
        errors.append(f"{report_id}: scorecard fixtures do not match report index order")

    if isinstance(overall, dict) and fixtures:
        expected_baseline_raw = baseline_total / Decimal(len(fixtures))
        expected_chefskills_raw = chefskills_total / Decimal(len(fixtures))
        expected_baseline = round_score(expected_baseline_raw)
        expected_chefskills = round_score(expected_chefskills_raw)
        expected_delta = round_score(expected_chefskills_raw - expected_baseline_raw)

        actual_baseline = decimal_from_number(overall.get("baseline_average"))
        actual_chefskills = decimal_from_number(overall.get("chefskills_average"))
        actual_delta = decimal_from_number(overall.get("delta"))

        if actual_baseline is not None and round_score(actual_baseline) != expected_baseline:
            errors.append(
                f"{report_id}: overall.baseline_average expected {expected_baseline}, found {actual_baseline}"
            )
        if actual_chefskills is not None and round_score(actual_chefskills) != expected_chefskills:
            errors.append(
                f"{report_id}: overall.chefskills_average expected {expected_chefskills}, found {actual_chefskills}"
            )
        if actual_delta is not None and round_score(actual_delta) != expected_delta:
            errors.append(f"{report_id}: overall.delta expected {expected_delta}, found {actual_delta}")

    return errors


def validate(repo_root: Path) -> list[str]:
    index_path = repo_root / "evaluation" / "reports" / "index.yaml"
    rubric_path = repo_root / "evaluation" / "rubric.yaml"
    fixtures_path = repo_root / "evaluation" / "fixtures.yaml"

    reports = parse_report_index(index_path)
    criterion_ids = parse_rubric_criteria(rubric_path)
    fixture_ids = parse_ids(fixtures_path, indent=2)

    errors: list[str] = []
    for report in reports:
        if "scorecard" not in report:
            errors.append(f"{report.get('id', '')}: missing report index field 'scorecard'")
            continue
        errors.extend(validate_scorecard(repo_root, report, criterion_ids, fixture_ids))

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
    print(f"Validated {report_count} evaluation scorecards.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
