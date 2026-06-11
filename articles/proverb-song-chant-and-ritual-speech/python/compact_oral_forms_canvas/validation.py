from __future__ import annotations

from .models import CompactOralFormItem


SCORE_FIELDS = [
    "form_identification",
    "speaker_role",
    "audience_documentation",
    "occasion_notes",
    "place_linkage",
    "use_context",
    "rhythm",
    "melody",
    "cadence",
    "refrain_or_formula",
    "participation",
    "embodiment",
    "role_legitimacy",
    "protocol_review",
    "consent_status",
    "access_control",
    "governance_oversight",
    "benefit_sharing",
    "quote_extraction_risk",
    "context_removal",
    "sound_loss",
    "translation_loss",
    "extraction_risk",
    "governance_control",
    "community_sensitivity",
    "public_consequence",
]


def validate_compact_oral_form_item(item: CompactOralFormItem) -> None:
    if not item.item.strip():
        raise ValueError("Item name is required.")
    if not item.oral_form.strip():
        raise ValueError("Oral form is required.")
    for field in SCORE_FIELDS:
        value = getattr(item, field)
        if value < 0 or value > 1:
            raise ValueError(f"{field} must be between 0 and 1.")
