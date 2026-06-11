from __future__ import annotations

from pathlib import Path
import argparse
import csv

from .models import MoralAgencyConfig, MoralAgencyRecord
from .validation import validate_record
from .scoring import excuse_risk, governance_priority_score, interpretation_readiness, moral_clarity, repair_readiness, review_priority
from .governance import build_moral_agency_card, governance_note
from .exporters import write_csv, write_json, write_markdown_queue


def load_records(path: Path, config: MoralAgencyConfig) -> list[MoralAgencyRecord]:
    records: list[MoralAgencyRecord] = []
    with path.open("r", encoding="utf-8", newline="") as handle:
        for row in csv.DictReader(handle):
            record = MoralAgencyRecord(
                item=row["item"],
                claim_context=row["claim_context"],
                action_naming=float(row["action_naming"]),
                intention_distinction=float(row["intention_distinction"]),
                consequence_clarity=float(row["consequence_clarity"]),
                harm_marking=float(row["harm_marking"]),
                repair_orientation=float(row["repair_orientation"]),
                other_visibility=float(row["other_visibility"]),
                context_overuse=float(row["context_overuse"]),
                intention_shielding=float(row["intention_shielding"]),
                victimhood_shielding=float(row["victimhood_shielding"]),
                blame_shifting=float(row["blame_shifting"]),
                growth_substitution=float(row["growth_substitution"]),
                harm_minimization=float(row["harm_minimization"]),
                harm_acknowledgment=float(row["harm_acknowledgment"]),
                apology_precision=float(row["apology_precision"]),
                material_response=float(row["material_response"]),
                conduct_change=float(row["conduct_change"]),
                future_accountability=float(row["future_accountability"]),
                third_party_oversight=float(row["third_party_oversight"]),
                source_context=float(row["source_context"]),
                evidence_visibility=float(row["evidence_visibility"]),
                uncertainty_notes=float(row["uncertainty_notes"]),
                cultural_context=float(row["cultural_context"]),
                method_limits=float(row["method_limits"]),
                review_owner_clarity=float(row["review_owner_clarity"]),
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


def record_to_row(record: MoralAgencyRecord, config: MoralAgencyConfig) -> dict[str, object]:
    return {
        "item": record.item,
        "claim_context": record.claim_context,
        "moral_clarity": round(moral_clarity(record), 4),
        "excuse_risk": round(excuse_risk(record), 4),
        "repair_readiness": round(repair_readiness(record), 4),
        "interpretation_readiness": round(interpretation_readiness(record), 4),
        "governance_priority_score": round(governance_priority_score(record, config), 4),
        "review_priority": review_priority(record, config),
        "owner": record.owner,
        "status": record.status,
        "governance_note": governance_note(record, config),
    }


def run(article_root: Path, input_path: Path | None = None, output_dir: Path | None = None) -> None:
    article_root = article_root.resolve()
    config = MoralAgencyConfig()
    input_path = input_path or article_root / "data" / "moral_agency_claims.csv"
    output_dir = output_dir or article_root / "outputs"

    records = load_records(input_path, config)
    rows = [record_to_row(record, config) for record in records]
    cards = [build_moral_agency_card(record, config) for record in records]

    priority_order = {"high": 3, "medium": 2, "standard": 1}
    rows = sorted(rows, key=lambda row: (priority_order.get(str(row["review_priority"]), 0), float(row["governance_priority_score"])), reverse=True)

    queue = [row for row in rows if row["review_priority"] != "standard"]
    queue_cards = [card for card in cards if card["review"]["priority"] != "standard"]

    write_csv(output_dir / "tables" / "moral_agency_audit.csv", rows)
    write_csv(output_dir / "tables" / "moral_agency_governance_queue.csv", queue)
    write_json(output_dir / "json" / "moral_agency_canvas_cards.json", cards)
    write_json(output_dir / "json" / "moral_agency_governance_queue.json", queue_cards)
    write_markdown_queue(output_dir / "markdown" / "moral_agency_governance_queue.md", queue)

    print("Moral agency Canvas audit complete.")
    print(output_dir / "tables" / "moral_agency_audit.csv")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Run moral agency Canvas audit.")
    parser.add_argument("--article-root", type=Path, default=Path(__file__).resolve().parents[2])
    parser.add_argument("--input", type=Path, default=None)
    parser.add_argument("--output-dir", type=Path, default=None)
    return parser


def main() -> None:
    args = build_parser().parse_args()
    run(args.article_root, args.input, args.output_dir)


if __name__ == "__main__":
    main()
