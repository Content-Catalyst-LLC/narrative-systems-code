from __future__ import annotations

from pathlib import Path
import argparse
import csv
from .models import SacredHistoryConfig, SacredHistoryRecord
from .validation import validate_record
from .scoring import governance_priority_score, interpretation_readiness, revelatory_claim_strength, review_priority, sacred_authority_risk, sacred_history_integration
from .governance import build_sacred_history_card, governance_note
from .exporters import write_csv, write_json, write_markdown_queue


def load_records(path: Path, config: SacredHistoryConfig) -> list[SacredHistoryRecord]:
    records: list[SacredHistoryRecord] = []
    with path.open("r", encoding="utf-8", newline="") as handle:
        for row in csv.DictReader(handle):
            record = SacredHistoryRecord(
                item=row["item"], claim_context=row["claim_context"],
                sacred_disclosure=float(row["sacred_disclosure"]), event_meaning=float(row["event_meaning"]), authority_clarity=float(row["authority_clarity"]), obligation=float(row["obligation"]), transformation=float(row["transformation"]), communal_memory=float(row["communal_memory"]), historical_context=float(row["historical_context"]), memory_depth=float(row["memory_depth"]), ritual_transmission=float(row["ritual_transmission"]), interpretive_authority=float(row["interpretive_authority"]), ethical_governance=float(row["ethical_governance"]), public_responsibility=float(row["public_responsibility"]), sacred_certainty=float(row["sacred_certainty"]), omission_risk=float(row["omission_risk"]), political_sanctification=float(row["political_sanctification"]), exclusion_risk=float(row["exclusion_risk"]), historical_flattening=float(row["historical_flattening"]), uncertainty_marking=float(row["uncertainty_marking"]), source_context=float(row["source_context"]), authority_notes=float(row["authority_notes"]), counterexamples=float(row["counterexamples"]), method_limits=float(row["method_limits"]), owner=row.get("owner", "editorial"), status=row.get("status", "active"), notes=row.get("notes", "")
            )
            validate_record(record, config)
            records.append(record)
    if not records:
        raise ValueError(f"No records found in {path}")
    return records


def record_to_row(record: SacredHistoryRecord, config: SacredHistoryConfig) -> dict[str, object]:
    return {"item": record.item, "claim_context": record.claim_context, "revelatory_claim_strength": round(revelatory_claim_strength(record), 4), "sacred_history_integration": round(sacred_history_integration(record), 4), "sacred_authority_risk": round(sacred_authority_risk(record), 4), "interpretation_readiness": round(interpretation_readiness(record), 4), "governance_priority_score": round(governance_priority_score(record, config), 4), "review_priority": review_priority(record, config), "owner": record.owner, "status": record.status, "governance_note": governance_note(record, config)}


def run(article_root: Path, input_path: Path | None = None, output_dir: Path | None = None) -> None:
    article_root = article_root.resolve()
    config = SacredHistoryConfig()
    input_path = input_path or article_root / "data" / "sacred_history_claims.csv"
    output_dir = output_dir or article_root / "outputs"
    records = load_records(input_path, config)
    rows = [record_to_row(record, config) for record in records]
    cards = [build_sacred_history_card(record, config) for record in records]
    priority_order = {"high": 3, "medium": 2, "standard": 1}
    rows = sorted(rows, key=lambda row: (priority_order.get(str(row["review_priority"]), 0), float(row["governance_priority_score"])), reverse=True)
    queue = [row for row in rows if row["review_priority"] != "standard"]
    queue_cards = [card for card in cards if card["review"]["priority"] != "standard"]
    write_csv(output_dir / "tables" / "sacred_history_audit.csv", rows)
    write_csv(output_dir / "tables" / "sacred_history_governance_queue.csv", queue)
    write_json(output_dir / "json" / "sacred_history_canvas_cards.json", cards)
    write_json(output_dir / "json" / "sacred_history_governance_queue.json", queue_cards)
    write_markdown_queue(output_dir / "markdown" / "sacred_history_governance_queue.md", queue)
    print("Sacred history Canvas audit complete.")
    print(output_dir / "tables" / "sacred_history_audit.csv")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Run sacred-history Canvas audit.")
    parser.add_argument("--article-root", type=Path, default=Path(__file__).resolve().parents[2])
    parser.add_argument("--input", type=Path, default=None)
    parser.add_argument("--output-dir", type=Path, default=None)
    return parser


def main() -> None:
    args = build_parser().parse_args()
    run(args.article_root, args.input, args.output_dir)


if __name__ == "__main__":
    main()
