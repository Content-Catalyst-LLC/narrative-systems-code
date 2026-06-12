from __future__ import annotations

from pathlib import Path
import argparse
import csv

from .models import NarrativeRiskGovernanceConfig, NarrativeRiskGovernanceRecord
from .validation import validate_record
from .scoring import ai_narrative_risk, evidence_integrity, governance_priority_score, narrative_risk, platform_amplification_risk, review_priority, trust_repair_priority
from .governance import build_narrative_risk_governance_card, governance_note
from .exporters import write_csv, write_json, write_markdown_queue


FIELD_NAMES = [
    "scapegoating", "evidence_immunity", "mythic_simplification",
    "context_loss", "group_blame_intensity", "revision_openness",
    "corroboration", "source_quality", "timeline_clarity",
    "uncertainty_disclosure", "accountability_clarity", "disconfirmation_openness",
    "institutional_failure", "opacity", "historical_distrust_reason",
    "public_consequence", "correction_difficulty", "affected_listener_stakes",
    "platform_speed", "repetition_intensity", "social_proof_pressure",
    "monetization_pressure", "synthetic_evidence", "provenance_opacity",
    "fabricated_patterning", "automated_consensus", "vulnerability_targeting",
    "human_review"
]


def load_records(path: Path, config: NarrativeRiskGovernanceConfig) -> list[NarrativeRiskGovernanceRecord]:
    records: list[NarrativeRiskGovernanceRecord] = []
    with path.open("r", encoding="utf-8", newline="") as handle:
        for row in csv.DictReader(handle):
            values = {name: float(row[name]) for name in FIELD_NAMES}
            record = NarrativeRiskGovernanceRecord(
                item=row["item"],
                narrative_context=row["narrative_context"],
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


def record_to_row(record: NarrativeRiskGovernanceRecord, config: NarrativeRiskGovernanceConfig) -> dict[str, object]:
    return {
        "item": record.item,
        "narrative_context": record.narrative_context,
        "narrative_risk": round(narrative_risk(record), 4),
        "evidence_integrity": round(evidence_integrity(record), 4),
        "trust_repair_priority": round(trust_repair_priority(record), 4),
        "platform_amplification_risk": round(platform_amplification_risk(record), 4),
        "ai_narrative_risk": round(ai_narrative_risk(record), 4),
        "governance_priority_score": round(governance_priority_score(record, config), 4),
        "review_priority": review_priority(record, config),
        "owner": record.owner,
        "status": record.status,
        "governance_note": governance_note(record, config),
    }


def run(article_root: Path, input_path: Path | None = None, output_dir: Path | None = None) -> None:
    article_root = article_root.resolve()
    config = NarrativeRiskGovernanceConfig()
    input_path = input_path or article_root / "data" / "narrative_risk_governance_claims.csv"
    output_dir = output_dir or article_root / "outputs"

    records = load_records(input_path, config)
    rows = [record_to_row(record, config) for record in records]
    cards = [build_narrative_risk_governance_card(record, config) for record in records]

    priority_order = {"high": 3, "medium": 2, "standard": 1}
    rows = sorted(rows, key=lambda row: (priority_order.get(str(row["review_priority"]), 0), float(row["governance_priority_score"])), reverse=True)

    queue = [row for row in rows if row["review_priority"] != "standard"]
    queue_cards = [card for card in cards if card["review"]["priority"] != "standard"]

    write_csv(output_dir / "tables" / "narrative_risk_governance_audit.csv", rows)
    write_csv(output_dir / "tables" / "narrative_risk_governance_queue.csv", queue)
    write_json(output_dir / "json" / "narrative_risk_governance_canvas_cards.json", cards)
    write_json(output_dir / "json" / "narrative_risk_governance_queue.json", queue_cards)
    write_markdown_queue(output_dir / "markdown" / "narrative_risk_governance_queue.md", queue)

    print("Narrative risk governance audit complete.")
    print(output_dir / "tables" / "narrative_risk_governance_audit.csv")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Run narrative risk governance Canvas audit.")
    parser.add_argument("--article-root", type=Path, default=Path(__file__).resolve().parents[2])
    parser.add_argument("--input", type=Path, default=None)
    parser.add_argument("--output-dir", type=Path, default=None)
    return parser


def main() -> None:
    args = build_parser().parse_args()
    run(args.article_root, args.input, args.output_dir)


if __name__ == "__main__":
    main()
