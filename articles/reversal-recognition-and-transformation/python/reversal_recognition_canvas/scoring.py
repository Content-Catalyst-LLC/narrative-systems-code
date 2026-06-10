from __future__ import annotations

from statistics import mean

from .models import ReversalRecognitionItem


def reversal_integrity(item: ReversalRecognitionItem) -> float:
    return mean([
        item.preparation_trace,
        item.causal_linkage,
        item.state_change,
        item.earned_surprise,
        item.action_fit,
        item.knowledge_reorientation,
    ])


def recognition_clarity(item: ReversalRecognitionItem) -> float:
    return mean([
        item.evidence_visibility,
        item.interpretive_support,
        item.meaning_revision,
        item.relation_linkage,
        item.uncertainty_clarity,
    ])


def transformation_depth(item: ReversalRecognitionItem) -> float:
    return mean([
        item.identity_change,
        item.action_consequence,
        item.relationship_change,
        item.value_change,
        item.future_possibility,
        item.governance_accountability,
    ])


def recognition_risk(item: ReversalRecognitionItem) -> float:
    return min(
        1.0,
        item.false_recognition * 0.25
        + item.arbitrary_twist * 0.25
        + item.closure_pressure * 0.20
        + item.evidence_omission * 0.20
        + (1 - item.uncertainty_clarity) * 0.10,
    )


def governance_priority_score(item: ReversalRecognitionItem) -> float:
    return min(
        1.0,
        recognition_risk(item) * 0.35
        + item.audience_sensitivity * 0.20
        + item.public_consequence * 0.25
        + (1 - recognition_clarity(item)) * 0.20,
    )


def review_priority(item: ReversalRecognitionItem) -> str:
    risk = recognition_risk(item)
    priority = governance_priority_score(item)
    integrity = reversal_integrity(item)
    transformation = transformation_depth(item)

    if item.status == "revise" or risk >= 0.55 or priority >= 0.62 or integrity < 0.55 or transformation < 0.50:
        return "high"
    if item.status == "review" or risk >= 0.40 or priority >= 0.48 or integrity < 0.68:
        return "medium"
    return "standard"
