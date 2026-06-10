from __future__ import annotations

from pathlib import Path
import argparse
import csv

from .models import PlotItem
from .validation import validate_plot_item
from .scoring import (
    plot_unity,
    reversal_recognition_strength,
    formula_risk,
    governance_score,
    review_priority,
)
from .governance import governance_note
from .exporters import write_csv, write_json, write_markdown_queue


def load_items(path: Path) -> list[PlotItem]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        rows = csv.DictReader(handle)
        items: list[PlotItem] = []

        for row in rows:
            item = PlotItem(
                item=row["item"],
                story_type=row["story_type"],
                action_clarity=float(row["action_clarity"]),
                causal_linkage=float(row["causal_linkage"]),
                episode_dependency=float(row["episode_dependency"]),
                turning_point_relevance=float(row["turning_point_relevance"]),
                resolution_support=float(row["resolution_support"]),
                goal_coherence=float(row["goal_coherence"]),
                direction_change=float(row["direction_change"]),
                knowledge_change=float(row["knowledge_change"]),
                preparation_strength=float(row["preparation_strength"]),
                consequence_pressure=float(row["consequence_pressure"]),
                emotional_intellectual_impact=float(row["emotional_intellectual_impact"]),
                character_action_integration=float(row["character_action_integration"]),
                genre_fit=float(row["genre_fit"]),
                medium_fit=float(row["medium_fit"]),
                cultural_awareness=float(row["cultural_awareness"]),
                hero_template_saturation=float(row["hero_template_saturation"]),
                closure_pressure=float(row["closure_pressure"]),
                unity_bias=float(row["unity_bias"]),
                genre_bias=float(row["genre_bias"]),
                owner=row["owner"],
                status=row["status"],
            )
            validate_plot_item(item)
            items.append(item)

    return items


def item_to_row(item: PlotItem) -> dict[str, object]:
    row = {
        "item": item.item,
        "story_type": item.story_type,
        "action_clarity": item.action_clarity,
        "causal_linkage": item.causal_linkage,
        "episode_dependency": item.episode_dependency,
        "turning_point_relevance": item.turning_point_relevance,
        "plot_unity": round(plot_unity(item), 3),
        "reversal_recognition_strength": round(reversal_recognition_strength(item), 3),
        "character_action_integration": item.character_action_integration,
        "formula_risk": round(formula_risk(item), 3),
        "governance_score": round(governance_score(item), 3),
        "review_priority": review_priority(item),
        "owner": item.owner,
        "status": item.status,
    }
    row["governance_note"] = governance_note(row)
    return row


def run(article_root: Path) -> None:
    data_path = article_root / "data" / "aristotelian_plot_items.csv"
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
        key=lambda row: (priority_order.get(str(row["review_priority"]), 0), float(row["formula_risk"])),
        reverse=True,
    )

    governance_queue = [
        row for row in rows
        if row["review_priority"] != "standard"
    ]

    write_csv(tables / "aristotelian_plot_audit.csv", rows)
    write_csv(tables / "aristotelian_plot_governance_queue.csv", governance_queue)

    write_json(json_dir / "aristotelian_plot_canvas_cards.json", rows)
    write_json(json_dir / "aristotelian_plot_governance_queue.json", governance_queue)

    write_json(canvas / "canvas_cards.json", rows)
    write_json(canvas / "governance_queue.json", governance_queue)

    write_markdown_queue(markdown / "aristotelian_plot_governance_queue.md", governance_queue)

    print("Aristotelian plot Canvas audit complete.")
    print(tables / "aristotelian_plot_audit.csv")
    print(json_dir / "aristotelian_plot_canvas_cards.json")
    print(markdown / "aristotelian_plot_governance_queue.md")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Run Aristotelian plot Canvas audit.")
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
