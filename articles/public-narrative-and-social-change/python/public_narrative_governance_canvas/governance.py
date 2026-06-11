from __future__ import annotations

from hashlib import sha256
from typing import Any

from .models import PublicNarrativeGovernanceConfig, PublicNarrativeGovernanceRecord
from .scoring import ai_public_narrative_risk, governance_priority_score, mobilization_readiness, public_narrative_coherence, public_voice_integrity, review_priority, testimony_extraction_risk


def card_id(record: PublicNarrativeGovernanceRecord, config: PublicNarrativeGovernanceConfig) -> str:
    raw = f"{config.article_slug}|{record.item}|{record.claim_context}"
    return sha256(raw.encode("utf-8")).hexdigest()[:16]


def governance_note(record: PublicNarrativeGovernanceRecord, config: PublicNarrativeGovernanceConfig) -> str:
    priority = review_priority(record, config)
    notes: list[str] = []
    if priority == "high":
        notes.append("High-priority public narrative governance review required.")
    elif priority == "medium":
        notes.append("Medium-priority review recommended before reuse.")
    else:
        notes.append("Standard editorial review sufficient.")
    if public_narrative_coherence(record) < 0.65:
        notes.append("Public narrative coherence is limited. Strengthen self, us, now, values, action clarity, and governance review.")
    if mobilization_readiness(record) < 0.65:
        notes.append("Mobilization readiness is limited. Strengthen diagnosis, solution, resource support, coalition openness, tactical action, and feedback loops.")
    if testimony_extraction_risk(record) >= 0.55:
        notes.append("Testimony-extraction risk is elevated. Review consent, emotional targeting, safety risk, reuse uncertainty, visibility risk, and agency.")
    if public_voice_integrity(record) < 0.65:
        notes.append("Public voice integrity is limited. Strengthen voice plurality, affected-community authority, evidence visibility, coalition openness, digital context, and governance.")
    if ai_public_narrative_risk(record) >= 0.55:
        notes.append("AI public narrative risk is elevated. Review summary dependence, omitted voices, context loss, bias reproduction, uncertainty erasure, and human review.")
    if record.notes:
        notes.append(record.notes)
    return " ".join(notes)


def build_public_narrative_governance_card(record: PublicNarrativeGovernanceRecord, config: PublicNarrativeGovernanceConfig) -> dict[str, Any]:
    return {
        "schema_version": "1.0.0",
        "card_id": card_id(record, config),
        "card_type": "public_narrative_governance",
        "article_title": config.article_title,
        "article_slug": config.article_slug,
        "item": record.item,
        "claim_context": record.claim_context,
        "scores": {
            "public_narrative_coherence": round(public_narrative_coherence(record), 4),
            "mobilization_readiness": round(mobilization_readiness(record), 4),
            "testimony_extraction_risk": round(testimony_extraction_risk(record), 4),
            "public_voice_integrity": round(public_voice_integrity(record), 4),
            "ai_public_narrative_risk": round(ai_public_narrative_risk(record), 4),
            "governance_priority_score": round(governance_priority_score(record, config), 4),
        },
        "review": {
            "priority": review_priority(record, config),
            "owner": record.owner,
            "status": record.status,
            "governance_note": governance_note(record, config),
        },
    }
