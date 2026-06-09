from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class StoryMedium:
    medium: str
    period_label: str
    preservation: float
    participation: float
    circulation: float
    repeatability: float
    governance_complexity: float
    archive_durability: float
    context_retention: float
    access_openness: float
    platform_stability: float
    owner: str
    status: str
