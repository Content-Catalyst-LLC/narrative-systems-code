from __future__ import annotations

from pathlib import Path
import argparse
import csv

from .models import PublicStoryItem
from .validation import validate_public_story_item
from .scoring import (
    rhetorical_balance,
    persuasion_force,
    public_story_risk,
    governance_priority_score,
    review_priority,
)
from .governance import governance_note
from .exporters import write_csv, write_json, write_markdown_queue


def load_items(path: Path) -> list[PublicStoryItem]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        rows = csv.DictReader(handle)
        items: list[PublicStoryItem] = []

        for row in rows:
            item = PublicStoryItem(
                item=row["item"],
                story_type=row["story_type"],
                ethos_strength=float(row["ethos_strength"]),
                logos_support=float(row["logos_support"]),
                pathos_proportionality=float(row["pathos_proportionality"]),
                audience_fit=float(row["audience_fit"]),
                context_clarity=float(row["context_clarity"]),
                identification_strength=float(row["identification_strength"]),
                emotional_intensity=float(row["emotional_intensity"]),
                causal_clarity=float(row["causal_clarity"]),
                urgency=float(row["urgency"]),
                action_clarity=float(row["action_clarity"]),
                verification_strength=float(row["verification_strength"]),
                emotional_coercion=float(row["emotional_coercion"]),
                scapegoating_risk=float(row["scapegoating_risk"]),
                identity_manipulation=float(row["identity_manipulation"]),
                closure_pressure=float(row["closure_pressure"]),
                audience_consequence=float(row["audience_consequence"]),
                representation_sensitivity=float(row["representation_sensitivity"]),
                owner=row["owner"],
                status=row["status"],
            )
            validate_public_story_item(item)
            items.append(item)

    return items


def item_to_row(item: PublicStoryItem) -> dict[str, object]:
    row = {
        "item": item.item,
        "story_type": item.story_type,
        "ethos_strength": item.ethos_strength,
        "logos_support": item.logos_support,
        "pathos_proportionality": item.pathos_proportionality,
        "rhetorical_balance": round(rhetorical_balance(item), 3),
        "persuasion_force": round(persuasion_force(item), 3),
        "public_story_risk": round(public_story_risk(item), 3),
        "governance_priority_score": round(governance_priority_score(item), 3),
        "review_priority": review_priority(item),
        "owner": item.owner,
        "status": item.status,
    }
    row["governance_note"] = governance_note(row)
    return row


def run(article_root: Path) -> None:
    data_path = article_root / "data" / "public_story_rhetoric_items.csv"
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
            float(row["public_story_risk"])
        ),
        reverse=True,
    )

    governance_queue = [
        row for row in rows
        if row["review_priority"] != "standard"
    ]

    write_csv(tables / "public_story_rhetoric_audit.csv", rows)
    write_csv(tables / "public_story_rhetoric_governance_queue.csv", governance_queue)

    write_json(json_dir / "public_story_rhetoric_canvas_cards.json", rows)
    write_json(json_dir / "public_story_rhetoric_governance_queue.json", governance_queue)

    write_json(canvas / "canvas_cards.json", rows)
    write_json(canvas / "governance_queue.json", governance_queue)

    write_markdown_queue(markdown / "public_story_rhetoric_governance_queue.md", governance_queue)

    print("Public story rhetoric Canvas audit complete.")
    print(tables / "public_story_rhetoric_audit.csv")
    print(json_dir / "public_story_rhetoric_canvas_cards.json")
    print(markdown / "public_story_rhetoric_governance_queue.md")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Run public story rhetoric Canvas audit.")
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
