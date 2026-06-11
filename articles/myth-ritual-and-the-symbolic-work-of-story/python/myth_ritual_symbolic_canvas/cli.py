from __future__ import annotations

from pathlib import Path
import argparse
import csv

from .models import MythRitualSymbolicItem
from .validation import validate_myth_ritual_symbolic_item
from .scoring import (
    symbolic_function,
    ritual_context,
    ethical_risk,
    interpretation_readiness,
    governance_priority_score,
    review_priority,
)
from .governance import governance_note
from .exporters import write_csv, write_json, write_markdown_queue


def load_items(path: Path) -> list[MythRitualSymbolicItem]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        rows = csv.DictReader(handle)
        items: list[MythRitualSymbolicItem] = []

        for row in rows:
            item = MythRitualSymbolicItem(
                item=row["item"],
                symbolic_context=row["symbolic_context"],
                origin_function=float(row["origin_function"]),
                cosmological_order=float(row["cosmological_order"]),
                memory_function=float(row["memory_function"]),
                identity_function=float(row["identity_function"]),
                transition_function=float(row["transition_function"]),
                authority_function=float(row["authority_function"]),
                sequence_clarity=float(row["sequence_clarity"]),
                place_linkage=float(row["place_linkage"]),
                gesture_documentation=float(row["gesture_documentation"]),
                object_symbolism=float(row["object_symbolism"]),
                participant_role=float(row["participant_role"]),
                protocol_transparency=float(row["protocol_transparency"]),
                totalizing_order=float(row["totalizing_order"]),
                scapegoating_risk=float(row["scapegoating_risk"]),
                exclusion_risk=float(row["exclusion_risk"]),
                appropriation_risk=float(row["appropriation_risk"]),
                harm_exposure=float(row["harm_exposure"]),
                governance_control=float(row["governance_control"]),
                context_explanation=float(row["context_explanation"]),
                ritual_verification=float(row["ritual_verification"]),
                language_notes=float(row["language_notes"]),
                access_control=float(row["access_control"]),
                governance_oversight=float(row["governance_oversight"]),
                uncertainty_marking=float(row["uncertainty_marking"]),
                community_sensitivity=float(row["community_sensitivity"]),
                public_consequence=float(row["public_consequence"]),
                owner=row["owner"],
                status=row["status"],
            )
            validate_myth_ritual_symbolic_item(item)
            items.append(item)

    return items


def item_to_row(item: MythRitualSymbolicItem) -> dict[str, object]:
    row = {
        "item": item.item,
        "symbolic_context": item.symbolic_context,
        "symbolic_function": round(symbolic_function(item), 3),
        "ritual_context": round(ritual_context(item), 3),
        "ethical_risk": round(ethical_risk(item), 3),
        "interpretation_readiness": round(interpretation_readiness(item), 3),
        "governance_priority_score": round(governance_priority_score(item), 3),
        "review_priority": review_priority(item),
        "owner": item.owner,
        "status": item.status,
    }
    row["governance_note"] = governance_note(row)
    return row


def run(article_root: Path) -> None:
    data_path = article_root / "data" / "myth_ritual_symbolic_items.csv"
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
            float(row["ethical_risk"])
        ),
        reverse=True,
    )

    governance_queue = [row for row in rows if row["review_priority"] != "standard"]

    write_csv(tables / "myth_ritual_symbolic_audit.csv", rows)
    write_csv(tables / "myth_ritual_symbolic_governance_queue.csv", governance_queue)

    write_json(json_dir / "myth_ritual_symbolic_canvas_cards.json", rows)
    write_json(json_dir / "myth_ritual_symbolic_governance_queue.json", governance_queue)

    write_json(canvas / "canvas_cards.json", rows)
    write_json(canvas / "governance_queue.json", governance_queue)

    write_markdown_queue(markdown / "myth_ritual_symbolic_governance_queue.md", governance_queue)

    print("Myth and ritual symbolic Canvas audit complete.")
    print(tables / "myth_ritual_symbolic_audit.csv")
    print(json_dir / "myth_ritual_symbolic_canvas_cards.json")
    print(markdown / "myth_ritual_symbolic_governance_queue.md")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Run myth and ritual symbolic Canvas audit.")
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
