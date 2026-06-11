from __future__ import annotations

from pathlib import Path
import argparse
import csv

from .models import DigitalStorytellingGovernanceConfig, DigitalStorytellingGovernanceRecord
from .validation import validate_record
from .scoring import ai_synthetic_story_risk, archive_memory_strength, context_collapse_risk, governance_priority_score, platform_formula_drift, platform_narrative_integrity, review_priority
from .governance import build_digital_storytelling_governance_card, governance_note
from .exporters import write_csv, write_json, write_markdown_queue


FIELD_NAMES = [
    "context_preservation", "source_authority", "visibility_provenance_fit",
    "audience_care", "medium_format_fit", "ethical_governance",
    "audience_spread", "compression_severity", "hostile_context_exposure",
    "engagement_intensity", "sensitive_visibility", "governance_review",
    "hook_overdependence", "trend_compliance", "metric_pressure",
    "retention_framing", "outrage_signaling", "judgment_stability",
    "archive_metadata", "consent_status", "preservation_plan", "access_context",
    "synthetic_opacity", "voice_imitation", "provenance_loss", "ai_context_loss",
    "manipulation_targeting", "human_review", "public_consequence"
]


def load_records(path: Path, config: DigitalStorytellingGovernanceConfig) -> list[DigitalStorytellingGovernanceRecord]:
    records: list[DigitalStorytellingGovernanceRecord] = []
    with path.open("r", encoding="utf-8", newline="") as handle:
        for row in csv.DictReader(handle):
            values = {name: float(row[name]) for name in FIELD_NAMES}
            record = DigitalStorytellingGovernanceRecord(
                item=row["item"],
                platform_context=row["platform_context"],
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


def record_to_row(record: DigitalStorytellingGovernanceRecord, config: DigitalStorytellingGovernanceConfig) -> dict[str, object]:
    return {
        "item": record.item,
        "platform_context": record.platform_context,
        "platform_narrative_integrity": round(platform_narrative_integrity(record), 4),
        "context_collapse_risk": round(context_collapse_risk(record), 4),
        "platform_formula_drift": round(platform_formula_drift(record), 4),
        "archive_memory_strength": round(archive_memory_strength(record), 4),
        "ai_synthetic_story_risk": round(ai_synthetic_story_risk(record), 4),
        "governance_priority_score": round(governance_priority_score(record, config), 4),
        "review_priority": review_priority(record, config),
        "owner": record.owner,
        "status": record.status,
        "governance_note": governance_note(record, config),
    }


def run(article_root: Path, input_path: Path | None = None, output_dir: Path | None = None) -> None:
    article_root = article_root.resolve()
    config = DigitalStorytellingGovernanceConfig()
    input_path = input_path or article_root / "data" / "digital_storytelling_governance_claims.csv"
    output_dir = output_dir or article_root / "outputs"

    records = load_records(input_path, config)
    rows = [record_to_row(record, config) for record in records]
    cards = [build_digital_storytelling_governance_card(record, config) for record in records]

    priority_order = {"high": 3, "medium": 2, "standard": 1}
    rows = sorted(rows, key=lambda row: (priority_order.get(str(row["review_priority"]), 0), float(row["governance_priority_score"])), reverse=True)

    queue = [row for row in rows if row["review_priority"] != "standard"]
    queue_cards = [card for card in cards if card["review"]["priority"] != "standard"]

    write_csv(output_dir / "tables" / "digital_storytelling_governance_audit.csv", rows)
    write_csv(output_dir / "tables" / "digital_storytelling_governance_queue.csv", queue)
    write_json(output_dir / "json" / "digital_storytelling_governance_canvas_cards.json", cards)
    write_json(output_dir / "json" / "digital_storytelling_governance_queue.json", queue_cards)
    write_markdown_queue(output_dir / "markdown" / "digital_storytelling_governance_queue.md", queue)

    print("Digital storytelling governance audit complete.")
    print(output_dir / "tables" / "digital_storytelling_governance_audit.csv")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Run digital storytelling governance Canvas audit.")
    parser.add_argument("--article-root", type=Path, default=Path(__file__).resolve().parents[2])
    parser.add_argument("--input", type=Path, default=None)
    parser.add_argument("--output-dir", type=Path, default=None)
    return parser


def main() -> None:
    args = build_parser().parse_args()
    run(args.article_root, args.input, args.output_dir)


if __name__ == "__main__":
    main()
