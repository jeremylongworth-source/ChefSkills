from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter
from decimal import Decimal, ROUND_HALF_UP
from pathlib import Path
from typing import Any


SUMMARY_VERSION = "0.1"
ROUNDING = Decimal("0.0001")


def clean_scalar(value: str) -> str:
    value = value.strip()
    if (value.startswith('"') and value.endswith('"')) or (
        value.startswith("'") and value.endswith("'")
    ):
        return value[1:-1]
    return value


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


def as_decimal(value: Any) -> Decimal:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise TypeError(f"Expected numeric score, found {value!r}")
    return Decimal(str(value))


def rounded(value: Decimal) -> float:
    return float(value.quantize(ROUNDING, rounding=ROUND_HALF_UP))


def average(values: list[Decimal]) -> Decimal:
    if not values:
        return Decimal("0")
    return sum(values, Decimal("0")) / Decimal(len(values))


def top_entries(
    rows: list[dict[str, Any]],
    *,
    key: str,
    reverse: bool,
    limit: int = 3,
) -> list[dict[str, Any]]:
    return sorted(
        rows,
        key=lambda row: (row[key], row.get("fixture_id", row.get("criterion", ""))),
        reverse=reverse,
    )[:limit]


def build_readiness(
    *,
    cards: list[dict[str, Any]],
    blocker_count: int,
    decision_counts: Counter[str],
    chefskills_average: Decimal,
    min_chefskills_fixture: dict[str, Any],
    min_delta_fixture: dict[str, Any],
) -> dict[str, Any]:
    ready_for_limited_05c = (
        blocker_count == 0
        and decision_counts == {"keep": len(cards)}
        and chefskills_average >= Decimal("4.25")
        and as_decimal(min_chefskills_fixture["chefskills_average"]) >= Decimal("4.0")
    )

    if not ready_for_limited_05c:
        return {
            "status": "hold_for_more_05b",
            "rationale": "ChefSkills has not yet cleared the foundation evidence gate for specialist expansion.",
            "next_milestone": "CHEFSKILLS-05B Follow-Up Evaluation",
            "constraints": [
                "Resolve blockers before adding new specialist skills.",
                "Improve the lowest-scored fixtures before broadening coverage.",
                "Safety-critical guidance still requires current authoritative source checks.",
                "Do not treat low-confidence reports as release-grade proof.",
            ],
            "lowest_scored_fixture": min_chefskills_fixture["fixture_id"],
            "lowest_delta_fixture": min_delta_fixture["fixture_id"],
        }

    suite_ids = {card["suite"] for card in cards}

    if "equipment-05c-stabilization" in suite_ids:
        status = "ready_for_public_alpha_readiness_work"
        rationale = (
            "ChefSkills cleared equipment stabilization with no blockers and a skill-enabled "
            "average above the release threshold. The next work should shift from specialist "
            "growth to public-alpha readiness because core specialist coverage is now stable enough "
            "for repository operations, documentation, and publication audits."
        )
        next_milestone = "CHEFSKILLS-06 Public Alpha Readiness Workflow"
        constraints = [
            "Do not add Michelin, Canadian commercial food safety, or other large specialist tracks before public-alpha gates are in place.",
            "Add CI, issue templates, PR templates, and public documentation before changing repository visibility.",
            "Label or improve medium-confidence simulated evaluation evidence before public release.",
            "Run publication audits for secrets, prompt injection, data exfiltration, script permissions, supply chain, safety, and attribution.",
        ]
    elif "equipment-05c-smoke" in suite_ids:
        status = "ready_for_equipment_stabilization"
        rationale = (
            "ChefSkills cleared the equipment smoke pass with no blockers and a skill-enabled "
            "average above the release threshold. Equipment should be stabilized before the next "
            "specialist because all report confidence values are medium and the domain has only one smoke report."
        )
        next_milestone = "CHEFSKILLS-05C Equipment Specialist Stabilization"
        constraints = [
            "Add lower-risk equipment quality fixtures and additional appliance safety cases before broadening specialist coverage.",
            "Every new or stabilized specialist skill needs fixtures, routing cases, and scorecard coverage.",
            "Safety-critical equipment advice still requires current authoritative source checks.",
            "Do not treat current medium-confidence reports as release-grade proof.",
        ]
    elif "fermentation-05c-stabilization" in suite_ids:
        status = "ready_for_next_05c_specialist"
        rationale = (
            "ChefSkills cleared the fermentation stabilization pass with no blockers and a skill-enabled "
            "average above the release threshold. Expansion should still stay narrow because all report "
            "confidence values are medium and the next specialist needs its own smoke evidence."
        )
        next_milestone = "CHEFSKILLS-05C Equipment Specialist Expansion"
        constraints = [
            "Add only one specialist domain before the next stabilization pass.",
            "Every new specialist skill needs fixtures, routing cases, and scorecard coverage.",
            "Safety-critical specialist domains still require current authoritative source checks.",
            "Do not treat current medium-confidence reports as release-grade proof.",
        ]
    elif "fermentation-05c-smoke" in suite_ids:
        status = "ready_for_fermentation_stabilization"
        rationale = (
            "ChefSkills cleared the fermentation smoke pass with no blockers and a skill-enabled "
            "average above the release threshold. Expansion should still be limited because all "
            "report confidence values are medium and fermentation has only one smoke report."
        )
        next_milestone = "CHEFSKILLS-05C Fermentation Stabilization"
        constraints = [
            "Add lower-risk fermentation flavor and troubleshooting fixtures before broadening preservation claims.",
            "Every new or stabilized specialist skill needs fixtures, routing cases, and scorecard coverage.",
            "Safety-critical specialist domains still require current authoritative source checks.",
            "Do not treat current medium-confidence reports as release-grade proof.",
        ]
    elif "specialist-05c-stabilization" in suite_ids:
        status = "ready_for_next_05c_specialist"
        rationale = (
            "ChefSkills cleared the first specialist stabilization pass with no blockers and a "
            "skill-enabled average above the release threshold. Expansion should still be limited "
            "because all report confidence values are medium and the fixture set is small."
        )
        next_milestone = "CHEFSKILLS-05C Next Specialist Expansion"
        constraints = [
            "Limit the next 05C expansion to one additional specialist domain.",
            "Every new specialist skill needs fixtures, routing cases, and scorecard coverage.",
            "Safety-critical specialist domains still require current authoritative source checks.",
            "Do not treat current medium-confidence reports as release-grade proof.",
        ]
    else:
        status = "ready_for_limited_05c"
        rationale = (
            "ChefSkills cleared the current foundation evidence gate with no blockers, all keep decisions, "
            "and a skill-enabled average above the release threshold. Expansion should still be limited "
            "because all report confidence values are medium and the fixture set is small."
        )
        next_milestone = "CHEFSKILLS-05C Specialist Expansion"
        constraints = [
            "Limit initial 05C work to a small number of specialist skills.",
            "Every new specialist skill needs fixtures, routing cases, and scorecard coverage.",
            "Safety-critical specialist domains still require current authoritative source checks.",
            "Do not treat current medium-confidence reports as release-grade proof.",
        ]

    return {
        "status": status,
        "rationale": rationale,
        "next_milestone": next_milestone,
        "constraints": constraints,
        "lowest_scored_fixture": min_chefskills_fixture["fixture_id"],
        "lowest_delta_fixture": min_delta_fixture["fixture_id"],
    }


