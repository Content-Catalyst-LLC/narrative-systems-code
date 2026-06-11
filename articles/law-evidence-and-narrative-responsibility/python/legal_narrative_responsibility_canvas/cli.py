from __future__ import annotations

from pathlib import Path
import argparse
import csv

from .models import LegalNarrativeResponsibilityConfig, LegalNarrativeResponsibilityRecord
from .validation import validate_record
from .scoring import ai_legal_narrative_risk, evidence_support, governance_priority_score, narrative_overreach_risk, procedural_voice, review_priority, testimony_responsibility
from .governance import build_legal_narrative_responsibility_card, governance_note
from .exporters import write_csv, write_json, write_markdown_queue


FIELD_NAMES = [
    "relevance", "authentication", "provenance", "corroboration", "cross_checking",
    "uncertainty_notation", "overcoherence", "evidentiary_gap", "stereotype_reliance",
    "causation_flattening", "affective_bias", "uncertainty_visibility",
    "opportunity_to_be_heard", "discovery_access", "testimony_context", "record_access",
    "correction_pathway", "procedural_posture_clarity", "witness_dignity",
    "testimony_care", "role_complexity", "remedy_connection", "hallucinated_authority",
    "summary_dependence", "context_loss", "procedural_distortion", "bias_reproduction",
    "human_review", "public_consequence"
]


def load_records(path: Path, config: LegalNarrativeResponsibilityConfig) -> list[LegalNarrativeResponsibilityRecord]:
    records: list[LegalNarrativeResponsibilityRecord] = []
    with path.open("r", encoding="utf-8", newline="") as handle:
        for row in csv.DictReader(handle):
            values = {name: float(row[name]) for name in FIELD_NAMES}
            record = LegalNarrativeResponsibilityRecord(
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


def record_to_row(record: LegalNarrativeResponsibilityRecord, config: LegalNarrativeResponsibilityConfig) -> dict[str, object]:
    return {
        "item": record.item,
        "claim_context": record.claim_context,
        "evidence_support": round(evidence_support(record), 4),
        "narrative_overreach_risk": round(narrative_overreach_risk(record), 4),
        "procedural_voice": round(procedural_voice(record), 4),
        "testimony_responsibility": round(testimony_responsibility(record), 4),
        "ai_legal_narrative_risk": round(ai_legal_narrative_risk(record), 4),
        "governance_priority_score": round(governance_priority_score(record, config), 4),
        "review_priority": review_priority(record, config),
        "owner": record.owner,
        "status": record.status,
        "governance_note": governance_note(record, config),
    }


def run(article_root: Path, input_path: Path | None = None, output_dir: Path | None = None) -> None:
    article_root = article_root.resolve()
    config = LegalNarrativeResponsibilityConfig()
    input_path = input_path or article_root / "data" / "legal_narrative_responsibility_claims.csv"
    output_dir = output_dir or article_root / "outputs"

    records = load_records(input_path, config)
    rows = [record_to_row(record, config) for record in records]
    cards = [build_legal_narrative_responsibility_card(record, config) for record in records]

    priority_order = {"high": 3, "medium": 2, "standard": 1}
    rows = sorted(rows, key=lambda row: (priority_order.get(str(row["review_priority"]), 0), float(row["governance_priority_score"])), reverse=True)

    queue = [row for row in rows if row["review_priority"] != "standard"]
    queue_cards = [card for card in cards if card["review"]["priority"] != "standard"]

    write_csv(output_dir / "tables" / "legal_narrative_responsibility_audit.csv", rows)
    write_csv(output_dir / "tables" / "legal_narrative_responsibility_queue.csv", queue)
    write_json(output_dir / "json" / "legal_narrative_responsibility_canvas_cards.json", cards)
    write_json(output_dir / "json" / "legal_narrative_responsibility_queue.json", queue_cards)
    write_markdown_queue(output_dir / "markdown" / "legal_narrative_responsibility_queue.md", queue)

    print("Legal narrative responsibility audit complete.")
    print(output_dir / "tables" / "legal_narrative_responsibility_audit.csv")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Run legal narrative responsibility Canvas audit.")
    parser.add_argument("--article-root", type=Path, default=Path(__file__).resolve().parents[2])
    parser.add_argument("--input", type=Path, default=None)
    parser.add_argument("--output-dir", type=Path, default=None)
    return parser


def main() -> None:
    args = build_parser().parse_args()
    run(args.article_root, args.input, args.output_dir)


if __name__ == "__main__":
    main()
