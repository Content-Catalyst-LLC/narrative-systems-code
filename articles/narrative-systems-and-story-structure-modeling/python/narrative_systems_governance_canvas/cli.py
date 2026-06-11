from __future__ import annotations

from pathlib import Path
import argparse
import csv

from .models import NarrativeSystemsGovernanceConfig, NarrativeSystemsGovernanceRecord
from .validation import validate_record
from .scoring import ai_story_structure_risk, formula_drift_risk, governance_priority_score, narrative_coherence, network_system_strength, responsibility_balance, review_priority
from .governance import build_narrative_systems_governance_card, governance_note
from .exporters import write_csv, write_json, write_markdown_queue


FIELD_NAMES = [
    "causal_alignment", "state_transition_clarity", "agent_goal_fit",
    "world_rule_consistency", "temporal_mapping", "evidence_quality",
    "beat_template_dependence", "universal_model_claims", "context_loss",
    "genre_flattening", "model_overconfidence", "judgment_review",
    "individual_agency_visibility", "systemic_agency_visibility",
    "network_mapping", "relationship_specificity", "constraint_visibility",
    "feedback_loop_clarity", "plot_hallucination", "causal_invention",
    "stereotype_tendency", "formula_generation", "biased_corpus",
    "human_review", "public_consequence"
]


def load_records(path: Path, config: NarrativeSystemsGovernanceConfig) -> list[NarrativeSystemsGovernanceRecord]:
    records: list[NarrativeSystemsGovernanceRecord] = []
    with path.open("r", encoding="utf-8", newline="") as handle:
        for row in csv.DictReader(handle):
            values = {name: float(row[name]) for name in FIELD_NAMES}
            record = NarrativeSystemsGovernanceRecord(
                item=row["item"],
                modeling_context=row["modeling_context"],
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


def record_to_row(record: NarrativeSystemsGovernanceRecord, config: NarrativeSystemsGovernanceConfig) -> dict[str, object]:
    return {
        "item": record.item,
        "modeling_context": record.modeling_context,
        "narrative_coherence": round(narrative_coherence(record), 4),
        "formula_drift_risk": round(formula_drift_risk(record), 4),
        "responsibility_balance": round(responsibility_balance(record), 4),
        "network_system_strength": round(network_system_strength(record), 4),
        "ai_story_structure_risk": round(ai_story_structure_risk(record), 4),
        "governance_priority_score": round(governance_priority_score(record, config), 4),
        "review_priority": review_priority(record, config),
        "owner": record.owner,
        "status": record.status,
        "governance_note": governance_note(record, config),
    }


def run(article_root: Path, input_path: Path | None = None, output_dir: Path | None = None) -> None:
    article_root = article_root.resolve()
    config = NarrativeSystemsGovernanceConfig()
    input_path = input_path or article_root / "data" / "narrative_systems_governance_claims.csv"
    output_dir = output_dir or article_root / "outputs"

    records = load_records(input_path, config)
    rows = [record_to_row(record, config) for record in records]
    cards = [build_narrative_systems_governance_card(record, config) for record in records]

    priority_order = {"high": 3, "medium": 2, "standard": 1}
    rows = sorted(rows, key=lambda row: (priority_order.get(str(row["review_priority"]), 0), float(row["governance_priority_score"])), reverse=True)

    queue = [row for row in rows if row["review_priority"] != "standard"]
    queue_cards = [card for card in cards if card["review"]["priority"] != "standard"]

    write_csv(output_dir / "tables" / "narrative_systems_governance_audit.csv", rows)
    write_csv(output_dir / "tables" / "narrative_systems_governance_queue.csv", queue)
    write_json(output_dir / "json" / "narrative_systems_governance_canvas_cards.json", cards)
    write_json(output_dir / "json" / "narrative_systems_governance_queue.json", queue_cards)
    write_markdown_queue(output_dir / "markdown" / "narrative_systems_governance_queue.md", queue)

    print("Narrative systems governance audit complete.")
    print(output_dir / "tables" / "narrative_systems_governance_audit.csv")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Run narrative systems governance Canvas audit.")
    parser.add_argument("--article-root", type=Path, default=Path(__file__).resolve().parents[2])
    parser.add_argument("--input", type=Path, default=None)
    parser.add_argument("--output-dir", type=Path, default=None)
    return parser


def main() -> None:
    args = build_parser().parse_args()
    run(args.article_root, args.input, args.output_dir)


if __name__ == "__main__":
    main()
