from __future__ import annotations

from pathlib import Path
import argparse
import csv

from .models import MeaningArchitectureItem
from .validation import validate_meaning_architecture_item
from .scoring import (
    temporal_coherence,
    memory_durability,
    drift_risk,
    revision_priority_score,
    review_priority,
)
from .governance import governance_note
from .exporters import write_csv, write_json, write_markdown_queue


def load_items(path: Path) -> list[MeaningArchitectureItem]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        rows = csv.DictReader(handle)
        items: list[MeaningArchitectureItem] = []

        for row in rows:
            item = MeaningArchitectureItem(
                item=row["item"],
                story_type=row["story_type"],
                origin_clarity=float(row["origin_clarity"]),
                sequence_clarity=float(row["sequence_clarity"]),
                continuity_support=float(row["continuity_support"]),
                rupture_recognition=float(row["rupture_recognition"]),
                future_projection=float(row["future_projection"]),
                governance_visibility=float(row["governance_visibility"]),
                preservation=float(row["preservation"]),
                archive_support=float(row["archive_support"]),
                repetition_strength=float(row["repetition_strength"]),
                context_retention=float(row["context_retention"]),
                transmission_strength=float(row["transmission_strength"]),
                evidence_strength=float(row["evidence_strength"]),
                source_age=float(row["source_age"]),
                link_breakage=float(row["link_breakage"]),
                audience_consequence=float(row["audience_consequence"]),
                representation_risk=float(row["representation_risk"]),
                map_dependency=float(row["map_dependency"]),
                owner=row["owner"],
                status=row["status"],
            )
            validate_meaning_architecture_item(item)
            items.append(item)

    return items


def item_to_row(item: MeaningArchitectureItem) -> dict[str, object]:
    row = {
        "item": item.item,
        "story_type": item.story_type,
        "origin_clarity": item.origin_clarity,
        "sequence_clarity": item.sequence_clarity,
        "continuity_support": item.continuity_support,
        "rupture_recognition": item.rupture_recognition,
        "future_projection": item.future_projection,
        "governance_visibility": item.governance_visibility,
        "memory_durability": round(memory_durability(item), 3),
        "temporal_coherence": round(temporal_coherence(item), 3),
        "drift_risk": round(drift_risk(item), 3),
        "revision_priority_score": round(revision_priority_score(item), 3),
        "review_priority": review_priority(item),
        "owner": item.owner,
        "status": item.status,
    }
    row["governance_note"] = governance_note(row)
    return row


def run(article_root: Path) -> None:
    data_path = article_root / "data" / "meaning_architecture_items.csv"
    outputs = article_root / "outputs"
    tables = outputs / "tables"
    json_dir = outputs / "json"
    markdown = outputs / "markdown"
    canvas = article_root / "canvas"

    items = load_items(data_path)
    rows = [item_to_row(item) for item in items]
    rows = sorted(rows, key=lambda row: float(row["revision_priority_score"]), reverse=True)

    governance_queue = [
        row for row in rows
        if row["review_priority"] != "standard"
    ]

    write_csv(tables / "meaning_architecture_audit.csv", rows)
    write_csv(tables / "meaning_architecture_governance_queue.csv", governance_queue)

    write_json(json_dir / "meaning_architecture_canvas_cards.json", rows)
    write_json(json_dir / "meaning_architecture_governance_queue.json", governance_queue)

    write_json(canvas / "canvas_cards.json", rows)
    write_json(canvas / "governance_queue.json", governance_queue)

    write_markdown_queue(markdown / "meaning_architecture_governance_queue.md", governance_queue)

    print("Meaning architecture Canvas audit complete.")
    print(tables / "meaning_architecture_audit.csv")
    print(json_dir / "meaning_architecture_canvas_cards.json")
    print(markdown / "meaning_architecture_governance_queue.md")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Run meaning architecture Canvas audit.")
    parser.add_argument(
        "--article-root",
        type=Path,
        default=Path(__file__).resolve().parents[2],
        help="Path to article root directory.",
    )
    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    run(args.article_root.resolve())


if __name__ == "__main__":
    main()
