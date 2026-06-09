from __future__ import annotations

from statistics import mean

from .models import StoryMedium


def transmission_strength(item: StoryMedium) -> float:
    return mean([
        item.preservation,
        item.repeatability,
        item.circulation,
        item.archive_durability,
    ])


def participation_score(item: StoryMedium) -> float:
    return item.participation


def preservation_risk(item: StoryMedium) -> float:
    return min(
        1.0,
        (1 - item.archive_durability) * 0.25
        + item.governance_complexity * 0.20
        + (1 - item.context_retention) * 0.25
        + (1 - item.access_openness) * 0.15
        + (1 - item.platform_stability) * 0.15,
    )


def review_priority(item: StoryMedium) -> str:
    risk = preservation_risk(item)
    if item.status == "review" or risk >= 0.50:
        return "high"
    if risk >= 0.35:
        return "medium"
    return "standard"


def transition_score(first: StoryMedium, second: StoryMedium) -> float:
    return mean([
        abs(second.preservation - first.preservation),
        abs(second.participation - first.participation),
        abs(second.circulation - first.circulation),
        abs(second.repeatability - first.repeatability),
        abs(second.governance_complexity - first.governance_complexity),
    ])
