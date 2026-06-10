from __future__ import annotations

from pathlib import Path
import argparse
import csv

from .models import BeginningClosureItem
from .validation import validate_beginning_closure_item
from .scoring import (
    opening_clarity,
    closure_integrity,
    beginning_ending_alignment,
    closure_risk,
    governance_priority_score,
    review_priority,
)
from .governance import governance_note
from .exporters import write_csv, write_json, write_markdown_queue


def load_items(path: Path) -> list[BeginningClosureItem]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        rows = csv.DictReader(handle)
        items: list[BeginningClosureItem] = []

        for row in rows:
            item = BeginningClosureItem(
                item=row["item"],
                story_type=row["story_type"],
                voice_signal=float(row["voice_signal"]),
                world_orientation=float(row["world_orientation"]),
                pressure_introduction=float(row["pressure_introduction"]),
                stakes_visibility=float(row["stakes_visibility"]),
                question_framing=float(row["question_framing"]),
                contract_transparency=float(row["contract_transparency"]),
                promise_fulfillment=float(row["promise_fulfillment"]),
                resolution_suitability=float(row["resolution_suitability"]),
                transformation_depth=float(row["transformation_depth"]),
                aftermath_clarity=float(row["aftermath_clarity"]),
                emotional_honesty=float(row["emotional_honesty"]),
                unresolved_harm_honesty=float(row["unresolved_harm_honesty"]),
                motif_return=float(row["motif_return"]),
                question_answer=float(row["question_answer"]),
                interpretive_echo=float(row["interpretive_echo"]),
                thematic_continuity=float(row["thematic_continuity"]),
                frame_revision=float(row["frame_revision"]),
                premature_repair=float(row["premature_repair"]),
                false_resolution=float(row["false_resolution"]),
                system_flattening=float(row["system_flattening"]),
                aftermath_omission=float(row["aftermath_omission"]),
                excessive_audience_comfort=float(row["excessive_audience_comfort"]),
                audience_sensitivity=float(row["audience_sensitivity"]),
                public_consequence=float(row["public_consequence"]),
                owner=row["owner"],
                status=row["status"],
            )
            validate_beginning_closure_item(item)
            items.append(item)

    return items


def item_to_row(item: BeginningClosureItem) -> dict[str, object]:
    row = {
        "item": item.item,
        "story_type": item.story_type,
        "opening_clarity": round(opening_clarity(item), 3),
        "closure_integrity": round(closure_integrity(item), 3),
        "beginning_ending_alignment": round(beginning_ending_alignment(item), 3),
        "closure_risk": round(closure_risk(item), 3),
        "governance_priority_score": round(governance_priority_score(item), 3),
        "review_priority": review_priority(item),
        "owner": item.owner,
        "status": item.status,
    }
    row["governance_note"] = governance_note(row)
    return row


def run(article_root: Path) -> None:
    data_path = article_root / "data" / "beginning_closure_items.csv"
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
            float(row["closure_risk"])
        ),
        reverse=True,
    )

    governance_queue = [
        row for row in rows
        if row["review_priority"] != "standard"
    ]

    write_csv(tables / "beginning_closure_audit.csv", rows)
    write_csv(tables / "beginning_closure_governance_queue.csv", governance_queue)

    write_json(json_dir / "beginning_closure_canvas_cards.json", rows)
    write_json(json_dir / "beginning_closure_governance_queue.json", governance_queue)

    write_json(canvas / "canvas_cards.json", rows)
    write_json(canvas / "governance_queue.json", governance_queue)

    write_markdown_queue(markdown / "beginning_closure_governance_queue.md", governance_queue)

    print("Beginning and closure Canvas audit complete.")
    print(tables / "beginning_closure_audit.csv")
    print(json_dir / "beginning_closure_canvas_cards.json")
    print(markdown / "beginning_closure_governance_queue.md")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Run beginning and closure Canvas audit.")
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
