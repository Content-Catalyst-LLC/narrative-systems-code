from __future__ import annotations

from pathlib import Path
import argparse
import csv

from .models import SerialNarrativeGovernanceConfig, SerialNarrativeGovernanceRecord
from .validation import validate_record
from .scoring import ai_serial_risk, continuity_burden, ensemble_and_ethics_strength, governance_priority_score, payoff_integrity, review_priority, season_coherence
from .governance import build_serial_narrative_governance_card, governance_note
from .exporters import write_csv, write_json, write_markdown_queue


FIELD_NAMES = [
    "episode_function", "arc_progression", "thematic_development",
    "character_memory", "payoff_integrity_signal", "finale_consequence",
    "unresolved_arcs", "lore_density", "memory_expectation",
    "recap_uncertainty", "continuity_saturation", "audience_accessibility",
    "foreshadowing_support", "character_relevance", "emotional_payoff",
    "mystery_logic", "retrospective_coherence", "thematic_alignment",
    "ensemble_balance", "representation_depth", "trauma_care",
    "audience_trust", "generic_plotting", "continuity_fabrication",
    "memory_erasure", "payoff_simplification", "franchise_overextension",
    "human_review", "public_consequence"
]


def load_records(path: Path, config: SerialNarrativeGovernanceConfig) -> list[SerialNarrativeGovernanceRecord]:
    records: list[SerialNarrativeGovernanceRecord] = []
    with path.open("r", encoding="utf-8", newline="") as handle:
        for row in csv.DictReader(handle):
            values = {name: float(row[name]) for name in FIELD_NAMES}
            record = SerialNarrativeGovernanceRecord(
                item=row["item"],
                serial_context=row["serial_context"],
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


def record_to_row(record: SerialNarrativeGovernanceRecord, config: SerialNarrativeGovernanceConfig) -> dict[str, object]:
    return {
        "item": record.item,
        "serial_context": record.serial_context,
        "season_coherence": round(season_coherence(record), 4),
        "continuity_burden": round(continuity_burden(record), 4),
        "payoff_integrity": round(payoff_integrity(record), 4),
        "ensemble_and_ethics_strength": round(ensemble_and_ethics_strength(record), 4),
        "ai_serial_risk": round(ai_serial_risk(record), 4),
        "governance_priority_score": round(governance_priority_score(record, config), 4),
        "review_priority": review_priority(record, config),
        "owner": record.owner,
        "status": record.status,
        "governance_note": governance_note(record, config),
    }


def run(article_root: Path, input_path: Path | None = None, output_dir: Path | None = None) -> None:
    article_root = article_root.resolve()
    config = SerialNarrativeGovernanceConfig()
    input_path = input_path or article_root / "data" / "serial_narrative_governance_claims.csv"
    output_dir = output_dir or article_root / "outputs"

    records = load_records(input_path, config)
    rows = [record_to_row(record, config) for record in records]
    cards = [build_serial_narrative_governance_card(record, config) for record in records]

    priority_order = {"high": 3, "medium": 2, "standard": 1}
    rows = sorted(rows, key=lambda row: (priority_order.get(str(row["review_priority"]), 0), float(row["governance_priority_score"])), reverse=True)

    queue = [row for row in rows if row["review_priority"] != "standard"]
    queue_cards = [card for card in cards if card["review"]["priority"] != "standard"]

    write_csv(output_dir / "tables" / "serial_narrative_governance_audit.csv", rows)
    write_csv(output_dir / "tables" / "serial_narrative_governance_queue.csv", queue)
    write_json(output_dir / "json" / "serial_narrative_governance_canvas_cards.json", cards)
    write_json(output_dir / "json" / "serial_narrative_governance_queue.json", queue_cards)
    write_markdown_queue(output_dir / "markdown" / "serial_narrative_governance_queue.md", queue)

    print("Serial narrative governance audit complete.")
    print(output_dir / "tables" / "serial_narrative_governance_audit.csv")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Run serial narrative governance Canvas audit.")
    parser.add_argument("--article-root", type=Path, default=Path(__file__).resolve().parents[2])
    parser.add_argument("--input", type=Path, default=None)
    parser.add_argument("--output-dir", type=Path, default=None)
    return parser


def main() -> None:
    args = build_parser().parse_args()
    run(args.article_root, args.input, args.output_dir)


if __name__ == "__main__":
    main()
