from __future__ import annotations

from .models import VoicePerspectiveItem


SCORE_FIELDS = [
    "tone_stability",
    "diction_coherence",
    "rhetorical_habit",
    "address_stability",
    "judgment_coherence",
    "knowledge_limits",
    "interior_access",
    "focalization_clarity",
    "level_stability",
    "source_boundaries",
    "factual_unreliability",
    "interpretive_unreliability",
    "ethical_unreliability",
    "memory_distortion",
    "agency_gap",
    "exposure_sensitivity",
    "public_consequence",
    "representation_gap",
    "institutional_evasion",
]


def validate_voice_perspective_item(item: VoicePerspectiveItem) -> None:
    if not item.item.strip():
        raise ValueError("Item name is required.")
    if not item.story_type.strip():
        raise ValueError("Story type is required.")
    for field in SCORE_FIELDS:
        value = getattr(item, field)
        if value < 0 or value > 1:
            raise ValueError(f"{field} must be between 0 and 1.")
