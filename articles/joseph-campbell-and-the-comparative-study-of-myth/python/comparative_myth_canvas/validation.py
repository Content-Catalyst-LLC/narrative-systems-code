from __future__ import annotations

from .models import ComparativeMythClaim


SCORE_FIELDS = [
    "departure_pattern",
    "threshold_crossing",
    "ordeal_or_trial",
    "helper_presence",
    "return_pattern",
    "boon_or_renewal",
    "language_notes",
    "ritual_context",
    "historical_context",
    "community_authority",
    "source_tradition",
    "performance_or_oral_context",
    "universal_claim_strength",
    "selective_evidence",
    "context_loss",
    "formula_reduction",
    "ethical_risk",
    "counterexample_inclusion",
    "method_limits",
    "ritual_verification",
    "ethics_governance",
    "uncertainty_marking",
    "community_sensitivity",
    "public_consequence",
]


def validate_comparative_myth_claim(claim: ComparativeMythClaim) -> None:
    if not claim.item.strip():
        raise ValueError("Item name is required.")
    if not claim.claim_context.strip():
        raise ValueError("Claim context is required.")
    for field in SCORE_FIELDS:
        value = getattr(claim, field)
        if value < 0 or value > 1:
            raise ValueError(f"{field} must be between 0 and 1.")
