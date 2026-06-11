from __future__ import annotations

from pathlib import Path
import argparse
import csv

from .models import NationalMemoryGovernanceConfig, NationalMemoryGovernanceRecord
from .validation import validate_record
from .scoring import ai_memory_risk, governance_priority_score, memory_accountability, memory_plurality, national_myth_risk, public_memory_infrastructure, review_priority
from .governance import build_national_memory_governance_card, governance_note
from .exporters import write_csv, write_json, write_markdown_queue


FIELD_NAMES = [
    "group_representation", "source_diversity", "testimony_visibility", "archive_coverage",
    "countermemory_inclusion", "dissent_space", "hero_compression", "innocence_story",
    "exclusion_omission", "victimhood_monopoly", "purity_symbolism", "revision_capacity",
    "evidence_visibility", "provenance_reliability", "record_access", "testimony_care",
    "contextual_explanation", "repair_linkage", "curriculum_balance", "monument_context",
    "platform_context", "summary_dependence", "context_loss", "dominant_archive_bias",
    "uncertainty_erasure", "omission_of_minority_memory", "human_review", "public_consequence"
]


def load_records(path: Path, config: NationalMemoryGovernanceConfig) -> list[NationalMemoryGovernanceRecord]:
    records: list[NationalMemoryGovernanceRecord] = []
    with path.open("r", encoding="utf-8", newline="") as handle:
        for row in csv.DictReader(handle):
            values = {name: float(row[name]) for name in FIELD_NAMES}
            record = NationalMemoryGovernanceRecord(
                item=row["item"],
                claim_context=row["claim_context"],
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


def record_to_row(record: NationalMemoryGovernanceRecord, config: NationalMemoryGovernanceConfig) -> dict[str, object]:
    return {
        "item": record.item,
        "claim_context": record.claim_context,
        "memory_plurality": round(memory_plurality(record), 4),
        "national_myth_risk": round(national_myth_risk(record), 4),
        "memory_accountability": round(memory_accountability(record), 4),
        "public_memory_infrastructure": round(public_memory_infrastructure(record), 4),
        "ai_memory_risk": round(ai_memory_risk(record), 4),
        "governance_priority_score": round(governance_priority_score(record, config), 4),
        "review_priority": review_priority(record, config),
        "owner": record.owner,
        "status": record.status,
        "governance_note": governance_note(record, config),
    }


def run(article_root: Path, input_path: Path | None = None, output_dir: Path | None = None) -> None:
    article_root = article_root.resolve()
    config = NationalMemoryGovernanceConfig()
    input_path = input_path or article_root / "data" / "national_memory_governance_claims.csv"
    output_dir = output_dir or article_root / "outputs"

    records = load_records(input_path, config)
    rows = [record_to_row(record, config) for record in records]
    cards = [build_national_memory_governance_card(record, config) for record in records]

    priority_order = {"high": 3, "medium": 2, "standard": 1}
    rows = sorted(rows, key=lambda row: (priority_order.get(str(row["review_priority"]), 0), float(row["governance_priority_score"])), reverse=True)

    queue = [row for row in rows if row["review_priority"] != "standard"]
    queue_cards = [card for card in cards if card["review"]["priority"] != "standard"]

    write_csv(output_dir / "tables" / "national_memory_governance_audit.csv", rows)
    write_csv(output_dir / "tables" / "national_memory_governance_queue.csv", queue)
    write_json(output_dir / "json" / "national_memory_governance_canvas_cards.json", cards)
    write_json(output_dir / "json" / "national_memory_governance_queue.json", queue_cards)
    write_markdown_queue(output_dir / "markdown" / "national_memory_governance_queue.md", queue)

    print("National memory governance audit complete.")
    print(output_dir / "tables" / "national_memory_governance_audit.csv")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Run national memory governance Canvas audit.")
    parser.add_argument("--article-root", type=Path, default=Path(__file__).resolve().parents[2])
    parser.add_argument("--input", type=Path, default=None)
    parser.add_argument("--output-dir", type=Path, default=None)
    return parser


def main() -> None:
    args = build_parser().parse_args()
    run(args.article_root, args.input, args.output_dir)


if __name__ == "__main__":
    main()
