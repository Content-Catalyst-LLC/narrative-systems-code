from __future__ import annotations

from pathlib import Path
import argparse
import csv

from .models import ReversalRecognitionItem
from .validation import validate_reversal_recognition_item
from .scoring import (
    reversal_integrity,
    recognition_clarity,
    transformation_depth,
    recognition_risk,
    governance_priority_score,
    review_priority,
)
from .governance import governance_note
from .exporters import write_csv, write_json, write_markdown_queue


def load_items(path: Path) -> list[ReversalRecognitionItem]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        rows = csv.DictReader(handle)
        items: list[ReversalRecognitionItem] = []

        for row in rows:
            item = ReversalRecognitionItem(
                item=row["item"],
                story_type=row["story_type"],
                preparation_trace=float(row["preparation_trace"]),
                causal_linkage=float(row["causal_linkage"]),
                state_change=float(row["state_change"]),
                earned_surprise=float(row["earned_surprise"]),
                action_fit=float(row["action_fit"]),
                knowledge_reorientation=float(row["knowledge_reorientation"]),
                evidence_visibility=float(row["evidence_visibility"]),
                interpretive_support=float(row["interpretive_support"]),
                meaning_revision=float(row["meaning_revision"]),
                relation_linkage=float(row["relation_linkage"]),
                uncertainty_clarity=float(row["uncertainty_clarity"]),
                identity_change=float(row["identity_change"]),
                action_consequence=float(row["action_consequence"]),
                relationship_change=float(row["relationship_change"]),
                value_change=float(row["value_change"]),
                future_possibility=float(row["future_possibility"]),
                governance_accountability=float(row["governance_accountability"]),
                false_recognition=float(row["false_recognition"]),
                arbitrary_twist=float(row["arbitrary_twist"]),
                closure_pressure=float(row["closure_pressure"]),
                evidence_omission=float(row["evidence_omission"]),
                audience_sensitivity=float(row["audience_sensitivity"]),
                public_consequence=float(row["public_consequence"]),
                owner=row["owner"],
                status=row["status"],
            )
            validate_reversal_recognition_item(item)
            items.append(item)

    return items


def item_to_row(item: ReversalRecognitionItem) -> dict[str, object]:
    row = {
        "item": item.item,
        "story_type": item.story_type,
        "reversal_integrity": round(reversal_integrity(item), 3),
        "recognition_clarity": round(recognition_clarity(item), 3),
        "transformation_depth": round(transformation_depth(item), 3),
        "recognition_risk": round(recognition_risk(item), 3),
        "governance_priority_score": round(governance_priority_score(item), 3),
        "review_priority": review_priority(item),
        "owner": item.owner,
        "status": item.status,
    }
    row["governance_note"] = governance_note(row)
    return row


def run(article_root: Path) -> None:
    data_path = article_root / "data" / "reversal_recognition_items.csv"
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
            float(row["recognition_risk"])
        ),
        reverse=True,
    )

    governance_queue = [
        row for row in rows
        if row["review_priority"] != "standard"
    ]

    write_csv(tables / "reversal_recognition_audit.csv", rows)
    write_csv(tables / "reversal_recognition_governance_queue.csv", governance_queue)

    write_json(json_dir / "reversal_recognition_canvas_cards.json", rows)
    write_json(json_dir / "reversal_recognition_governance_queue.json", governance_queue)

    write_json(canvas / "canvas_cards.json", rows)
    write_json(canvas / "governance_queue.json", governance_queue)

    write_markdown_queue(markdown / "reversal_recognition_governance_queue.md", governance_queue)

    print("Reversal and recognition Canvas audit complete.")
    print(tables / "reversal_recognition_audit.csv")
    print(json_dir / "reversal_recognition_canvas_cards.json")
    print(markdown / "reversal_recognition_governance_queue.md")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Run reversal recognition Canvas audit.")
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
