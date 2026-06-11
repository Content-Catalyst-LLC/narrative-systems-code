from __future__ import annotations

from statistics import mean

from .models import TraditionalNarrativeItem


def form_classification(item: TraditionalNarrativeItem) -> float:
    return mean([
        item.truth_claim_clarity,
        item.social_function,
        item.memory_orientation,
        item.performance_trace,
        item.authority_context,
        item.genre_notes,
    ])


def narrative_distinction(item: TraditionalNarrativeItem) -> float:
    return mean([
        item.boundary_clarity,
        item.category_specificity,
        item.hybrid_tracking,
        item.responsible_analogy,
        item.variation_management,
    ])


def cultural_memory_function(item: TraditionalNarrativeItem) -> float:
    return mean([
        item.origin_memory,
        item.place_memory,
        item.ritual_memory,
        item.heroic_memory,
        item.identity_memory,
        item.future_obligation,
    ])


def adaptation_risk(item: TraditionalNarrativeItem) -> float:
    return min(
        1.0,
        item.context_removal * 0.18
        + item.sacred_or_restricted_material * 0.22
        + item.performance_omission * 0.16
        + item.translation_loss * 0.16
        + item.extraction_risk * 0.18
        + (1 - item.governance_control) * 0.10,
    )


def governance_priority_score(item: TraditionalNarrativeItem) -> float:
    return min(
        1.0,
        adaptation_risk(item) * 0.35
        + item.community_sensitivity * 0.25
        + item.public_consequence * 0.20
        + (1 - narrative_distinction(item)) * 0.20,
    )


def review_priority(item: TraditionalNarrativeItem) -> str:
    risk = adaptation_risk(item)
    priority = governance_priority_score(item)
    distinction = narrative_distinction(item)

    if item.status == "revise" or risk >= 0.55 or priority >= 0.62 or distinction < 0.55:
        return "high"
    if item.status == "review" or risk >= 0.40 or priority >= 0.48 or distinction < 0.68:
        return "medium"
    return "standard"
