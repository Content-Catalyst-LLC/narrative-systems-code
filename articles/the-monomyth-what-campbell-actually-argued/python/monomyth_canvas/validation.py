from __future__ import annotations

from .models import MonomythClaim


SCORE_FIELDS = [
    "departure_pattern",
    "threshold_crossing",
    "initiation_trial",
    "descent_symbolic_death",
    "boon",
    "return_pattern",
    "language_notes",
    "cultural_tradition",
    "ritual_context",
    "historical_context",
    "oral_performance_context",
    "authority_notes",
    "stage_literalism",
    "beat_matching",
    "context_loss",
    "overfitting",
    "universal_claim_strength",
    "counterexample_inclusion",
    "method_limits",
    "ethics_governance",
    "ritual_verification",
    "uncertainty_marking",
    "community_sensitivity",
    "public_consequence",
]


def validate_monomyth_claim(claim: MonomythClaim) -> None:
    if not claim.item.strip():
        raise ValueError("Item name is required.")
    if not claim.claim_context.strip():
        raise ValueError("Claim context is required.")
    for field in SCORE_FIELDS:
        value = getattr(claim, field)
        if value < 0 or value > 1:
            raise ValueError(f"{field} must be between 0 and 1.")
