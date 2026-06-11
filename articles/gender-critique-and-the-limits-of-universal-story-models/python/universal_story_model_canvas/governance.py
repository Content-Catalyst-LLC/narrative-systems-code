from __future__ import annotations

from hashlib import sha256
from typing import Any

from .models import UniversalStoryModelConfig, UniversalStoryModelRecord
from .scoring import alternative_structure_signal, critique_readiness, governance_priority_score, review_priority, universal_model_fit, universalism_risk


def card_id(record: UniversalStoryModelRecord, config: UniversalStoryModelConfig) -> str:
    raw = f"{config.article_slug}|{record.item}|{record.claim_context}"
    return sha256(raw.encode("utf-8")).hexdigest()[:16]


def governance_note(record: UniversalStoryModelRecord, config: UniversalStoryModelConfig) -> str:
    priority = review_priority(record, config)
    notes: list[str] = []
    if priority == "high":
        notes.append("High-priority universal-story-model governance review required.")
    elif priority == "medium":
        notes.append("Medium-priority review recommended before reuse.")
    else:
        notes.append("Standard editorial review sufficient.")
    if universalism_risk(record) >= 0.55:
        notes.append("Universalism risk is elevated. Review archive bias gender binary pressure cultural flattening intersectional erasure queer or trans narrative pressure and local context.")
    if critique_readiness(record) < 0.65:
        notes.append("Critique readiness is limited. Strengthen source context local context alternative lenses gender complexity intersectional context uncertainty notes and review ownership.")
    if alternative_structure_signal(record) >= 0.65:
        notes.append("Alternative structure signal is strong. Consider relational cyclical witness care fragmented or open-process frameworks before using a universal model.")
    if record.notes:
        notes.append(record.notes)
    return " ".join(notes)


def build_universal_story_model_card(record: UniversalStoryModelRecord, config: UniversalStoryModelConfig) -> dict[str, Any]:
    return {
        "schema_version": "1.0.0",
        "card_id": card_id(record, config),
        "card_type": "gender_critique_universal_story_model",
        "article_title": config.article_title,
        "article_slug": config.article_slug,
        "item": record.item,
        "claim_context": record.claim_context,
        "scores": {
            "universal_model_fit": round(universal_model_fit(record), 4),
            "universalism_risk": round(universalism_risk(record), 4),
            "critique_readiness": round(critique_readiness(record), 4),
            "alternative_structure_signal": round(alternative_structure_signal(record), 4),
            "governance_priority_score": round(governance_priority_score(record, config), 4),
        },
        "review": {
            "priority": review_priority(record, config),
            "owner": record.owner,
            "status": record.status,
            "governance_note": governance_note(record, config),
        },
    }
