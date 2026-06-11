from __future__ import annotations

from pathlib import Path
import argparse
import csv

from .models import ComparativeStoryGovernanceConfig, ComparativeStoryGovernanceRecord
from .validation import validate_record
from .scoring import ai_comparative_risk, comparative_integrity, contextual_grounding, flattening_risk, governance_priority_score, review_priority, transmission_uncertainty
from .governance import build_comparative_story_governance_card, governance_note
from .exporters import write_csv, write_json, write_markdown_queue


FIELD_NAMES = [
    "source_context", "difference_preservation", "evidence_quality",
    "translation_reliability", "protocol_compliance", "human_review",
    "universalism_claims", "template_capture", "context_loss",
    "archive_bias", "power_imbalance",
    "language_gap", "media_shift", "archive_gap", "performance_loss",
    "restricted_source_concern", "version_documentation",
    "local_interpretation", "community_review", "attribution_quality", "corpus_balance",
    "biased_corpus", "hallucinated_source_risk", "ai_translation_loss",
    "sacred_material_risk", "overgeneralized_claims", "expert_review",
    "public_consequence"
]


def load_records(path: Path, config: ComparativeStoryGovernanceConfig) -> list[ComparativeStoryGovernanceRecord]:
    records: list[ComparativeStoryGovernanceRecord] = []
    with path.open("r", encoding="utf-8", newline="") as handle:
        for row in csv.DictReader(handle):
            values = {name: float(row[name]) for name in FIELD_NAMES}
            record = ComparativeStoryGovernanceRecord(
                item=row["item"],
                comparison_context=row["comparison_context"],
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


def record_to_row(record: ComparativeStoryGovernanceRecord, config: ComparativeStoryGovernanceConfig) -> dict[str, object]:
    return {
        "item": record.item,
        "comparison_context": record.comparison_context,
        "comparative_integrity": round(comparative_integrity(record), 4),
        "flattening_risk": round(flattening_risk(record), 4),
        "transmission_uncertainty": round(transmission_uncertainty(record), 4),
        "contextual_grounding": round(contextual_grounding(record), 4),
        "ai_comparative_risk": round(ai_comparative_risk(record), 4),
        "governance_priority_score": round(governance_priority_score(record, config), 4),
        "review_priority": review_priority(record, config),
        "owner": record.owner,
        "status": record.status,
        "governance_note": governance_note(record, config),
    }


def run(article_root: Path, input_path: Path | None = None, output_dir: Path | None = None) -> None:
    article_root = article_root.resolve()
    config = ComparativeStoryGovernanceConfig()
    input_path = input_path or article_root / "data" / "comparative_story_governance_claims.csv"
    output_dir = output_dir or article_root / "outputs"

    records = load_records(input_path, config)
    rows = [record_to_row(record, config) for record in records]
    cards = [build_comparative_story_governance_card(record, config) for record in records]

    priority_order = {"high": 3, "medium": 2, "standard": 1}
    rows = sorted(rows, key=lambda row: (priority_order.get(str(row["review_priority"]), 0), float(row["governance_priority_score"])), reverse=True)

    queue = [row for row in rows if row["review_priority"] != "standard"]
    queue_cards = [card for card in cards if card["review"]["priority"] != "standard"]

    write_csv(output_dir / "tables" / "comparative_story_governance_audit.csv", rows)
    write_csv(output_dir / "tables" / "comparative_story_governance_queue.csv", queue)
    write_json(output_dir / "json" / "comparative_story_governance_canvas_cards.json", cards)
    write_json(output_dir / "json" / "comparative_story_governance_queue.json", queue_cards)
    write_markdown_queue(output_dir / "markdown" / "comparative_story_governance_queue.md", queue)

    print("Comparative story governance audit complete.")
    print(output_dir / "tables" / "comparative_story_governance_audit.csv")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Run comparative story governance Canvas audit.")
    parser.add_argument("--article-root", type=Path, default=Path(__file__).resolve().parents[2])
    parser.add_argument("--input", type=Path, default=None)
    parser.add_argument("--output-dir", type=Path, default=None)
    return parser


def main() -> None:
    args = build_parser().parse_args()
    run(args.article_root, args.input, args.output_dir)


if __name__ == "__main__":
    main()
