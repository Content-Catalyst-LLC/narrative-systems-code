from __future__ import annotations

from .models import MeaningArchitectureItem


SCORE_FIELDS = [
    "origin_clarity",
    "sequence_clarity",
    "continuity_support",
    "rupture_recognition",
    "future_projection",
    "governance_visibility",
    "preservation",
    "archive_support",
    "repetition_strength",
    "context_retention",
    "transmission_strength",
    "evidence_strength",
    "source_age",
    "link_breakage",
    "audience_consequence",
    "representation_risk",
    "map_dependency",
]


def validate_meaning_architecture_item(item: MeaningArchitectureItem) -> None:
    if not item.item.strip():
        raise ValueError("Item name is required.")
    if not item.story_type.strip():
        raise ValueError("Story type is required.")
    for field in SCORE_FIELDS:
        value = getattr(item, field)
        if value < 0 or value > 1:
            raise ValueError(f"{field} must be between 0 and 1.")
