from __future__ import annotations

from pathlib import Path
import argparse
import csv

from .models import FolktaleMorphologyItem
from .validation import validate_folktale_morphology_item
from .scoring import (
    function_coverage,
    sequence_integrity,
    morphology_context_balance,
    reduction_risk,
    governance_priority_score,
    review_priority,
)
from .governance import governance_note
from .exporters import write_csv, write_json, write_markdown_queue


def load_items(path: Path) -> list[FolktaleMorphologyItem]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        rows = csv.DictReader(handle)
        items: list[FolktaleMorphologyItem] = []

        for row in rows:
            item = FolktaleMorphologyItem(
                item=row["item"],
                tale_type=row["tale_type"],
                function_identification=float(row["function_identification"]),
                sequence_clarity=float(row["sequence_clarity"]),
                role_mapping=float(row["role_mapping"]),
                variation_tracking=float(row["variation_tracking"]),
                context_notes=float(row["context_notes"]),
                order_coherence=float(row["order_coherence"]),
                transition_logic=float(row["transition_logic"]),
                gap_management=float(row["gap_management"]),
                repetition_awareness=float(row["repetition_awareness"]),
                closure_handling=float(row["closure_handling"]),
                performance_context=float(row["performance_context"]),
                cultural_specificity=float(row["cultural_specificity"]),
                language_notes=float(row["language_notes"]),
                tradition_review=float(row["tradition_review"]),
                ethical_governance=float(row["ethical_governance"]),
                universalization_risk=float(row["universalization_risk"]),
                cultural_erasure_risk=float(row["cultural_erasure_risk"]),
                performance_omission=float(row["performance_omission"]),
                variation_omission=float(row["variation_omission"]),
                archive_bias=float(row["archive_bias"]),
                community_sensitivity=float(row["community_sensitivity"]),
                public_consequence=float(row["public_consequence"]),
                owner=row["owner"],
                status=row["status"],
            )
            validate_folktale_morphology_item(item)
            items.append(item)

    return items


def item_to_row(item: FolktaleMorphologyItem) -> dict[str, object]:
    row = {
        "item": item.item,
        "tale_type": item.tale_type,
        "function_coverage": round(function_coverage(item), 3),
        "sequence_integrity": round(sequence_integrity(item), 3),
        "morphology_context_balance": round(morphology_context_balance(item), 3),
        "reduction_risk": round(reduction_risk(item), 3),
        "governance_priority_score": round(governance_priority_score(item), 3),
        "review_priority": review_priority(item),
        "owner": item.owner,
        "status": item.status,
    }
    row["governance_note"] = governance_note(row)
    return row


def run(article_root: Path) -> None:
    data_path = article_root / "data" / "folktale_morphology_items.csv"
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
            float(row["reduction_risk"])
        ),
        reverse=True,
    )

    governance_queue = [
        row for row in rows
        if row["review_priority"] != "standard"
    ]

    write_csv(tables / "folktale_morphology_audit.csv", rows)
    write_csv(tables / "folktale_morphology_governance_queue.csv", governance_queue)

    write_json(json_dir / "folktale_morphology_canvas_cards.json", rows)
    write_json(json_dir / "folktale_morphology_governance_queue.json", governance_queue)

    write_json(canvas / "canvas_cards.json", rows)
    write_json(canvas / "governance_queue.json", governance_queue)

    write_markdown_queue(markdown / "folktale_morphology_governance_queue.md", governance_queue)

    print("Folktale morphology Canvas audit complete.")
    print(tables / "folktale_morphology_audit.csv")
    print(json_dir / "folktale_morphology_canvas_cards.json")
    print(markdown / "folktale_morphology_governance_queue.md")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Run folktale morphology Canvas audit.")
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
