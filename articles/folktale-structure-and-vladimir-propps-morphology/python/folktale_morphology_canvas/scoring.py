from __future__ import annotations

from statistics import mean

from .models import FolktaleMorphologyItem


def function_coverage(item: FolktaleMorphologyItem) -> float:
    return mean([
        item.function_identification,
        item.sequence_clarity,
        item.role_mapping,
        item.variation_tracking,
        item.context_notes,
    ])


def sequence_integrity(item: FolktaleMorphologyItem) -> float:
    return mean([
        item.order_coherence,
        item.transition_logic,
        item.gap_management,
        item.repetition_awareness,
        item.closure_handling,
    ])


def morphology_context_balance(item: FolktaleMorphologyItem) -> float:
    return mean([
        item.performance_context,
        item.cultural_specificity,
        item.language_notes,
        item.tradition_review,
        item.ethical_governance,
    ])


def reduction_risk(item: FolktaleMorphologyItem) -> float:
    return min(
        1.0,
        item.universalization_risk * 0.22
        + item.cultural_erasure_risk * 0.22
        + item.performance_omission * 0.18
        + item.variation_omission * 0.18
        + (1 - morphology_context_balance(item)) * 0.20,
    )


def governance_priority_score(item: FolktaleMorphologyItem) -> float:
    return min(
        1.0,
        reduction_risk(item) * 0.35
        + item.archive_bias * 0.20
        + item.community_sensitivity * 0.20
        + item.public_consequence * 0.15
        + (1 - morphology_context_balance(item)) * 0.10,
    )


def review_priority(item: FolktaleMorphologyItem) -> str:
    risk = reduction_risk(item)
    priority = governance_priority_score(item)
    balance = morphology_context_balance(item)

    if item.status == "revise" or risk >= 0.55 or priority >= 0.62 or balance < 0.55:
        return "high"
    if item.status == "review" or risk >= 0.40 or priority >= 0.48 or balance < 0.68:
        return "medium"
    return "standard"
