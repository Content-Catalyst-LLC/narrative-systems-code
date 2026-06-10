from __future__ import annotations

from .models import BeginningClosureItem


SCORE_FIELDS = [
    "voice_signal",
    "world_orientation",
    "pressure_introduction",
    "stakes_visibility",
    "question_framing",
    "contract_transparency",
    "promise_fulfillment",
    "resolution_suitability",
    "transformation_depth",
    "aftermath_clarity",
    "emotional_honesty",
    "unresolved_harm_honesty",
    "motif_return",
    "question_answer",
    "interpretive_echo",
    "thematic_continuity",
    "frame_revision",
    "premature_repair",
    "false_resolution",
    "system_flattening",
    "aftermath_omission",
    "excessive_audience_comfort",
    "audience_sensitivity",
    "public_consequence",
]


def validate_beginning_closure_item(item: BeginningClosureItem) -> None:
    if not item.item.strip():
        raise ValueError("Item name is required.")
    if not item.story_type.strip():
        raise ValueError("Story type is required.")
    for field in SCORE_FIELDS:
        value = getattr(item, field)
        if value < 0 or value > 1:
            raise ValueError(f"{field} must be between 0 and 1.")
