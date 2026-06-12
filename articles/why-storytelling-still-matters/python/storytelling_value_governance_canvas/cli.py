from __future__ import annotations

from pathlib import Path
import argparse
import csv

from .models import StorytellingValueGovernanceConfig, StorytellingValueGovernanceRecord
from .validation import validate_record
from .scoring import ai_storytelling_governance, governance_priority_score, misuse_risk, narrative_responsibility, review_priority, storytelling_value
from .governance import build_storytelling_value_governance_card, governance_note
from .exporters import write_csv, write_json, write_markdown_queue


FIELD_NAMES = [
    "clarity", "evidence_grounding", "memory_continuity",
    "audience_reasoning", "dignity_protection", "public_usefulness",
    "truthfulness", "context_adequacy", "consent_discipline",
    "uncertainty_disclosure", "revision_openness", "accountability",
    "oversimplification", "emotional_exploitation", "scapegoating",
    "context_loss", "platform_frictionlessness", "human_review",
    "provenance_visibility", "source_traceability", "ai_human_review",
    "ai_consent_discipline", "use_limit_clarity", "correction_process",
    "cultural_context", "ethical_stakes"
]


def load_records(path: Path, config: StorytellingValueGovernanceConfig) -> list[StorytellingValueGovernanceRecord]:
    records: list[StorytellingValueGovernanceRecord] = []
    with path.open("r", encoding="utf-8", newline="") as handle:
        for row in csv.DictReader(handle):
            values = {name: float(row[name]) for name in FIELD_NAMES}
            record = StorytellingValueGovernanceRecord(
                item=row["item"],
                story_context=row["story_context"],
                owner=row.get("owner", "editorial"),
                status=row.get("status", "active"),
                notes=row.get("notes", ""),
                **values,
            )
            validate_record(record, config)
            records.append(record)
    if not records:
        raise ValueError(f"No records found in {path}")
    return records


def record_to_row(record: StorytellingValueGovernanceRecord, config: StorytellingValueGovernanceConfig) -> dict[str, object]:
    return {
        "item": record.item,
        "story_context": record.story_context,
        "storytelling_value": round(storytelling_value(record), 4),
        "narrative_responsibility": round(narrative_responsibility(record), 4),
        "misuse_risk": round(misuse_risk(record), 4),
        "ai_storytelling_governance": round(ai_storytelling_governance(record), 4),
        "governance_priority_score": round(governance_priority_score(record, config), 4),
        "review_priority": review_priority(record, config),
        "owner": record.owner,
        "status": record.status,
        "governance_note": governance_note(record, config),
    }


def run(article_root: Path, input_path: Path | None = None, output_dir: Path | None = None) -> None:
    article_root = article_root.resolve()
    config = StorytellingValueGovernanceConfig()
    input_path = input_path or article_root / "data" / "storytelling_value_governance_claims.csv"
    output_dir = output_dir or article_root / "outputs"

    records = load_records(input_path, config)
    rows = [record_to_row(record, config) for record in records]
    cards = [build_storytelling_value_governance_card(record, config) for record in records]

    priority_order = {"high": 3, "medium": 2, "standard": 1}
    rows = sorted(rows, key=lambda row: (priority_order.get(str(row["review_priority"]), 0), float(row["governance_priority_score"])), reverse=True)

    queue = [row for row in rows if row["review_priority"] != "standard"]
    queue_cards = [card for card in cards if card["review"]["priority"] != "standard"]

    write_csv(output_dir / "tables" / "storytelling_value_governance_audit.csv", rows)
    write_csv(output_dir / "tables" / "storytelling_value_governance_queue.csv", queue)
    write_json(output_dir / "json" / "storytelling_value_governance_canvas_cards.json", cards)
    write_json(output_dir / "json" / "storytelling_value_governance_queue.json", queue_cards)
    write_markdown_queue(output_dir / "markdown" / "storytelling_value_governance_queue.md", queue)

    print("Storytelling value governance audit complete.")
    print(output_dir / "tables" / "storytelling_value_governance_audit.csv")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Run storytelling value governance Canvas audit.")
    parser.add_argument("--article-root", type=Path, default=Path(__file__).resolve().parents[2])
    parser.add_argument("--input", type=Path, default=None)
    parser.add_argument("--output-dir", type=Path, default=None)
    return parser


def main() -> None:
    args = build_parser().parse_args()
    run(args.article_root, args.input, args.output_dir)


if __name__ == "__main__":
    main()
