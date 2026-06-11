from __future__ import annotations

from .models import TraditionalNarrativeItem


SCORE_FIELDS = [
    "truth_claim_clarity",
    "social_function",
    "memory_orientation",
    "performance_trace",
    "authority_context",
    "genre_notes",
    "boundary_clarity",
    "category_specificity",
    "hybrid_tracking",
    "responsible_analogy",
    "variation_management",
    "origin_memory",
    "place_memory",
    "ritual_memory",
    "heroic_memory",
    "identity_memory",
    "future_obligation",
    "context_removal",
    "sacred_or_restricted_material",
    "performance_omission",
    "translation_loss",
    "extraction_risk",
    "governance_control",
    "community_sensitivity",
    "public_consequence",
]


def validate_traditional_narrative_item(item: TraditionalNarrativeItem) -> None:
    if not item.item.strip():
        raise ValueError("Item name is required.")
    if not item.proposed_form.strip():
        raise ValueError("Proposed form is required.")
    for field in SCORE_FIELDS:
        value = getattr(item, field)
        if value < 0 or value > 1:
            raise ValueError(f"{field} must be between 0 and 1.")
