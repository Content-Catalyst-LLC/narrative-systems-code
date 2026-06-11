from __future__ import annotations

from pathlib import Path
import argparse
import csv

from .models import OrganizationalStoryGovernanceConfig, OrganizationalStoryGovernanceRecord
from .validation import validate_record
from .scoring import ai_organizational_story_risk, change_credibility, employee_voice_integrity, governance_priority_score, narrative_extraction_risk, organizational_memory_strength, purpose_alignment, review_priority
from .governance import build_organizational_story_governance_card, governance_note
from .exporters import write_csv, write_json, write_markdown_queue


FIELD_NAMES = [
    "mission_clarity", "decision_alignment", "budget_fit", "stakeholder_impact",
    "employee_experience", "governance_transparency", "evidence_visibility",
    "participation_integrity", "resource_support", "loss_acknowledgment",
    "feedback_loops", "accountability_measures", "consent_deficit",
    "selection_bias", "power_asymmetry", "emotional_targeting",
    "brand_repurposing", "agency", "employee_voice_protection",
    "dissent_visibility", "memory_preservation", "learning_followthrough",
    "summary_dependence", "omitted_dissent", "context_loss", "privacy_risk",
    "uncertainty_erasure", "human_review", "public_consequence"
]


def load_records(path: Path, config: OrganizationalStoryGovernanceConfig) -> list[OrganizationalStoryGovernanceRecord]:
    records: list[OrganizationalStoryGovernanceRecord] = []
    with path.open("r", encoding="utf-8", newline="") as handle:
        for row in csv.DictReader(handle):
            values = {name: float(row[name]) for name in FIELD_NAMES}
            record = OrganizationalStoryGovernanceRecord(
                item=row["item"],
                claim_context=row["claim_context"],
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


def record_to_row(record: OrganizationalStoryGovernanceRecord, config: OrganizationalStoryGovernanceConfig) -> dict[str, object]:
    return {
        "item": record.item,
        "claim_context": record.claim_context,
        "purpose_alignment": round(purpose_alignment(record), 4),
        "change_credibility": round(change_credibility(record), 4),
        "narrative_extraction_risk": round(narrative_extraction_risk(record), 4),
        "employee_voice_integrity": round(employee_voice_integrity(record), 4),
        "organizational_memory_strength": round(organizational_memory_strength(record), 4),
        "ai_organizational_story_risk": round(ai_organizational_story_risk(record), 4),
        "governance_priority_score": round(governance_priority_score(record, config), 4),
        "review_priority": review_priority(record, config),
        "owner": record.owner,
        "status": record.status,
        "governance_note": governance_note(record, config),
    }


def run(article_root: Path, input_path: Path | None = None, output_dir: Path | None = None) -> None:
    article_root = article_root.resolve()
    config = OrganizationalStoryGovernanceConfig()
    input_path = input_path or article_root / "data" / "organizational_story_governance_claims.csv"
    output_dir = output_dir or article_root / "outputs"

    records = load_records(input_path, config)
    rows = [record_to_row(record, config) for record in records]
    cards = [build_organizational_story_governance_card(record, config) for record in records]

    priority_order = {"high": 3, "medium": 2, "standard": 1}
    rows = sorted(rows, key=lambda row: (priority_order.get(str(row["review_priority"]), 0), float(row["governance_priority_score"])), reverse=True)

    queue = [row for row in rows if row["review_priority"] != "standard"]
    queue_cards = [card for card in cards if card["review"]["priority"] != "standard"]

    write_csv(output_dir / "tables" / "organizational_story_governance_audit.csv", rows)
    write_csv(output_dir / "tables" / "organizational_story_governance_queue.csv", queue)
    write_json(output_dir / "json" / "organizational_story_governance_canvas_cards.json", cards)
    write_json(output_dir / "json" / "organizational_story_governance_queue.json", queue_cards)
    write_markdown_queue(output_dir / "markdown" / "organizational_story_governance_queue.md", queue)

    print("Organizational story governance audit complete.")
    print(output_dir / "tables" / "organizational_story_governance_audit.csv")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Run organizational story governance Canvas audit.")
    parser.add_argument("--article-root", type=Path, default=Path(__file__).resolve().parents[2])
    parser.add_argument("--input", type=Path, default=None)
    parser.add_argument("--output-dir", type=Path, default=None)
    return parser


def main() -> None:
    args = build_parser().parse_args()
    run(args.article_root, args.input, args.output_dir)


if __name__ == "__main__":
    main()
