from __future__ import annotations

from pathlib import Path
import argparse
import csv

from .models import TraditionalNarrativeItem
from .validation import validate_traditional_narrative_item
from .scoring import (
    form_classification,
    narrative_distinction,
    cultural_memory_function,
    adaptation_risk,
    governance_priority_score,
    review_priority,
)
from .governance import governance_note
from .exporters import write_csv, write_json, write_markdown_queue


def load_items(path: Path) -> list[TraditionalNarrativeItem]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        rows = csv.DictReader(handle)
        items: list[TraditionalNarrativeItem] = []
        for row in rows:
            item = TraditionalNarrativeItem(
                item=row["item"],
                proposed_form=row["proposed_form"],
                truth_claim_clarity=float(row["truth_claim_clarity"]),
                social_function=float(row["social_function"]),
                memory_orientation=float(row["memory_orientation"]),
                performance_trace=float(row["performance_trace"]),
                authority_context=float(row["authority_context"]),
                genre_notes=float(row["genre_notes"]),
                boundary_clarity=float(row["boundary_clarity"]),
                category_specificity=float(row["category_specificity"]),
                hybrid_tracking=float(row["hybrid_tracking"]),
                responsible_analogy=float(row["responsible_analogy"]),
                variation_management=float(row["variation_management"]),
                origin_memory=float(row["origin_memory"]),
                place_memory=float(row["place_memory"]),
                ritual_memory=float(row["ritual_memory"]),
                heroic_memory=float(row["heroic_memory"]),
                identity_memory=float(row["identity_memory"]),
                future_obligation=float(row["future_obligation"]),
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
            validate_traditional_narrative_item(item)
            items.append(item)
    return items


def item_to_row(item: TraditionalNarrativeItem) -> dict[str, object]:
    row = {
        "item": item.item,
        "proposed_form": item.proposed_form,
        "form_classification": round(form_classification(item), 3),
        "narrative_distinction": round(narrative_distinction(item), 3),
        "cultural_memory_function": round(cultural_memory_function(item), 3),
        "adaptation_risk": round(adaptation_risk(item), 3),
        "governance_priority_score": round(governance_priority_score(item), 3),
        "review_priority": review_priority(item),
        "owner": item.owner,
        "status": item.status,
    }
    row["governance_note"] = governance_note(row)
    return row


def run(article_root: Path) -> None:
    data_path = article_root / "data" / "traditional_narrative_forms_items.csv"
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
            float(row["adaptation_risk"])
        ),
        reverse=True,
    )

    governance_queue = [row for row in rows if row["review_priority"] != "standard"]

    write_csv(tables / "traditional_narrative_forms_audit.csv", rows)
    write_csv(tables / "traditional_narrative_forms_governance_queue.csv", governance_queue)

    write_json(json_dir / "traditional_narrative_forms_canvas_cards.json", rows)
    write_json(json_dir / "traditional_narrative_forms_governance_queue.json", governance_queue)

    write_json(canvas / "canvas_cards.json", rows)
    write_json(canvas / "governance_queue.json", governance_queue)

    write_markdown_queue(markdown / "traditional_narrative_forms_governance_queue.md", governance_queue)

    print("Traditional narrative forms Canvas audit complete.")
    print(tables / "traditional_narrative_forms_audit.csv")
    print(json_dir / "traditional_narrative_forms_canvas_cards.json")
    print(markdown / "traditional_narrative_forms_governance_queue.md")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Run traditional narrative forms Canvas audit.")
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
