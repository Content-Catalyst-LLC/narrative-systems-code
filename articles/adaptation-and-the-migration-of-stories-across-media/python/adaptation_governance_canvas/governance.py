from __future__ import annotations

from hashlib import sha256
from typing import Any

from .models import AdaptationGovernanceConfig, AdaptationGovernanceRecord
from .scoring import adaptation_integrity, ai_adaptation_risk, consent_and_context_strength, franchise_drift, governance_priority_score, review_priority, transfer_loss


def card_id(record: AdaptationGovernanceRecord, config: AdaptationGovernanceConfig) -> str:
    raw = f"{config.article_slug}|{record.item}|{record.adaptation_context}"
    return sha256(raw.encode("utf-8")).hexdigest()[:16]


def governance_note(record: AdaptationGovernanceRecord, config: AdaptationGovernanceConfig) -> str:
    priority = review_priority(record, config)
    notes: list[str] = []
    if priority == "high":
        notes.append("High-priority adaptation governance review required.")
    elif priority == "medium":
        notes.append("Medium-priority adaptation review recommended before reuse.")
    else:
        notes.append("Standard editorial review sufficient.")
    if adaptation_integrity(record) < 0.65:
        notes.append("Adaptation integrity is limited. Strengthen source-core preservation, medium fit, transformation purpose, context preservation, reception value, and ethical governance.")
    if transfer_loss(record) >= 0.55:
        notes.append("Transfer loss is elevated. Review voice loss, interiority loss, context loss, provenance loss, agency loss, and governance review.")
    if franchise_drift(record) >= 0.55:
        notes.append("Franchise drift is elevated. Review repetition, lore excess, nostalgia reliance, continuity saturation, market overextension, and weak story purpose.")
    if ai_adaptation_risk(record) >= 0.55:
        notes.append("AI adaptation risk is elevated. Review plot-summary dependence, voice/style imitation, context loss, synthetic opacity, uncertainty erasure, and human review.")
    if consent_and_context_strength(record) < 0.65:
        notes.append("Consent/context strength is limited. Review authorization, source authority, cultural context, provenance, and governance.")
    if record.notes:
        notes.append(record.notes)
    return " ".join(notes)


def build_adaptation_governance_card(record: AdaptationGovernanceRecord, config: AdaptationGovernanceConfig) -> dict[str, Any]:
    return {
        "schema_version": "1.0.0",
        "card_id": card_id(record, config),
        "card_type": "adaptation_governance",
        "article_title": config.article_title,
        "article_slug": config.article_slug,
        "item": record.item,
        "adaptation_context": record.adaptation_context,
        "scores": {
            "adaptation_integrity": round(adaptation_integrity(record), 4),
            "transfer_loss": round(transfer_loss(record), 4),
            "franchise_drift": round(franchise_drift(record), 4),
            "ai_adaptation_risk": round(ai_adaptation_risk(record), 4),
            "consent_and_context_strength": round(consent_and_context_strength(record), 4),
            "governance_priority_score": round(governance_priority_score(record, config), 4),
        },
        "review": {
            "priority": review_priority(record, config),
            "owner": record.owner,
            "status": record.status,
            "governance_note": governance_note(record, config),
        },
    }
