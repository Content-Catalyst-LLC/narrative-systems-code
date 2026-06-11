from __future__ import annotations

from .models import MythRitualSymbolicItem


SCORE_FIELDS = [
    "origin_function",
    "cosmological_order",
    "memory_function",
    "identity_function",
    "transition_function",
    "authority_function",
    "sequence_clarity",
    "place_linkage",
    "gesture_documentation",
    "object_symbolism",
    "participant_role",
    "protocol_transparency",
    "totalizing_order",
    "scapegoating_risk",
    "exclusion_risk",
    "appropriation_risk",
    "harm_exposure",
    "governance_control",
    "context_explanation",
    "ritual_verification",
    "language_notes",
    "access_control",
    "governance_oversight",
    "uncertainty_marking",
    "community_sensitivity",
    "public_consequence",
]


def validate_myth_ritual_symbolic_item(item: MythRitualSymbolicItem) -> None:
    if not item.item.strip():
        raise ValueError("Item name is required.")
    if not item.symbolic_context.strip():
        raise ValueError("Symbolic context is required.")
    for field in SCORE_FIELDS:
        value = getattr(item, field)
        if value < 0 or value > 1:
            raise ValueError(f"{field} must be between 0 and 1.")
