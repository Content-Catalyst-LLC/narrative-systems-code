from __future__ import annotations

from hashlib import sha256
from typing import Any

from .models import RhetoricalMovesGovernanceConfig, RhetoricalMovesGovernanceRecord
from .scoring import ai_persuasion_risk, audience_agency_score, governance_priority_score, manipulation_risk, platform_persuasion_risk, rhetorical_integrity, review_priority


def card_id(record: RhetoricalMovesGovernanceRecord, config: RhetoricalMovesGovernanceConfig) -> str:
    raw = f"{config.article_slug}|{record.item}|{record.persuasion_context}"
    return sha256(raw.encode("utf-8")).hexdigest()[:16]


def governance_note(record: RhetoricalMovesGovernanceRecord, config: RhetoricalMovesGovernanceConfig) -> str:
    priority = review_priority(record, config)
    notes: list[str] = []
    if priority == "high":
        notes.append("High-priority persuasive story governance review required.")
    elif priority == "medium":
        notes.append("Medium-priority rhetorical ethics review recommended.")
    else:
        notes.append("Standard editorial review sufficient.")
    if rhetorical_integrity(record) < 0.65:
        notes.append("Rhetorical integrity is limited. Strengthen evidence, proportionality, context, dignity, agency, and transparency.")
    if manipulation_risk(record) >= 0.55:
        notes.append("Manipulation risk is elevated. Review fear, emotional exploitation, context omission, social proof, urgency, and judgment review.")
    if audience_agency_score(record) < 0.65:
        notes.append("Audience agency is limited. Improve claim clarity, uncertainty disclosure, tradeoff openness, evidence visibility, optionality, and question space.")
    if platform_persuasion_risk(record) >= 0.55:
        notes.append("Platform persuasion risk is elevated. Review amplification, microtargeting, context collapse, sponsorship clarity, and social proof.")
    if ai_persuasion_risk(record) >= 0.55:
        notes.append("AI persuasion risk is elevated. Review targeting, vulnerability exploitation, synthetic evidence, opaque testing, data opacity, and human review.")
    if record.notes:
        notes.append(record.notes)
    return " ".join(notes)


def build_rhetorical_moves_governance_card(record: RhetoricalMovesGovernanceRecord, config: RhetoricalMovesGovernanceConfig) -> dict[str, Any]:
    return {
        "schema_version": "1.0.0",
        "card_id": card_id(record, config),
        "card_type": "rhetorical_moves_governance",
        "article_title": config.article_title,
        "article_slug": config.article_slug,
        "item": record.item,
        "persuasion_context": record.persuasion_context,
        "scores": {
            "rhetorical_integrity": round(rhetorical_integrity(record), 4),
            "manipulation_risk": round(manipulation_risk(record), 4),
            "audience_agency_score": round(audience_agency_score(record), 4),
            "platform_persuasion_risk": round(platform_persuasion_risk(record), 4),
            "ai_persuasion_risk": round(ai_persuasion_risk(record), 4),
            "governance_priority_score": round(governance_priority_score(record, config), 4),
        },
        "review": {
            "priority": review_priority(record, config),
            "owner": record.owner,
            "status": record.status,
            "governance_note": governance_note(record, config),
        },
    }
