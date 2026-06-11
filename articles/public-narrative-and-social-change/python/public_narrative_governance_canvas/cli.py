from __future__ import annotations

from pathlib import Path
import argparse
import csv

from .models import PublicNarrativeGovernanceConfig, PublicNarrativeGovernanceRecord
from .validation import validate_record
from .scoring import ai_public_narrative_risk, governance_priority_score, mobilization_readiness, public_narrative_coherence, public_voice_integrity, review_priority, testimony_extraction_risk
from .governance import build_public_narrative_governance_card, governance_note
from .exporters import write_csv, write_json, write_markdown_queue


FIELD_NAMES = [
    "self_clarity", "us_clarity", "now_clarity", "value_articulation",
    "action_clarity", "governance_review", "diagnostic_frame",
    "proposed_solution", "resource_support", "coalition_openness",
    "tactical_action", "feedback_loop", "consent_deficit",
    "emotional_targeting", "safety_risk", "reuse_uncertainty",
    "visibility_risk", "agency", "voice_plurality",
    "affected_community_authority", "evidence_visibility", "digital_context",
    "summary_dependence", "omitted_voices", "context_loss",
    "bias_reproduction", "uncertainty_erasure", "human_review",
    "public_consequence"
]


def load_records(path: Path, config: PublicNarrativeGovernanceConfig) -> list[PublicNarrativeGovernanceRecord]:
    records: list[PublicNarrativeGovernanceRecord] = []
    with path.open("r", encoding="utf-8", newline="") as handle:
        for row in csv.DictReader(handle):
            values = {name: float(row[name]) for name in FIELD_NAMES}
            record = PublicNarrativeGovernanceRecord(
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


def record_to_row(record: PublicNarrativeGovernanceRecord, config: PublicNarrativeGovernanceConfig) -> dict[str, object]:
    return {
        "item": record.item,
        "claim_context": record.claim_context,
        "public_narrative_coherence": round(public_narrative_coherence(record), 4),
        "mobilization_readiness": round(mobilization_readiness(record), 4),
        "testimony_extraction_risk": round(testimony_extraction_risk(record), 4),
        "public_voice_integrity": round(public_voice_integrity(record), 4),
        "ai_public_narrative_risk": round(ai_public_narrative_risk(record), 4),
        "governance_priority_score": round(governance_priority_score(record, config), 4),
        "review_priority": review_priority(record, config),
        "owner": record.owner,
        "status": record.status,
        "governance_note": governance_note(record, config),
    }


def run(article_root: Path, input_path: Path | None = None, output_dir: Path | None = None) -> None:
    article_root = article_root.resolve()
    config = PublicNarrativeGovernanceConfig()
    input_path = input_path or article_root / "data" / "public_narrative_governance_claims.csv"
    output_dir = output_dir or article_root / "outputs"

    records = load_records(input_path, config)
    rows = [record_to_row(record, config) for record in records]
    cards = [build_public_narrative_governance_card(record, config) for record in records]

    priority_order = {"high": 3, "medium": 2, "standard": 1}
    rows = sorted(rows, key=lambda row: (priority_order.get(str(row["review_priority"]), 0), float(row["governance_priority_score"])), reverse=True)

    queue = [row for row in rows if row["review_priority"] != "standard"]
    queue_cards = [card for card in cards if card["review"]["priority"] != "standard"]

    write_csv(output_dir / "tables" / "public_narrative_governance_audit.csv", rows)
    write_csv(output_dir / "tables" / "public_narrative_governance_queue.csv", queue)
    write_json(output_dir / "json" / "public_narrative_governance_canvas_cards.json", cards)
    write_json(output_dir / "json" / "public_narrative_governance_queue.json", queue_cards)
    write_markdown_queue(output_dir / "markdown" / "public_narrative_governance_queue.md", queue)

    print("Public narrative governance audit complete.")
    print(output_dir / "tables" / "public_narrative_governance_audit.csv")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Run public narrative governance Canvas audit.")
    parser.add_argument("--article-root", type=Path, default=Path(__file__).resolve().parents[2])
    parser.add_argument("--input", type=Path, default=None)
    parser.add_argument("--output-dir", type=Path, default=None)
    return parser


def main() -> None:
    args = build_parser().parse_args()
    run(args.article_root, args.input, args.output_dir)


if __name__ == "__main__":
    main()
