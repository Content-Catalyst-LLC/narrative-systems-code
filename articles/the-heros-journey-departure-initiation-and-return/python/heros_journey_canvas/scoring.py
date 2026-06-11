from __future__ import annotations

from dataclasses import dataclass
from statistics import mean


@dataclass(frozen=True)
class HerosJourneyClaim:
    item: str
    claim_context: str
    departure_pattern: float
    threshold_crossing: float
    initiation_trial: float
    descent_symbolic_death: float
    boon: float
    return_pattern: float
    transformation_depth: float
    return_responsibility: float
    specificity_preservation: float
    stage_literalism: float
    beat_matching: float
    context_loss: float
    overfitting: float
    universal_claim_strength: float
    counterexample_inclusion: float
    method_limits: float
    ethics_governance: float
    uncertainty_marking: float
    community_sensitivity: float
    public_consequence: float
    owner: str
    status: str


def journey_structure(claim: HerosJourneyClaim) -> float:
    return mean([
        claim.departure_pattern,
        claim.threshold_crossing,
        claim.initiation_trial,
        claim.descent_symbolic_death,
        claim.boon,
        claim.return_pattern,
    ])


def formula_drift(claim: HerosJourneyClaim) -> float:
    return min(
        1.0,
        claim.stage_literalism * 0.18
        + claim.beat_matching * 0.18
        + claim.context_loss * 0.18
        + claim.overfitting * 0.16
        + claim.universal_claim_strength * 0.16
        + (1 - claim.counterexample_inclusion) * 0.14,
    )


def interpretation_readiness(claim: HerosJourneyClaim) -> float:
    return mean([
        claim.specificity_preservation,
        claim.counterexample_inclusion,
        claim.method_limits,
        claim.ethics_governance,
        claim.uncertainty_marking,
    ])


def governance_priority_score(claim: HerosJourneyClaim) -> float:
    return min(
        1.0,
        formula_drift(claim) * 0.30
        + claim.community_sensitivity * 0.22
        + claim.public_consequence * 0.18
        + (1 - claim.return_responsibility) * 0.15
        + (1 - interpretation_readiness(claim)) * 0.15,
    )


def review_priority(claim: HerosJourneyClaim) -> str:
    drift = formula_drift(claim)
    readiness = interpretation_readiness(claim)
    priority = governance_priority_score(claim)
    if claim.status == "revise" or drift >= 0.55 or priority >= 0.62 or readiness < 0.55:
        return "high"
    if claim.status == "review" or drift >= 0.40 or priority >= 0.48 or readiness < 0.68:
        return "medium"
    return "standard"
