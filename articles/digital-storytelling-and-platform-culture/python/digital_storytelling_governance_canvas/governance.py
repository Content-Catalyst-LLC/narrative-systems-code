from __future__ import annotations

from hashlib import sha256
from typing import Any

from .models import DigitalStorytellingGovernanceConfig, DigitalStorytellingGovernanceRecord
from .scoring import ai_synthetic_story_risk, archive_memory_strength, context_collapse_risk, governance_priority_score, platform_formula_drift, platform_narrative_integrity, review_priority


def card_id(record: DigitalStorytellingGovernanceRecord, config: DigitalStorytellingGovernanceConfig) -> str:
    raw = f"{config.article_slug}|{record.item}|{record.platform_context}"
    return sha256(raw.encode("utf-8")).hexdigest()[:16]


def governance_note(record: DigitalStorytellingGovernanceRecord, config: DigitalStorytellingGovernanceConfig) -> str:
    priority = review_priority(record, config)
    notes: list[str] = []
    if priority == "high":
        notes.append("High-priority digital storytelling governance review required.")
    elif priority == "medium":
        notes.append("Medium-priority platform narrative review recommended.")
    else:
        notes.append("Standard editorial review sufficient.")
    if platform_narrative_integrity(record) < 0.65:
        notes.append("Platform narrative integrity is limited. Strengthen context, source authority, provenance, audience care, medium fit, and ethical governance.")
    if context_collapse_risk(record) >= 0.55:
        notes.append("Context-collapse risk is elevated. Review audience spread, compression, hostile-context exposure, engagement intensity, sensitive visibility, and governance.")
    if platform_formula_drift(record) >= 0.55:
        notes.append("Platform formula drift is elevated. Review hooks, trends, metrics, retention framing, outrage signals, and judgment stability.")
    if archive_memory_strength(record) < 0.65:
        notes.append("Archive/memory strength is limited. Review metadata, consent, preservation plan, access context, source authority, and context.")
    if ai_synthetic_story_risk(record) >= 0.55:
        notes.append("AI synthetic-story risk is elevated. Review synthetic opacity, voice imitation, provenance loss, context loss, manipulation targeting, and human review.")
    if record.notes:
        notes.append(record.notes)
    return " ".join(notes)


def build_digital_storytelling_governance_card(record: DigitalStorytellingGovernanceRecord, config: DigitalStorytellingGovernanceConfig) -> dict[str, Any]:
    return {
        "schema_version": "1.0.0",
        "card_id": card_id(record, config),
        "card_type": "digital_storytelling_governance",
        "article_title": config.article_title,
        "article_slug": config.article_slug,
        "item": record.item,
        "platform_context": record.platform_context,
        "scores": {
            "platform_narrative_integrity": round(platform_narrative_integrity(record), 4),
            "context_collapse_risk": round(context_collapse_risk(record), 4),
            "platform_formula_drift": round(platform_formula_drift(record), 4),
            "archive_memory_strength": round(archive_memory_strength(record), 4),
            "ai_synthetic_story_risk": round(ai_synthetic_story_risk(record), 4),
            "governance_priority_score": round(governance_priority_score(record, config), 4),
        },
        "review": {
            "priority": review_priority(record, config),
            "owner": record.owner,
            "status": record.status,
            "governance_note": governance_note(record, config),
        },
    }
