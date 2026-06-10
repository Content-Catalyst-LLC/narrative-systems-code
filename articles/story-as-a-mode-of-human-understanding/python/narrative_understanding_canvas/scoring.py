from __future__ import annotations

from statistics import mean

from .models import NarrativeUnderstandingItem


def understanding_score(item: NarrativeUnderstandingItem) -> float:
    return mean([
        item.sequence_clarity,
        item.causal_framing,
        item.agency_mapping,
        item.memory_integration,
        item.evidence_support,
        item.openness_to_revision,
    ])


def moral_understanding_score(item: NarrativeUnderstandingItem) -> float:
    return mean([
        item.consequence_visibility,
        item.agency_mapping,
        item.harm_recognition,
        item.responsibility_mapping,
        item.repair_awareness,
    ])


def possible_world_score(item: NarrativeUnderstandingItem) -> float:
    return mean([
        item.alternative_logic,
        item.causal_framing,
        item.uncertainty_signaling,
        item.interpretive_diversity,
        item.openness_to_revision,
    ])


def overreach_risk(item: NarrativeUnderstandingItem) -> float:
    return min(
        1.0,
        (1 - item.evidence_support) * 0.25
        + item.hindsight_bias * 0.20
        + item.false_coherence * 0.25
        + item.selection_bias * 0.15
        + item.closure_pressure * 0.15,
    )


def review_priority(item: NarrativeUnderstandingItem) -> str:
    risk = overreach_risk(item)
    if item.status == "revise" or risk >= 0.50:
        return "high"
    if item.status == "review" or risk >= 0.35:
        return "medium"
    return "standard"
