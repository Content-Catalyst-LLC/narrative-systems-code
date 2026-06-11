from __future__ import annotations

from hashlib import sha256
from typing import Any

from .models import LifeWritingConfig, LifeWritingRecord
from .scoring import ethical_risk, governance_priority_score, interpretation_readiness, life_writing_coherence, review_priority, truth_practice


def card_id(record: LifeWritingRecord, config: LifeWritingConfig) -> str:
    raw = f"{config.article_slug}|{record.item}|{record.claim_context}"
    return sha256(raw.encode("utf-8")).hexdigest()[:16]


def governance_note(record: LifeWritingRecord, config: LifeWritingConfig) -> str:
    priority = review_priority(record, config)
    notes: list[str] = []
    if priority == "high":
        notes.append("High-priority life-writing governance review required.")
    elif priority == "medium":
        notes.append("Medium-priority review recommended before reuse.")
    else:
        notes.append("Standard editorial review sufficient.")
    if ethical_risk(record) >= 0.55:
        notes.append("Life-writing ethical risk is elevated; review privacy, consent, other-person exposure, trauma extraction, and self-mythology.")
    if truth_practice(record) < 0.65:
        notes.append("Truth-practice signals are limited; strengthen fact checking, memory framing, evidence visibility, interpretation distinction, uncertainty notes, and archive review.")
    if interpretation_readiness(record) < 0.60:
        notes.append("Interpretation readiness is limited; strengthen source context, cultural context, evidence visibility, uncertainty notes, method limits, and review owner clarity.")
    if record.notes:
        notes.append(record.notes)
    return " ".join(notes)


def build_life_writing_card(record: LifeWritingRecord, config: LifeWritingConfig) -> dict[str, Any]:
    return {
        "schema_version": "1.0.0",
        "card_id": card_id(record, config),
        "card_type": "autobiography_memoir_life_writing",
        "article_title": config.article_title,
        "article_slug": config.article_slug,
        "item": record.item,
        "claim_context": record.claim_context,
        "scores": {
            "life_writing_coherence": round(life_writing_coherence(record), 4),
            "truth_practice": round(truth_practice(record), 4),
            "ethical_risk": round(ethical_risk(record), 4),
            "interpretation_readiness": round(interpretation_readiness(record), 4),
            "governance_priority_score": round(governance_priority_score(record, config), 4),
        },
        "review": {
            "priority": review_priority(record, config),
            "owner": record.owner,
            "status": record.status,
            "governance_note": governance_note(record, config),
        },
    }
