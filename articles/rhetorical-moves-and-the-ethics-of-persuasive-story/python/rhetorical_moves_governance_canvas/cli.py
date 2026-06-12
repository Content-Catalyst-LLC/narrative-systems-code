from __future__ import annotations

from pathlib import Path
import argparse
import csv

from .models import RhetoricalMovesGovernanceConfig, RhetoricalMovesGovernanceRecord
from .validation import validate_record
from .scoring import ai_persuasion_risk, audience_agency_score, governance_priority_score, manipulation_risk, platform_persuasion_risk, rhetorical_integrity, review_priority
from .governance import build_rhetorical_moves_governance_card, governance_note
from .exporters import write_csv, write_json, write_markdown_queue


FIELD_NAMES = [
    "evidence_truthfulness", "proportionality", "context_adequacy",
    "dignity_protection", "audience_agency", "transparency",
    "fear_amplification", "emotional_exploitation", "omission_of_context",
    "social_proof_pressure", "urgency_coercion", "judgment_review",
    "claim_clarity", "uncertainty_disclosure", "tradeoff_openness",
    "evidence_visibility", "response_optionality", "question_space",
    "platform_amplification", "microtargeting_intensity", "context_collapse_risk",
    "sponsorship_clarity", "personalization_targeting", "vulnerability_exploitation",
    "synthetic_evidence_risk", "opaque_testing", "data_opacity",
    "human_review", "public_consequence"
]


def load_records(path: Path, config: RhetoricalMovesGovernanceConfig) -> list[RhetoricalMovesGovernanceRecord]:
    records: list[RhetoricalMovesGovernanceRecord] = []
    with path.open("r", encoding="utf-8", newline="") as handle:
        for row in csv.DictReader(handle):
            values = {name: float(row[name]) for name in FIELD_NAMES}
            record = RhetoricalMovesGovernanceRecord(
                item=row["item"],
                persuasion_context=row["persuasion_context"],
                owner=row.get("owner", "editorial"),
                status=row.get("status", "active"),
                notes=row.get("notes", ""),
                **values,
            )
            validate_record(record, config)
            records.append(record)
    if not records:
        raise ValueError(f"No records found in {path}")
    return records


def record_to_row(record: RhetoricalMovesGovernanceRecord, config: RhetoricalMovesGovernanceConfig) -> dict[str, object]:
    return {
        "item": record.item,
        "persuasion_context": record.persuasion_context,
        "rhetorical_integrity": round(rhetorical_integrity(record), 4),
        "manipulation_risk": round(manipulation_risk(record), 4),
        "audience_agency_score": round(audience_agency_score(record), 4),
        "platform_persuasion_risk": round(platform_persuasion_risk(record), 4),
        "ai_persuasion_risk": round(ai_persuasion_risk(record), 4),
        "governance_priority_score": round(governance_priority_score(record, config), 4),
        "review_priority": review_priority(record, config),
        "owner": record.owner,
        "status": record.status,
        "governance_note": governance_note(record, config),
    }


def run(article_root: Path, input_path: Path | None = None, output_dir: Path | None = None) -> None:
    article_root = article_root.resolve()
    config = RhetoricalMovesGovernanceConfig()
    input_path = input_path or article_root / "data" / "rhetorical_moves_governance_claims.csv"
    output_dir = output_dir or article_root / "outputs"

    records = load_records(input_path, config)
    rows = [record_to_row(record, config) for record in records]
    cards = [build_rhetorical_moves_governance_card(record, config) for record in records]

    priority_order = {"high": 3, "medium": 2, "standard": 1}
    rows = sorted(rows, key=lambda row: (priority_order.get(str(row["review_priority"]), 0), float(row["governance_priority_score"])), reverse=True)

    queue = [row for row in rows if row["review_priority"] != "standard"]
    queue_cards = [card for card in cards if card["review"]["priority"] != "standard"]

    write_csv(output_dir / "tables" / "rhetorical_moves_governance_audit.csv", rows)
    write_csv(output_dir / "tables" / "rhetorical_moves_governance_queue.csv", queue)
    write_json(output_dir / "json" / "rhetorical_moves_governance_canvas_cards.json", cards)
    write_json(output_dir / "json" / "rhetorical_moves_governance_queue.json", queue_cards)
    write_markdown_queue(output_dir / "markdown" / "rhetorical_moves_governance_queue.md", queue)

    print("Rhetorical moves governance audit complete.")
    print(output_dir / "tables" / "rhetorical_moves_governance_audit.csv")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Run rhetorical moves governance Canvas audit.")
    parser.add_argument("--article-root", type=Path, default=Path(__file__).resolve().parents[2])
    parser.add_argument("--input", type=Path, default=None)
    parser.add_argument("--output-dir", type=Path, default=None)
    return parser


def main() -> None:
    args = build_parser().parse_args()
    run(args.article_root, args.input, args.output_dir)


if __name__ == "__main__":
    main()
