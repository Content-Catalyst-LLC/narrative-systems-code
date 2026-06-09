from __future__ import annotations

from .models import CulturalStoryItem


SCORE_FIELDS = [
    "memory_function",
    "teaching_value",
    "identity_function",
    "belonging_function",
    "moral_imagination",
    "social_coordination",
    "transmission_strength",
    "source_transparency",
    "representation_care",
    "persuasive_intensity",
    "audience_consequence",
    "public_impact",
]


def validate_cultural_story_item(item: CulturalStoryItem) -> None:
    if not item.item.strip():
        raise ValueError("Item name is required.")
    if not item.story_type.strip():
        raise ValueError("Story type is required.")
    for field in SCORE_FIELDS:
        value = getattr(item, field)
        if value < 0 or value > 1:
            raise ValueError(f"{field} must be between 0 and 1.")
