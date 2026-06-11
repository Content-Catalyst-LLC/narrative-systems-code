from __future__ import annotations

from pathlib import Path
import argparse
import csv

from .models import NarrativeTimeConfig, NarrativeTimeRecord
from .validation import validate_record
from .scoring import emplotment_strength, governance_priority_score, interpretation_readiness, narrative_identity_readiness, narrative_time_configuration, review_priority, temporal_governance_risk
from .governance import build_ricoeur_card, governance_note
from .exporters import write_csv, write_json, write_markdown_queue


def load_records(path: Path, config: NarrativeTimeConfig) -> list[NarrativeTimeRecord]:
    records: list[NarrativeTimeRecord] = []
    with path.open("r", encoding="utf-8", newline="") as handle:
        for row in csv.DictReader(handle):
            record = NarrativeTimeRecord(
                item=row["item"],
                claim_context=row["claim_context"],
                memory_mapping=float(row["memory_mapping"]),
                anticipation=float(row["anticipation"]),
                plot_logic=float(row["plot_logic"]),
                configuration=float(row["configuration"]),
                refiguration=float(row["refiguration"]),
                ending_function=float(row["ending_function"]),
                event_selection=float(row["event_selection"]),
                causal_articulation=float(row["causal_articulation"]),
                reversal_recognition=float(row["reversal_recognition"]),
                concordance=float(row["concordance"]),
                discordance=float(row["discordance"]),
                whole_plot_coherence=float(row["whole_plot_coherence"]),
                continuity=float(row["continuity"]),
                change=float(row["change"]),
                promise_responsibility=float(row["promise_responsibility"]),
                memory_revision=float(row["memory_revision"]),
                agency=float(row["agency"]),
                relational_recognition=float(row["relational_recognition"]),
                premature_closure=float(row["premature_closure"]),
                redemptive_shortcut=float(row["redemptive_shortcut"]),
                erased_continuity=float(row["erased_continuity"]),
                delayed_accountability=float(row["delayed_accountability"]),
                nostalgic_origin=float(row["nostalgic_origin"]),
                uncertainty_notes=float(row["uncertainty_notes"]),
                source_context=float(row["source_context"]),
                counterexamples=float(row["counterexamples"]),
                method_limits=float(row["method_limits"]),
                owner=row.get("owner", "editorial"),
                status=row.get("status", "active"),
                notes=row.get("notes", ""),
            )
            validate_record(record, config)
            records.append(record)
    if not records:
        raise ValueError(f"No records found in {path}")
    return records


def record_to_row(record: NarrativeTimeRecord, config: NarrativeTimeConfig) -> dict[str, object]:
    return {
        "item": record.item,
        "claim_context": record.claim_context,
        "narrative_time_configuration": round(narrative_time_configuration(record), 4),
        "emplotment_strength": round(emplotment_strength(record), 4),
        "narrative_identity_readiness": round(narrative_identity_readiness(record), 4),
        "temporal_governance_risk": round(temporal_governance_risk(record), 4),
        "interpretation_readiness": round(interpretation_readiness(record), 4),
        "governance_priority_score": round(governance_priority_score(record, config), 4),
        "review_priority": review_priority(record, config),
        "owner": record.owner,
        "status": record.status,
        "governance_note": governance_note(record, config),
    }


def run(article_root: Path, input_path: Path | None = None, output_dir: Path | None = None) -> None:
    article_root = article_root.resolve()
    config = NarrativeTimeConfig()
    input_path = input_path or article_root / "data" / "ricoeur_narrative_time_claims.csv"
    output_dir = output_dir or article_root / "outputs"
    records = load_records(input_path, config)
    rows = [record_to_row(record, config) for record in records]
    cards = [build_ricoeur_card(record, config) for record in records]
    priority_order = {"high": 3, "medium": 2, "standard": 1}
    rows = sorted(rows, key=lambda row: (priority_order.get(str(row["review_priority"]), 0), float(row["governance_priority_score"])), reverse=True)
    queue = [row for row in rows if row["review_priority"] != "standard"]
    queue_cards = [card for card in cards if card["review"]["priority"] != "standard"]
    write_csv(output_dir / "tables" / "ricoeur_narrative_time_audit.csv", rows)
    write_csv(output_dir / "tables" / "ricoeur_narrative_time_governance_queue.csv", queue)
    write_json(output_dir / "json" / "ricoeur_narrative_time_canvas_cards.json", cards)
    write_json(output_dir / "json" / "ricoeur_narrative_time_governance_queue.json", queue_cards)
    write_markdown_queue(output_dir / "markdown" / "ricoeur_narrative_time_governance_queue.md", queue)
    print("Ricoeur narrative time Canvas audit complete.")
    print(output_dir / "tables" / "ricoeur_narrative_time_audit.csv")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Run Ricoeur narrative time Canvas audit.")
    parser.add_argument("--article-root", type=Path, default=Path(__file__).resolve().parents[2])
    parser.add_argument("--input", type=Path, default=None)
    parser.add_argument("--output-dir", type=Path, default=None)
    return parser


def main() -> None:
    args = build_parser().parse_args()
    run(args.article_root, args.input, args.output_dir)


if __name__ == "__main__":
    main()
