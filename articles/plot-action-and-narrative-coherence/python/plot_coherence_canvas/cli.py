from __future__ import annotations

from pathlib import Path
import argparse
import csv

from .models import PlotCoherenceItem
from .validation import validate_plot_coherence_item
from .scoring import (
    plot_coherence,
    action_dependency,
    coherence_risk,
    governance_priority_score,
    review_priority,
)
from .governance import governance_note
from .exporters import write_csv, write_json, write_markdown_queue


def load_items(path: Path) -> list[PlotCoherenceItem]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        rows = csv.DictReader(handle)
        items: list[PlotCoherenceItem] = []

        for row in rows:
            item = PlotCoherenceItem(
                item=row["item"],
                story_type=row["story_type"],
                action_clarity=float(row["action_clarity"]),
                causal_linkage=float(row["causal_linkage"]),
                motivation_visibility=float(row["motivation_visibility"]),
                episode_dependency=float(row["episode_dependency"]),
                turning_point_strength=float(row["turning_point_strength"]),
                resolution_consequence=float(row["resolution_consequence"]),
                state_change=float(row["state_change"]),
                knowledge_change=float(row["knowledge_change"]),
                pressure_change=float(row["pressure_change"]),
                relationship_impact=float(row["relationship_impact"]),
                future_movement=float(row["future_movement"]),
                false_causality=float(row["false_causality"]),
                simplification_bias=float(row["simplification_bias"]),
                closure_pressure=float(row["closure_pressure"]),
                evidence_omission=float(row["evidence_omission"]),
                uncertainty_clarity=float(row["uncertainty_clarity"]),
                audience_sensitivity=float(row["audience_sensitivity"]),
                public_consequence=float(row["public_consequence"]),
                owner=row["owner"],
                status=row["status"],
            )
            validate_plot_coherence_item(item)
            items.append(item)

    return items


def item_to_row(item: PlotCoherenceItem) -> dict[str, object]:
    row = {
        "item": item.item,
        "story_type": item.story_type,
        "action_clarity": item.action_clarity,
        "causal_linkage": item.causal_linkage,
        "motivation_visibility": item.motivation_visibility,
        "episode_dependency": item.episode_dependency,
        "plot_coherence": round(plot_coherence(item), 3),
        "action_dependency": round(action_dependency(item), 3),
        "coherence_risk": round(coherence_risk(item), 3),
        "governance_priority_score": round(governance_priority_score(item), 3),
        "review_priority": review_priority(item),
        "owner": item.owner,
        "status": item.status,
    }
    row["governance_note"] = governance_note(row)
    return row


def run(article_root: Path) -> None:
    data_path = article_root / "data" / "plot_coherence_items.csv"
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
            float(row["coherence_risk"])
        ),
        reverse=True,
    )

    governance_queue = [
        row for row in rows
        if row["review_priority"] != "standard"
    ]

    write_csv(tables / "plot_coherence_audit.csv", rows)
    write_csv(tables / "plot_coherence_governance_queue.csv", governance_queue)

    write_json(json_dir / "plot_coherence_canvas_cards.json", rows)
    write_json(json_dir / "plot_coherence_governance_queue.json", governance_queue)

    write_json(canvas / "canvas_cards.json", rows)
    write_json(canvas / "governance_queue.json", governance_queue)

    write_markdown_queue(markdown / "plot_coherence_governance_queue.md", governance_queue)

    print("Plot coherence Canvas audit complete.")
    print(tables / "plot_coherence_audit.csv")
    print(json_dir / "plot_coherence_canvas_cards.json")
    print(markdown / "plot_coherence_governance_queue.md")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Run plot coherence Canvas audit.")
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
