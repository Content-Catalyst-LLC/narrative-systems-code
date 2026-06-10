from __future__ import annotations

from .models import FolktaleMorphologyItem


SCORE_FIELDS = [
    "function_identification",
    "sequence_clarity",
    "role_mapping",
    "variation_tracking",
    "context_notes",
    "order_coherence",
    "transition_logic",
    "gap_management",
    "repetition_awareness",
    "closure_handling",
    "performance_context",
    "cultural_specificity",
    "language_notes",
    "tradition_review",
    "ethical_governance",
    "universalization_risk",
    "cultural_erasure_risk",
    "performance_omission",
    "variation_omission",
    "archive_bias",
    "community_sensitivity",
    "public_consequence",
]


def validate_folktale_morphology_item(item: FolktaleMorphologyItem) -> None:
    if not item.item.strip():
        raise ValueError("Item name is required.")
    if not item.tale_type.strip():
        raise ValueError("Tale type is required.")
    for field in SCORE_FIELDS:
        value = getattr(item, field)
        if value < 0 or value > 1:
            raise ValueError(f"{field} must be between 0 and 1.")
