from __future__ import annotations

from pathlib import Path
import argparse
import csv

from .models import UniversalStoryModelConfig, UniversalStoryModelRecord
from .validation import validate_record
from .scoring import alternative_structure_signal, critique_readiness, governance_priority_score, review_priority, universal_model_fit, universalism_risk
from .governance import build_universal_story_model_card, governance_note
from .exporters import write_csv, write_json, write_markdown_queue


def load_records(path: Path, config: UniversalStoryModelConfig) -> list[UniversalStoryModelRecord]:
    records: list[UniversalStoryModelRecord] = []
    with path.open("r", encoding="utf-8", newline="") as handle:
        for row in csv.DictReader(handle):
            record = UniversalStoryModelRecord(
                item=row["item"],
                claim_context=row["claim_context"],
                stage_evidence=float(row["stage_evidence"]),
                agency_match=float(row["agency_match"]),
                transformation_correspondence=float(row["transformation_correspondence"]),
                contextual_harmony=float(row["contextual_harmony"]),
                resolution_similarity=float(row["resolution_similarity"]),
                evidence_visibility=float(row["evidence_visibility"]),
                archive_bias=float(row["archive_bias"]),
                gender_binary_pressure=float(row["gender_binary_pressure"]),
                cultural_flattening=float(row["cultural_flattening"]),
                intersectional_erasure=float(row["intersectional_erasure"]),
                queer_trans_pressure=float(row["queer_trans_pressure"]),
                local_context=float(row["local_context"]),
                source_context=float(row["source_context"]),
                alternative_lens=float(row["alternative_lens"]),
                gender_complexity=float(row["gender_complexity"]),
                intersectional_context=float(row["intersectional_context"]),
                uncertainty_notes=float(row["uncertainty_notes"]),
                review_owner_clarity=float(row["review_owner_clarity"]),
                relational_motion=float(row["relational_motion"]),
                cyclical_form=float(row["cyclical_form"]),
                witness_structure=float(row["witness_structure"]),
                care_labor=float(row["care_labor"]),
                fragmented_form=float(row["fragmented_form"]),
                open_process=float(row["open_process"]),
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


def record_to_row(record: UniversalStoryModelRecord, config: UniversalStoryModelConfig) -> dict[str, object]:
    return {
        "item": record.item,
        "claim_context": record.claim_context,
        "universal_model_fit": round(universal_model_fit(record), 4),
        "universalism_risk": round(universalism_risk(record), 4),
        "critique_readiness": round(critique_readiness(record), 4),
        "alternative_structure_signal": round(alternative_structure_signal(record), 4),
        "governance_priority_score": round(governance_priority_score(record, config), 4),
        "review_priority": review_priority(record, config),
        "owner": record.owner,
        "status": record.status,
        "governance_note": governance_note(record, config),
    }


def run(article_root: Path, input_path: Path | None = None, output_dir: Path | None = None) -> None:
    article_root = article_root.resolve()
    config = UniversalStoryModelConfig()
    input_path = input_path or article_root / "data" / "universal_story_model_claims.csv"
    output_dir = output_dir or article_root / "outputs"

    records = load_records(input_path, config)
    rows = [record_to_row(record, config) for record in records]
    cards = [build_universal_story_model_card(record, config) for record in records]

    priority_order = {"high": 3, "medium": 2, "standard": 1}
    rows = sorted(rows, key=lambda row: (priority_order.get(str(row["review_priority"]), 0), float(row["governance_priority_score"])), reverse=True)

    queue = [row for row in rows if row["review_priority"] != "standard"]
    queue_cards = [card for card in cards if card["review"]["priority"] != "standard"]

    write_csv(output_dir / "tables" / "universal_story_model_audit.csv", rows)
    write_csv(output_dir / "tables" / "universal_story_model_governance_queue.csv", queue)
    write_json(output_dir / "json" / "universal_story_model_canvas_cards.json", cards)
    write_json(output_dir / "json" / "universal_story_model_governance_queue.json", queue_cards)
    write_markdown_queue(output_dir / "markdown" / "universal_story_model_governance_queue.md", queue)

    print("Universal story model audit complete.")
    print(output_dir / "tables" / "universal_story_model_audit.csv")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Run universal story model Canvas audit.")
    parser.add_argument("--article-root", type=Path, default=Path(__file__).resolve().parents[2])
    parser.add_argument("--input", type=Path, default=None)
    parser.add_argument("--output-dir", type=Path, default=None)
    return parser


def main() -> None:
    args = build_parser().parse_args()
    run(args.article_root, args.input, args.output_dir)


if __name__ == "__main__":
    main()
