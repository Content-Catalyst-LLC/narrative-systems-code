from __future__ import annotations

from dataclasses import dataclass
from statistics import mean, pstdev


@dataclass(frozen=True)
class MythFunctionClaim:
    item: str
    claim_context: str
    mystical_function: float
    cosmological_function: float
    sociological_function: float
    pedagogical_function: float
    ritual_memory: float
    authority_clarity: float
    hierarchy_protection: float
    exclusion_risk: float
    coercive_compliance: float
    omission_risk: float
    power_invisibility: float
    accountability_marking: float
    source_context: float
    counterexample_inclusion: float
    method_limits: float
    ethics_governance: float
    uncertainty_notes: float
    community_sensitivity: float
    public_consequence: float
    owner: str
    status: str


def function_balance(claim: MythFunctionClaim) -> float:
    values = [
        claim.mystical_function,
        claim.cosmological_function,
        claim.sociological_function,
        claim.pedagogical_function,
    ]
    return max(0.0, 1 - (pstdev(values) / (mean(values) + 0.0001)))


def cultural_work(claim: MythFunctionClaim) -> float:
    return mean([
        claim.mystical_function,
        claim.cosmological_function,
        claim.sociological_function,
        claim.pedagogical_function,
        claim.ritual_memory,
        claim.authority_clarity,
    ])


def sociological_risk(claim: MythFunctionClaim) -> float:
    return min(
        1.0,
        claim.hierarchy_protection * 0.20
        + claim.exclusion_risk * 0.20
        + claim.coercive_compliance * 0.18
        + claim.omission_risk * 0.16
        + claim.power_invisibility * 0.16
        + (1 - claim.accountability_marking) * 0.10,
    )


def interpretation_readiness(claim: MythFunctionClaim) -> float:
    return mean([
        claim.source_context,
        claim.counterexample_inclusion,
        claim.method_limits,
        claim.ethics_governance,
        claim.accountability_marking,
        claim.uncertainty_notes,
    ])


def governance_priority_score(claim: MythFunctionClaim) -> float:
    return min(
        1.0,
        sociological_risk(claim) * 0.34
        + claim.community_sensitivity * 0.22
        + claim.public_consequence * 0.18
        + (1 - interpretation_readiness(claim)) * 0.16
        + (1 - claim.source_context) * 0.10,
    )


def review_priority(claim: MythFunctionClaim) -> str:
    risk = sociological_risk(claim)
    readiness = interpretation_readiness(claim)
    priority = governance_priority_score(claim)
    if claim.status == "revise" or risk >= 0.55 or priority >= 0.62 or readiness < 0.55:
        return "high"
    if claim.status == "review" or risk >= 0.40 or priority >= 0.48 or readiness < 0.68:
        return "medium"
    return "standard"
