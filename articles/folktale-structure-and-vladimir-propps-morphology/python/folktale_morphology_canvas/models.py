from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class FolktaleMorphologyItem:
    item: str
    tale_type: str
    function_identification: float
    sequence_clarity: float
    role_mapping: float
    variation_tracking: float
    context_notes: float
    order_coherence: float
    transition_logic: float
    gap_management: float
    repetition_awareness: float
    closure_handling: float
    performance_context: float
    cultural_specificity: float
    language_notes: float
    tradition_review: float
    ethical_governance: float
    universalization_risk: float
    cultural_erasure_risk: float
    performance_omission: float
    variation_omission: float
    archive_bias: float
    community_sensitivity: float
    public_consequence: float
    owner: str
    status: str
