from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class MonomythClaim:
    item: str
    claim_context: str
    departure_pattern: float
    threshold_crossing: float
    initiation_trial: float
    descent_symbolic_death: float
    boon: float
    return_pattern: float
    language_notes: float
    cultural_tradition: float
    ritual_context: float
    historical_context: float
    oral_performance_context: float
    authority_notes: float
    stage_literalism: float
    beat_matching: float
    context_loss: float
    overfitting: float
    universal_claim_strength: float
    counterexample_inclusion: float
    method_limits: float
    ethics_governance: float
    ritual_verification: float
    uncertainty_marking: float
    community_sensitivity: float
    public_consequence: float
    owner: str
    status: str
