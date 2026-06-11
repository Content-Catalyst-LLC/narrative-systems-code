from __future__ import annotations

from pathlib import Path
import argparse
import csv

from .models import HeroineJourneyConfig, HeroineJourneyRecord
from .validation import validate_record
from .scoring import critique_readiness, framework_risk, governance_priority_score, heroine_alignment, integration_quality, review_priority
from .governance import build_heroine_journey_card, governance_note
from .exporters import write_csv, write_json, write_markdown_queue


def load_records(path: Path, config: HeroineJourneyConfig) -> list[HeroineJourneyRecord]:
    records: list[HeroineJourneyRecord] = []
    with path.open("r", encoding="utf-8", newline="") as handle:
        for row in csv.DictReader(handle):
            record = HeroineJourneyRecord(
                item=row["item"],
                claim_context=row["claim_context"],
                separation_from_feminine=float(row["separation_from_feminine"]),
                masculine_identification=float(row["masculine_identification"]),
                aridity_after_success=float(row["aridity_after_success"]),
                descent_crisis=float(row["descent_crisis"]),
                reconnection_feminine=float(row["reconnection_feminine"]),
                integration_wholeness=float(row["integration_wholeness"]),
                template_forcing=float(row["template_forcing"]),
                gender_essentialism=float(row["gender_essentialism"]),
                universal_womanhood=float(row["universal_womanhood"]),
                psychological_overreach=float(row["psychological_overreach"]),
                healing_pressure=float(row["healing_pressure"]),
                cultural_context=float(row["cultural_context"]),
                source_context=float(row["source_context"]),
                alternative_lens=float(row["alternative_lens"]),
                gender_complexity=float(row["gender_complexity"]),
                uncertainty_notes=float(row["uncertainty_notes"]),
                review_owner_clarity=float(row["review_owner_clarity"]),
                agency=float(row["agency"]),
                relational_grounding=float(row["relational_grounding"]),
                embodiment=float(row["embodiment"]),
                healthy_power=float(row["healthy_power"]),
                emotional_maturity=float(row["emotional_maturity"]),
                open_process=float(row["open_process"]),
                public_consequence=float(row["public_consequence"]),
                owner=row.get("owner", "editorial"),
                status=row.get("status", "active"),
                notes=row.get("notes", ""),
            )
            validate_record(record, config)
            records.append(record)
    if not records:
        raise ValueError(f"No records found in {path}")
    return records


def record_to_row(record: HeroineJourneyRecord, config: HeroineJourneyConfig) -> dict[str, object]:
    return {
        "item": record.item,
        "claim_context": record.claim_context,
        "heroine_alignment": round(heroine_alignment(record), 4),
        "framework_risk": round(framework_risk(record), 4),
        "critique_readiness": round(critique_readiness(record), 4),
        "integration_quality": round(integration_quality(record), 4),
        "governance_priority_score": round(governance_priority_score(record, config), 4),
        "review_priority": review_priority(record, config),
        "owner": record.owner,
        "status": record.status,
        "governance_note": governance_note(record, config),
    }


def run(article_root: Path, input_path: Path | None = None, output_dir: Path | None = None) -> None:
    article_root = article_root.resolve()
    config = HeroineJourneyConfig()
    input_path = input_path or article_root / "data" / "heroine_journey_claims.csv"
    output_dir = output_dir or article_root / "outputs"

    records = load_records(input_path, config)
    rows = [record_to_row(record, config) for record in records]
    cards = [build_heroine_journey_card(record, config) for record in records]

    priority_order = {"high": 3, "medium": 2, "standard": 1}
    rows = sorted(rows, key=lambda row: (priority_order.get(str(row["review_priority"]), 0), float(row["governance_priority_score"])), reverse=True)

    queue = [row for row in rows if row["review_priority"] != "standard"]
    queue_cards = [card for card in cards if card["review"]["priority"] != "standard"]

    write_csv(output_dir / "tables" / "heroine_journey_audit.csv", rows)
    write_csv(output_dir / "tables" / "heroine_journey_governance_queue.csv", queue)
    write_json(output_dir / "json" / "heroine_journey_canvas_cards.json", cards)
    write_json(output_dir / "json" / "heroine_journey_governance_queue.json", queue_cards)
    write_markdown_queue(output_dir / "markdown" / "heroine_journey_governance_queue.md", queue)

    print("Heroine journey Canvas audit complete.")
    print(output_dir / "tables" / "heroine_journey_audit.csv")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Run heroine journey Canvas audit.")
    parser.add_argument("--article-root", type=Path, default=Path(__file__).resolve().parents[2])
    parser.add_argument("--input", type=Path, default=None)
    parser.add_argument("--output-dir", type=Path, default=None)
    return parser


def main() -> None:
    args = build_parser().parse_args()
    run(args.article_root, args.input, args.output_dir)


if __name__ == "__main__":
    main()
