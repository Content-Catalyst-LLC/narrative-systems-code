from __future__ import annotations

from pathlib import Path
import argparse
import csv

from .models import PublicStoryGovernanceConfig, PublicStoryGovernanceRecord
from .validation import validate_record
from .scoring import ai_public_rhetoric_risk, civil_religion_accountability, governance_priority_score, mythic_simplification_risk, public_narrative_strength, review_priority, testimony_ethics
from .governance import build_public_story_governance_card, governance_note
from .exporters import write_csv, write_json, write_markdown_queue


def load_records(path: Path, config: PublicStoryGovernanceConfig) -> list[PublicStoryGovernanceRecord]:
    records: list[PublicStoryGovernanceRecord] = []
    with path.open("r", encoding="utf-8", newline="") as handle:
        for row in csv.DictReader(handle):
            record = PublicStoryGovernanceRecord(
                item=row["item"],
                claim_context=row["claim_context"],
                self_story_evidence=float(row["self_story_evidence"]),
                shared_value_clarity=float(row["shared_value_clarity"]),
                now_challenge_clarity=float(row["now_challenge_clarity"]),
                agency=float(row["agency"]),
                hope=float(row["hope"]),
                responsibility=float(row["responsibility"]),
                enemy_simplification=float(row["enemy_simplification"]),
                boundary_hardening=float(row["boundary_hardening"]),
                crisis_compression=float(row["crisis_compression"]),
                urgency_pressure=float(row["urgency_pressure"]),
                scapegoat_intensity=float(row["scapegoat_intensity"]),
                evidence_visibility=float(row["evidence_visibility"]),
                memory_plurality=float(row["memory_plurality"]),
                historical_truthfulness=float(row["historical_truthfulness"]),
                public_limit_clarity=float(row["public_limit_clarity"]),
                dissent_space=float(row["dissent_space"]),
                repair_justice=float(row["repair_justice"]),
                anti_idolatry_critique=float(row["anti_idolatry_critique"]),
                witness_care=float(row["witness_care"]),
                testimony_context=float(row["testimony_context"]),
                harm_visibility=float(row["harm_visibility"]),
                extraction_resistance=float(row["extraction_resistance"]),
                formulaic_default=float(row["formulaic_default"]),
                outrage_intensity=float(row["outrage_intensity"]),
                resolution_smoothing=float(row["resolution_smoothing"]),
                identity_boundary_pressure=float(row["identity_boundary_pressure"]),
                context_missingness=float(row["context_missingness"]),
                human_governance=float(row["human_governance"]),
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


def record_to_row(record: PublicStoryGovernanceRecord, config: PublicStoryGovernanceConfig) -> dict[str, object]:
    return {
        "item": record.item,
        "claim_context": record.claim_context,
        "public_narrative_strength": round(public_narrative_strength(record), 4),
        "mythic_simplification_risk": round(mythic_simplification_risk(record), 4),
        "civil_religion_accountability": round(civil_religion_accountability(record), 4),
        "testimony_ethics": round(testimony_ethics(record), 4),
        "ai_public_rhetoric_risk": round(ai_public_rhetoric_risk(record), 4),
        "governance_priority_score": round(governance_priority_score(record, config), 4),
        "review_priority": review_priority(record, config),
        "owner": record.owner,
        "status": record.status,
        "governance_note": governance_note(record, config),
    }


def run(article_root: Path, input_path: Path | None = None, output_dir: Path | None = None) -> None:
    article_root = article_root.resolve()
    config = PublicStoryGovernanceConfig()
    input_path = input_path or article_root / "data" / "public_story_governance_claims.csv"
    output_dir = output_dir or article_root / "outputs"

    records = load_records(input_path, config)
    rows = [record_to_row(record, config) for record in records]
    cards = [build_public_story_governance_card(record, config) for record in records]

    priority_order = {"high": 3, "medium": 2, "standard": 1}
    rows = sorted(rows, key=lambda row: (priority_order.get(str(row["review_priority"]), 0), float(row["governance_priority_score"])), reverse=True)

    queue = [row for row in rows if row["review_priority"] != "standard"]
    queue_cards = [card for card in cards if card["review"]["priority"] != "standard"]

    write_csv(output_dir / "tables" / "public_story_governance_audit.csv", rows)
    write_csv(output_dir / "tables" / "public_story_governance_queue.csv", queue)
    write_json(output_dir / "json" / "public_story_governance_canvas_cards.json", cards)
    write_json(output_dir / "json" / "public_story_governance_queue.json", queue_cards)
    write_markdown_queue(output_dir / "markdown" / "public_story_governance_queue.md", queue)

    print("Public story governance audit complete.")
    print(output_dir / "tables" / "public_story_governance_audit.csv")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Run public story governance Canvas audit.")
    parser.add_argument("--article-root", type=Path, default=Path(__file__).resolve().parents[2])
    parser.add_argument("--input", type=Path, default=None)
    parser.add_argument("--output-dir", type=Path, default=None)
    return parser


def main() -> None:
    args = build_parser().parse_args()
    run(args.article_root, args.input, args.output_dir)


if __name__ == "__main__":
    main()
