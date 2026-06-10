from __future__ import annotations

from .models import NarrativeUnderstandingItem


SCORE_FIELDS = [
    "sequence_clarity",
    "causal_framing",
    "agency_mapping",
    "memory_integration",
    "evidence_support",
    "openness_to_revision",
    "consequence_visibility",
    "harm_recognition",
    "responsibility_mapping",
    "repair_awareness",
    "alternative_logic",
    "uncertainty_signaling",
    "interpretive_diversity",
    "hindsight_bias",
    "false_coherence",
    "selection_bias",
    "closure_pressure",
]


def validate_narrative_understanding_item(item: NarrativeUnderstandingItem) -> None:
    if not item.item.strip():
        raise ValueError("Item name is required.")
    if not item.story_type.strip():
        raise ValueError("Story type is required.")
    for field in SCORE_FIELDS:
        value = getattr(item, field)
        if value < 0 or value > 1:
            raise ValueError(f"{field} must be between 0 and 1.")
