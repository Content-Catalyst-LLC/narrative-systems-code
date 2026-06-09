from __future__ import annotations

from .models import StoryItem


SCORE_FIELDS = [
    "sequence_clarity",
    "agency_clarity",
    "causal_connection",
    "conflict_definition",
    "transformation_clarity",
    "motif_use",
    "interpretive_relevance",
    "evidence_strength",
    "representation_care",
    "persuasive_intensity",
    "audience_consequence",
]


def validate_story_item(item: StoryItem) -> None:
    if not item.item.strip():
        raise ValueError("Story item name is required.")
    if not item.story_type.strip():
        raise ValueError("Story type is required.")
    for field in SCORE_FIELDS:
        value = getattr(item, field)
        if value < 0 or value > 1:
            raise ValueError(f"{field} must be between 0 and 1.")
