from __future__ import annotations

from pathlib import Path
import argparse
import csv

from .models import RepresentationEthicsGovernanceConfig, RepresentationEthicsGovernanceRecord
from .validation import validate_record
from .scoring import ai_representation_risk, consent_adequacy, cultural_and_visual_strength, governance_priority_score, representation_integrity, representation_risk, review_priority
from .governance import build_representation_ethics_governance_card, governance_note
from .exporters import write_csv, write_json, write_markdown_queue


FIELD_NAMES = [
    "voice_agency", "context_preservation", "dignity_protection",
    "source_accuracy", "provenance_visibility", "accountability_capacity",
    "stereotype_tendency", "exposure_risk", "context_loss",
    "voice_replacement", "power_asymmetry", "governance_review",
    "informed_consent", "ongoing_consent", "use_clarity",
    "platform_circulation_clarity", "withdrawal_clarity", "reuse_ai_clarity",
    "cultural_protocols", "community_review", "attribution_quality",
    "image_context", "visual_dignity", "caption_accuracy",
    "synthetic_opacity", "likeness_imitation", "cultural_fabrication",
    "provenance_loss", "evidence_confusion", "human_review",
    "public_consequence"
]


def load_records(path: Path, config: RepresentationEthicsGovernanceConfig) -> list[RepresentationEthicsGovernanceRecord]:
    records: list[RepresentationEthicsGovernanceRecord] = []
    with path.open("r", encoding="utf-8", newline="") as handle:
        for row in csv.DictReader(handle):
            values = {name: float(row[name]) for name in FIELD_NAMES}
            record = RepresentationEthicsGovernanceRecord(
                item=row["item"],
                representation_context=row["representation_context"],
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


def record_to_row(record: RepresentationEthicsGovernanceRecord, config: RepresentationEthicsGovernanceConfig) -> dict[str, object]:
    return {
        "item": record.item,
        "representation_context": record.representation_context,
        "representation_integrity": round(representation_integrity(record), 4),
        "representation_risk": round(representation_risk(record), 4),
        "consent_adequacy": round(consent_adequacy(record), 4),
        "cultural_and_visual_strength": round(cultural_and_visual_strength(record), 4),
        "ai_representation_risk": round(ai_representation_risk(record), 4),
        "governance_priority_score": round(governance_priority_score(record, config), 4),
        "review_priority": review_priority(record, config),
        "owner": record.owner,
        "status": record.status,
        "governance_note": governance_note(record, config),
    }


def run(article_root: Path, input_path: Path | None = None, output_dir: Path | None = None) -> None:
    article_root = article_root.resolve()
    config = RepresentationEthicsGovernanceConfig()
    input_path = input_path or article_root / "data" / "representation_ethics_governance_claims.csv"
    output_dir = output_dir or article_root / "outputs"

    records = load_records(input_path, config)
    rows = [record_to_row(record, config) for record in records]
    cards = [build_representation_ethics_governance_card(record, config) for record in records]

    priority_order = {"high": 3, "medium": 2, "standard": 1}
    rows = sorted(rows, key=lambda row: (priority_order.get(str(row["review_priority"]), 0), float(row["governance_priority_score"])), reverse=True)

    queue = [row for row in rows if row["review_priority"] != "standard"]
    queue_cards = [card for card in cards if card["review"]["priority"] != "standard"]

    write_csv(output_dir / "tables" / "representation_ethics_governance_audit.csv", rows)
    write_csv(output_dir / "tables" / "representation_ethics_governance_queue.csv", queue)
    write_json(output_dir / "json" / "representation_ethics_governance_canvas_cards.json", cards)
    write_json(output_dir / "json" / "representation_ethics_governance_queue.json", queue_cards)
    write_markdown_queue(output_dir / "markdown" / "representation_ethics_governance_queue.md", queue)

    print("Representation ethics governance audit complete.")
    print(output_dir / "tables" / "representation_ethics_governance_audit.csv")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Run representation ethics governance Canvas audit.")
    parser.add_argument("--article-root", type=Path, default=Path(__file__).resolve().parents[2])
    parser.add_argument("--input", type=Path, default=None)
    parser.add_argument("--output-dir", type=Path, default=None)
    return parser


def main() -> None:
    args = build_parser().parse_args()
    run(args.article_root, args.input, args.output_dir)


if __name__ == "__main__":
    main()
