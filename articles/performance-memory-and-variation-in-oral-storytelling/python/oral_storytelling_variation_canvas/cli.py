from __future__ import annotations

from pathlib import Path
import argparse
import csv

from .models import OralStorytellingVariationItem
from .validation import validate_oral_storytelling_variation_item
from .scoring import (
    performance_context,
    memory_support,
    variation_accountability,
    archive_risk,
    governance_priority_score,
    review_priority,
)
from .governance import governance_note
from .exporters import write_csv, write_json, write_markdown_queue


def load_items(path: Path) -> list[OralStorytellingVariationItem]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        rows = csv.DictReader(handle)
        items: list[OralStorytellingVariationItem] = []

        for row in rows:
            item = OralStorytellingVariationItem(
                item=row["item"],
                storytelling_context=row["storytelling_context"],
                teller_role=float(row["teller_role"]),
                audience_documentation=float(row["audience_documentation"]),
                occasion_context=float(row["occasion_context"]),
                place_linkage=float(row["place_linkage"]),
                embodiment=float(row["embodiment"]),
                interaction_notes=float(row["interaction_notes"]),
                repetition=float(row["repetition"]),
                formula_use=float(row["formula_use"]),
                sequence_clarity=float(row["sequence_clarity"]),
                audience_recognition=float(row["audience_recognition"]),
                community_correction=float(row["community_correction"]),
                transmission_pathway=float(row["transmission_pathway"]),
                variation_tracking=float(row["variation_tracking"]),
                context_explanation=float(row["context_explanation"]),
                language_notes=float(row["language_notes"]),
                source_review=float(row["source_review"]),
                access_protocol=float(row["access_protocol"]),
                governance_oversight=float(row["governance_oversight"]),
                fixation_risk=float(row["fixation_risk"]),
                context_removal=float(row["context_removal"]),
                performance_omission=float(row["performance_omission"]),
                translation_loss=float(row["translation_loss"]),
                extraction_risk=float(row["extraction_risk"]),
                governance_control=float(row["governance_control"]),
                community_sensitivity=float(row["community_sensitivity"]),
                public_consequence=float(row["public_consequence"]),
                owner=row["owner"],
                status=row["status"],
            )
            validate_oral_storytelling_variation_item(item)
            items.append(item)

    return items


def item_to_row(item: OralStorytellingVariationItem) -> dict[str, object]:
    row = {
        "item": item.item,
        "storytelling_context": item.storytelling_context,
        "performance_context": round(performance_context(item), 3),
        "memory_support": round(memory_support(item), 3),
        "variation_accountability": round(variation_accountability(item), 3),
        "archive_risk": round(archive_risk(item), 3),
        "governance_priority_score": round(governance_priority_score(item), 3),
        "review_priority": review_priority(item),
        "owner": item.owner,
        "status": item.status,
    }
    row["governance_note"] = governance_note(row)
    return row


def run(article_root: Path) -> None:
    data_path = article_root / "data" / "oral_storytelling_variation_items.csv"
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
            float(row["archive_risk"])
        ),
        reverse=True,
    )

    governance_queue = [
        row for row in rows
        if row["review_priority"] != "standard"
    ]

    write_csv(tables / "oral_storytelling_variation_audit.csv", rows)
    write_csv(tables / "oral_storytelling_variation_governance_queue.csv", governance_queue)

    write_json(json_dir / "oral_storytelling_variation_canvas_cards.json", rows)
    write_json(json_dir / "oral_storytelling_variation_governance_queue.json", governance_queue)

    write_json(canvas / "canvas_cards.json", rows)
    write_json(canvas / "governance_queue.json", governance_queue)

    write_markdown_queue(markdown / "oral_storytelling_variation_governance_queue.md", governance_queue)

    print("Oral storytelling variation Canvas audit complete.")
    print(tables / "oral_storytelling_variation_audit.csv")
    print(json_dir / "oral_storytelling_variation_canvas_cards.json")
    print(markdown / "oral_storytelling_variation_governance_queue.md")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Run oral storytelling variation Canvas audit.")
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
