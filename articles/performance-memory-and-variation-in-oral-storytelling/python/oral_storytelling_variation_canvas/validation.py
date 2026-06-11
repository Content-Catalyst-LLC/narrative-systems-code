from __future__ import annotations

from .models import OralStorytellingVariationItem


SCORE_FIELDS = [
    "teller_role",
    "audience_documentation",
    "occasion_context",
    "place_linkage",
    "embodiment",
    "interaction_notes",
    "repetition",
    "formula_use",
    "sequence_clarity",
    "audience_recognition",
    "community_correction",
    "transmission_pathway",
    "variation_tracking",
    "context_explanation",
    "language_notes",
    "source_review",
    "access_protocol",
    "governance_oversight",
    "fixation_risk",
    "context_removal",
    "performance_omission",
    "translation_loss",
    "extraction_risk",
    "governance_control",
    "community_sensitivity",
    "public_consequence",
]


def validate_oral_storytelling_variation_item(item: OralStorytellingVariationItem) -> None:
    if not item.item.strip():
        raise ValueError("Item name is required.")
    if not item.storytelling_context.strip():
        raise ValueError("Storytelling context is required.")
    for field in SCORE_FIELDS:
        value = getattr(item, field)
        if value < 0 or value > 1:
            raise ValueError(f"{field} must be between 0 and 1.")
