from __future__ import annotations

from pathlib import Path
import argparse
import csv

from .models import LifeWritingConfig, LifeWritingRecord
from .validation import validate_record
from .scoring import ethical_risk, governance_priority_score, interpretation_readiness, life_writing_coherence, review_priority, truth_practice
from .governance import build_life_writing_card, governance_note
from .exporters import write_csv, write_json, write_markdown_queue


def load_records(path: Path, config: LifeWritingConfig) -> list[LifeWritingRecord]:
    records: list[LifeWritingRecord] = []
    with path.open("r", encoding="utf-8", newline="") as handle:
        for row in csv.DictReader(handle):
            record = LifeWritingRecord(
                item=row["item"],
                claim_context=row["claim_context"],
                memory_clarity=float(row["memory_clarity"]),
                temporal_structure=float(row["temporal_structure"]),
                voice_consistency=float(row["voice_consistency"]),
                agency=float(row["agency"]),
                relational_grounding=float(row["relational_grounding"]),
                contextual_depth=float(row["contextual_depth"]),
                fact_checking=float(row["fact_checking"]),
                memory_framing=float(row["memory_framing"]),
                evidence_visibility=float(row["evidence_visibility"]),
                interpretation_distinction=float(row["interpretation_distinction"]),
                uncertainty_notes=float(row["uncertainty_notes"]),
                archive_review=float(row["archive_review"]),
                privacy_risk=float(row["privacy_risk"]),
                consent_limits=float(row["consent_limits"]),
                other_person_exposure=float(row["other_person_exposure"]),
                trauma_extraction=float(row["trauma_extraction"]),
                self_mythology=float(row["self_mythology"]),
                method_limits=float(row["method_limits"]),
                source_context=float(row["source_context"]),
                cultural_context=float(row["cultural_context"]),
                review_owner_clarity=float(row["review_owner_clarity"]),
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


def record_to_row(record: LifeWritingRecord, config: LifeWritingConfig) -> dict[str, object]:
    return {
        "item": record.item,
        "claim_context": record.claim_context,
        "life_writing_coherence": round(life_writing_coherence(record), 4),
        "truth_practice": round(truth_practice(record), 4),
        "ethical_risk": round(ethical_risk(record), 4),
        "interpretation_readiness": round(interpretation_readiness(record), 4),
        "governance_priority_score": round(governance_priority_score(record, config), 4),
        "review_priority": review_priority(record, config),
        "owner": record.owner,
        "status": record.status,
        "governance_note": governance_note(record, config),
    }


def run(article_root: Path, input_path: Path | None = None, output_dir: Path | None = None) -> None:
    article_root = article_root.resolve()
    config = LifeWritingConfig()
    input_path = input_path or article_root / "data" / "life_writing_claims.csv"
    output_dir = output_dir or article_root / "outputs"

    records = load_records(input_path, config)
    rows = [record_to_row(record, config) for record in records]
    cards = [build_life_writing_card(record, config) for record in records]

    priority_order = {"high": 3, "medium": 2, "standard": 1}
    rows = sorted(rows, key=lambda row: (priority_order.get(str(row["review_priority"]), 0), float(row["governance_priority_score"])), reverse=True)

    queue = [row for row in rows if row["review_priority"] != "standard"]
    queue_cards = [card for card in cards if card["review"]["priority"] != "standard"]

    write_csv(output_dir / "tables" / "life_writing_audit.csv", rows)
    write_csv(output_dir / "tables" / "life_writing_governance_queue.csv", queue)
    write_json(output_dir / "json" / "life_writing_canvas_cards.json", cards)
    write_json(output_dir / "json" / "life_writing_governance_queue.json", queue_cards)
    write_markdown_queue(output_dir / "markdown" / "life_writing_governance_queue.md", queue)

    print("Life-writing Canvas audit complete.")
    print(output_dir / "tables" / "life_writing_audit.csv")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Run life-writing Canvas audit.")
    parser.add_argument("--article-root", type=Path, default=Path(__file__).resolve().parents[2])
    parser.add_argument("--input", type=Path, default=None)
    parser.add_argument("--output-dir", type=Path, default=None)
    return parser


def main() -> None:
    args = build_parser().parse_args()
    run(args.article_root, args.input, args.output_dir)


if __name__ == "__main__":
    main()
