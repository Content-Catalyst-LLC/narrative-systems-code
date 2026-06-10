from __future__ import annotations

from pathlib import Path
import argparse
import csv

from .models import OralTraditionItem
from .validation import validate_oral_tradition_item
from .scoring import (
    performance_context,
    transmission_integrity,
    memory_function,
    archive_risk,
    governance_priority_score,
    review_priority,
)
from .governance import governance_note
from .exporters import write_csv, write_json, write_markdown_queue


def load_items(path: Path) -> list[OralTraditionItem]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        rows = csv.DictReader(handle)
        items: list[OralTraditionItem] = []

        for row in rows:
            item = OralTraditionItem(
                item=row["item"],
                tradition_type=row["tradition_type"],
                teller_role=float(row["teller_role"]),
                audience_response=float(row["audience_response"]),
                occasion_clarity=float(row["occasion_clarity"]),
                embodiment=float(row["embodiment"]),
                setting_place=float(row["setting_place"]),
                cultural_frame=float(row["cultural_frame"]),
                lineage_clarity=float(row["lineage_clarity"]),
                variation_tracking=float(row["variation_tracking"]),
                memory_supports=float(row["memory_supports"]),
                governance_protocol=float(row["governance_protocol"]),
                authority_permission=float(row["authority_permission"]),
                record_context=float(row["record_context"]),
                origin_memory=float(row["origin_memory"]),
                place_memory=float(row["place_memory"]),
                identity_memory=float(row["identity_memory"]),
                historical_memory=float(row["historical_memory"]),
                ritual_memory=float(row["ritual_memory"]),
                future_obligation=float(row["future_obligation"]),
                consent_limits=float(row["consent_limits"]),
                restricted_knowledge=float(row["restricted_knowledge"]),
                exposure_risk=float(row["exposure_risk"]),
                ownership_risk=float(row["ownership_risk"]),
                extraction_risk=float(row["extraction_risk"]),
                governance_control=float(row["governance_control"]),
                community_sensitivity=float(row["community_sensitivity"]),
                public_consequence=float(row["public_consequence"]),
                owner=row["owner"],
                status=row["status"],
            )
            validate_oral_tradition_item(item)
            items.append(item)

    return items


def item_to_row(item: OralTraditionItem) -> dict[str, object]:
    row = {
        "item": item.item,
        "tradition_type": item.tradition_type,
        "performance_context": round(performance_context(item), 3),
        "transmission_integrity": round(transmission_integrity(item), 3),
        "memory_function": round(memory_function(item), 3),
        "archive_risk": round(archive_risk(item), 3),
        "governance_priority_score": round(governance_priority_score(item), 3),
        "review_priority": review_priority(item),
        "owner": item.owner,
        "status": item.status,
    }
    row["governance_note"] = governance_note(row)
    return row


def run(article_root: Path) -> None:
    data_path = article_root / "data" / "oral_tradition_items.csv"
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

    write_csv(tables / "oral_tradition_audit.csv", rows)
    write_csv(tables / "oral_tradition_governance_queue.csv", governance_queue)

    write_json(json_dir / "oral_tradition_canvas_cards.json", rows)
    write_json(json_dir / "oral_tradition_governance_queue.json", governance_queue)

    write_json(canvas / "canvas_cards.json", rows)
    write_json(canvas / "governance_queue.json", governance_queue)

    write_markdown_queue(markdown / "oral_tradition_governance_queue.md", governance_queue)

    print("Oral tradition Canvas audit complete.")
    print(tables / "oral_tradition_audit.csv")
    print(json_dir / "oral_tradition_canvas_cards.json")
    print(markdown / "oral_tradition_governance_queue.md")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Run oral tradition Canvas audit.")
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
