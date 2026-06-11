from __future__ import annotations

from hashlib import sha256
from typing import Any

from .models import InteractiveNarrativeGovernanceConfig, InteractiveNarrativeGovernanceRecord
from .scoring import agency_integrity, ai_interactive_narrative_risk, branching_burden, failure_and_identity_strength, governance_priority_score, review_priority, system_story_alignment


def card_id(record: InteractiveNarrativeGovernanceRecord, config: InteractiveNarrativeGovernanceConfig) -> str:
    raw = f"{config.article_slug}|{record.item}|{record.game_context}"
    return sha256(raw.encode("utf-8")).hexdigest()[:16]


def governance_note(record: InteractiveNarrativeGovernanceRecord, config: InteractiveNarrativeGovernanceConfig) -> str:
    priority = review_priority(record, config)
    notes: list[str] = []
    if priority == "high":
        notes.append("High-priority interactive narrative governance review required.")
    elif priority == "medium":
        notes.append("Medium-priority interactive narrative review recommended.")
    else:
        notes.append("Standard editorial review sufficient.")
    if agency_integrity(record) < 0.65:
        notes.append("Agency integrity is limited. Strengthen choice meaningfulness, system response, feedback clarity, role variation, world memory, and ethical governance.")
    if branching_burden(record) >= 0.55:
        notes.append("Branching burden is elevated. Review branch pressure, state dependency, consequence tracking, testing load, localization cost, and recombination coherence.")
    if system_story_alignment(record) < 0.65:
        notes.append("System-story alignment is limited. Review mechanics, rules, goals, progression, interface, and consequence consistency.")
    if failure_and_identity_strength(record) < 0.65:
        notes.append("Failure/identity strength is limited. Review failure meaning, replay value, consent, identity care, feedback, and ethical governance.")
    if ai_interactive_narrative_risk(record) >= 0.55:
        notes.append("AI interactive-narrative risk is elevated. Review generic quests, character-memory failure, opaque response, player manipulation, stereotype risk, and human review.")
    if record.notes:
        notes.append(record.notes)
    return " ".join(notes)


def build_interactive_narrative_governance_card(record: InteractiveNarrativeGovernanceRecord, config: InteractiveNarrativeGovernanceConfig) -> dict[str, Any]:
    return {
        "schema_version": "1.0.0",
        "card_id": card_id(record, config),
        "card_type": "interactive_narrative_governance",
        "article_title": config.article_title,
        "article_slug": config.article_slug,
        "item": record.item,
        "game_context": record.game_context,
        "scores": {
            "agency_integrity": round(agency_integrity(record), 4),
            "branching_burden": round(branching_burden(record), 4),
            "system_story_alignment": round(system_story_alignment(record), 4),
            "failure_and_identity_strength": round(failure_and_identity_strength(record), 4),
            "ai_interactive_narrative_risk": round(ai_interactive_narrative_risk(record), 4),
            "governance_priority_score": round(governance_priority_score(record, config), 4),
        },
        "review": {
            "priority": review_priority(record, config),
            "owner": record.owner,
            "status": record.status,
            "governance_note": governance_note(record, config),
        },
    }
