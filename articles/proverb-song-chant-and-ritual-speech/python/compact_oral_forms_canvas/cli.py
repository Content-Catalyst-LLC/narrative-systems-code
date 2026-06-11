from __future__ import annotations

from pathlib import Path
import argparse
import csv

from .models import CompactOralFormItem
from .validation import validate_compact_oral_form_item
from .scoring import (
    oral_form_context,
    sound_and_repetition,
    ritual_authority,
    archive_risk,
    governance_priority_score,
    review_priority,
)
from .governance import governance_note
from .exporters import write_csv, write_json, write_markdown_queue


def load_items(path: Path) -> list[CompactOralFormItem]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        rows = csv.DictReader(handle)
        items: list[CompactOralFormItem] = []

        for row in rows:
            item = CompactOralFormItem(
                item=row["item"],
                oral_form=row["oral_form"],
                form_identification=float(row["form_identification"]),
                speaker_role=float(row["speaker_role"]),
                audience_documentation=float(row["audience_documentation"]),
                occasion_notes=float(row["occasion_notes"]),
                place_linkage=float(row["place_linkage"]),
                use_context=float(row["use_context"]),
                rhythm=float(row["rhythm"]),
                melody=float(row["melody"]),
                cadence=float(row["cadence"]),
                refrain_or_formula=float(row["refrain_or_formula"]),
                participation=float(row["participation"]),
                embodiment=float(row["embodiment"]),
                role_legitimacy=float(row["role_legitimacy"]),
                protocol_review=float(row["protocol_review"]),
                consent_status=float(row["consent_status"]),
                access_control=float(row["access_control"]),
                governance_oversight=float(row["governance_oversight"]),
                benefit_sharing=float(row["benefit_sharing"]),
                quote_extraction_risk=float(row["quote_extraction_risk"]),
                context_removal=float(row["context_removal"]),
                sound_loss=float(row["sound_loss"]),
                translation_loss=float(row["translation_loss"]),
                extraction_risk=float(row["extraction_risk"]),
                governance_control=float(row["governance_control"]),
                community_sensitivity=float(row["community_sensitivity"]),
                public_consequence=float(row["public_consequence"]),
                owner=row["owner"],
                status=row["status"],
            )
            validate_compact_oral_form_item(item)
            items.append(item)

    return items


def item_to_row(item: CompactOralFormItem) -> dict[str, object]:
    row = {
        "item": item.item,
        "oral_form": item.oral_form,
        "oral_form_context": round(oral_form_context(item), 3),
        "sound_and_repetition": round(sound_and_repetition(item), 3),
        "ritual_authority": round(ritual_authority(item), 3),
        "archive_risk": round(archive_risk(item), 3),
        "governance_priority_score": round(governance_priority_score(item), 3),
        "review_priority": review_priority(item),
        "owner": item.owner,
        "status": item.status,
    }
    row["governance_note"] = governance_note(row)
    return row


def run(article_root: Path) -> None:
    data_path = article_root / "data" / "compact_oral_forms_items.csv"
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

    governance_queue = [row for row in rows if row["review_priority"] != "standard"]

    write_csv(tables / "compact_oral_forms_audit.csv", rows)
    write_csv(tables / "compact_oral_forms_governance_queue.csv", governance_queue)
    write_json(json_dir / "compact_oral_forms_canvas_cards.json", rows)
    write_json(json_dir / "compact_oral_forms_governance_queue.json", governance_queue)
    write_json(canvas / "canvas_cards.json", rows)
    write_json(canvas / "governance_queue.json", governance_queue)
    write_markdown_queue(markdown / "compact_oral_forms_governance_queue.md", governance_queue)

    print("Compact oral forms Canvas audit complete.")
    print(tables / "compact_oral_forms_audit.csv")
    print(json_dir / "compact_oral_forms_canvas_cards.json")
    print(markdown / "compact_oral_forms_governance_queue.md")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Run compact oral forms Canvas audit.")
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
