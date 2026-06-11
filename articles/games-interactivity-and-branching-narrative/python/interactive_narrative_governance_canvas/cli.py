from __future__ import annotations

from pathlib import Path
import argparse
import csv

from .models import InteractiveNarrativeGovernanceConfig, InteractiveNarrativeGovernanceRecord
from .validation import validate_record
from .scoring import agency_integrity, ai_interactive_narrative_risk, branching_burden, failure_and_identity_strength, governance_priority_score, review_priority, system_story_alignment
from .governance import build_interactive_narrative_governance_card, governance_note
from .exporters import write_csv, write_json, write_markdown_queue


FIELD_NAMES = [
    "choice_meaningfulness", "system_response", "feedback_clarity",
    "role_variation", "world_memory", "ethical_governance",
    "branch_count_pressure", "state_dependency", "consequence_tracking",
    "testing_load", "localization_cost", "recombination_coherence",
    "mechanic_theme_fit", "rule_fiction_fit", "goal_value_fit",
    "progression_coherence", "interface_legibility", "consequence_consistency",
    "failure_meaning", "replay_value", "player_consent", "identity_care",
    "generic_quest_generation", "character_memory_failure", "opaque_system_response",
    "player_manipulation", "harmful_stereotype_risk", "human_review",
    "public_consequence"
]


def load_records(path: Path, config: InteractiveNarrativeGovernanceConfig) -> list[InteractiveNarrativeGovernanceRecord]:
    records: list[InteractiveNarrativeGovernanceRecord] = []
    with path.open("r", encoding="utf-8", newline="") as handle:
        for row in csv.DictReader(handle):
            values = {name: float(row[name]) for name in FIELD_NAMES}
            record = InteractiveNarrativeGovernanceRecord(
                item=row["item"],
                game_context=row["game_context"],
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


def record_to_row(record: InteractiveNarrativeGovernanceRecord, config: InteractiveNarrativeGovernanceConfig) -> dict[str, object]:
    return {
        "item": record.item,
        "game_context": record.game_context,
        "agency_integrity": round(agency_integrity(record), 4),
        "branching_burden": round(branching_burden(record), 4),
        "system_story_alignment": round(system_story_alignment(record), 4),
        "failure_and_identity_strength": round(failure_and_identity_strength(record), 4),
        "ai_interactive_narrative_risk": round(ai_interactive_narrative_risk(record), 4),
        "governance_priority_score": round(governance_priority_score(record, config), 4),
        "review_priority": review_priority(record, config),
        "owner": record.owner,
        "status": record.status,
        "governance_note": governance_note(record, config),
    }


def run(article_root: Path, input_path: Path | None = None, output_dir: Path | None = None) -> None:
    article_root = article_root.resolve()
    config = InteractiveNarrativeGovernanceConfig()
    input_path = input_path or article_root / "data" / "interactive_narrative_governance_claims.csv"
    output_dir = output_dir or article_root / "outputs"

    records = load_records(input_path, config)
    rows = [record_to_row(record, config) for record in records]
    cards = [build_interactive_narrative_governance_card(record, config) for record in records]

    priority_order = {"high": 3, "medium": 2, "standard": 1}
    rows = sorted(rows, key=lambda row: (priority_order.get(str(row["review_priority"]), 0), float(row["governance_priority_score"])), reverse=True)

    queue = [row for row in rows if row["review_priority"] != "standard"]
    queue_cards = [card for card in cards if card["review"]["priority"] != "standard"]

    write_csv(output_dir / "tables" / "interactive_narrative_governance_audit.csv", rows)
    write_csv(output_dir / "tables" / "interactive_narrative_governance_queue.csv", queue)
    write_json(output_dir / "json" / "interactive_narrative_governance_canvas_cards.json", cards)
    write_json(output_dir / "json" / "interactive_narrative_governance_queue.json", queue_cards)
    write_markdown_queue(output_dir / "markdown" / "interactive_narrative_governance_queue.md", queue)

    print("Interactive narrative governance audit complete.")
    print(output_dir / "tables" / "interactive_narrative_governance_audit.csv")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Run interactive narrative governance Canvas audit.")
    parser.add_argument("--article-root", type=Path, default=Path(__file__).resolve().parents[2])
    parser.add_argument("--input", type=Path, default=None)
    parser.add_argument("--output-dir", type=Path, default=None)
    return parser


def main() -> None:
    args = build_parser().parse_args()
    run(args.article_root, args.input, args.output_dir)


if __name__ == "__main__":
    main()
