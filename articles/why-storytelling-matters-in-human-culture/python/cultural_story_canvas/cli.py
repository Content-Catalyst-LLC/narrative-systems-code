from __future__ import annotations

from pathlib import Path
import argparse
import csv

from .models import CulturalStoryItem
from .validation import validate_cultural_story_item
from .scoring import (
    cultural_context_score,
    cultural_value_score,
    transmission_score,
    narrative_risk,
    review_priority_score,
    review_priority,
)
from .governance import governance_note
from .exporters import write_csv, write_json, write_markdown_queue


def load_items(path: Path) -> list[CulturalStoryItem]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        rows = csv.DictReader(handle)
        items: list[CulturalStoryItem] = []

        for row in rows:
            item = CulturalStoryItem(
                item=row["item"],
                story_type=row["story_type"],
                cultural_context=row["cultural_context"],
                memory_function=float(row["memory_function"]),
                teaching_value=float(row["teaching_value"]),
                identity_function=float(row["identity_function"]),
                belonging_function=float(row["belonging_function"]),
                moral_imagination=float(row["moral_imagination"]),
                social_coordination=float(row["social_coordination"]),
                transmission_strength=float(row["transmission_strength"]),
                source_transparency=float(row["source_transparency"]),
                representation_care=float(row["representation_care"]),
                persuasive_intensity=float(row["persuasive_intensity"]),
                audience_consequence=float(row["audience_consequence"]),
                public_impact=float(row["public_impact"]),
                owner=row["owner"],
                status=row["status"],
            )
            validate_cultural_story_item(item)
            items.append(item)

    return items


def item_to_row(item: CulturalStoryItem) -> dict[str, object]:
    row = {
        "item": item.item,
        "story_type": item.story_type,
        "cultural_context": item.cultural_context,
        "memory_function": item.memory_function,
        "teaching_value": item.teaching_value,
        "identity_function": item.identity_function,
        "belonging_function": item.belonging_function,
        "moral_imagination": item.moral_imagination,
        "social_coordination": item.social_coordination,
        "transmission_strength": item.transmission_strength,
        "source_transparency": item.source_transparency,
        "representation_care": item.representation_care,
        "persuasive_intensity": item.persuasive_intensity,
        "audience_consequence": item.audience_consequence,
        "public_impact": item.public_impact,
        "cultural_context_score": round(cultural_context_score(item), 3),
        "cultural_value_score": round(cultural_value_score(item), 3),
        "transmission_score": round(transmission_score(item), 3),
        "narrative_risk": round(narrative_risk(item), 3),
        "review_priority_score": round(review_priority_score(item), 3),
        "review_priority": review_priority(item),
        "owner": item.owner,
        "status": item.status,
    }
    row["governance_note"] = governance_note(row)
    return row


def run(article_root: Path) -> None:
    data_path = article_root / "data" / "cultural_story_items.csv"
    outputs = article_root / "outputs"
    tables = outputs / "tables"
    json_dir = outputs / "json"
    markdown = outputs / "markdown"
    canvas = article_root / "canvas"

    items = load_items(data_path)
    rows = [item_to_row(item) for item in items]
    rows = sorted(rows, key=lambda row: float(row["review_priority_score"]), reverse=True)

    governance_queue = [
        row for row in rows
        if row["review_priority"] != "standard"
    ]

    write_csv(tables / "cultural_story_function_audit.csv", rows)
    write_csv(tables / "cultural_story_governance_queue.csv", governance_queue)
    write_json(json_dir / "cultural_story_canvas_cards.json", rows)
    write_json(json_dir / "cultural_story_governance_queue.json", governance_queue)
    write_json(canvas / "canvas_cards.json", rows)
    write_json(canvas / "governance_queue.json", governance_queue)
    write_markdown_queue(markdown / "cultural_story_governance_queue.md", governance_queue)

    print("Cultural Story Canvas audit complete.")
    print(tables / "cultural_story_function_audit.csv")
    print(json_dir / "cultural_story_canvas_cards.json")
    print(markdown / "cultural_story_governance_queue.md")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Run cultural storytelling Canvas audit.")
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
