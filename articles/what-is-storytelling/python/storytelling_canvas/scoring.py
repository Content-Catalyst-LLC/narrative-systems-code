from __future__ import annotations

from statistics import mean

from .models import StoryItem


def coherence_score(item: StoryItem) -> float:
    return mean([
        item.sequence_clarity,
        item.agency_clarity,
        item.causal_connection,
        item.transformation_clarity,
        item.interpretive_relevance,
    ])


def craft_score(item: StoryItem) -> float:
    return mean([
        item.sequence_clarity,
        item.conflict_definition,
        item.transformation_clarity,
        item.motif_use,
        item.interpretive_relevance,
    ])


def governance_risk(item: StoryItem) -> float:
    return min(
        1.0,
        (1 - item.evidence_strength) * 0.30
        + (1 - item.representation_care) * 0.30
        + item.persuasive_intensity * 0.20
        + item.audience_consequence * 0.20,
    )


def review_priority(item: StoryItem) -> str:
    risk = governance_risk(item)
    if item.status == "revise" or risk >= 0.48:
        return "high"
    if item.status == "review" or risk >= 0.34:
        return "medium"
    return "standard"
