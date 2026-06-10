from __future__ import annotations

from .models import ReversalRecognitionItem


SCORE_FIELDS = [
    "preparation_trace",
    "causal_linkage",
    "state_change",
    "earned_surprise",
    "action_fit",
    "knowledge_reorientation",
    "evidence_visibility",
    "interpretive_support",
    "meaning_revision",
    "relation_linkage",
    "uncertainty_clarity",
    "identity_change",
    "action_consequence",
    "relationship_change",
    "value_change",
    "future_possibility",
    "governance_accountability",
    "false_recognition",
    "arbitrary_twist",
    "closure_pressure",
    "evidence_omission",
    "audience_sensitivity",
    "public_consequence",
]


def validate_reversal_recognition_item(item: ReversalRecognitionItem) -> None:
    if not item.item.strip():
        raise ValueError("Item name is required.")
    if not item.story_type.strip():
        raise ValueError("Story type is required.")
    for field in SCORE_FIELDS:
        value = getattr(item, field)
        if value < 0 or value > 1:
            raise ValueError(f"{field} must be between 0 and 1.")
