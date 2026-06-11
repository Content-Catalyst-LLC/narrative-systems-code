from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class ComparativeMythClaim:
    item: str
    claim_context: str
    departure_pattern: float
    threshold_crossing: float
    ordeal_or_trial: float
    helper_presence: float
    return_pattern: float
    boon_or_renewal: float
    language_notes: float
    ritual_context: float
    historical_context: float
    community_authority: float
    source_tradition: float
    performance_or_oral_context: float
    universal_claim_strength: float
    selective_evidence: float
    context_loss: float
    formula_reduction: float
    ethical_risk: float
    counterexample_inclusion: float
    method_limits: float
    ritual_verification: float
    ethics_governance: float
    uncertainty_marking: float
    community_sensitivity: float
    public_consequence: float
    owner: str
    status: str
