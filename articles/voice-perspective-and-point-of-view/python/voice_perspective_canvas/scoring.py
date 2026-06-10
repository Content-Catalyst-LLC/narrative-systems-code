from __future__ import annotations

from statistics import mean

from .models import VoicePerspectiveItem


def voice_consistency(item: VoicePerspectiveItem) -> float:
    return mean([
        item.tone_stability,
        item.diction_coherence,
        item.rhetorical_habit,
        item.address_stability,
        item.judgment_coherence,
    ])


def perspective_access(item: VoicePerspectiveItem) -> float:
    return mean([
        item.knowledge_limits,
        item.interior_access,
        item.focalization_clarity,
        item.level_stability,
        item.source_boundaries,
    ])


def reliability_risk(item: VoicePerspectiveItem) -> float:
    return min(
        1.0,
        item.factual_unreliability * 0.20
        + item.interpretive_unreliability * 0.20
        + item.ethical_unreliability * 0.20
        + item.memory_distortion * 0.20
        + item.agency_gap * 0.20,
    )


def governance_priority_score(item: VoicePerspectiveItem) -> float:
    return min(
        1.0,
        (1 - perspective_access(item)) * 0.20
        + reliability_risk(item) * 0.30
        + item.exposure_sensitivity * 0.20
        + item.public_consequence * 0.20
        + item.representation_gap * 0.10,
    )


def review_priority(item: VoicePerspectiveItem) -> str:
    risk = reliability_risk(item)
    priority = governance_priority_score(item)
    access = perspective_access(item)

    if item.status == "revise" or risk >= 0.55 or priority >= 0.62 or access < 0.55:
        return "high"
    if item.status == "review" or risk >= 0.40 or priority >= 0.48 or access < 0.68:
        return "medium"
    return "standard"
