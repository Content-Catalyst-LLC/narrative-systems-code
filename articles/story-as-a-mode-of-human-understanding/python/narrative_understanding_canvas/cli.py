from __future__ import annotations

from pathlib import Path
import argparse
import csv

from .models import NarrativeUnderstandingItem
from .validation import validate_narrative_understanding_item
from .scoring import (
    understanding_score,
    moral_understanding_score,
    possible_world_score,
    overreach_risk,
    review_priority,
)
from .governance import governance_note
from .exporters import write_csv, write_json, write_markdown_queue


def load_items(path: Path) -> list[NarrativeUnderstandingItem]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        rows = csv.DictReader(handle)
        items: list[NarrativeUnderstandingItem] = []

        for row in rows:
            item = NarrativeUnderstandingItem(
                item=row["item"],
                story_type=row["story_type"],
                sequence_clarity=float(row["sequence_clarity"]),
                causal_framing=float(row["causal_framing"]),
                agency_mapping=float(row["agency_mapping"]),
                memory_integration=float(row["memory_integration"]),
                evidence_support=float(row["evidence_support"]),
                openness_to_revision=float(row["openness_to_revision"]),
                consequence_visibility=float(row["consequence_visibility"]),
                harm_recognition=float(row["harm_recognition"]),
                responsibility_mapping=float(row["responsibility_mapping"]),
                repair_awareness=float(row["repair_awareness"]),
                alternative_logic=float(row["alternative_logic"]),
                uncertainty_signaling=float(row["uncertainty_signaling"]),
                interpretive_diversity=float(row["interpretive_diversity"]),
                hindsight_bias=float(row["hindsight_bias"]),
                false_coherence=float(row["false_coherence"]),
                selection_bias=float(row["selection_bias"]),
                closure_pressure=float(row["closure_pressure"]),
                owner=row["owner"],
                status=row["status"],
            )
            validate_narrative_understanding_item(item)
            items.append(item)

    return items


def item_to_row(item: NarrativeUnderstandingItem) -> dict[str, object]:
    row = {
        "item": item.item,
        "story_type": item.story_type,
        "sequence_clarity": item.sequence_clarity,
        "causal_framing": item.causal_framing,
        "agency_mapping": item.agency_mapping,
        "memory_integration": item.memory_integration,
        "evidence_support": item.evidence_support,
        "openness_to_revision": item.openness_to_revision,
        "moral_understanding_score": round(moral_understanding_score(item), 3),
        "possible_world_score": round(possible_world_score(item), 3),
        "understanding_score": round(understanding_score(item), 3),
        "overreach_risk": round(overreach_risk(item), 3),
        "review_priority": review_priority(item),
        "owner": item.owner,
        "status": item.status,
    }
    row["governance_note"] = governance_note(row)
    return row


def run(article_root: Path) -> None:
    data_path = article_root / "data" / "narrative_understanding_items.csv"
    outputs = article_root / "outputs"
    tables = outputs / "tables"
    json_dir = outputs / "json"
    markdown = outputs / "markdown"
    canvas = article_root / "canvas"

    items = load_items(data_path)
    rows = [item_to_row(item) for item in items]
    rows = sorted(rows, key=lambda row: float(row["overreach_risk"]), reverse=True)

    governance_queue = [
        row for row in rows
        if row["review_priority"] != "standard"
    ]

    write_csv(tables / "narrative_understanding_audit.csv", rows)
    write_csv(tables / "narrative_understanding_governance_queue.csv", governance_queue)

    write_json(json_dir / "narrative_understanding_canvas_cards.json", rows)
    write_json(json_dir / "narrative_understanding_governance_queue.json", governance_queue)

    write_json(canvas / "canvas_cards.json", rows)
    write_json(canvas / "governance_queue.json", governance_queue)

    write_markdown_queue(markdown / "narrative_understanding_governance_queue.md", governance_queue)

    print("Narrative understanding Canvas audit complete.")
    print(tables / "narrative_understanding_audit.csv")
    print(json_dir / "narrative_understanding_canvas_cards.json")
    print(markdown / "narrative_understanding_governance_queue.md")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Run narrative understanding Canvas audit.")
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
