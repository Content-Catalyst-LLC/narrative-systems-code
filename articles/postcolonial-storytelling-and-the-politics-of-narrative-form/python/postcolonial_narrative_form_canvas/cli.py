from __future__ import annotations

from pathlib import Path
import argparse
import csv

from .models import PostcolonialNarrativeFormConfig, PostcolonialNarrativeFormRecord
from .validation import validate_record
from .scoring import colonial_form_risk, digital_coloniality, governance_priority_score, postcolonial_form_strength, review_priority, translation_governance
from .governance import build_postcolonial_narrative_form_card, governance_note
from .exporters import write_csv, write_json, write_markdown_queue


def load_records(path: Path, config: PostcolonialNarrativeFormConfig) -> list[PostcolonialNarrativeFormRecord]:
    records: list[PostcolonialNarrativeFormRecord] = []
    with path.open("r", encoding="utf-8", newline="") as handle:
        for row in csv.DictReader(handle):
            record = PostcolonialNarrativeFormRecord(
                item=row["item"],
                claim_context=row["claim_context"],
                archive_dominance=float(row["archive_dominance"]),
                language_hierarchy=float(row["language_hierarchy"]),
                gaze_centrality=float(row["gaze_centrality"]),
                template_forcing=float(row["template_forcing"]),
                extraction_anxiety=float(row["extraction_anxiety"]),
                opacity_protection=float(row["opacity_protection"]),
                voice_complexity=float(row["voice_complexity"]),
                language_politics=float(row["language_politics"]),
                memory_fragmentation=float(row["memory_fragmentation"]),
                archive_critique=float(row["archive_critique"]),
                temporal_multiplicity=float(row["temporal_multiplicity"]),
                spatial_politics=float(row["spatial_politics"]),
                relational_land_context=float(row["relational_land_context"]),
                cultural_specificity=float(row["cultural_specificity"]),
                local_authority=float(row["local_authority"]),
                opacity_notes=float(row["opacity_notes"]),
                untranslated_terms=float(row["untranslated_terms"]),
                reviewer_visibility=float(row["reviewer_visibility"]),
                harm_review=float(row["harm_review"]),
                english_dominance=float(row["english_dominance"]),
                stereotype_bias=float(row["stereotype_bias"]),
                extraction_risk=float(row["extraction_risk"]),
                archive_flattening=float(row["archive_flattening"]),
                visual_orientalism=float(row["visual_orientalism"]),
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


def record_to_row(record: PostcolonialNarrativeFormRecord, config: PostcolonialNarrativeFormConfig) -> dict[str, object]:
    return {
        "item": record.item,
        "claim_context": record.claim_context,
        "colonial_form_risk": round(colonial_form_risk(record), 4),
        "postcolonial_form_strength": round(postcolonial_form_strength(record), 4),
        "translation_governance": round(translation_governance(record), 4),
        "digital_coloniality": round(digital_coloniality(record), 4),
        "governance_priority_score": round(governance_priority_score(record, config), 4),
        "review_priority": review_priority(record, config),
        "owner": record.owner,
        "status": record.status,
        "governance_note": governance_note(record, config),
    }


def run(article_root: Path, input_path: Path | None = None, output_dir: Path | None = None) -> None:
    article_root = article_root.resolve()
    config = PostcolonialNarrativeFormConfig()
    input_path = input_path or article_root / "data" / "postcolonial_narrative_form_claims.csv"
    output_dir = output_dir or article_root / "outputs"

    records = load_records(input_path, config)
    rows = [record_to_row(record, config) for record in records]
    cards = [build_postcolonial_narrative_form_card(record, config) for record in records]

    priority_order = {"high": 3, "medium": 2, "standard": 1}
    rows = sorted(rows, key=lambda row: (priority_order.get(str(row["review_priority"]), 0), float(row["governance_priority_score"])), reverse=True)

    queue = [row for row in rows if row["review_priority"] != "standard"]
    queue_cards = [card for card in cards if card["review"]["priority"] != "standard"]

    write_csv(output_dir / "tables" / "postcolonial_narrative_form_audit.csv", rows)
    write_csv(output_dir / "tables" / "postcolonial_narrative_form_governance_queue.csv", queue)
    write_json(output_dir / "json" / "postcolonial_narrative_form_canvas_cards.json", cards)
    write_json(output_dir / "json" / "postcolonial_narrative_form_governance_queue.json", queue_cards)
    write_markdown_queue(output_dir / "markdown" / "postcolonial_narrative_form_governance_queue.md", queue)

    print("Postcolonial narrative form audit complete.")
    print(output_dir / "tables" / "postcolonial_narrative_form_audit.csv")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Run postcolonial narrative form Canvas audit.")
    parser.add_argument("--article-root", type=Path, default=Path(__file__).resolve().parents[2])
    parser.add_argument("--input", type=Path, default=None)
    parser.add_argument("--output-dir", type=Path, default=None)
    return parser


def main() -> None:
    args = build_parser().parse_args()
    run(args.article_root, args.input, args.output_dir)


if __name__ == "__main__":
    main()
