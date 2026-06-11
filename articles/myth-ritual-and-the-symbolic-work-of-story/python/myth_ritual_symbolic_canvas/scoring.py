from __future__ import annotations

from statistics import mean

from .models import MythRitualSymbolicItem


def symbolic_function(item: MythRitualSymbolicItem) -> float:
    return mean([
        item.origin_function,
        item.cosmological_order,
        item.memory_function,
        item.identity_function,
        item.transition_function,
        item.authority_function,
    ])


def ritual_context(item: MythRitualSymbolicItem) -> float:
    return mean([
        item.sequence_clarity,
        item.place_linkage,
        item.gesture_documentation,
        item.object_symbolism,
        item.participant_role,
        item.protocol_transparency,
    ])


def ethical_risk(item: MythRitualSymbolicItem) -> float:
    return min(
        1.0,
        item.totalizing_order * 0.18
        + item.scapegoating_risk * 0.20
        + item.exclusion_risk * 0.18
        + item.appropriation_risk * 0.18
        + item.harm_exposure * 0.16
        + (1 - item.governance_control) * 0.10,
    )


def interpretation_readiness(item: MythRitualSymbolicItem) -> float:
    return mean([
        item.context_explanation,
        item.ritual_verification,
        item.language_notes,
        item.access_control,
        item.governance_oversight,
        item.uncertainty_marking,
    ])


def governance_priority_score(item: MythRitualSymbolicItem) -> float:
    return min(
        1.0,
        ethical_risk(item) * 0.35
        + item.community_sensitivity * 0.25
        + item.public_consequence * 0.20
        + (1 - interpretation_readiness(item)) * 0.20,
    )


def review_priority(item: MythRitualSymbolicItem) -> str:
    risk = ethical_risk(item)
    priority = governance_priority_score(item)
    readiness = interpretation_readiness(item)

    if item.status == "revise" or risk >= 0.55 or priority >= 0.62 or readiness < 0.55:
        return "high"
    if item.status == "review" or risk >= 0.40 or priority >= 0.48 or readiness < 0.68:
        return "medium"
    return "standard"
