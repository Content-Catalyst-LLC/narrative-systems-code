from __future__ import annotations

from pathlib import Path
import argparse
import csv

from .models import InstitutionalMemoryGovernanceConfig, InstitutionalMemoryGovernanceRecord
from .validation import validate_record
from .scoring import ai_memory_distortion_risk, governance_priority_score, institutional_memory_strength, legitimacy_alignment, origin_myth_risk, reform_credibility, review_priority
from .governance import build_institutional_memory_governance_card, governance_note
from .exporters import write_csv, write_json, write_markdown_queue


FIELD_NAMES = [
    "purpose_clarity", "mission_action_alignment", "record_evidence", "affected_community_testimony",
    "conduct_visibility", "governance_openness", "founder_heroization", "exclusion_omission",
    "harm_removal", "commemoration_saturation", "reputational_branding", "voice_multiplicity",
    "record_preservation", "archive_completeness", "metadata_quality", "testimony_stewardship",
    "knowledge_retention", "public_access", "harm_naming", "structural_change", "evidence_release",
    "material_repair", "oversight", "transparent_progress", "ai_summary_dependence",
    "archive_bias_risk", "context_loss", "correction_pathway", "public_consequence"
]


def load_records(path: Path, config: InstitutionalMemoryGovernanceConfig) -> list[InstitutionalMemoryGovernanceRecord]:
    records: list[InstitutionalMemoryGovernanceRecord] = []
    with path.open("r", encoding="utf-8", newline="") as handle:
        for row in csv.DictReader(handle):
            values = {name: float(row[name]) for name in FIELD_NAMES}
            record = InstitutionalMemoryGovernanceRecord(
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


def record_to_row(record: InstitutionalMemoryGovernanceRecord, config: InstitutionalMemoryGovernanceConfig) -> dict[str, object]:
    return {
        "item": record.item,
        "claim_context": record.claim_context,
        "legitimacy_alignment": round(legitimacy_alignment(record), 4),
        "origin_myth_risk": round(origin_myth_risk(record), 4),
        "institutional_memory_strength": round(institutional_memory_strength(record), 4),
        "reform_credibility": round(reform_credibility(record), 4),
        "ai_memory_distortion_risk": round(ai_memory_distortion_risk(record), 4),
        "governance_priority_score": round(governance_priority_score(record, config), 4),
        "review_priority": review_priority(record, config),
        "owner": record.owner,
        "status": record.status,
        "governance_note": governance_note(record, config),
    }


def run(article_root: Path, input_path: Path | None = None, output_dir: Path | None = None) -> None:
    article_root = article_root.resolve()
    config = InstitutionalMemoryGovernanceConfig()
    input_path = input_path or article_root / "data" / "institutional_memory_governance_claims.csv"
    output_dir = output_dir or article_root / "outputs"

    records = load_records(input_path, config)
    rows = [record_to_row(record, config) for record in records]
    cards = [build_institutional_memory_governance_card(record, config) for record in records]

    priority_order = {"high": 3, "medium": 2, "standard": 1}
    rows = sorted(rows, key=lambda row: (priority_order.get(str(row["review_priority"]), 0), float(row["governance_priority_score"])), reverse=True)

    queue = [row for row in rows if row["review_priority"] != "standard"]
    queue_cards = [card for card in cards if card["review"]["priority"] != "standard"]

    write_csv(output_dir / "tables" / "institutional_memory_governance_audit.csv", rows)
    write_csv(output_dir / "tables" / "institutional_memory_governance_queue.csv", queue)
    write_json(output_dir / "json" / "institutional_memory_governance_canvas_cards.json", cards)
    write_json(output_dir / "json" / "institutional_memory_governance_queue.json", queue_cards)
    write_markdown_queue(output_dir / "markdown" / "institutional_memory_governance_queue.md", queue)

    print("Institutional memory governance audit complete.")
    print(output_dir / "tables" / "institutional_memory_governance_audit.csv")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Run institutional memory governance Canvas audit.")
    parser.add_argument("--article-root", type=Path, default=Path(__file__).resolve().parents[2])
    parser.add_argument("--input", type=Path, default=None)
    parser.add_argument("--output-dir", type=Path, default=None)
    return parser


def main() -> None:
    args = build_parser().parse_args()
    run(args.article_root, args.input, args.output_dir)


if __name__ == "__main__":
    main()
