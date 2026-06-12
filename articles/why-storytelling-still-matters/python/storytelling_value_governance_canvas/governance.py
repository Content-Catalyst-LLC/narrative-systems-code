from __future__ import annotations

from hashlib import sha256
from typing import Any

from .models import StorytellingValueGovernanceConfig, StorytellingValueGovernanceRecord
from .scoring import ai_storytelling_governance, governance_priority_score, misuse_risk, narrative_responsibility, review_priority, storytelling_value


def card_id(record: StorytellingValueGovernanceRecord, config: StorytellingValueGovernanceConfig) -> str:
    raw = f"{config.article_slug}|{record.item}|{record.story_context}"
    return sha256(raw.encode("utf-8")).hexdigest()[:16]


def governance_note(record: StorytellingValueGovernanceRecord, config: StorytellingValueGovernanceConfig) -> str:
    priority = review_priority(record, config)
    notes: list[str] = []
    if priority == "high":
        notes.append("High-priority storytelling governance review required.")
    elif priority == "medium":
        notes.append("Medium-priority storytelling value review recommended.")
    else:
        notes.append("Standard editorial review sufficient.")
    if storytelling_value(record) < 0.65:
        notes.append("Storytelling value is limited. Strengthen clarity, evidence grounding, memory continuity, audience reasoning, dignity, and public usefulness.")
    if narrative_responsibility(record) < 0.65:
        notes.append("Narrative responsibility is limited. Strengthen truthfulness, context, consent, uncertainty disclosure, revision openness, and accountability.")
    if misuse_risk(record) >= 0.55:
        notes.append("Misuse risk is elevated. Review oversimplification, emotional exploitation, scapegoating, context loss, platform frictionlessness, and human review.")
    if ai_storytelling_governance(record) < 0.65:
        notes.append("AI storytelling governance is limited. Improve provenance, source traceability, human review, consent discipline, use limits, and correction process.")
    if record.notes:
        notes.append(record.notes)
    return " ".join(notes)


def build_storytelling_value_governance_card(record: StorytellingValueGovernanceRecord, config: StorytellingValueGovernanceConfig) -> dict[str, Any]:
    return {
        "schema_version": "1.0.0",
        "card_id": card_id(record, config),
        "card_type": "storytelling_value_governance",
        "article_title": config.article_title,
        "article_slug": config.article_slug,
        "item": record.item,
        "story_context": record.story_context,
        "scores": {
            "storytelling_value": round(storytelling_value(record), 4),
            "narrative_responsibility": round(narrative_responsibility(record), 4),
            "misuse_risk": round(misuse_risk(record), 4),
            "ai_storytelling_governance": round(ai_storytelling_governance(record), 4),
            "governance_priority_score": round(governance_priority_score(record, config), 4),
        },
        "review": {
            "priority": review_priority(record, config),
            "owner": record.owner,
            "status": record.status,
            "governance_note": governance_note(record, config),
        },
    }
