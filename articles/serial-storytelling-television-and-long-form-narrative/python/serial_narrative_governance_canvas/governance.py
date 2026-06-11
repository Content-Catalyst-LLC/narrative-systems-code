from __future__ import annotations

from hashlib import sha256
from typing import Any

from .models import SerialNarrativeGovernanceConfig, SerialNarrativeGovernanceRecord
from .scoring import ai_serial_risk, continuity_burden, ensemble_and_ethics_strength, governance_priority_score, payoff_integrity, review_priority, season_coherence


def card_id(record: SerialNarrativeGovernanceRecord, config: SerialNarrativeGovernanceConfig) -> str:
    raw = f"{config.article_slug}|{record.item}|{record.serial_context}"
    return sha256(raw.encode("utf-8")).hexdigest()[:16]


def governance_note(record: SerialNarrativeGovernanceRecord, config: SerialNarrativeGovernanceConfig) -> str:
    priority = review_priority(record, config)
    notes: list[str] = []
    if priority == "high":
        notes.append("High-priority serial narrative governance review required.")
    elif priority == "medium":
        notes.append("Medium-priority serial narrative review recommended.")
    else:
        notes.append("Standard editorial review sufficient.")
    if season_coherence(record) < 0.65:
        notes.append("Season coherence is limited. Strengthen episode function, arc progression, thematic development, character memory, payoff integrity, and finale consequence.")
    if continuity_burden(record) >= 0.55:
        notes.append("Continuity burden is elevated. Review unresolved arcs, lore density, memory expectation, recap uncertainty, continuity saturation, and audience accessibility.")
    if payoff_integrity(record) < 0.65:
        notes.append("Payoff integrity is limited. Strengthen foreshadowing support, character relevance, emotional payoff, mystery logic, retrospective coherence, and thematic alignment.")
    if ensemble_and_ethics_strength(record) < 0.65:
        notes.append("Ensemble/ethics strength is limited. Review character distribution, representation, trauma care, audience trust, memory, and finale consequence.")
    if ai_serial_risk(record) >= 0.55:
        notes.append("AI serial risk is elevated. Review generic plotting, continuity fabrication, memory erasure, payoff simplification, franchise overextension, and human review.")
    if record.notes:
        notes.append(record.notes)
    return " ".join(notes)


def build_serial_narrative_governance_card(record: SerialNarrativeGovernanceRecord, config: SerialNarrativeGovernanceConfig) -> dict[str, Any]:
    return {
        "schema_version": "1.0.0",
        "card_id": card_id(record, config),
        "card_type": "serial_narrative_governance",
        "article_title": config.article_title,
        "article_slug": config.article_slug,
        "item": record.item,
        "serial_context": record.serial_context,
        "scores": {
            "season_coherence": round(season_coherence(record), 4),
            "continuity_burden": round(continuity_burden(record), 4),
            "payoff_integrity": round(payoff_integrity(record), 4),
            "ensemble_and_ethics_strength": round(ensemble_and_ethics_strength(record), 4),
            "ai_serial_risk": round(ai_serial_risk(record), 4),
            "governance_priority_score": round(governance_priority_score(record, config), 4),
        },
        "review": {
            "priority": review_priority(record, config),
            "owner": record.owner,
            "status": record.status,
            "governance_note": governance_note(record, config),
        },
    }
