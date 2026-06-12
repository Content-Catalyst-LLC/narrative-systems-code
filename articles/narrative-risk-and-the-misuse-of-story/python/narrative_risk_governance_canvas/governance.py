from __future__ import annotations

from hashlib import sha256
from typing import Any

from .models import NarrativeRiskGovernanceConfig, NarrativeRiskGovernanceRecord
from .scoring import ai_narrative_risk, evidence_integrity, governance_priority_score, narrative_risk, platform_amplification_risk, review_priority, trust_repair_priority


def card_id(record: NarrativeRiskGovernanceRecord, config: NarrativeRiskGovernanceConfig) -> str:
    raw = f"{config.article_slug}|{record.item}|{record.narrative_context}"
    return sha256(raw.encode("utf-8")).hexdigest()[:16]


def governance_note(record: NarrativeRiskGovernanceRecord, config: NarrativeRiskGovernanceConfig) -> str:
    priority = review_priority(record, config)
    notes: list[str] = []
    if priority == "high":
        notes.append("High-priority narrative risk governance review required.")
    elif priority == "medium":
        notes.append("Medium-priority narrative risk review recommended.")
    else:
        notes.append("Standard editorial review sufficient.")
    if narrative_risk(record) >= 0.55:
        notes.append("Narrative risk is elevated. Review scapegoating, evidence immunity, mythic simplification, context loss, group-blame intensity, and revision openness.")
    if evidence_integrity(record) < 0.65:
        notes.append("Evidence integrity is limited. Strengthen corroboration, source quality, timeline clarity, uncertainty disclosure, accountability clarity, and disconfirmation openness.")
    if trust_repair_priority(record) >= 0.55:
        notes.append("Trust-repair priority is elevated. Review institutional failure, opacity, historical distrust, public consequence, correction difficulty, and affected-listener stakes.")
    if platform_amplification_risk(record) >= 0.55:
        notes.append("Platform amplification risk is elevated. Review speed, repetition, social proof, monetization, and context loss.")
    if ai_narrative_risk(record) >= 0.55:
        notes.append("AI narrative risk is elevated. Review synthetic evidence, provenance opacity, fabricated patterning, automated consensus, vulnerability targeting, and human review.")
    if record.notes:
        notes.append(record.notes)
    return " ".join(notes)


def build_narrative_risk_governance_card(record: NarrativeRiskGovernanceRecord, config: NarrativeRiskGovernanceConfig) -> dict[str, Any]:
    return {
        "schema_version": "1.0.0",
        "card_id": card_id(record, config),
        "card_type": "narrative_risk_governance",
        "article_title": config.article_title,
        "article_slug": config.article_slug,
        "item": record.item,
        "narrative_context": record.narrative_context,
        "scores": {
            "narrative_risk": round(narrative_risk(record), 4),
            "evidence_integrity": round(evidence_integrity(record), 4),
            "trust_repair_priority": round(trust_repair_priority(record), 4),
            "platform_amplification_risk": round(platform_amplification_risk(record), 4),
            "ai_narrative_risk": round(ai_narrative_risk(record), 4),
            "governance_priority_score": round(governance_priority_score(record, config), 4),
        },
        "review": {
            "priority": review_priority(record, config),
            "owner": record.owner,
            "status": record.status,
            "governance_note": governance_note(record, config),
        },
    }
