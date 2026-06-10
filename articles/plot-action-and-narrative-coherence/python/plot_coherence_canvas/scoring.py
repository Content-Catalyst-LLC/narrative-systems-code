from __future__ import annotations

from statistics import mean

from .models import PlotCoherenceItem


def plot_coherence(item: PlotCoherenceItem) -> float:
    return mean([
        item.action_clarity,
        item.causal_linkage,
        item.motivation_visibility,
        item.episode_dependency,
        item.turning_point_strength,
        item.resolution_consequence,
    ])


def action_dependency(item: PlotCoherenceItem) -> float:
    return mean([
        item.state_change,
        item.knowledge_change,
        item.pressure_change,
        item.relationship_impact,
        item.future_movement,
    ])


def coherence_risk(item: PlotCoherenceItem) -> float:
    return min(
        1.0,
        item.false_causality * 0.25
        + item.simplification_bias * 0.20
        + item.closure_pressure * 0.20
        + item.evidence_omission * 0.20
        + (1 - item.uncertainty_clarity) * 0.15,
    )


def governance_priority_score(item: PlotCoherenceItem) -> float:
    return min(
        1.0,
        plot_coherence(item) * 0.20
        + coherence_risk(item) * 0.35
        + item.audience_sensitivity * 0.20
        + item.public_consequence * 0.25,
    )


def review_priority(item: PlotCoherenceItem) -> str:
    risk = coherence_risk(item)
    priority = governance_priority_score(item)
    coherence = plot_coherence(item)

    if item.status == "revise" or risk >= 0.55 or coherence < 0.55 or priority >= 0.62:
        return "high"
    if item.status == "review" or risk >= 0.40 or coherence < 0.68 or priority >= 0.48:
        return "medium"
    return "standard"
