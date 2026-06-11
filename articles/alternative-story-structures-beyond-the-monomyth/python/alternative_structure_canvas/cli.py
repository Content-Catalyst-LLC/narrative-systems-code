from __future__ import annotations

from pathlib import Path
import argparse
import csv

from .models import AlternativeStructureConfig, AlternativeStructureRecord
from .validation import validate_record
from .scoring import alternative_readiness, governance_priority_score, medium_fit, monomyth_overfit_risk, review_priority, structural_plurality
from .governance import build_alternative_structure_card, governance_note
from .exporters import write_csv, write_json, write_markdown_queue


def load_records(path: Path, config: AlternativeStructureConfig) -> list[AlternativeStructureRecord]:
    records: list[AlternativeStructureRecord] = []
    with path.open("r", encoding="utf-8", newline="") as handle:
        for row in csv.DictReader(handle):
            record = AlternativeStructureRecord(
                item=row["item"],
                claim_context=row["claim_context"],
                arc_signal=float(row["arc_signal"]),
                cycle_signal=float(row["cycle_signal"]),
                braid_signal=float(row["braid_signal"]),
                mosaic_signal=float(row["mosaic_signal"]),
                network_signal=float(row["network_signal"]),
                relational_signal=float(row["relational_signal"]),
                fragment_signal=float(row["fragment_signal"]),
                hero_forcing=float(row["hero_forcing"]),
                conflict_substitution=float(row["conflict_substitution"]),
                return_pressure=float(row["return_pressure"]),
                individualization_pressure=float(row["individualization_pressure"]),
                template_forcing=float(row["template_forcing"]),
                evidence_visibility=float(row["evidence_visibility"]),
                source_context=float(row["source_context"]),
                method_limits=float(row["method_limits"]),
                alternative_lens=float(row["alternative_lens"]),
                cultural_context=float(row["cultural_context"]),
                uncertainty_notes=float(row["uncertainty_notes"]),
                review_owner_clarity=float(row["review_owner_clarity"]),
                temporal_match=float(row["temporal_match"]),
                agency_design=float(row["agency_design"]),
                pacing_compatibility=float(row["pacing_compatibility"]),
                sequence_logic=float(row["sequence_logic"]),
                interaction_affordance=float(row["interaction_affordance"]),
                experiential_coherence=float(row["experiential_coherence"]),
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


def record_to_row(record: AlternativeStructureRecord, config: AlternativeStructureConfig) -> dict[str, object]:
    return {
        "item": record.item,
        "claim_context": record.claim_context,
        "structural_plurality": round(structural_plurality(record), 4),
        "monomyth_overfit_risk": round(monomyth_overfit_risk(record), 4),
        "alternative_readiness": round(alternative_readiness(record), 4),
        "medium_fit": round(medium_fit(record), 4),
        "governance_priority_score": round(governance_priority_score(record, config), 4),
        "review_priority": review_priority(record, config),
        "owner": record.owner,
        "status": record.status,
        "governance_note": governance_note(record, config),
    }


def run(article_root: Path, input_path: Path | None = None, output_dir: Path | None = None) -> None:
    article_root = article_root.resolve()
    config = AlternativeStructureConfig()
    input_path = input_path or article_root / "data" / "alternative_structure_claims.csv"
    output_dir = output_dir or article_root / "outputs"

    records = load_records(input_path, config)
    rows = [record_to_row(record, config) for record in records]
    cards = [build_alternative_structure_card(record, config) for record in records]

    priority_order = {"high": 3, "medium": 2, "standard": 1}
    rows = sorted(rows, key=lambda row: (priority_order.get(str(row["review_priority"]), 0), float(row["governance_priority_score"])), reverse=True)

    queue = [row for row in rows if row["review_priority"] != "standard"]
    queue_cards = [card for card in cards if card["review"]["priority"] != "standard"]

    write_csv(output_dir / "tables" / "alternative_structure_audit.csv", rows)
    write_csv(output_dir / "tables" / "alternative_structure_governance_queue.csv", queue)
    write_json(output_dir / "json" / "alternative_structure_canvas_cards.json", cards)
    write_json(output_dir / "json" / "alternative_structure_governance_queue.json", queue_cards)
    write_markdown_queue(output_dir / "markdown" / "alternative_structure_governance_queue.md", queue)

    print("Alternative structure Canvas audit complete.")
    print(output_dir / "tables" / "alternative_structure_audit.csv")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Run alternative structure Canvas audit.")
    parser.add_argument("--article-root", type=Path, default=Path(__file__).resolve().parents[2])
    parser.add_argument("--input", type=Path, default=None)
    parser.add_argument("--output-dir", type=Path, default=None)
    return parser


def main() -> None:
    args = build_parser().parse_args()
    run(args.article_root, args.input, args.output_dir)


if __name__ == "__main__":
    main()
