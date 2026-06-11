from __future__ import annotations

from hashlib import sha256
from typing import Any

from .models import HeroJourneyFilmGovernanceConfig, HeroJourneyFilmGovernanceRecord
from .scoring import ai_hero_template_risk, cinematic_transformation, culture_gender_integrity, formula_risk, governance_priority_score, heroic_arc_integrity, review_priority


def card_id(record: HeroJourneyFilmGovernanceRecord, config: HeroJourneyFilmGovernanceConfig) -> str:
    raw = f"{config.article_slug}|{record.item}|{record.film_context}"
    return sha256(raw.encode("utf-8")).hexdigest()[:16]


def governance_note(record: HeroJourneyFilmGovernanceRecord, config: HeroJourneyFilmGovernanceConfig) -> str:
    priority = review_priority(record, config)
    notes: list[str] = []
    if priority == "high":
        notes.append("High-priority hero’s journey governance review required.")
    elif priority == "medium":
        notes.append("Medium-priority review recommended before reuse.")
    else:
        notes.append("Standard editorial review sufficient.")
    if heroic_arc_integrity(record) < 0.65:
        notes.append("Heroic arc integrity is limited. Strengthen call authenticity, threshold significance, ordeal relevance, value change, return boon, and ethical consequence.")
    if formula_risk(record) >= 0.55:
        notes.append("Formula risk is elevated. Review beat compliance, generic mentor use, mechanical call, spectacle ordeal, forced return, and weak story particularity.")
    if cinematic_transformation(record) < 0.65:
        notes.append("Cinematic transformation is limited. Strengthen visual motif, sound design, editing rhythm, performance shift, blocking, and mise-en-scene.")
    if culture_gender_integrity(record) < 0.65:
        notes.append("Culture/gender integrity is limited. Review collective agency, cultural specificity, gender complexity, and non-heroic alternatives.")
    if ai_hero_template_risk(record) >= 0.55:
        notes.append("AI hero-template risk is elevated. Review stage compliance, cultural loss, genre cliché, universalist pressure, trope recycling, and human review.")
    if record.notes:
        notes.append(record.notes)
    return " ".join(notes)


def build_hero_journey_film_governance_card(record: HeroJourneyFilmGovernanceRecord, config: HeroJourneyFilmGovernanceConfig) -> dict[str, Any]:
    return {
        "schema_version": "1.0.0",
        "card_id": card_id(record, config),
        "card_type": "hero_journey_film_governance",
        "article_title": config.article_title,
        "article_slug": config.article_slug,
        "item": record.item,
        "film_context": record.film_context,
        "scores": {
            "heroic_arc_integrity": round(heroic_arc_integrity(record), 4),
            "formula_risk": round(formula_risk(record), 4),
            "cinematic_transformation": round(cinematic_transformation(record), 4),
            "culture_gender_integrity": round(culture_gender_integrity(record), 4),
            "ai_hero_template_risk": round(ai_hero_template_risk(record), 4),
            "governance_priority_score": round(governance_priority_score(record, config), 4),
        },
        "review": {
            "priority": review_priority(record, config),
            "owner": record.owner,
            "status": record.status,
            "governance_note": governance_note(record, config),
        },
    }