def build_summary(repo_root: Path) -> dict[str, Any]:
    index_path = repo_root / "evaluation" / "reports" / "index.yaml"
    reports = parse_report_index(index_path)
    cards: list[dict[str, Any]] = []

    for report in reports:
        scorecard_path = repo_root / str(report["scorecard"])
        cards.append(json.loads(scorecard_path.read_text(encoding="utf-8")))

    fixtures: list[tuple[dict[str, Any], dict[str, Any]]] = [
        (card, fixture) for card in cards for fixture in card["fixtures"]
    ]

    if not fixtures:
        raise ValueError("No scorecard fixtures found")

    criteria = list(fixtures[0][1]["scores"]["baseline"].keys())
    baseline_average = average([as_decimal(fixture["baseline_average"]) for _, fixture in fixtures])
    chefskills_average = average([as_decimal(fixture["chefskills_average"]) for _, fixture in fixtures])
    delta = chefskills_average - baseline_average

    by_report: list[dict[str, Any]] = []
    for card in cards:
        by_report.append(
            {
                "report_id": card["report_id"],
                "suite": card["suite"],
                "decision": card["decision"],
                "confidence": card["confidence"],
                "fixture_count": len(card["fixtures"]),
                "baseline_average": rounded(as_decimal(card["overall"]["baseline_average"])),
                "chefskills_average": rounded(as_decimal(card["overall"]["chefskills_average"])),
                "delta": rounded(as_decimal(card["overall"]["delta"])),
                "blockers": card["blockers"],
            }
        )

    by_fixture: list[dict[str, Any]] = []
    for card, fixture in fixtures:
        by_fixture.append(
            {
                "fixture_id": fixture["fixture_id"],
                "report_id": card["report_id"],
                "decision": fixture["decision"],
                "baseline_average": rounded(as_decimal(fixture["baseline_average"])),
                "chefskills_average": rounded(as_decimal(fixture["chefskills_average"])),
                "delta": rounded(as_decimal(fixture["delta"])),
                "blockers": fixture["blockers"],
            }
        )

    by_criterion: dict[str, dict[str, float]] = {}
    criterion_rows: list[dict[str, Any]] = []
    for criterion in criteria:
        baseline = average(
            [as_decimal(fixture["scores"]["baseline"][criterion]) for _, fixture in fixtures]
        )
        chefskills = average(
            [as_decimal(fixture["scores"]["chefskills"][criterion]) for _, fixture in fixtures]
        )
        criterion_delta = chefskills - baseline
        row = {
            "criterion": criterion,
            "baseline_average": rounded(baseline),
            "chefskills_average": rounded(chefskills),
            "delta": rounded(criterion_delta),
        }
        by_criterion[criterion] = {
            "baseline_average": row["baseline_average"],
            "chefskills_average": row["chefskills_average"],
            "delta": row["delta"],
        }
        criterion_rows.append(row)

    blocker_count = sum(len(card["blockers"]) for card in cards) + sum(
        len(fixture["blockers"]) for _, fixture in fixtures
    )
    decision_counts = Counter(card["decision"] for card in cards)
    confidence_counts = Counter(card["confidence"] for card in cards)
    min_chefskills_fixture = min(by_fixture, key=lambda row: row["chefskills_average"])
    min_delta_fixture = min(by_fixture, key=lambda row: row["delta"])

    return {
        "summary_version": SUMMARY_VERSION,
        "date": max(card["date"] for card in cards),
        "source": "evaluation/reports/index.yaml",
        "report_count": len(cards),
        "fixture_count": len(fixtures),
        "blocker_count": blocker_count,
        "decision_counts": dict(sorted(decision_counts.items())),
        "confidence_counts": dict(sorted(confidence_counts.items())),
        "overall": {
            "baseline_average": rounded(baseline_average),
            "chefskills_average": rounded(chefskills_average),
            "delta": rounded(delta),
        },
        "by_report": by_report,
        "by_criterion": by_criterion,
        "largest_criterion_gains": top_entries(criterion_rows, key="delta", reverse=True),
        "weakest_chefskills_criteria": top_entries(
            criterion_rows, key="chefskills_average", reverse=False
        ),
        "by_fixture": by_fixture,
        "largest_fixture_gains": top_entries(by_fixture, key="delta", reverse=True),
        "lowest_fixture_gains": top_entries(by_fixture, key="delta", reverse=False),
        "readiness": build_readiness(
            cards=cards,
            blocker_count=blocker_count,
            decision_counts=decision_counts,
            chefskills_average=chefskills_average,
            min_chefskills_fixture=min_chefskills_fixture,
            min_delta_fixture=min_delta_fixture,
        ),
    }


