from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class OralStorytellingVariationItem:
    item: str
    storytelling_context: str
    teller_role: float
    audience_documentation: float
    occasion_context: float
    place_linkage: float
    embodiment: float
    interaction_notes: float
    repetition: float
    formula_use: float
    sequence_clarity: float
    audience_recognition: float
    community_correction: float
    transmission_pathway: float
    variation_tracking: float
    context_explanation: float
    language_notes: float
    source_review: float
    access_protocol: float
    governance_oversight: float
    fixation_risk: float
    context_removal: float
    performance_omission: float
    translation_loss: float
    extraction_risk: float
    governance_control: float
    community_sensitivity: float
    public_consequence: float
    owner: str
    status: str
