from __future__ import annotations

from .models import StoryMedium


SCORE_FIELDS = [
    "preservation",
    "participation",
    "circulation",
    "repeatability",
    "governance_complexity",
    "archive_durability",
    "context_retention",
    "access_openness",
    "platform_stability",
]


def validate_story_medium(item: StoryMedium) -> None:
    if not item.medium.strip():
        raise ValueError("Medium name is required.")
    if not item.period_label.strip():
        raise ValueError("Period label is required.")
    for field in SCORE_FIELDS:
        value = getattr(item, field)
        if value < 0 or value > 1:
            raise ValueError(f"{field} must be between 0 and 1.")
