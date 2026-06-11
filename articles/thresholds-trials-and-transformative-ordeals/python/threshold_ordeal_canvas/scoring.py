from __future__ import annotations

from dataclasses import dataclass
from statistics import mean


@dataclass(frozen=True)
class ThresholdOrdealClaim:
    item: str
    claim_context: str
    threshold_strength: float
    trial_depth: float
    ordeal_transformation: float
    harm_romanticization: float
    suffering_spectacle: float
    forced_closure: float
    context_loss: float
    power_hiding: float
    unresolved_marking: float
    specificity_preservation: float
    counterexample_inclusion: float
    method_limits: float
    ethics_governance: float
    uncertainty_marking: float
    community_sensitivity: float
    public_consequence: float
    owner: str
    status: str


def ethical_risk(claim: ThresholdOrdealClaim) -> float:
    return min(
        1.0,
        claim.harm_romanticization * 0.20
        + claim.suffering_spectacle * 0.18
        + claim.forced_closure * 0.18
        + claim.context_loss * 0.16
        + claim.power_hiding * 0.16
        + (1 - claim.unresolved_marking) * 0.12,
    )


def interpretation_readiness(claim: ThresholdOrdealClaim) -> float:
    return mean([
        claim.specificity_preservation,
        claim.counterexample_inclusion,
        claim.method_limits,
        claim.ethics_governance,
        claim.uncertainty_marking,
    ])


def governance_priority_score(claim: ThresholdOrdealClaim) -> float:
    return min(
        1.0,
        ethical_risk(claim) * 0.32
        + claim.community_sensitivity * 0.22
        + claim.public_consequence * 0.18
        + (1 - claim.ordeal_transformation) * 0.14
        + (1 - interpretation_readiness(claim)) * 0.14,
    )


def review_priority(claim: ThresholdOrdealClaim) -> str:
    risk = ethical_risk(claim)
    readiness = interpretation_readiness(claim)
    priority = governance_priority_score(claim)
    if claim.status == "revise" or risk >= 0.55 or priority >= 0.62 or readiness < 0.55:
        return "high"
    if claim.status == "review" or risk >= 0.40 or priority >= 0.48 or readiness < 0.68:
        return "medium"
    return "standard"
