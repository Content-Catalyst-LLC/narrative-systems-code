from __future__ import annotations

from statistics import mean
from .models import RhetoricalMovesGovernanceConfig, RhetoricalMovesGovernanceRecord


def rhetorical_integrity(record: RhetoricalMovesGovernanceRecord) -> float:
    return mean([
        record.evidence_truthfulness,
        record.proportionality,
        record.context_adequacy,
        record.dignity_protection,
        record.audience_agency,
        record.transparency,
    ])


def manipulation_risk(record: RhetoricalMovesGovernanceRecord) -> float:
    return min(
        1.0,
        record.fear_amplification * 0.18
        + record.emotional_exploitation * 0.18
        + record.omission_of_context * 0.18
        + record.social_proof_pressure * 0.16
        + record.urgency_coercion * 0.16
        + (1 - record.judgment_review) * 0.14,
    )


def audience_agency_score(record: RhetoricalMovesGovernanceRecord) -> float:
    return mean([
        record.claim_clarity,
        record.uncertainty_disclosure,
        record.tradeoff_openness,
        record.evidence_visibility,
        record.response_optionality,
        record.question_space,
    ])


def platform_persuasion_risk(record: RhetoricalMovesGovernanceRecord) -> float:
    return min(
        1.0,
        record.platform_amplification * 0.24
        + record.microtargeting_intensity * 0.24
        + record.context_collapse_risk * 0.22
        + (1 - record.sponsorship_clarity) * 0.14
        + record.social_proof_pressure * 0.16,
    )


def ai_persuasion_risk(record: RhetoricalMovesGovernanceRecord) -> float:
    return min(
        1.0,
        record.personalization_targeting * 0.18
        + record.vulnerability_exploitation * 0.20
        + record.synthetic_evidence_risk * 0.20
        + record.opaque_testing * 0.16
        + record.data_opacity * 0.14
        + (1 - record.human_review) * 0.12,
    )


def governance_priority_score(record: RhetoricalMovesGovernanceRecord, config: RhetoricalMovesGovernanceConfig) -> float:
    score = (
        manipulation_risk(record) * 0.22
        + platform_persuasion_risk(record) * 0.16
        + ai_persuasion_risk(record) * 0.20
        + (1 - rhetorical_integrity(record)) * 0.16
        + (1 - audience_agency_score(record)) * 0.12
        + record.public_consequence * 0.14
    )
    if record.status == "revise":
        score = max(score, config.high_threshold)
    elif record.status == "review":
        score = max(score, config.medium_threshold)
    return min(1.0, max(0.0, score))


def review_priority(record: RhetoricalMovesGovernanceRecord, config: RhetoricalMovesGovernanceConfig) -> str:
    score = governance_priority_score(record, config)
    if score >= config.high_threshold:
        return "high"
    if score >= config.medium_threshold:
        return "medium"
    return "standard"
