from __future__ import annotations

from hashlib import sha256
from typing import Any

from .models import IndigenousStoryGovernanceConfig, IndigenousStoryGovernanceRecord
from .scoring import digital_sovereignty_risk, governance_priority_score, place_memory_strength, protocol_risk, relational_accountability, review_priority, translation_governance


def card_id(record: IndigenousStoryGovernanceRecord, config: IndigenousStoryGovernanceConfig) -> str:
    raw = f"{config.article_slug}|{record.item}|{record.claim_context}"
    return sha256(raw.encode("utf-8")).hexdigest()[:16]


def governance_note(record: IndigenousStoryGovernanceRecord, config: IndigenousStoryGovernanceConfig) -> str:
    priority = review_priority(record, config)
    notes: list[str] = []
    if priority == "high":
        notes.append("High-priority Indigenous story governance review required.")
    elif priority == "medium":
        notes.append("Medium-priority review recommended before reuse.")
    else:
        notes.append("Standard editorial review sufficient.")
    if protocol_risk(record) >= 0.55:
        notes.append("Protocol risk is elevated. Review access pressure, seasonal restriction, ceremonial restriction, template forcing, digital exposure, and governance visibility.")
    if digital_sovereignty_risk(record) >= 0.55:
        notes.append("Digital-sovereignty risk is elevated. Review extraction risk, open-access assumptions, AI training risk, stereotype bias, metadata flattening, and community governance.")
    if relational_accountability(record) < 0.70:
        notes.append("Relational accountability is limited. Strengthen place specificity, community authority, teller relationship, listener context, obligation visibility, and governance visibility.")
    if translation_governance(record) < 0.65:
        notes.append("Translation governance is limited. Strengthen cultural specificity, language context, opacity notes, untranslated terms, reviewer visibility, and harm review.")
    if place_memory_strength(record) >= 0.70:
        notes.append("Place-memory strength is high. Preserve land naming, ecological knowledge, ancestral memory, route teaching, seasonal context, and future-generation responsibility.")
    if record.notes:
        notes.append(record.notes)
    return " ".join(notes)


def build_indigenous_story_governance_card(record: IndigenousStoryGovernanceRecord, config: IndigenousStoryGovernanceConfig) -> dict[str, Any]:
    return {
        "schema_version": "1.0.0",
        "card_id": card_id(record, config),
        "card_type": "indigenous_story_governance",
        "article_title": config.article_title,
        "article_slug": config.article_slug,
        "item": record.item,
        "claim_context": record.claim_context,
        "scores": {
            "relational_accountability": round(relational_accountability(record), 4),
            "protocol_risk": round(protocol_risk(record), 4),
            "place_memory_strength": round(place_memory_strength(record), 4),
            "translation_governance": round(translation_governance(record), 4),
            "digital_sovereignty_risk": round(digital_sovereignty_risk(record), 4),
            "governance_priority_score": round(governance_priority_score(record, config), 4),
        },
        "review": {
            "priority": review_priority(record, config),
            "owner": record.owner,
            "status": record.status,
            "governance_note": governance_note(record, config),
        },
    }
