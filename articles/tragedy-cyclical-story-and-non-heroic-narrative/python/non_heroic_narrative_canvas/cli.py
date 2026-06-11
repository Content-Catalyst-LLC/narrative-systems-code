from __future__ import annotations

from pathlib import Path
import argparse
import csv

from .models import NonHeroicNarrativeConfig, NonHeroicNarrativeRecord
from .validation import validate_record
from .scoring import cyclical_structure, governance_priority_score, heroic_overfit_risk, non_heroic_agency, review_priority, review_readiness, tragic_structure
from .governance import build_non_heroic_narrative_card, governance_note
from .exporters import write_csv, write_json, write_markdown_queue


def load_records(path: Path, config: NonHeroicNarrativeConfig) -> list[NonHeroicNarrativeRecord]:
    records: list[NonHeroicNarrativeRecord] = []
    with path.open("r", encoding="utf-8", newline="") as handle:
        for row in csv.DictReader(handle):
            record = NonHeroicNarrativeRecord(
                item=row["item"],
                claim_context=row["claim_context"],
                consequential_action=float(row["consequential_action"]),
                limit_pressure=float(row["limit_pressure"]),
                reversal=float(row["reversal"]),
                recognition_knowledge=float(row["recognition_knowledge"]),
                irreversibility=float(row["irreversibility"]),
                witness_burden=float(row["witness_burden"]),
                repeated_pattern=float(row["repeated_pattern"]),
                seasonal_ritual_signal=float(row["seasonal_ritual_signal"]),
                generational_transmission=float(row["generational_transmission"]),
                institutional_habit=float(row["institutional_habit"]),
                ecological_feedback=float(row["ecological_feedback"]),
                variation_across_return=float(row["variation_across_return"]),
                care=float(row["care"]),
                endurance=float(row["endurance"]),
                witness=float(row["witness"]),
                refusal=float(row["refusal"]),
                maintenance=float(row["maintenance"]),
                survival=float(row["survival"]),
                hero_forcing=float(row["hero_forcing"]),
                victory_pressure=float(row["victory_pressure"]),
                closure_pressure=float(row["closure_pressure"]),
                return_pressure=float(row["return_pressure"]),
                growth_pressure=float(row["growth_pressure"]),
                evidence_visibility=float(row["evidence_visibility"]),
                public_consequence=float(row["public_consequence"]),
                source_context=float(row["source_context"]),
                method_limits=float(row["method_limits"]),
                uncertainty_notes=float(row["uncertainty_notes"]),
                review_owner_clarity=float(row["review_owner_clarity"]),
                owner=row.get("owner", "editorial"),
                status=row.get("status", "active"),
                notes=row.get("notes", ""),
            )
            validate_record(record, config)
            records.append(record)
    if not records:
        raise ValueError(f"No records found in {path}")
    return records


def record_to_row(record: NonHeroicNarrativeRecord, config: NonHeroicNarrativeConfig) -> dict[str, object]:
    return {
        "item": record.item,
        "claim_context": record.claim_context,
        "tragic_structure": round(tragic_structure(record), 4),
        "cyclical_structure": round(cyclical_structure(record), 4),
        "non_heroic_agency": round(non_heroic_agency(record), 4),
        "heroic_overfit_risk": round(heroic_overfit_risk(record), 4),
        "review_readiness": round(review_readiness(record), 4),
        "governance_priority_score": round(governance_priority_score(record, config), 4),
        "review_priority": review_priority(record, config),
        "owner": record.owner,
        "status": record.status,
        "governance_note": governance_note(record, config),
    }


def run(article_root: Path, input_path: Path | None = None, output_dir: Path | None = None) -> None:
    article_root = article_root.resolve()
    config = NonHeroicNarrativeConfig()
    input_path = input_path or article_root / "data" / "non_heroic_narrative_claims.csv"
    output_dir = output_dir or article_root / "outputs"

    records = load_records(input_path, config)
    rows = [record_to_row(record, config) for record in records]
    cards = [build_non_heroic_narrative_card(record, config) for record in records]

    priority_order = {"high": 3, "medium": 2, "standard": 1}
    rows = sorted(rows, key=lambda row: (priority_order.get(str(row["review_priority"]), 0), float(row["governance_priority_score"])), reverse=True)

    queue = [row for row in rows if row["review_priority"] != "standard"]
    queue_cards = [card for card in cards if card["review"]["priority"] != "standard"]

    write_csv(output_dir / "tables" / "non_heroic_narrative_audit.csv", rows)
    write_csv(output_dir / "tables" / "non_heroic_narrative_governance_queue.csv", queue)
    write_json(output_dir / "json" / "non_heroic_narrative_canvas_cards.json", cards)
    write_json(output_dir / "json" / "non_heroic_narrative_governance_queue.json", queue_cards)
    write_markdown_queue(output_dir / "markdown" / "non_heroic_narrative_governance_queue.md", queue)

    print("Non-heroic narrative Canvas audit complete.")
    print(output_dir / "tables" / "non_heroic_narrative_audit.csv")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Run non-heroic narrative Canvas audit.")
    parser.add_argument("--article-root", type=Path, default=Path(__file__).resolve().parents[2])
    parser.add_argument("--input", type=Path, default=None)
    parser.add_argument("--output-dir", type=Path, default=None)
    return parser


def main() -> None:
    args = build_parser().parse_args()
    run(args.article_root, args.input, args.output_dir)


if __name__ == "__main__":
    main()
