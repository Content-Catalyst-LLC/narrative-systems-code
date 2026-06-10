from __future__ import annotations

from pathlib import Path
import argparse
import csv

from .models import ConflictTensionItem
from .validation import validate_conflict_tension_item
from .scoring import (
    conflict_clarity,
    tension_durability,
    narrative_movement,
    conflict_risk,
    governance_priority_score,
    review_priority,
)
from .governance import governance_note
from .exporters import write_csv, write_json, write_markdown_queue


def load_items(path: Path) -> list[ConflictTensionItem]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        rows = csv.DictReader(handle)
        items: list[ConflictTensionItem] = []

        for row in rows:
            item = ConflictTensionItem(
                item=row["item"],
                story_type=row["story_type"],
                desire_clarity=float(row["desire_clarity"]),
                obstacle_clarity=float(row["obstacle_clarity"]),
                pressure_strength=float(row["pressure_strength"]),
                agency_visibility=float(row["agency_visibility"]),
                stakes_visibility=float(row["stakes_visibility"]),
                relation_legibility=float(row["relation_legibility"]),
                unresolved_pressure=float(row["unresolved_pressure"]),
                meaningful_delay=float(row["meaningful_delay"]),
                stakes_heightening=float(row["stakes_heightening"]),
                expectation_pressure=float(row["expectation_pressure"]),
                complication_movement=float(row["complication_movement"]),
                state_change=float(row["state_change"]),
                knowledge_change=float(row["knowledge_change"]),
                relationship_impact=float(row["relationship_impact"]),
                pressure_change=float(row["pressure_change"]),
                future_movement=float(row["future_movement"]),
                value_transformation=float(row["value_transformation"]),
                scapegoating=float(row["scapegoating"]),
                conflict_inflation=float(row["conflict_inflation"]),
                trauma_spectacle=float(row["trauma_spectacle"]),
                false_balance=float(row["false_balance"]),
                closure_pressure=float(row["closure_pressure"]),
                audience_sensitivity=float(row["audience_sensitivity"]),
                public_consequence=float(row["public_consequence"]),
                owner=row["owner"],
                status=row["status"],
            )
            validate_conflict_tension_item(item)
            items.append(item)

    return items


def item_to_row(item: ConflictTensionItem) -> dict[str, object]:
    row = {
        "item": item.item,
        "story_type": item.story_type,
        "conflict_clarity": round(conflict_clarity(item), 3),
        "tension_durability": round(tension_durability(item), 3),
        "narrative_movement": round(narrative_movement(item), 3),
        "conflict_risk": round(conflict_risk(item), 3),
        "governance_priority_score": round(governance_priority_score(item), 3),
        "review_priority": review_priority(item),
        "owner": item.owner,
        "status": item.status,
    }
    row["governance_note"] = governance_note(row)
    return row


def run(article_root: Path) -> None:
    data_path = article_root / "data" / "conflict_tension_items.csv"
    outputs = article_root / "outputs"
    tables = outputs / "tables"
    json_dir = outputs / "json"
    markdown = outputs / "markdown"
    canvas = article_root / "canvas"

    items = load_items(data_path)
    rows = [item_to_row(item) for item in items]
    priority_order = {"high": 3, "medium": 2, "standard": 1}
    rows = sorted(
        rows,
        key=lambda row: (
            priority_order.get(str(row["review_priority"]), 0),
            float(row["conflict_risk"])
        ),
        reverse=True,
    )

    governance_queue = [
        row for row in rows
        if row["review_priority"] != "standard"
    ]

    write_csv(tables / "conflict_tension_audit.csv", rows)
    write_csv(tables / "conflict_tension_governance_queue.csv", governance_queue)

    write_json(json_dir / "conflict_tension_canvas_cards.json", rows)
    write_json(json_dir / "conflict_tension_governance_queue.json", governance_queue)

    write_json(canvas / "canvas_cards.json", rows)
    write_json(canvas / "governance_queue.json", governance_queue)

    write_markdown_queue(markdown / "conflict_tension_governance_queue.md", governance_queue)

    print("Conflict and tension Canvas audit complete.")
    print(tables / "conflict_tension_audit.csv")
    print(json_dir / "conflict_tension_canvas_cards.json")
    print(markdown / "conflict_tension_governance_queue.md")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Run conflict and tension Canvas audit.")
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
