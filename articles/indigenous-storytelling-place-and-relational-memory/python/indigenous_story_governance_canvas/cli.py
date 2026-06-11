from __future__ import annotations

from pathlib import Path
import argparse
import csv

from .models import IndigenousStoryGovernanceConfig, IndigenousStoryGovernanceRecord
from .validation import validate_record
from .scoring import digital_sovereignty_risk, governance_priority_score, place_memory_strength, protocol_risk, relational_accountability, review_priority, translation_governance
from .governance import build_indigenous_story_governance_card, governance_note
from .exporters import write_csv, write_json, write_markdown_queue


def load_records(path: Path, config: IndigenousStoryGovernanceConfig) -> list[IndigenousStoryGovernanceRecord]:
    records: list[IndigenousStoryGovernanceRecord] = []
    with path.open("r", encoding="utf-8", newline="") as handle:
        for row in csv.DictReader(handle):
            record = IndigenousStoryGovernanceRecord(
                item=row["item"],
                claim_context=row["claim_context"],
                place_specificity=float(row["place_specificity"]),
                community_authority=float(row["community_authority"]),
                teller_relationship=float(row["teller_relationship"]),
                listener_context=float(row["listener_context"]),
                obligation_visibility=float(row["obligation_visibility"]),
                governance_visibility=float(row["governance_visibility"]),
                access_pressure=float(row["access_pressure"]),
                seasonal_restriction=float(row["seasonal_restriction"]),
                ceremonial_restriction=float(row["ceremonial_restriction"]),
                template_forcing=float(row["template_forcing"]),
                digital_exposure=float(row["digital_exposure"]),
                land_naming=float(row["land_naming"]),
                ecological_knowledge=float(row["ecological_knowledge"]),
                ancestral_memory=float(row["ancestral_memory"]),
                route_teaching=float(row["route_teaching"]),
                seasonal_context=float(row["seasonal_context"]),
                future_generation_responsibility=float(row["future_generation_responsibility"]),
                cultural_specificity=float(row["cultural_specificity"]),
                language_context=float(row["language_context"]),
                opacity_notes=float(row["opacity_notes"]),
                untranslated_terms=float(row["untranslated_terms"]),
                reviewer_visibility=float(row["reviewer_visibility"]),
                harm_review=float(row["harm_review"]),
                extraction_risk=float(row["extraction_risk"]),
                open_access_assumption=float(row["open_access_assumption"]),
                ai_training_risk=float(row["ai_training_risk"]),
                stereotype_bias=float(row["stereotype_bias"]),
                metadata_flattening=float(row["metadata_flattening"]),
                community_governance=float(row["community_governance"]),
                public_consequence=float(row["public_consequence"]),
                owner=row.get("owner", "editorial"),
                status=row.get("status", "active"),
                notes=row.get("notes", ""),
            )
            validate_record(record, config)
            records.append(record)
    if not records:
        raise ValueError(f"No records found in {path}")
    return records


def record_to_row(record: IndigenousStoryGovernanceRecord, config: IndigenousStoryGovernanceConfig) -> dict[str, object]:
    return {
        "item": record.item,
        "claim_context": record.claim_context,
        "relational_accountability": round(relational_accountability(record), 4),
        "protocol_risk": round(protocol_risk(record), 4),
        "place_memory_strength": round(place_memory_strength(record), 4),
        "translation_governance": round(translation_governance(record), 4),
        "digital_sovereignty_risk": round(digital_sovereignty_risk(record), 4),
        "governance_priority_score": round(governance_priority_score(record, config), 4),
        "review_priority": review_priority(record, config),
        "owner": record.owner,
        "status": record.status,
        "governance_note": governance_note(record, config),
    }


def run(article_root: Path, input_path: Path | None = None, output_dir: Path | None = None) -> None:
    article_root = article_root.resolve()
    config = IndigenousStoryGovernanceConfig()
    input_path = input_path or article_root / "data" / "indigenous_story_governance_claims.csv"
    output_dir = output_dir or article_root / "outputs"

    records = load_records(input_path, config)
    rows = [record_to_row(record, config) for record in records]
    cards = [build_indigenous_story_governance_card(record, config) for record in records]

    priority_order = {"high": 3, "medium": 2, "standard": 1}
    rows = sorted(rows, key=lambda row: (priority_order.get(str(row["review_priority"]), 0), float(row["governance_priority_score"])), reverse=True)

    queue = [row for row in rows if row["review_priority"] != "standard"]
    queue_cards = [card for card in cards if card["review"]["priority"] != "standard"]

    write_csv(output_dir / "tables" / "indigenous_story_governance_audit.csv", rows)
    write_csv(output_dir / "tables" / "indigenous_story_governance_queue.csv", queue)
    write_json(output_dir / "json" / "indigenous_story_governance_canvas_cards.json", cards)
    write_json(output_dir / "json" / "indigenous_story_governance_queue.json", queue_cards)
    write_markdown_queue(output_dir / "markdown" / "indigenous_story_governance_queue.md", queue)

    print("Indigenous story governance audit complete.")
    print(output_dir / "tables" / "indigenous_story_governance_audit.csv")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Run Indigenous story governance Canvas audit.")
    parser.add_argument("--article-root", type=Path, default=Path(__file__).resolve().parents[2])
    parser.add_argument("--input", type=Path, default=None)
    parser.add_argument("--output-dir", type=Path, default=None)
    return parser


def main() -> None:
    args = build_parser().parse_args()
    run(args.article_root, args.input, args.output_dir)


if __name__ == "__main__":
    main()
