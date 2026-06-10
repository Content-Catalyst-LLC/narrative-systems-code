from __future__ import annotations

from .models import PublicStoryItem


SCORE_FIELDS = [
    "ethos_strength",
    "logos_support",
    "pathos_proportionality",
    "audience_fit",
    "context_clarity",
    "identification_strength",
    "emotional_intensity",
    "causal_clarity",
    "urgency",
    "action_clarity",
    "verification_strength",
    "emotional_coercion",
    "scapegoating_risk",
    "identity_manipulation",
    "closure_pressure",
    "audience_consequence",
    "representation_sensitivity",
]


def validate_public_story_item(item: PublicStoryItem) -> None:
    if not item.item.strip():
        raise ValueError("Item name is required.")
    if not item.story_type.strip():
        raise ValueError("Story type is required.")
    for field in SCORE_FIELDS:
        value = getattr(item, field)
        if value < 0 or value > 1:
            raise ValueError(f"{field} must be between 0 and 1.")
