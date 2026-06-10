from __future__ import annotations

from .models import ConflictTensionItem


SCORE_FIELDS = [
    "desire_clarity",
    "obstacle_clarity",
    "pressure_strength",
    "agency_visibility",
    "stakes_visibility",
    "relation_legibility",
    "unresolved_pressure",
    "meaningful_delay",
    "stakes_heightening",
    "expectation_pressure",
    "complication_movement",
    "state_change",
    "knowledge_change",
    "relationship_impact",
    "pressure_change",
    "future_movement",
    "value_transformation",
    "scapegoating",
    "conflict_inflation",
    "trauma_spectacle",
    "false_balance",
    "closure_pressure",
    "audience_sensitivity",
    "public_consequence",
]


def validate_conflict_tension_item(item: ConflictTensionItem) -> None:
    if not item.item.strip():
        raise ValueError("Item name is required.")
    if not item.story_type.strip():
        raise ValueError("Story type is required.")
    for field in SCORE_FIELDS:
        value = getattr(item, field)
        if value < 0 or value > 1:
            raise ValueError(f"{field} must be between 0 and 1.")
