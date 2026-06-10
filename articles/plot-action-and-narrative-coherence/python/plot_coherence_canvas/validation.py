from __future__ import annotations

from .models import PlotCoherenceItem


SCORE_FIELDS = [
    "action_clarity",
    "causal_linkage",
    "motivation_visibility",
    "episode_dependency",
    "turning_point_strength",
    "resolution_consequence",
    "state_change",
    "knowledge_change",
    "pressure_change",
    "relationship_impact",
    "future_movement",
    "false_causality",
    "simplification_bias",
    "closure_pressure",
    "evidence_omission",
    "uncertainty_clarity",
    "audience_sensitivity",
    "public_consequence",
]


def validate_plot_coherence_item(item: PlotCoherenceItem) -> None:
    if not item.item.strip():
        raise ValueError("Item name is required.")
    if not item.story_type.strip():
        raise ValueError("Story type is required.")
    for field in SCORE_FIELDS:
        value = getattr(item, field)
        if value < 0 or value > 1:
            raise ValueError(f"{field} must be between 0 and 1.")
