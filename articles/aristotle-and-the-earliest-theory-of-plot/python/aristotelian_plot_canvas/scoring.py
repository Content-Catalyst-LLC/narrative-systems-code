from __future__ import annotations

from statistics import mean

from .models import PlotItem


def plot_unity(item: PlotItem) -> float:
    return mean([
        item.action_clarity,
        item.causal_linkage,
        item.episode_dependency,
        item.turning_point_relevance,
        item.resolution_support,
        item.goal_coherence,
    ])


def reversal_recognition_strength(item: PlotItem) -> float:
    return mean([
        item.direction_change,
        item.knowledge_change,
        item.preparation_strength,
        item.consequence_pressure,
        item.emotional_intellectual_impact,
    ])


def formula_risk(item: PlotItem) -> float:
    return min(
        1.0,
        item.hero_template_saturation * 0.20
        + item.closure_pressure * 0.25
        + item.unity_bias * 0.20
        + item.genre_bias * 0.20
        + (1 - item.medium_fit) * 0.15,
    )


def governance_score(item: PlotItem) -> float:
    return mean([
        plot_unity(item),
        item.character_action_integration,
        item.genre_fit,
        item.medium_fit,
        item.cultural_awareness,
    ])


def review_priority(item: PlotItem) -> str:
    risk = formula_risk(item)
    unity = plot_unity(item)
    if item.status == "revise" or risk >= 0.55 or unity < 0.55:
        return "high"
    if item.status == "review" or risk >= 0.40 or unity < 0.68:
        return "medium"
    return "standard"
