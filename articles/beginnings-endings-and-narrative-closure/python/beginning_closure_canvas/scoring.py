from __future__ import annotations

from statistics import mean

from .models import BeginningClosureItem


def opening_clarity(item: BeginningClosureItem) -> float:
    return mean([
        item.voice_signal,
        item.world_orientation,
        item.pressure_introduction,
        item.stakes_visibility,
        item.question_framing,
        item.contract_transparency,
    ])


def closure_integrity(item: BeginningClosureItem) -> float:
    return mean([
        item.promise_fulfillment,
        item.resolution_suitability,
        item.transformation_depth,
        item.aftermath_clarity,
        item.emotional_honesty,
        item.unresolved_harm_honesty,
    ])


def beginning_ending_alignment(item: BeginningClosureItem) -> float:
    return mean([
        item.motif_return,
        item.question_answer,
        item.interpretive_echo,
        item.thematic_continuity,
        item.frame_revision,
    ])


def closure_risk(item: BeginningClosureItem) -> float:
    return min(
        1.0,
        item.premature_repair * 0.24
        + item.false_resolution * 0.24
        + item.system_flattening * 0.20
        + item.aftermath_omission * 0.18
        + item.excessive_audience_comfort * 0.14,
    )


def governance_priority_score(item: BeginningClosureItem) -> float:
    return min(
        1.0,
        closure_risk(item) * 0.35
        + item.audience_sensitivity * 0.20
        + item.public_consequence * 0.25
        + (1 - closure_integrity(item)) * 0.20,
    )


def review_priority(item: BeginningClosureItem) -> str:
    risk = closure_risk(item)
    priority = governance_priority_score(item)
    closure = closure_integrity(item)
    opening = opening_clarity(item)

    if item.status == "revise" or risk >= 0.55 or priority >= 0.62 or closure < 0.55 or opening < 0.50:
        return "high"
    if item.status == "review" or risk >= 0.40 or priority >= 0.48 or closure < 0.68:
        return "medium"
    return "standard"
