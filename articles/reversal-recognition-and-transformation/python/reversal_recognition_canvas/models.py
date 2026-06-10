from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class ReversalRecognitionItem:
    item: str
    story_type: str
    preparation_trace: float
    causal_linkage: float
    state_change: float
    earned_surprise: float
    action_fit: float
    knowledge_reorientation: float
    evidence_visibility: float
    interpretive_support: float
    meaning_revision: float
    relation_linkage: float
    uncertainty_clarity: float
    identity_change: float
    action_consequence: float
    relationship_change: float
    value_change: float
    future_possibility: float
    governance_accountability: float
    false_recognition: float
    arbitrary_twist: float
    closure_pressure: float
    evidence_omission: float
    audience_sensitivity: float
    public_consequence: float
    owner: str
    status: str
