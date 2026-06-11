from __future__ import annotations

from statistics import mean

from .models import PublicStoryGovernanceConfig, PublicStoryGovernanceRecord


def public_narrative_strength(record: PublicStoryGovernanceRecord) -> float:
    return mean([
        record.self_story_evidence,
        record.shared_value_clarity,
        record.now_challenge_clarity,
        record.agency,
        record.hope,
        record.responsibility,
    ])


def mythic_simplification_risk(record: PublicStoryGovernanceRecord) -> float:
    return min(
        1.0,
        record.enemy_simplification * 0.18
        + record.boundary_hardening * 0.18
        + record.crisis_compression * 0.17
        + record.urgency_pressure * 0.16
        + record.scapegoat_intensity * 0.17
        + (1 - record.evidence_visibility) * 0.14,
    )


def civil_religion_accountability(record: PublicStoryGovernanceRecord) -> float:
    return mean([
        record.memory_plurality,
        record.historical_truthfulness,
        record.public_limit_clarity,
        record.dissent_space,
        record.repair_justice,
        record.anti_idolatry_critique,
    ])


def testimony_ethics(record: PublicStoryGovernanceRecord) -> float:
    return mean([
        record.witness_care,
        record.testimony_context,
        record.harm_visibility,
        record.extraction_resistance,
        record.responsibility,
        record.repair_justice,
    ])


def ai_public_rhetoric_risk(record: PublicStoryGovernanceRecord) -> float:
    return min(
        1.0,
        record.formulaic_default * 0.18
        + record.outrage_intensity * 0.18
        + record.resolution_smoothing * 0.16
        + record.identity_boundary_pressure * 0.18
        + record.context_missingness * 0.16
        + (1 - record.human_governance) * 0.14,
    )


def governance_priority_score(record: PublicStoryGovernanceRecord, config: PublicStoryGovernanceConfig) -> float:
    score = (
        mythic_simplification_risk(record) * 0.30
        + ai_public_rhetoric_risk(record) * 0.24
        + (1 - civil_religion_accountability(record)) * 0.14
        + (1 - testimony_ethics(record)) * 0.12
        + record.public_consequence * 0.20
    )
    if record.status == "revise":
        score = max(score, config.high_threshold)
    elif record.status == "review":
        score = max(score, config.medium_threshold)
    return min(1.0, max(0.0, score))


def review_priority(record: PublicStoryGovernanceRecord, config: PublicStoryGovernanceConfig) -> str:
    score = governance_priority_score(record, config)
    if score >= config.high_threshold:
        return "high"
    if score >= config.medium_threshold:
        return "medium"
    return "standard"
