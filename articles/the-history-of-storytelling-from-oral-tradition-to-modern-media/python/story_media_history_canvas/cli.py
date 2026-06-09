from __future__ import annotations

from pathlib import Path
import argparse
import csv

from .models import StoryMedium
from .validation import validate_story_medium
from .scoring import (
    transmission_strength,
    participation_score,
    preservation_risk,
    review_priority,
    transition_score,
)
from .governance import governance_note
from .exporters import write_csv, write_json, write_markdown_queue


def load_media(path: Path) -> list[StoryMedium]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        rows = csv.DictReader(handle)
        media: list[StoryMedium] = []

        for row in rows:
            item = StoryMedium(
                medium=row["medium"],
                period_label=row["period_label"],
                preservation=float(row["preservation"]),
                participation=float(row["participation"]),
                circulation=float(row["circulation"]),
                repeatability=float(row["repeatability"]),
                governance_complexity=float(row["governance_complexity"]),
                archive_durability=float(row["archive_durability"]),
                context_retention=float(row["context_retention"]),
                access_openness=float(row["access_openness"]),
                platform_stability=float(row["platform_stability"]),
                owner=row["owner"],
                status=row["status"],
            )
            validate_story_medium(item)
            media.append(item)

    return media


def item_to_row(item: StoryMedium) -> dict[str, object]:
    row = {
        "medium": item.medium,
        "period_label": item.period_label,
        "preservation": item.preservation,
        "participation_score": round(participation_score(item), 3),
        "circulation": item.circulation,
        "repeatability": item.repeatability,
        "governance_complexity": item.governance_complexity,
        "archive_durability": item.archive_durability,
        "context_retention": item.context_retention,
        "access_openness": item.access_openness,
        "platform_stability": item.platform_stability,
        "transmission_strength": round(transmission_strength(item), 3),
        "preservation_risk": round(preservation_risk(item), 3),
        "review_priority": review_priority(item),
        "owner": item.owner,
        "status": item.status,
    }
    row["governance_note"] = governance_note(row)
    return row


def run(article_root: Path) -> None:
    data_path = article_root / "data" / "story_media_history.csv"
    outputs = article_root / "outputs"
    tables = outputs / "tables"
    json_dir = outputs / "json"
    markdown = outputs / "markdown"
    canvas = article_root / "canvas"

    media = load_media(data_path)
    rows = [item_to_row(item) for item in media]
    rows = sorted(rows, key=lambda row: float(row["preservation_risk"]), reverse=True)

    transition_rows = []
    for first, second in zip(media, media[1:]):
        transition_rows.append({
            "from_medium": first.medium,
            "to_medium": second.medium,
            "transition_score": round(transition_score(first, second), 3),
        })

    governance_queue = [
        row for row in rows
        if row["review_priority"] != "standard"
    ]

    write_csv(tables / "story_media_audit.csv", rows)
    write_csv(tables / "story_media_transition_scores.csv", transition_rows)
    write_csv(tables / "story_media_preservation_queue.csv", governance_queue)

    write_json(json_dir / "story_media_canvas_cards.json", rows)
    write_json(json_dir / "story_media_transition_scores.json", transition_rows)
    write_json(json_dir / "story_media_preservation_queue.json", governance_queue)

    write_json(canvas / "canvas_cards.json", rows)
    write_json(canvas / "governance_queue.json", governance_queue)
    write_markdown_queue(markdown / "story_media_preservation_queue.md", governance_queue)

    print("Story media history Canvas audit complete.")
    print(tables / "story_media_audit.csv")
    print(tables / "story_media_transition_scores.csv")
    print(markdown / "story_media_preservation_queue.md")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Run historical storytelling media Canvas audit.")
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
