from __future__ import annotations

from statistics import mean

from .models import ComparativeMythClaim


def comparative_pattern(claim: ComparativeMythClaim) -> float:
    return mean([
        claim.departure_pattern,
        claim.threshold_crossing,
        claim.ordeal_or_trial,
        claim.helper_presence,
        claim.return_pattern,
        claim.boon_or_renewal,
    ])


def cultural_specificity(claim: ComparativeMythClaim) -> float:
    return mean([
        claim.language_notes,
        claim.ritual_context,
        claim.historical_context,
        claim.community_authority,
        claim.source_tradition,
        claim.performance_or_oral_context,
    ])


def generalization_risk(claim: ComparativeMythClaim) -> float:
    return min(
        1.0,
        claim.universal_claim_strength * 0.18
        + claim.selective_evidence * 0.18
        + claim.context_loss * 0.18
        + claim.formula_reduction * 0.16
        + claim.ethical_risk * 0.16
        + (1 - claim.counterexample_inclusion) * 0.14,
    )


def interpretation_readiness(claim: ComparativeMythClaim) -> float:
    return mean([
        cultural_specificity(claim),
        claim.counterexample_inclusion,
        claim.method_limits,
        claim.ritual_verification,
        claim.ethics_governance,
        claim.uncertainty_marking,
    ])


def governance_priority_score(claim: ComparativeMythClaim) -> float:
    return min(
        1.0,
        generalization_risk(claim) * 0.35
        + claim.community_sensitivity * 0.25
        + claim.public_consequence * 0.20
        + (1 - interpretation_readiness(claim)) * 0.20,
    )


def review_priority(claim: ComparativeMythClaim) -> str:
    risk = generalization_risk(claim)
    priority = governance_priority_score(claim)
    readiness = interpretation_readiness(claim)

    if claim.status == "revise" or risk >= 0.55 or priority >= 0.62 or readiness < 0.55:
        return "high"
    if claim.status == "review" or risk >= 0.40 or priority >= 0.48 or readiness < 0.68:
        return "medium"
    return "standard"
