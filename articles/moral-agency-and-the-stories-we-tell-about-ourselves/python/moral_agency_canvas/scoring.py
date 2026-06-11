from __future__ import annotations

from statistics import mean

from .models import MoralAgencyConfig, MoralAgencyRecord


def moral_clarity(record: MoralAgencyRecord) -> float:
    return mean([
        record.action_naming,
        record.intention_distinction,
        record.consequence_clarity,
        record.harm_marking,
        record.repair_orientation,
        record.other_visibility,
    ])


def excuse_risk(record: MoralAgencyRecord) -> float:
    return min(
        1.0,
        record.context_overuse * 0.16
        + record.intention_shielding * 0.18
        + record.victimhood_shielding * 0.18
        + record.blame_shifting * 0.18
        + record.growth_substitution * 0.16
        + record.harm_minimization * 0.14,
    )


def repair_readiness(record: MoralAgencyRecord) -> float:
    return mean([
        record.harm_acknowledgment,
        record.apology_precision,
        record.material_response,
        record.conduct_change,
        record.future_accountability,
        record.third_party_oversight,
    ])


def interpretation_readiness(record: MoralAgencyRecord) -> float:
    return mean([
        record.source_context,
        record.evidence_visibility,
        record.uncertainty_notes,
        record.cultural_context,
        record.method_limits,
        record.review_owner_clarity,
    ])


def governance_priority_score(record: MoralAgencyRecord, config: MoralAgencyConfig) -> float:
    score = (
        excuse_risk(record) * 0.36
        + (1 - repair_readiness(record)) * 0.24
        + (1 - interpretation_readiness(record)) * 0.22
        + record.public_consequence * 0.18
    )
    if record.status == "revise":
        score = max(score, config.high_threshold)
    elif record.status == "review":
        score = max(score, config.medium_threshold)
    return min(1.0, max(0.0, score))


def review_priority(record: MoralAgencyRecord, config: MoralAgencyConfig) -> str:
    score = governance_priority_score(record, config)
    if score >= config.high_threshold:
        return "high"
    if score >= config.medium_threshold:
        return "medium"
    return "standard"
