from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class TraditionalNarrativeItem:
    item: str
    proposed_form: str
    truth_claim_clarity: float
    social_function: float
    memory_orientation: float
    performance_trace: float
    authority_context: float
    genre_notes: float
    boundary_clarity: float
    category_specificity: float
    hybrid_tracking: float
    responsible_analogy: float
    variation_management: float
    origin_memory: float
    place_memory: float
    ritual_memory: float
    heroic_memory: float
    identity_memory: float
    future_obligation: float
    context_removal: float
    sacred_or_restricted_material: float
    performance_omission: float
    translation_loss: float
    extraction_risk: float
    governance_control: float
    community_sensitivity: float
    public_consequence: float
    owner: str
    status: str
