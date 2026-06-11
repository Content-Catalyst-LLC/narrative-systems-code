from __future__ import annotations

from pathlib import Path
import argparse
import csv

from .models import NarratologyConfig, NarratologyRecord
from .validation import validate_record
from .scoring import focalization_complexity, governance_priority_score, governance_risk, interpretation_readiness, narrative_grammar_strength, review_priority, temporal_complexity
from .governance import build_narratology_card, governance_note
from .exporters import write_csv, write_json, write_markdown_queue


def load_records(path: Path, config: NarratologyConfig) -> list[NarratologyRecord]:
    records: list[NarratologyRecord] = []
    with path.open("r", encoding="utf-8", newline="") as handle:
        for row in csv.DictReader(handle):
            record = NarratologyRecord(
                item=row["item"],
                claim_context=row["claim_context"],
                story_discourse_clarity=float(row["story_discourse_clarity"]),
                voice_clarity=float(row["voice_clarity"]),
                focalization_clarity=float(row["focalization_clarity"]),
                temporal_mapping=float(row["temporal_mapping"]),
                character_agency_mapping=float(row["character_agency_mapping"]),
                information_control_analysis=float(row["information_control_analysis"]),
                perspective_shifts=float(row["perspective_shifts"]),
                knowledge_restriction=float(row["knowledge_restriction"]),
                interior_access=float(row["interior_access"]),
                source_hierarchy=float(row["source_hierarchy"]),
                multiple_focalizers=float(row["multiple_focalizers"]),
                analepsis=float(row["analepsis"]),
                prolepsis=float(row["prolepsis"]),
                ellipsis=float(row["ellipsis"]),
                duration_variation=float(row["duration_variation"]),
                repetition_frequency=float(row["repetition_frequency"]),
                omission_risk=float(row["omission_risk"]),
                power_blindness=float(row["power_blindness"]),
                voice_imbalance=float(row["voice_imbalance"]),
                closure_pressure=float(row["closure_pressure"]),
                unreliable_framing_risk=float(row["unreliable_framing_risk"]),
                method_limits=float(row["method_limits"]),
                source_context=float(row["source_context"]),
                counterexamples=float(row["counterexamples"]),
                uncertainty_notes=float(row["uncertainty_notes"]),
                owner=row.get("owner", "editorial"),
                status=row.get("status", "active"),
                notes=row.get("notes", ""),
            )
            validate_record(record, config)
            records.append(record)
    if not records:
        raise ValueError(f"No records found in {path}")
    return records


def record_to_row(record: NarratologyRecord, config: NarratologyConfig) -> dict[str, object]:
    return {
        "item": record.item,
        "claim_context": record.claim_context,
        "narrative_grammar_strength": round(narrative_grammar_strength(record), 4),
        "focalization_complexity": round(focalization_complexity(record), 4),
        "temporal_complexity": round(temporal_complexity(record), 4),
        "governance_risk": round(governance_risk(record), 4),
        "interpretation_readiness": round(interpretation_readiness(record), 4),
        "governance_priority_score": round(governance_priority_score(record, config), 4),
        "review_priority": review_priority(record, config),
        "owner": record.owner,
        "status": record.status,
        "governance_note": governance_note(record, config),
    }


def run(article_root: Path, input_path: Path | None = None, output_dir: Path | None = None) -> None:
    article_root = article_root.resolve()
    config = NarratologyConfig()
    input_path = input_path or article_root / "data" / "narratology_claims.csv"
    output_dir = output_dir or article_root / "outputs"
    records = load_records(input_path, config)
    rows = [record_to_row(record, config) for record in records]
    cards = [build_narratology_card(record, config) for record in records]
    priority_order = {"high": 3, "medium": 2, "standard": 1}
    rows = sorted(rows, key=lambda row: (priority_order.get(str(row["review_priority"]), 0), float(row["governance_priority_score"])), reverse=True)
    queue = [row for row in rows if row["review_priority"] != "standard"]
    queue_cards = [card for card in cards if card["review"]["priority"] != "standard"]
    write_csv(output_dir / "tables" / "narratology_audit.csv", rows)
    write_csv(output_dir / "tables" / "narratology_governance_queue.csv", queue)
    write_json(output_dir / "json" / "narratology_canvas_cards.json", cards)
    write_json(output_dir / "json" / "narratology_governance_queue.json", queue_cards)
    write_markdown_queue(output_dir / "markdown" / "narratology_governance_queue.md", queue)
    print("Narratology Canvas audit complete.")
    print(output_dir / "tables" / "narratology_audit.csv")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Run narratology Canvas audit.")
    parser.add_argument("--article-root", type=Path, default=Path(__file__).resolve().parents[2])
    parser.add_argument("--input", type=Path, default=None)
    parser.add_argument("--output-dir", type=Path, default=None)
    return parser


def main() -> None:
    args = build_parser().parse_args()
    run(args.article_root, args.input, args.output_dir)


if __name__ == "__main__":
    main()
