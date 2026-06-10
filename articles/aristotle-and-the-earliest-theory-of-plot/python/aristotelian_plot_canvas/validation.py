from __future__ import annotations

from .models import PlotItem


SCORE_FIELDS = [
    "action_clarity",
    "causal_linkage",
    "episode_dependency",
    "turning_point_relevance",
    "resolution_support",
    "goal_coherence",
    "direction_change",
    "knowledge_change",
    "preparation_strength",
    "consequence_pressure",
    "emotional_intellectual_impact",
    "character_action_integration",
    "genre_fit",
    "medium_fit",
    "cultural_awareness",
    "hero_template_saturation",
    "closure_pressure",
    "unity_bias",
    "genre_bias",
]


def validate_plot_item(item: PlotItem) -> None:
    if not item.item.strip():
        raise ValueError("Item name is required.")
    if not item.story_type.strip():
        raise ValueError("Story type is required.")
    for field in SCORE_FIELDS:
        value = getattr(item, field)
        if value < 0 or value > 1:
            raise ValueError(f"{field} must be between 0 and 1.")
