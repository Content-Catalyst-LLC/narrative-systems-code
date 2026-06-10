from __future__ import annotations

from statistics import mean

from .models import PublicStoryItem


def rhetorical_balance(item: PublicStoryItem) -> float:
    return mean([
        item.ethos_strength,
        item.logos_support,
        item.pathos_proportionality,
        item.audience_fit,
        item.context_clarity,
    ])


def persuasion_force(item: PublicStoryItem) -> float:
    return min(
        1.0,
        item.identification_strength * 0.25
        + item.emotional_intensity * 0.20
        + item.causal_clarity * 0.20
        + item.urgency * 0.15
        + item.action_clarity * 0.20,
    )


def public_story_risk(item: PublicStoryItem) -> float:
    return min(
        1.0,
        (1 - item.verification_strength) * 0.25
        + item.emotional_coercion * 0.20
        + item.scapegoating_risk * 0.25
        + item.identity_manipulation * 0.15
        + item.closure_pressure * 0.15,
    )


def governance_priority_score(item: PublicStoryItem) -> float:
    return min(
        1.0,
        persuasion_force(item) * 0.25
        + public_story_risk(item) * 0.35
        + item.audience_consequence * 0.20
        + item.representation_sensitivity * 0.20,
    )


def review_priority(item: PublicStoryItem) -> str:
    risk = public_story_risk(item)
    priority = governance_priority_score(item)
    if item.status == "revise" or risk >= 0.55 or priority >= 0.60:
        return "high"
    if item.status == "review" or risk >= 0.40 or priority >= 0.45:
        return "medium"
    return "standard"
