from __future__ import annotations

from pathlib import Path
import argparse
import csv

from .models import FragmentedNarrativeConfig, FragmentedNarrativeRecord
from .validation import validate_record
from .scoring import fragmentation_sensitivity, governance_priority_score, interpretation_readiness, review_priority, trauma_narrative_risk, witness_care
from .governance import build_fragmented_narrative_card, governance_note
from .exporters import write_csv, write_json, write_markdown_queue


def load_records(path: Path, config: FragmentedNarrativeConfig) -> list[FragmentedNarrativeRecord]:
    records: list[FragmentedNarrativeRecord] = []
    with path.open("r", encoding="utf-8", newline="") as handle:
        for row in csv.DictReader(handle):
            record = FragmentedNarrativeRecord(
                item=row["item"],
                claim_context=row["claim_context"],
                temporal_rupture=float(row["temporal_rupture"]),
                gap_marking=float(row["gap_marking"]),
                repetition_patterning=float(row["repetition_patterning"]),
                silence_respect=float(row["silence_respect"]),
                uncertainty_notes=float(row["uncertainty_notes"]),
                contextual_care=float(row["contextual_care"]),
                consent=float(row["consent"]),
                agency=float(row["agency"]),
                privacy=float(row["privacy"]),
                relational_context=float(row["relational_context"]),
                safety_framing=float(row["safety_framing"]),
                boundary_discipline=float(row["boundary_discipline"]),
                forced_coherence=float(row["forced_coherence"]),
                redemptive_shortcut=float(row["redemptive_shortcut"]),
                extraction_risk=float(row["extraction_risk"]),
                identity_reduction=float(row["identity_reduction"]),
                spectacle_pressure=float(row["spectacle_pressure"]),
                method_limits=float(row["method_limits"]),
                source_context=float(row["source_context"]),
                cultural_context=float(row["cultural_context"]),
                ethics_governance=float(row["ethics_governance"]),
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


def record_to_row(record: FragmentedNarrativeRecord, config: FragmentedNarrativeConfig) -> dict[str, object]:
    return {
        "item": record.item,
        "claim_context": record.claim_context,
        "fragmentation_sensitivity": round(fragmentation_sensitivity(record), 4),
        "witness_care": round(witness_care(record), 4),
        "trauma_narrative_risk": round(trauma_narrative_risk(record), 4),
        "interpretation_readiness": round(interpretation_readiness(record), 4),
        "governance_priority_score": round(governance_priority_score(record, config), 4),
        "review_priority": review_priority(record, config),
        "owner": record.owner,
        "status": record.status,
        "governance_note": governance_note(record, config),
    }


def run(article_root: Path, input_path: Path | None = None, output_dir: Path | None = None) -> None:
    article_root = article_root.resolve()
    config = FragmentedNarrativeConfig()
    input_path = input_path or article_root / "data" / "fragmented_narrative_claims.csv"
    output_dir = output_dir or article_root / "outputs"

    records = load_records(input_path, config)
    rows = [record_to_row(record, config) for record in records]
    cards = [build_fragmented_narrative_card(record, config) for record in records]

    priority_order = {"high": 3, "medium": 2, "standard": 1}
    rows = sorted(rows, key=lambda row: (priority_order.get(str(row["review_priority"]), 0), float(row["governance_priority_score"])), reverse=True)

    queue = [row for row in rows if row["review_priority"] != "standard"]
    queue_cards = [card for card in cards if card["review"]["priority"] != "standard"]

    write_csv(output_dir / "tables" / "fragmented_narrative_audit.csv", rows)
    write_csv(output_dir / "tables" / "fragmented_narrative_governance_queue.csv", queue)
    write_json(output_dir / "json" / "fragmented_narrative_canvas_cards.json", cards)
    write_json(output_dir / "json" / "fragmented_narrative_governance_queue.json", queue_cards)
    write_markdown_queue(output_dir / "markdown" / "fragmented_narrative_governance_queue.md", queue)

    print("Fragmented narrative Canvas audit complete.")
    print(output_dir / "tables" / "fragmented_narrative_audit.csv")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Run fragmented narrative Canvas audit.")
    parser.add_argument("--article-root", type=Path, default=Path(__file__).resolve().parents[2])
    parser.add_argument("--input", type=Path, default=None)
    parser.add_argument("--output-dir", type=Path, default=None)
    return parser


def main() -> None:
    args = build_parser().parse_args()
    run(args.article_root, args.input, args.output_dir)


if __name__ == "__main__":
    main()
