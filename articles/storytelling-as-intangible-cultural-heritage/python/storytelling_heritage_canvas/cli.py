from __future__ import annotations

from pathlib import Path
import argparse
import csv

from .models import StorytellingHeritageItem
from .validation import validate_storytelling_heritage_item
from .scoring import (
    living_continuity,
    safeguarding_readiness,
    heritage_context_preservation,
    archive_risk,
    governance_priority_score,
    review_priority,
)
from .governance import governance_note
from .exporters import write_csv, write_json, write_markdown_queue


def load_items(path: Path) -> list[StorytellingHeritageItem]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        rows = csv.DictReader(handle)
        items: list[StorytellingHeritageItem] = []

        for row in rows:
            item = StorytellingHeritageItem(
                item=row["item"],
                heritage_context=row["heritage_context"],
                transmission_support=float(row["transmission_support"]),
                performance_context=float(row["performance_context"]),
                language_vitality=float(row["language_vitality"]),
                apprenticeship_pathways=float(row["apprenticeship_pathways"]),
                community_recognition=float(row["community_recognition"]),
                variation_management=float(row["variation_management"]),
                consent_clarity=float(row["consent_clarity"]),
                governance_protocol=float(row["governance_protocol"]),
                metadata_quality=float(row["metadata_quality"]),
                access_control=float(row["access_control"]),
                benefit_sharing=float(row["benefit_sharing"]),
                review_process=float(row["review_process"]),
                occasion_context=float(row["occasion_context"]),
                place_linkage=float(row["place_linkage"]),
                ritual_frame=float(row["ritual_frame"]),
                embodiment=float(row["embodiment"]),
                social_transmission=float(row["social_transmission"]),
                knowledge_holder_context=float(row["knowledge_holder_context"]),
                context_removal=float(row["context_removal"]),
                sacred_or_restricted_material=float(row["sacred_or_restricted_material"]),
                performance_omission=float(row["performance_omission"]),
                translation_loss=float(row["translation_loss"]),
                extraction_risk=float(row["extraction_risk"]),
                governance_control=float(row["governance_control"]),
                community_sensitivity=float(row["community_sensitivity"]),
                public_consequence=float(row["public_consequence"]),
                owner=row["owner"],
                status=row["status"],
            )
            validate_storytelling_heritage_item(item)
            items.append(item)

    return items


def item_to_row(item: StorytellingHeritageItem) -> dict[str, object]:
    row = {
        "item": item.item,
        "heritage_context": item.heritage_context,
        "living_continuity": round(living_continuity(item), 3),
        "safeguarding_readiness": round(safeguarding_readiness(item), 3),
        "heritage_context_preservation": round(heritage_context_preservation(item), 3),
        "archive_risk": round(archive_risk(item), 3),
        "governance_priority_score": round(governance_priority_score(item), 3),
        "review_priority": review_priority(item),
        "owner": item.owner,
        "status": item.status,
    }
    row["governance_note"] = governance_note(row)
    return row


def run(article_root: Path) -> None:
    data_path = article_root / "data" / "storytelling_heritage_items.csv"
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

    write_csv(tables / "storytelling_heritage_audit.csv", rows)
    write_csv(tables / "storytelling_heritage_governance_queue.csv", governance_queue)

    write_json(json_dir / "storytelling_heritage_canvas_cards.json", rows)
    write_json(json_dir / "storytelling_heritage_governance_queue.json", governance_queue)

    write_json(canvas / "canvas_cards.json", rows)
    write_json(canvas / "governance_queue.json", governance_queue)

    write_markdown_queue(markdown / "storytelling_heritage_governance_queue.md", governance_queue)

    print("Storytelling heritage Canvas audit complete.")
    print(tables / "storytelling_heritage_audit.csv")
    print(json_dir / "storytelling_heritage_canvas_cards.json")
    print(markdown / "storytelling_heritage_governance_queue.md")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Run storytelling heritage Canvas audit.")
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
