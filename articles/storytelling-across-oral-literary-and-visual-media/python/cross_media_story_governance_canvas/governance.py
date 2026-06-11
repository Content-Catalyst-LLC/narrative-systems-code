from __future__ import annotations

from hashlib import sha256
from typing import Any

from .models import CrossMediaStoryGovernanceConfig, CrossMediaStoryGovernanceRecord
from .scoring import ai_cross_media_risk, consent_and_context_strength, governance_priority_score, media_transfer_risk, medium_affordance_fit, multimodal_coherence, review_priority


def card_id(record: CrossMediaStoryGovernanceRecord, config: CrossMediaStoryGovernanceConfig) -> str:
    raw = f"{config.article_slug}|{record.item}|{record.transfer_context}"
    return sha256(raw.encode("utf-8")).hexdigest()[:16]


def governance_note(record: CrossMediaStoryGovernanceRecord, config: CrossMediaStoryGovernanceConfig) -> str:
    priority = review_priority(record, config)
    notes: list[str] = []
    if priority == "high":
        notes.append("High-priority cross-media story governance review required.")
    elif priority == "medium":
        notes.append("Medium-priority review recommended before reuse.")
    else:
        notes.append("Standard editorial review sufficient.")
    if medium_affordance_fit(record) < 0.65:
        notes.append("Medium affordance fit is limited. Check whether this medium supports embodiment, interiority, spatial relation, temporal control, audience relation, and context.")
    if media_transfer_risk(record) >= 0.55:
        notes.append("Media-transfer risk is elevated. Review voice loss, context loss, provenance loss, audience shift, representational distortion, and governance review.")
    if multimodal_coherence(record) < 0.65:
        notes.append("Multimodal coherence is limited. Strengthen text-image integration, sequence logic, sound alignment, rhythm, provenance, and uncertainty notation.")
    if consent_and_context_strength(record) < 0.65:
        notes.append("Consent and context strength is limited. Review authorization, source authority, cultural context, reuse boundaries, provenance, and governance.")
    if ai_cross_media_risk(record) >= 0.55:
        notes.append("AI cross-media risk is elevated. Review synthetic-documentary ambiguity, provenance opacity, voice or likeness imitation, bias reproduction, and human review.")
    if record.notes:
        notes.append(record.notes)
    return " ".join(notes)


def build_cross_media_story_governance_card(record: CrossMediaStoryGovernanceRecord, config: CrossMediaStoryGovernanceConfig) -> dict[str, Any]:
    return {
        "schema_version": "1.0.0",
        "card_id": card_id(record, config),
        "card_type": "cross_media_story_governance",
        "article_title": config.article_title,
        "article_slug": config.article_slug,
        "item": record.item,
        "transfer_context": record.transfer_context,
        "scores": {
            "medium_affordance_fit": round(medium_affordance_fit(record), 4),
            "media_transfer_risk": round(media_transfer_risk(record), 4),
            "multimodal_coherence": round(multimodal_coherence(record), 4),
            "consent_and_context_strength": round(consent_and_context_strength(record), 4),
            "ai_cross_media_risk": round(ai_cross_media_risk(record), 4),
            "governance_priority_score": round(governance_priority_score(record, config), 4),
        },
        "review": {
            "priority": review_priority(record, config),
            "owner": record.owner,
            "status": record.status,
            "governance_note": governance_note(record, config),
        },
    }
