from __future__ import annotations

from hashlib import sha256
from typing import Any

from .models import NarrativeSystemsGovernanceConfig, NarrativeSystemsGovernanceRecord
from .scoring import ai_story_structure_risk, formula_drift_risk, governance_priority_score, narrative_coherence, network_system_strength, responsibility_balance, review_priority


def card_id(record: NarrativeSystemsGovernanceRecord, config: NarrativeSystemsGovernanceConfig) -> str:
    raw = f"{config.article_slug}|{record.item}|{record.modeling_context}"
    return sha256(raw.encode("utf-8")).hexdigest()[:16]


def governance_note(record: NarrativeSystemsGovernanceRecord, config: NarrativeSystemsGovernanceConfig) -> str:
    priority = review_priority(record, config)
    notes: list[str] = []
    if priority == "high":
        notes.append("High-priority narrative systems governance review required.")
    elif priority == "medium":
        notes.append("Medium-priority story structure review recommended.")
    else:
        notes.append("Standard editorial review sufficient.")
    if narrative_coherence(record) < 0.65:
        notes.append("Narrative coherence is limited. Strengthen causality, state transitions, agent-goal fit, world rules, temporal mapping, and evidence.")
    if formula_drift_risk(record) >= 0.55:
        notes.append("Formula-drift risk is elevated. Review beat-template dependence, universal model claims, context loss, genre flattening, overconfidence, and judgment review.")
    if responsibility_balance(record) < 0.55:
        notes.append("Responsibility balance is weak. Review whether individual or systemic agency is being erased.")
    if network_system_strength(record) < 0.65:
        notes.append("Network/system strength is limited. Review relationships, constraints, feedback loops, agents, and world rules.")
    if ai_story_structure_risk(record) >= 0.55:
        notes.append("AI story-structure risk is elevated. Review plot hallucination, causal invention, stereotype tendency, formula generation, corpus bias, and human review.")
    if record.notes:
        notes.append(record.notes)
    return " ".join(notes)


def build_narrative_systems_governance_card(record: NarrativeSystemsGovernanceRecord, config: NarrativeSystemsGovernanceConfig) -> dict[str, Any]:
    return {
        "schema_version": "1.0.0",
        "card_id": card_id(record, config),
        "card_type": "narrative_systems_governance",
        "article_title": config.article_title,
        "article_slug": config.article_slug,
        "item": record.item,
        "modeling_context": record.modeling_context,
        "scores": {
            "narrative_coherence": round(narrative_coherence(record), 4),
            "formula_drift_risk": round(formula_drift_risk(record), 4),
            "responsibility_balance": round(responsibility_balance(record), 4),
            "network_system_strength": round(network_system_strength(record), 4),
            "ai_story_structure_risk": round(ai_story_structure_risk(record), 4),
            "governance_priority_score": round(governance_priority_score(record, config), 4),
        },
        "review": {
            "priority": review_priority(record, config),
            "owner": record.owner,
            "status": record.status,
            "governance_note": governance_note(record, config),
        },
    }
