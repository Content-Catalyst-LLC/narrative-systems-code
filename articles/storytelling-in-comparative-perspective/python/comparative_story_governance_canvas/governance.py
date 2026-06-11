from __future__ import annotations

from hashlib import sha256
from typing import Any

from .models import ComparativeStoryGovernanceConfig, ComparativeStoryGovernanceRecord
from .scoring import ai_comparative_risk, comparative_integrity, contextual_grounding, flattening_risk, governance_priority_score, review_priority, transmission_uncertainty


def card_id(record: ComparativeStoryGovernanceRecord, config: ComparativeStoryGovernanceConfig) -> str:
    raw = f"{config.article_slug}|{record.item}|{record.comparison_context}"
    return sha256(raw.encode("utf-8")).hexdigest()[:16]


def governance_note(record: ComparativeStoryGovernanceRecord, config: ComparativeStoryGovernanceConfig) -> str:
    priority = review_priority(record, config)
    notes: list[str] = []
    if priority == "high":
        notes.append("High-priority comparative story governance review required.")
    elif priority == "medium":
        notes.append("Medium-priority comparative narrative review recommended.")
    else:
        notes.append("Standard editorial review sufficient.")
    if comparative_integrity(record) < 0.65:
        notes.append("Comparative integrity is limited. Strengthen source context, difference preservation, evidence, translation reliability, protocol compliance, and human review.")
    if flattening_risk(record) >= 0.55:
        notes.append("Flattening risk is elevated. Review universalism claims, template capture, context loss, archive bias, power imbalance, and difference preservation.")
    if transmission_uncertainty(record) >= 0.55:
        notes.append("Transmission uncertainty is elevated. Review language gap, media shift, archive gap, performance loss, restricted-source concern, and version documentation.")
    if contextual_grounding(record) < 0.65:
        notes.append("Contextual grounding is limited. Review local interpretation, community review, attribution, corpus balance, source context, and protocol compliance.")
    if ai_comparative_risk(record) >= 0.55:
        notes.append("AI comparative risk is elevated. Review corpus bias, hallucinated sources, translation loss, sacred-material risk, overgeneralized claims, and expert review.")
    if record.notes:
        notes.append(record.notes)
    return " ".join(notes)


def build_comparative_story_governance_card(record: ComparativeStoryGovernanceRecord, config: ComparativeStoryGovernanceConfig) -> dict[str, Any]:
    return {
        "schema_version": "1.0.0",
        "card_id": card_id(record, config),
        "card_type": "comparative_story_governance",
        "article_title": config.article_title,
        "article_slug": config.article_slug,
        "item": record.item,
        "comparison_context": record.comparison_context,
        "scores": {
            "comparative_integrity": round(comparative_integrity(record), 4),
            "flattening_risk": round(flattening_risk(record), 4),
            "transmission_uncertainty": round(transmission_uncertainty(record), 4),
            "contextual_grounding": round(contextual_grounding(record), 4),
            "ai_comparative_risk": round(ai_comparative_risk(record), 4),
            "governance_priority_score": round(governance_priority_score(record, config), 4),
        },
        "review": {
            "priority": review_priority(record, config),
            "owner": record.owner,
            "status": record.status,
            "governance_note": governance_note(record, config),
        },
    }
