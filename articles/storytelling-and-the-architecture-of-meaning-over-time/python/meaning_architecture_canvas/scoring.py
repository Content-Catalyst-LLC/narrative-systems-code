from __future__ import annotations

from statistics import mean

from .models import MeaningArchitectureItem


def temporal_coherence(item: MeaningArchitectureItem) -> float:
    return mean([
        item.origin_clarity,
        item.sequence_clarity,
        item.continuity_support,
        item.rupture_recognition,
        item.future_projection,
        item.governance_visibility,
    ])


def memory_durability(item: MeaningArchitectureItem) -> float:
    return mean([
        item.preservation,
        item.archive_support,
        item.repetition_strength,
        item.context_retention,
        item.transmission_strength,
    ])


def drift_risk(item: MeaningArchitectureItem) -> float:
    return min(
        1.0,
        (1 - item.evidence_strength) * 0.25
        + item.source_age * 0.20
        + item.link_breakage * 0.20
        + (1 - item.context_retention) * 0.20
        + item.repetition_strength * 0.15,
    )


def revision_priority_score(item: MeaningArchitectureItem) -> float:
    return min(
        1.0,
        drift_risk(item) * 0.40
        + item.audience_consequence * 0.20
        + item.representation_risk * 0.20
        + item.map_dependency * 0.20,
    )


def review_priority(item: MeaningArchitectureItem) -> str:
    score = revision_priority_score(item)
    if item.status == "revise" or score >= 0.50:
        return "high"
    if item.status == "review" or score >= 0.35:
        return "medium"
    return "standard"
