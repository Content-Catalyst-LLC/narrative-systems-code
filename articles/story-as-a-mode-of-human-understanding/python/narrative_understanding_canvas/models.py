from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class NarrativeUnderstandingItem:
    item: str
    story_type: str
    sequence_clarity: float
    causal_framing: float
    agency_mapping: float
    memory_integration: float
    evidence_support: float
    openness_to_revision: float
    consequence_visibility: float
    harm_recognition: float
    responsibility_mapping: float
    repair_awareness: float
    alternative_logic: float
    uncertainty_signaling: float
    interpretive_diversity: float
    hindsight_bias: float
    false_coherence: float
    selection_bias: float
    closure_pressure: float
    owner: str
    status: str
