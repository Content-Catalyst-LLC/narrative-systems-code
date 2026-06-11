from __future__ import annotations

from statistics import mean

from .models import MonomythClaim


def monomyth_pattern(claim: MonomythClaim) -> float:
    return mean([
        claim.departure_pattern,
        claim.threshold_crossing,
        claim.initiation_trial,
        claim.descent_symbolic_death,
        claim.boon,
        claim.return_pattern,
    ])


def specificity_preservation(claim: MonomythClaim) -> float:
    return mean([
        claim.language_notes,
        claim.cultural_tradition,
        claim.ritual_context,
        claim.historical_context,
        claim.oral_performance_context,
        claim.authority_notes,
    ])


def formula_drift(claim: MonomythClaim) -> float:
    return min(
        1.0,
        claim.stage_literalism * 0.18
        + claim.beat_matching * 0.18
        + claim.context_loss * 0.18
        + claim.overfitting * 0.16
        + claim.universal_claim_strength * 0.16
        + (1 - claim.counterexample_inclusion) * 0.14,
    )


def interpretation_readiness(claim: MonomythClaim) -> float:
    return mean([
        specificity_preservation(claim),
        claim.counterexample_inclusion,
        claim.method_limits,
        claim.ethics_governance,
        claim.ritual_verification,
        claim.uncertainty_marking,
    ])


def governance_priority_score(claim: MonomythClaim) -> float:
    return min(
        1.0,
        formula_drift(claim) * 0.35
        + claim.community_sensitivity * 0.25
        + claim.public_consequence * 0.20
        + (1 - interpretation_readiness(claim)) * 0.20,
    )


def review_priority(claim: MonomythClaim) -> str:
    drift = formula_drift(claim)
    priority = governance_priority_score(claim)
    readiness = interpretation_readiness(claim)

    if claim.status == "revise" or drift >= 0.55 or priority >= 0.62 or readiness < 0.55:
        return "high"
    if claim.status == "review" or drift >= 0.40 or priority >= 0.48 or readiness < 0.68:
        return "medium"
    return "standard"