def resolve_output(repo_root: Path, value: str) -> Path:
    path = Path(value)
    if not path.is_absolute():
        path = repo_root / path
    return path


def render(summary: dict[str, Any]) -> str:
    return json.dumps(summary, indent=2, sort_keys=False) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo-root", default=Path(__file__).resolve().parents[1])
    parser.add_argument("--output", help="Write the summary JSON to this path.")
    parser.add_argument("--check", help="Fail if this summary JSON is missing or stale.")
    args = parser.parse_args()

    repo_root = Path(args.repo_root).resolve()
    summary = build_summary(repo_root)

    if args.check:
        output_path = resolve_output(repo_root, args.check)
        if not output_path.exists():
            print(f"Missing scorecard summary: {output_path}", file=sys.stderr)
            return 1
        actual = json.loads(output_path.read_text(encoding="utf-8"))
        if actual != summary:
            print(f"Scorecard summary is stale: {output_path}", file=sys.stderr)
            print(
                "Regenerate it with scripts/summarize-scorecards.py "
                "--output evaluation/scorecards/summary.json",
                file=sys.stderr,
            )
            return 1
        print("Validated scorecard summary.")
        return 0

    if args.output:
        output_path = resolve_output(repo_root, args.output)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(render(summary), encoding="utf-8")
        print(f"Wrote {output_path}")
        return 0

    print(render(summary), end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
