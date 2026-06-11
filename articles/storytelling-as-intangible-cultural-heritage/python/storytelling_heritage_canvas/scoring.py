from __future__ import annotations

from statistics import mean

from .models import StorytellingHeritageItem


def living_continuity(item: StorytellingHeritageItem) -> float:
    return mean([
        item.transmission_support,
        item.performance_context,
        item.language_vitality,
        item.apprenticeship_pathways,
        item.community_recognition,
        item.variation_management,
    ])


def safeguarding_readiness(item: StorytellingHeritageItem) -> float:
    return mean([
        item.consent_clarity,
        item.governance_protocol,
        item.metadata_quality,
        item.access_control,
        item.benefit_sharing,
        item.review_process,
    ])


def heritage_context_preservation(item: StorytellingHeritageItem) -> float:
    return mean([
        item.occasion_context,
        item.place_linkage,
        item.ritual_frame,
        item.embodiment,
        item.social_transmission,
        item.knowledge_holder_context,
    ])


def archive_risk(item: StorytellingHeritageItem) -> float:
    return min(
        1.0,
        item.context_removal * 0.18
        + item.sacred_or_restricted_material * 0.22
        + item.performance_omission * 0.16
        + item.translation_loss * 0.16
        + item.extraction_risk * 0.18
        + (1 - item.governance_control) * 0.10,
    )


def governance_priority_score(item: StorytellingHeritageItem) -> float:
    return min(
        1.0,
        archive_risk(item) * 0.35
        + item.community_sensitivity * 0.25
        + item.public_consequence * 0.20
        + (1 - safeguarding_readiness(item)) * 0.20,
    )


def review_priority(item: StorytellingHeritageItem) -> str:
    risk = archive_risk(item)
    priority = governance_priority_score(item)
    readiness = safeguarding_readiness(item)

    if item.status == "revise" or risk >= 0.55 or priority >= 0.62 or readiness < 0.55:
        return "high"
    if item.status == "review" or risk >= 0.40 or priority >= 0.48 or readiness < 0.68:
        return "medium"
    return "standard"
