from __future__ import annotations

from .models import StorytellingHeritageItem


SCORE_FIELDS = [
    "transmission_support",
    "performance_context",
    "language_vitality",
    "apprenticeship_pathways",
    "community_recognition",
    "variation_management",
    "consent_clarity",
    "governance_protocol",
    "metadata_quality",
    "access_control",
    "benefit_sharing",
    "review_process",
    "occasion_context",
    "place_linkage",
    "ritual_frame",
    "embodiment",
    "social_transmission",
    "knowledge_holder_context",
    "context_removal",
    "sacred_or_restricted_material",
    "performance_omission",
    "translation_loss",
    "extraction_risk",
    "governance_control",
    "community_sensitivity",
    "public_consequence",
]


def validate_storytelling_heritage_item(item: StorytellingHeritageItem) -> None:
    if not item.item.strip():
        raise ValueError("Item name is required.")
    if not item.heritage_context.strip():
        raise ValueError("Heritage context is required.")
    for field in SCORE_FIELDS:
        value = getattr(item, field)
        if value < 0 or value > 1:
            raise ValueError(f"{field} must be between 0 and 1.")
