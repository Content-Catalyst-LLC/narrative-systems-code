from __future__ import annotations

from pathlib import Path
import argparse
import csv

from .models import StoryItem
from .validation import validate_story_item
from .scoring import coherence_score, craft_score, governance_risk, review_priority
from .governance import governance_note
from .exporters import write_csv, write_json, write_markdown_queue


def load_items(path: Path) -> list[StoryItem]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        rows = csv.DictReader(handle)
        items: list[StoryItem] = []
        for row in rows:
            item = StoryItem(
                item=row["item"],
                story_type=row["story_type"],
                description=row["description"],
                sequence_clarity=float(row["sequence_clarity"]),
                agency_clarity=float(row["agency_clarity"]),
                causal_connection=float(row["causal_connection"]),
                conflict_definition=float(row["conflict_definition"]),
                transformation_clarity=float(row["transformation_clarity"]),
                motif_use=float(row["motif_use"]),
                interpretive_relevance=float(row["interpretive_relevance"]),
                evidence_strength=float(row["evidence_strength"]),
                representation_care=float(row["representation_care"]),
                persuasive_intensity=float(row["persuasive_intensity"]),
                audience_consequence=float(row["audience_consequence"]),
                owner=row["owner"],
                status=row["status"],
            )
            validate_story_item(item)
            items.append(item)
    return items


def item_to_row(item: StoryItem) -> dict[str, object]:
    row = {
        "item": item.item,
        "story_type": item.story_type,
        "description": item.description,
        "sequence_clarity": item.sequence_clarity,
        "agency_clarity": item.agency_clarity,
        "causal_connection": item.causal_connection,
        "conflict_definition": item.conflict_definition,
        "transformation_clarity": item.transformation_clarity,
        "motif_use": item.motif_use,
        "interpretive_relevance": item.interpretive_relevance,
        "evidence_strength": item.evidence_strength,
        "representation_care": item.representation_care,
        "persuasive_intensity": item.persuasive_intensity,
        "audience_consequence": item.audience_consequence,
        "coherence_score": round(coherence_score(item), 3),
        "craft_score": round(craft_score(item), 3),
        "governance_risk": round(governance_risk(item), 3),
        "review_priority": review_priority(item),
        "owner": item.owner,
        "status": item.status,
    }
    row["governance_note"] = governance_note(row)
    return row


def run(article_root: Path) -> None:
    data_path = article_root / "data" / "storytelling_items.csv"
    outputs = article_root / "outputs"
    tables = outputs / "tables"
    json_dir = outputs / "json"
    markdown = outputs / "markdown"
    canvas = article_root / "canvas"

    items = load_items(data_path)
    rows = [item_to_row(item) for item in items]
    rows = sorted(rows, key=lambda row: float(row["governance_risk"]), reverse=True)

    governance_queue = [
        row for row in rows
        if row["review_priority"] != "standard"
    ]

    write_csv(tables / "storytelling_structure_audit.csv", rows)
    write_csv(tables / "storytelling_governance_queue.csv", governance_queue)
    write_json(json_dir / "storytelling_canvas_cards.json", rows)
    write_json(json_dir / "storytelling_governance_queue.json", governance_queue)
    write_json(canvas / "canvas_cards.json", rows)
    write_json(canvas / "governance_queue.json", governance_queue)
    write_markdown_queue(markdown / "storytelling_governance_queue.md", governance_queue)

    print("Storytelling Canvas audit complete.")
    print(tables / "storytelling_structure_audit.csv")
    print(json_dir / "storytelling_canvas_cards.json")
    print(markdown / "storytelling_governance_queue.md")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Run storytelling Canvas audit.")
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
