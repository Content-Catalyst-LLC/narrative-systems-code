from __future__ import annotations

from hashlib import sha256
from typing import Any

from .models import PublicStoryGovernanceConfig, PublicStoryGovernanceRecord
from .scoring import ai_public_rhetoric_risk, civil_religion_accountability, governance_priority_score, mythic_simplification_risk, public_narrative_strength, review_priority, testimony_ethics


def card_id(record: PublicStoryGovernanceRecord, config: PublicStoryGovernanceConfig) -> str:
    raw = f"{config.article_slug}|{record.item}|{record.claim_context}"
    return sha256(raw.encode("utf-8")).hexdigest()[:16]


def governance_note(record: PublicStoryGovernanceRecord, config: PublicStoryGovernanceConfig) -> str:
    priority = review_priority(record, config)
    notes: list[str] = []
    if priority == "high":
        notes.append("High-priority public-story governance review required.")
    elif priority == "medium":
        notes.append("Medium-priority review recommended before reuse.")
    else:
        notes.append("Standard editorial review sufficient.")
    if mythic_simplification_risk(record) >= 0.55:
        notes.append("Mythic-simplification risk is elevated. Review enemy simplification, boundary hardening, crisis compression, urgency pressure, scapegoating, and evidence visibility.")
    if ai_public_rhetoric_risk(record) >= 0.55:
        notes.append("AI-public-rhetoric risk is elevated. Review formulaic defaults, outrage intensity, resolution smoothing, identity-boundary pressure, missing context, and human governance.")
    if civil_religion_accountability(record) < 0.65:
        notes.append("Civil-religion accountability is limited. Strengthen memory plurality, historical truthfulness, public limits, dissent space, repair justice, and anti-idolatry critique.")
    if testimony_ethics(record) < 0.65:
        notes.append("Testimony ethics is limited. Strengthen witness care, context, harm visibility, extraction resistance, responsibility, and repair.")
    if record.notes:
        notes.append(record.notes)
    return " ".join(notes)


def build_public_story_governance_card(record: PublicStoryGovernanceRecord, config: PublicStoryGovernanceConfig) -> dict[str, Any]:
    return {
        "schema_version": "1.0.0",
        "card_id": card_id(record, config),
        "card_type": "public_story_governance",
        "article_title": config.article_title,
        "article_slug": config.article_slug,
        "item": record.item,
        "claim_context": record.claim_context,
        "scores": {
            "public_narrative_strength": round(public_narrative_strength(record), 4),
            "mythic_simplification_risk": round(mythic_simplification_risk(record), 4),
            "civil_religion_accountability": round(civil_religion_accountability(record), 4),
            "testimony_ethics": round(testimony_ethics(record), 4),
            "ai_public_rhetoric_risk": round(ai_public_rhetoric_risk(record), 4),
            "governance_priority_score": round(governance_priority_score(record, config), 4),
        },
        "review": {
            "priority": review_priority(record, config),
            "owner": record.owner,
            "status": record.status,
            "governance_note": governance_note(record, config),
        },
    }
