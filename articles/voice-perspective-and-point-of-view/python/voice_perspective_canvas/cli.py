from __future__ import annotations

from pathlib import Path
import argparse
import csv

from .models import VoicePerspectiveItem
from .validation import validate_voice_perspective_item
from .scoring import (
    voice_consistency,
    perspective_access,
    reliability_risk,
    governance_priority_score,
    review_priority,
)
from .governance import governance_note
from .exporters import write_csv, write_json, write_markdown_queue


def load_items(path: Path) -> list[VoicePerspectiveItem]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        rows = csv.DictReader(handle)
        items: list[VoicePerspectiveItem] = []

        for row in rows:
            item = VoicePerspectiveItem(
                item=row["item"],
                story_type=row["story_type"],
                tone_stability=float(row["tone_stability"]),
                diction_coherence=float(row["diction_coherence"]),
                rhetorical_habit=float(row["rhetorical_habit"]),
                address_stability=float(row["address_stability"]),
                judgment_coherence=float(row["judgment_coherence"]),
                knowledge_limits=float(row["knowledge_limits"]),
                interior_access=float(row["interior_access"]),
                focalization_clarity=float(row["focalization_clarity"]),
                level_stability=float(row["level_stability"]),
                source_boundaries=float(row["source_boundaries"]),
                factual_unreliability=float(row["factual_unreliability"]),
                interpretive_unreliability=float(row["interpretive_unreliability"]),
                ethical_unreliability=float(row["ethical_unreliability"]),
                memory_distortion=float(row["memory_distortion"]),
                agency_gap=float(row["agency_gap"]),
                exposure_sensitivity=float(row["exposure_sensitivity"]),
                public_consequence=float(row["public_consequence"]),
                representation_gap=float(row["representation_gap"]),
                institutional_evasion=float(row["institutional_evasion"]),
                owner=row["owner"],
                status=row["status"],
            )
            validate_voice_perspective_item(item)
            items.append(item)

    return items


def item_to_row(item: VoicePerspectiveItem) -> dict[str, object]:
    row = {
        "item": item.item,
        "story_type": item.story_type,
        "voice_consistency": round(voice_consistency(item), 3),
        "perspective_access": round(perspective_access(item), 3),
        "reliability_risk": round(reliability_risk(item), 3),
        "governance_priority_score": round(governance_priority_score(item), 3),
        "review_priority": review_priority(item),
        "owner": item.owner,
        "status": item.status,
    }
    row["governance_note"] = governance_note(row)
    return row


def run(article_root: Path) -> None:
    data_path = article_root / "data" / "voice_perspective_items.csv"
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
            float(row["governance_priority_score"])
        ),
        reverse=True,
    )

    governance_queue = [
        row for row in rows
        if row["review_priority"] != "standard"
    ]

    write_csv(tables / "voice_perspective_audit.csv", rows)
    write_csv(tables / "voice_perspective_governance_queue.csv", governance_queue)

    write_json(json_dir / "voice_perspective_canvas_cards.json", rows)
    write_json(json_dir / "voice_perspective_governance_queue.json", governance_queue)

    write_json(canvas / "canvas_cards.json", rows)
    write_json(canvas / "governance_queue.json", governance_queue)

    write_markdown_queue(markdown / "voice_perspective_governance_queue.md", governance_queue)

    print("Voice and perspective Canvas audit complete.")
    print(tables / "voice_perspective_audit.csv")
    print(json_dir / "voice_perspective_canvas_cards.json")
    print(markdown / "voice_perspective_governance_queue.md")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Run voice and perspective Canvas audit.")
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
