from __future__ import annotations

from .models import OralTraditionItem


SCORE_FIELDS = [
    "teller_role",
    "audience_response",
    "occasion_clarity",
    "embodiment",
    "setting_place",
    "cultural_frame",
    "lineage_clarity",
    "variation_tracking",
    "memory_supports",
    "governance_protocol",
    "authority_permission",
    "record_context",
    "origin_memory",
    "place_memory",
    "identity_memory",
    "historical_memory",
    "ritual_memory",
    "future_obligation",
    "consent_limits",
    "restricted_knowledge",
    "exposure_risk",
    "ownership_risk",
    "extraction_risk",
    "governance_control",
    "community_sensitivity",
    "public_consequence",
]


def validate_oral_tradition_item(item: OralTraditionItem) -> None:
    if not item.item.strip():
        raise ValueError("Item name is required.")
    if not item.tradition_type.strip():
        raise ValueError("Tradition type is required.")
    for field in SCORE_FIELDS:
        value = getattr(item, field)
        if value < 0 or value > 1:
            raise ValueError(f"{field} must be between 0 and 1.")
