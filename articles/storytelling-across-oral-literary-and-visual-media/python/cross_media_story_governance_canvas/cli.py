from __future__ import annotations

from pathlib import Path
import argparse
import csv

from .models import CrossMediaStoryGovernanceConfig, CrossMediaStoryGovernanceRecord
from .validation import validate_record
from .scoring import ai_cross_media_risk, consent_and_context_strength, governance_priority_score, media_transfer_risk, medium_affordance_fit, multimodal_coherence, review_priority
from .governance import build_cross_media_story_governance_card, governance_note
from .exporters import write_csv, write_json, write_markdown_queue


FIELD_NAMES = [
    "embodiment", "interior_depth", "spatial_quality", "temporal_control",
    "audience_relation", "contextual_fit", "voice_loss", "context_loss",
    "provenance_loss", "audience_shift", "representational_distortion",
    "governance_review", "text_image_integration", "image_sequence_logic",
    "sound_design_alignment", "rhythm_harmony", "provenance_visibility",
    "uncertainty_notation", "consent_clarity", "source_authority",
    "cultural_context", "reuse_boundaries", "synthetic_documentary_ambiguity",
    "provenance_opacity", "voice_likeness_imitation", "bias_reproduction",
    "human_review", "public_consequence"
]


def load_records(path: Path, config: CrossMediaStoryGovernanceConfig) -> list[CrossMediaStoryGovernanceRecord]:
    records: list[CrossMediaStoryGovernanceRecord] = []
    with path.open("r", encoding="utf-8", newline="") as handle:
        for row in csv.DictReader(handle):
            values = {name: float(row[name]) for name in FIELD_NAMES}
            record = CrossMediaStoryGovernanceRecord(
                item=row["item"],
                transfer_context=row["transfer_context"],
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


def record_to_row(record: CrossMediaStoryGovernanceRecord, config: CrossMediaStoryGovernanceConfig) -> dict[str, object]:
    return {
        "item": record.item,
        "transfer_context": record.transfer_context,
        "medium_affordance_fit": round(medium_affordance_fit(record), 4),
        "media_transfer_risk": round(media_transfer_risk(record), 4),
        "multimodal_coherence": round(multimodal_coherence(record), 4),
        "consent_and_context_strength": round(consent_and_context_strength(record), 4),
        "ai_cross_media_risk": round(ai_cross_media_risk(record), 4),
        "governance_priority_score": round(governance_priority_score(record, config), 4),
        "review_priority": review_priority(record, config),
        "owner": record.owner,
        "status": record.status,
        "governance_note": governance_note(record, config),
    }


def run(article_root: Path, input_path: Path | None = None, output_dir: Path | None = None) -> None:
    article_root = article_root.resolve()
    config = CrossMediaStoryGovernanceConfig()
    input_path = input_path or article_root / "data" / "cross_media_story_governance_claims.csv"
    output_dir = output_dir or article_root / "outputs"

    records = load_records(input_path, config)
    rows = [record_to_row(record, config) for record in records]
    cards = [build_cross_media_story_governance_card(record, config) for record in records]

    priority_order = {"high": 3, "medium": 2, "standard": 1}
    rows = sorted(rows, key=lambda row: (priority_order.get(str(row["review_priority"]), 0), float(row["governance_priority_score"])), reverse=True)

    queue = [row for row in rows if row["review_priority"] != "standard"]
    queue_cards = [card for card in cards if card["review"]["priority"] != "standard"]

    write_csv(output_dir / "tables" / "cross_media_story_governance_audit.csv", rows)
    write_csv(output_dir / "tables" / "cross_media_story_governance_queue.csv", queue)
    write_json(output_dir / "json" / "cross_media_story_governance_canvas_cards.json", cards)
    write_json(output_dir / "json" / "cross_media_story_governance_queue.json", queue_cards)
    write_markdown_queue(output_dir / "markdown" / "cross_media_story_governance_queue.md", queue)

    print("Cross-media story governance audit complete.")
    print(output_dir / "tables" / "cross_media_story_governance_audit.csv")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Run cross-media story governance Canvas audit.")
    parser.add_argument("--article-root", type=Path, default=Path(__file__).resolve().parents[2])
    parser.add_argument("--input", type=Path, default=None)
    parser.add_argument("--output-dir", type=Path, default=None)
    return parser


def main() -> None:
    args = build_parser().parse_args()
    run(args.article_root, args.input, args.output_dir)


if __name__ == "__main__":
    main()
