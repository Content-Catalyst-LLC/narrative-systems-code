from __future__ import annotations

from hashlib import sha256
from typing import Any

from .models import OrganizationalStoryGovernanceConfig, OrganizationalStoryGovernanceRecord
from .scoring import ai_organizational_story_risk, change_credibility, employee_voice_integrity, governance_priority_score, narrative_extraction_risk, organizational_memory_strength, purpose_alignment, review_priority


def card_id(record: OrganizationalStoryGovernanceRecord, config: OrganizationalStoryGovernanceConfig) -> str:
    raw = f"{config.article_slug}|{record.item}|{record.claim_context}"
    return sha256(raw.encode("utf-8")).hexdigest()[:16]


def governance_note(record: OrganizationalStoryGovernanceRecord, config: OrganizationalStoryGovernanceConfig) -> str:
    priority = review_priority(record, config)
    notes: list[str] = []
    if priority == "high":
        notes.append("High-priority organizational-story governance review required.")
    elif priority == "medium":
        notes.append("Medium-priority review recommended before reuse.")
    else:
        notes.append("Standard editorial review sufficient.")
    if purpose_alignment(record) < 0.65:
        notes.append("Purpose alignment is limited. Compare mission language with decisions, budgets, stakeholder impact, employee experience, and governance transparency.")
    if change_credibility(record) < 0.65:
        notes.append("Change credibility is limited. Strengthen evidence visibility, participation integrity, resource support, loss acknowledgment, feedback loops, and accountability measures.")
    if narrative_extraction_risk(record) >= 0.55:
        notes.append("Narrative-extraction risk is elevated. Review consent, selection bias, power asymmetry, emotional targeting, brand repurposing, and agency.")
    if employee_voice_integrity(record) < 0.65:
        notes.append("Employee voice integrity is limited. Strengthen protection, dissent visibility, learning follow-through, and governance transparency.")
    if organizational_memory_strength(record) < 0.65:
        notes.append("Organizational memory is limited. Strengthen preservation, retrospectives, dissent capture, and accountability measures.")
    if ai_organizational_story_risk(record) >= 0.55:
        notes.append("AI organizational story risk is elevated. Review summary dependence, omitted dissent, context loss, privacy risk, uncertainty erasure, and human review.")
    if record.notes:
        notes.append(record.notes)
    return " ".join(notes)


def build_organizational_story_governance_card(record: OrganizationalStoryGovernanceRecord, config: OrganizationalStoryGovernanceConfig) -> dict[str, Any]:
    return {
        "schema_version": "1.0.0",
        "card_id": card_id(record, config),
        "card_type": "organizational_story_governance",
        "article_title": config.article_title,
        "article_slug": config.article_slug,
        "item": record.item,
        "claim_context": record.claim_context,
        "scores": {
            "purpose_alignment": round(purpose_alignment(record), 4),
            "change_credibility": round(change_credibility(record), 4),
            "narrative_extraction_risk": round(narrative_extraction_risk(record), 4),
            "employee_voice_integrity": round(employee_voice_integrity(record), 4),
            "organizational_memory_strength": round(organizational_memory_strength(record), 4),
            "ai_organizational_story_risk": round(ai_organizational_story_risk(record), 4),
            "governance_priority_score": round(governance_priority_score(record, config), 4),
        },
        "review": {
            "priority": review_priority(record, config),
            "owner": record.owner,
            "status": record.status,
            "governance_note": governance_note(record, config),
        },
    }
