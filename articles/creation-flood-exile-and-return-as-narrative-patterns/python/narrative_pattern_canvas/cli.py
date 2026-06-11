from __future__ import annotations

from pathlib import Path
import argparse
import csv

from .models import NarrativePatternRecord, PatternConfig
from .validation import validate_record
from .scoring import (
    ethical_risk,
    governance_priority_score,
    interpretation_readiness,
    pattern_strength,
    review_priority,
    rupture_renewal_strength,
)
from .governance import build_pattern_card, governance_note
from .exporters import write_csv, write_json, write_markdown_queue


def load_records(path: Path, config: PatternConfig) -> list[NarrativePatternRecord]:
    records: list[NarrativePatternRecord] = []
    with path.open("r", encoding="utf-8", newline="") as handle:
        for row in csv.DictReader(handle):
            record = NarrativePatternRecord(
                item=row["item"],
                claim_context=row["claim_context"],
                creation_signal=float(row["creation_signal"]),
                flood_signal=float(row["flood_signal"]),
                exile_signal=float(row["exile_signal"]),
                return_signal=float(row["return_signal"]),
                memory_maintenance=float(row["memory_maintenance"]),
                repair_responsibility=float(row["repair_responsibility"]),
                source_context=float(row["source_context"]),
                historical_context=float(row["historical_context"]),
                counterexamples=float(row["counterexamples"]),
                method_limits=float(row["method_limits"]),
                ethics_governance=float(row["ethics_governance"]),
                uncertainty_notes=float(row["uncertainty_notes"]),
                origin_nostalgia=float(row["origin_nostalgia"]),
                cleansing_fantasy=float(row["cleansing_fantasy"]),
                exile_romanticization=float(row["exile_romanticization"]),
                false_return=float(row["false_return"]),
                power_blindness=float(row["power_blindness"]),
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


def record_to_row(record: NarrativePatternRecord, config: PatternConfig) -> dict[str, object]:
    return {
        "item": record.item,
        "claim_context": record.claim_context,
        "pattern_strength": round(pattern_strength(record), 4),
        "rupture_renewal_strength": round(rupture_renewal_strength(record), 4),
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
    config = PatternConfig()
    input_path = input_path or article_root / "data" / "narrative_pattern_claims.csv"
    output_dir = output_dir or article_root / "outputs"

    records = load_records(input_path, config)
    rows = [record_to_row(record, config) for record in records]
    cards = [build_pattern_card(record, config) for record in records]

    priority_order = {"high": 3, "medium": 2, "standard": 1}
    rows = sorted(
        rows,
        key=lambda row: (
            priority_order.get(str(row["review_priority"]), 0),
            float(row["governance_priority_score"]),
        ),
        reverse=True,
    )

    queue = [row for row in rows if row["review_priority"] != "standard"]
    queue_cards = [card for card in cards if card["review"]["priority"] != "standard"]

    write_csv(output_dir / "tables" / "creation_flood_exile_return_audit.csv", rows)
    write_csv(output_dir / "tables" / "creation_flood_exile_return_governance_queue.csv", queue)
    write_json(output_dir / "json" / "creation_flood_exile_return_canvas_cards.json", cards)
    write_json(output_dir / "json" / "creation_flood_exile_return_governance_queue.json", queue_cards)
    write_markdown_queue(output_dir / "markdown" / "creation_flood_exile_return_governance_queue.md", queue)

    print("Creation, flood, exile, and return Canvas audit complete.")
    print(output_dir / "tables" / "creation_flood_exile_return_audit.csv")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Run creation/flood/exile/return narrative pattern Canvas audit.")
    parser.add_argument("--article-root", type=Path, default=Path(__file__).resolve().parents[2])
    parser.add_argument("--input", type=Path, default=None)
    parser.add_argument("--output-dir", type=Path, default=None)
    return parser


def main() -> None:
    args = build_parser().parse_args()
    run(args.article_root, args.input, args.output_dir)


if __name__ == "__main__":
    main()
