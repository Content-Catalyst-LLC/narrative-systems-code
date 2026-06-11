from __future__ import annotations

from hashlib import sha256
from typing import Any

from .models import NonHeroicNarrativeConfig, NonHeroicNarrativeRecord
from .scoring import cyclical_structure, governance_priority_score, heroic_overfit_risk, non_heroic_agency, review_priority, review_readiness, tragic_structure


def card_id(record: NonHeroicNarrativeRecord, config: NonHeroicNarrativeConfig) -> str:
    raw = f"{config.article_slug}|{record.item}|{record.claim_context}"
    return sha256(raw.encode("utf-8")).hexdigest()[:16]


def governance_note(record: NonHeroicNarrativeRecord, config: NonHeroicNarrativeConfig) -> str:
    priority = review_priority(record, config)
    notes: list[str] = []
    if priority == "high":
        notes.append("High-priority non-heroic narrative governance review required.")
    elif priority == "medium":
        notes.append("Medium-priority review recommended before reuse.")
    else:
        notes.append("Standard editorial review sufficient.")
    if heroic_overfit_risk(record) >= 0.55:
        notes.append("Heroic-overfit risk is elevated. Review hero forcing, victory pressure, closure pressure, return pressure, growth pressure, and evidence visibility.")
    if non_heroic_agency(record) >= 0.65:
        notes.append("Non-heroic agency is strong. Preserve care, endurance, witness, refusal, maintenance, and survival as narrative action.")
    if cyclical_structure(record) >= 0.65:
        notes.append("Cyclical structure is strong. Preserve recurrence, ritual, generational, institutional, ecological, and variation patterns.")
    if tragic_structure(record) >= 0.65:
        notes.append("Tragic structure is strong. Preserve consequence, limit, reversal, recognition, irreversibility, and witness burden.")
    if review_readiness(record) < 0.65:
        notes.append("Review readiness is limited. Strengthen source context, method limits, uncertainty notes, evidence visibility, and review ownership.")
    if record.notes:
        notes.append(record.notes)
    return " ".join(notes)


def build_non_heroic_narrative_card(record: NonHeroicNarrativeRecord, config: NonHeroicNarrativeConfig) -> dict[str, Any]:
    return {
        "schema_version": "1.0.0",
        "card_id": card_id(record, config),
        "card_type": "tragedy_cyclical_non_heroic_narrative",
        "article_title": config.article_title,
        "article_slug": config.article_slug,
        "item": record.item,
        "claim_context": record.claim_context,
        "scores": {
            "tragic_structure": round(tragic_structure(record), 4),
            "cyclical_structure": round(cyclical_structure(record), 4),
            "non_heroic_agency": round(non_heroic_agency(record), 4),
            "heroic_overfit_risk": round(heroic_overfit_risk(record), 4),
            "review_readiness": round(review_readiness(record), 4),
            "governance_priority_score": round(governance_priority_score(record, config), 4),
        },
        "review": {
            "priority": review_priority(record, config),
            "owner": record.owner,
            "status": record.status,
            "governance_note": governance_note(record, config),
        },
    }
