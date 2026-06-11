from __future__ import annotations

from pathlib import Path
import argparse
import csv

from .models import HeroJourneyFilmGovernanceConfig, HeroJourneyFilmGovernanceRecord
from .validation import validate_record
from .scoring import ai_hero_template_risk, cinematic_transformation, culture_gender_integrity, formula_risk, governance_priority_score, heroic_arc_integrity, review_priority
from .governance import build_hero_journey_film_governance_card, governance_note
from .exporters import write_csv, write_json, write_markdown_queue


FIELD_NAMES = [
    "call_authenticity", "threshold_significance", "ordeal_relevance",
    "value_change", "return_boon", "ethical_consequence", "beat_compliance",
    "generic_mentor", "mechanical_call", "ordeal_spectacle", "forced_return",
    "story_particularity", "visual_motif", "sound_design", "editing_rhythm",
    "performance_shift", "blocking_change", "mise_en_scene", "collective_agency",
    "cultural_specificity", "gender_complexity", "nonheroic_alternatives",
    "stage_compliance", "cultural_loss", "genre_cliche", "universalist_pressure",
    "trope_recycling", "human_review", "public_consequence"
]


def load_records(path: Path, config: HeroJourneyFilmGovernanceConfig) -> list[HeroJourneyFilmGovernanceRecord]:
    records: list[HeroJourneyFilmGovernanceRecord] = []
    with path.open("r", encoding="utf-8", newline="") as handle:
        for row in csv.DictReader(handle):
            values = {name: float(row[name]) for name in FIELD_NAMES}
            record = HeroJourneyFilmGovernanceRecord(
                item=row["item"],
                film_context=row["film_context"],
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


def record_to_row(record: HeroJourneyFilmGovernanceRecord, config: HeroJourneyFilmGovernanceConfig) -> dict[str, object]:
    return {
        "item": record.item,
        "film_context": record.film_context,
        "heroic_arc_integrity": round(heroic_arc_integrity(record), 4),
        "formula_risk": round(formula_risk(record), 4),
        "cinematic_transformation": round(cinematic_transformation(record), 4),
        "culture_gender_integrity": round(culture_gender_integrity(record), 4),
        "ai_hero_template_risk": round(ai_hero_template_risk(record), 4),
        "governance_priority_score": round(governance_priority_score(record, config), 4),
        "review_priority": review_priority(record, config),
        "owner": record.owner,
        "status": record.status,
        "governance_note": governance_note(record, config),
    }


def run(article_root: Path, input_path: Path | None = None, output_dir: Path | None = None) -> None:
    article_root = article_root.resolve()
    config = HeroJourneyFilmGovernanceConfig()
    input_path = input_path or article_root / "data" / "hero_journey_film_governance_claims.csv"
    output_dir = output_dir or article_root / "outputs"

    records = load_records(input_path, config)
    rows = [record_to_row(record, config) for record in records]
    cards = [build_hero_journey_film_governance_card(record, config) for record in records]

    priority_order = {"high": 3, "medium": 2, "standard": 1}
    rows = sorted(rows, key=lambda row: (priority_order.get(str(row["review_priority"]), 0), float(row["governance_priority_score"])), reverse=True)

    queue = [row for row in rows if row["review_priority"] != "standard"]
    queue_cards = [card for card in cards if card["review"]["priority"] != "standard"]

    write_csv(output_dir / "tables" / "hero_journey_film_governance_audit.csv", rows)
    write_csv(output_dir / "tables" / "hero_journey_film_governance_queue.csv", queue)
    write_json(output_dir / "json" / "hero_journey_film_governance_canvas_cards.json", cards)
    write_json(output_dir / "json" / "hero_journey_film_governance_queue.json", queue_cards)
    write_markdown_queue(output_dir / "markdown" / "hero_journey_film_governance_queue.md", queue)

    print("Hero’s journey film governance audit complete.")
    print(output_dir / "tables" / "hero_journey_film_governance_audit.csv")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Run hero’s journey film governance Canvas audit.")
    parser.add_argument("--article-root", type=Path, default=Path(__file__).resolve().parents[2])
    parser.add_argument("--input", type=Path, default=None)
    parser.add_argument("--output-dir", type=Path, default=None)
    return parser


def main() -> None:
    args = build_parser().parse_args()
    run(args.article_root, args.input, args.output_dir)


if __name__ == "__main__":
    main()
