from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class CompactOralFormItem:
    item: str
    oral_form: str
    form_identification: float
    speaker_role: float
    audience_documentation: float
    occasion_notes: float
    place_linkage: float
    use_context: float
    rhythm: float
    melody: float
    cadence: float
    refrain_or_formula: float
    participation: float
    embodiment: float
    role_legitimacy: float
    protocol_review: float
    consent_status: float
    access_control: float
    governance_oversight: float
    benefit_sharing: float
    quote_extraction_risk: float
    context_removal: float
    sound_loss: float
    translation_loss: float
    extraction_risk: float
    governance_control: float
    community_sensitivity: float
    public_consequence: float
    owner: str
    status: str
