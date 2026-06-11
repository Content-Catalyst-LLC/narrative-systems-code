from __future__ import annotations

import argparse
import csv
from pathlib import Path

from .exporters import write_csv, write_json, write_markdown_queue
from .governance import build_narrative_formula_drift_card, governance_note
from .models import NarrativeFormulaDriftConfig, NarrativeFormulaDriftRecord
from .scoring import ai_template_risk, formula_drift, framework_health, governance_priority_score, narrative_specificity, review_priority
from .validation import validate_record


def load_records(path: Path, config: NarrativeFormulaDriftConfig) -> list[NarrativeFormulaDriftRecord]:
    records = []
    with path.open("r", encoding="utf-8", newline="") as handle:
        for row in csv.DictReader(handle):
            record = NarrativeFormulaDriftRecord(
                item=row["item"], claim_context=row["claim_context"],
                template_forcing=float(row["template_forcing"]), beat_rigidity=float(row["beat_rigidity"]),
                closure_pressure=float(row["closure_pressure"]), universality_pressure=float(row["universality_pressure"]),
                automation_dependence=float(row["automation_dependence"]), story_specificity=float(row["story_specificity"]),
                scope_clarity=float(row["scope_clarity"]), context_sensitivity=float(row["context_sensitivity"]),
                alternative_lenses=float(row["alternative_lenses"]), refusal_monitoring=float(row["refusal_monitoring"]),
                ethical_governance=float(row["ethical_governance"]), human_judgment=float(row["human_judgment"]),
                voice_originality=float(row["voice_originality"]), place_logic=float(row["place_logic"]),
                temporal_method=float(row["temporal_method"]), material_detail=float(row["material_detail"]),
                relational_logic=float(row["relational_logic"]), cultural_specificity=float(row["cultural_specificity"]),
                default_arc_use=float(row["default_arc_use"]), generic_phrasing=float(row["generic_phrasing"]),
                heroic_arc_pressure=float(row["heroic_arc_pressure"]), market_story_pressure=float(row["market_story_pressure"]),
                resolution_smoothing=float(row["resolution_smoothing"]), variant_comparison=float(row["variant_comparison"]),
                public_consequence=float(row["public_consequence"]), owner=row.get("owner", "editorial"),
                status=row.get("status", "active"), notes=row.get("notes", ""),
            )
            validate_record(record, config)
            records.append(record)
    if not records:
        raise ValueError(f"No records found in {path}")
    return records


def record_to_row(record: NarrativeFormulaDriftRecord, config: NarrativeFormulaDriftConfig) -> dict[str, object]:
    return {
        "item": record.item,
        "claim_context": record.claim_context,
        "formula_drift": round(formula_drift(record), 4),
        "framework_health": round(framework_health(record), 4),
        "narrative_specificity": round(narrative_specificity(record), 4),
        "ai_template_risk": round(ai_template_risk(record), 4),
        "governance_priority_score": round(governance_priority_score(record, config), 4),
        "review_priority": review_priority(record, config),
        "owner": record.owner,
        "status": record.status,
        "governance_note": governance_note(record, config),
    }


def run(article_root: Path) -> None:
    article_root = article_root.resolve()
    config = NarrativeFormulaDriftConfig()
    records = load_records(article_root / "data" / "narrative_formula_drift_claims.csv", config)
    rows = [record_to_row(record, config) for record in records]
    cards = [build_narrative_formula_drift_card(record, config) for record in records]
    rows.sort(key=lambda row: float(row["governance_priority_score"]), reverse=True)
    queue = [row for row in rows if row["review_priority"] != "standard"]
    queue_cards = [card for card in cards if card["review"]["priority"] != "standard"]
    write_csv(article_root / "outputs" / "tables" / "narrative_formula_drift_audit.csv", rows)
    write_csv(article_root / "outputs" / "tables" / "narrative_formula_drift_governance_queue.csv", queue)
    write_json(article_root / "outputs" / "json" / "narrative_formula_drift_canvas_cards.json", cards)
    write_json(article_root / "outputs" / "json" / "narrative_formula_drift_governance_queue.json", queue_cards)
    write_markdown_queue(article_root / "outputs" / "markdown" / "narrative_formula_drift_governance_queue.md", queue)
    print("Narrative formula drift audit complete.")
    print(article_root / "outputs" / "tables" / "narrative_formula_drift_audit.csv")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--article-root", type=Path, default=Path(__file__).resolve().parents[2])
    args = parser.parse_args()
    run(args.article_root)


if __name__ == "__main__":
    main()
