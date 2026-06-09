from __future__ import annotations

from statistics import mean

from .models import CulturalStoryItem


def cultural_context_score(item: CulturalStoryItem) -> float:
    return 0.85 if len(item.cultural_context.strip()) >= 20 else 0.45


def cultural_value_score(item: CulturalStoryItem) -> float:
    return mean([
        item.memory_function,
        item.teaching_value,
        item.identity_function,
        item.belonging_function,
        item.moral_imagination,
        item.social_coordination,
    ])


def transmission_score(item: CulturalStoryItem) -> float:
    return mean([
        item.transmission_strength,
        item.source_transparency,
        item.memory_function,
        cultural_context_score(item),
    ])


def narrative_risk(item: CulturalStoryItem) -> float:
    return min(
        1.0,
        item.persuasive_intensity * 0.25
        + (1 - item.source_transparency) * 0.25
        + (1 - item.representation_care) * 0.30
        + item.audience_consequence * 0.20,
    )


def review_priority_score(item: CulturalStoryItem) -> float:
    return min(
        1.0,
        narrative_risk(item) * 0.45
        + (1 - cultural_context_score(item)) * 0.20
        + (1 - item.source_transparency) * 0.15
        + item.public_impact * 0.20,
    )


def review_priority(item: CulturalStoryItem) -> str:
    score = review_priority_score(item)
    if item.status == "revise" or score >= 0.50:
        return "high"
    if item.status == "review" or score >= 0.35:
        return "medium"
    return "standard"
