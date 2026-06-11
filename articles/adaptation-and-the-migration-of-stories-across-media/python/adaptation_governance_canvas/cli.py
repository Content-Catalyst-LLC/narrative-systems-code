from __future__ import annotations

from pathlib import Path
import argparse
import csv

from .models import AdaptationGovernanceConfig, AdaptationGovernanceRecord
from .validation import validate_record
from .scoring import adaptation_integrity, ai_adaptation_risk, consent_and_context_strength, franchise_drift, governance_priority_score, review_priority, transfer_loss
from .governance import build_adaptation_governance_card, governance_note
from .exporters import write_csv, write_json, write_markdown_queue


FIELD_NAMES = [
    "source_core_preservation", "medium_fit", "transformation_purpose",
    "context_preservation", "reception_value", "ethical_governance",
    "voice_loss", "interiority_loss", "context_loss", "provenance_loss",
    "agency_loss", "governance_review", "repetition_compliance",
    "lore_excess", "nostalgia_reliance", "continuity_saturation",
    "market_overextension", "story_purpose", "plot_summary_dependence",
    "voice_style_imitation", "synthetic_opacity", "uncertainty_erasure",
    "human_review", "consent_clarity", "source_authority",
    "cultural_context", "public_consequence"
]


def load_records(path: Path, config: AdaptationGovernanceConfig) -> list[AdaptationGovernanceRecord]:
    records: list[AdaptationGovernanceRecord] = []
    with path.open("r", encoding="utf-8", newline="") as handle:
        for row in csv.DictReader(handle):
            values = {name: float(row[name]) for name in FIELD_NAMES}
            record = AdaptationGovernanceRecord(
                item=row["item"],
                adaptation_context=row["adaptation_context"],
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


def record_to_row(record: AdaptationGovernanceRecord, config: AdaptationGovernanceConfig) -> dict[str, object]:
    return {
        "item": record.item,
        "adaptation_context": record.adaptation_context,
        "adaptation_integrity": round(adaptation_integrity(record), 4),
        "transfer_loss": round(transfer_loss(record), 4),
        "franchise_drift": round(franchise_drift(record), 4),
        "ai_adaptation_risk": round(ai_adaptation_risk(record), 4),
        "consent_and_context_strength": round(consent_and_context_strength(record), 4),
        "governance_priority_score": round(governance_priority_score(record, config), 4),
        "review_priority": review_priority(record, config),
        "owner": record.owner,
        "status": record.status,
        "governance_note": governance_note(record, config),
    }


def run(article_root: Path, input_path: Path | None = None, output_dir: Path | None = None) -> None:
    article_root = article_root.resolve()
    config = AdaptationGovernanceConfig()
    input_path = input_path or article_root / "data" / "adaptation_governance_claims.csv"
    output_dir = output_dir or article_root / "outputs"

    records = load_records(input_path, config)
    rows = [record_to_row(record, config) for record in records]
    cards = [build_adaptation_governance_card(record, config) for record in records]

    priority_order = {"high": 3, "medium": 2, "standard": 1}
    rows = sorted(rows, key=lambda row: (priority_order.get(str(row["review_priority"]), 0), float(row["governance_priority_score"])), reverse=True)

    queue = [row for row in rows if row["review_priority"] != "standard"]
    queue_cards = [card for card in cards if card["review"]["priority"] != "standard"]

    write_csv(output_dir / "tables" / "adaptation_governance_audit.csv", rows)
    write_csv(output_dir / "tables" / "adaptation_governance_queue.csv", queue)
    write_json(output_dir / "json" / "adaptation_governance_canvas_cards.json", cards)
    write_json(output_dir / "json" / "adaptation_governance_queue.json", queue_cards)
    write_markdown_queue(output_dir / "markdown" / "adaptation_governance_queue.md", queue)

    print("Adaptation governance audit complete.")
    print(output_dir / "tables" / "adaptation_governance_audit.csv")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Run adaptation governance Canvas audit.")
    parser.add_argument("--article-root", type=Path, default=Path(__file__).resolve().parents[2])
    parser.add_argument("--input", type=Path, default=None)
    parser.add_argument("--output-dir", type=Path, default=None)
    return parser


def main() -> None:
    args = build_parser().parse_args()
    run(args.article_root, args.input, args.output_dir)


if __name__ == "__main__":
    main()
