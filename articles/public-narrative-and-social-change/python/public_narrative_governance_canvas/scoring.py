from __future__ import annotations

from statistics import mean
from .models import PublicNarrativeGovernanceConfig, PublicNarrativeGovernanceRecord


def public_narrative_coherence(record: PublicNarrativeGovernanceRecord) -> float:
    return mean([
        record.self_clarity,
        record.us_clarity,
        record.now_clarity,
        record.value_articulation,
        record.action_clarity,
        record.governance_review,
    ])


def mobilization_readiness(record: PublicNarrativeGovernanceRecord) -> float:
    return mean([
        record.diagnostic_frame,
        record.proposed_solution,
        record.resource_support,
        record.coalition_openness,
        record.tactical_action,
        record.feedback_loop,
    ])


def testimony_extraction_risk(record: PublicNarrativeGovernanceRecord) -> float:
    return min(
        1.0,
        record.consent_deficit * 0.18
        + record.emotional_targeting * 0.18
        + record.safety_risk * 0.18
        + record.reuse_uncertainty * 0.16
        + record.visibility_risk * 0.16
        + (1 - record.agency) * 0.14,
    )


def public_voice_integrity(record: PublicNarrativeGovernanceRecord) -> float:
    return mean([
        record.voice_plurality,
        record.affected_community_authority,
        record.evidence_visibility,
        record.coalition_openness,
        record.digital_context,
        record.governance_review,
    ])


def ai_public_narrative_risk(record: PublicNarrativeGovernanceRecord) -> float:
    return min(
        1.0,
        record.summary_dependence * 0.18
        + record.omitted_voices * 0.20
        + record.context_loss * 0.18
        + record.bias_reproduction * 0.16
        + record.uncertainty_erasure * 0.16
        + (1 - record.human_review) * 0.12,
    )


def governance_priority_score(record: PublicNarrativeGovernanceRecord, config: PublicNarrativeGovernanceConfig) -> float:
    score = (
        testimony_extraction_risk(record) * 0.22
        + ai_public_narrative_risk(record) * 0.20
        + (1 - public_narrative_coherence(record)) * 0.16
        + (1 - mobilization_readiness(record)) * 0.14
        + (1 - public_voice_integrity(record)) * 0.12
        + record.public_consequence * 0.16
    )
    if record.status == "revise":
        score = max(score, config.high_threshold)
    elif record.status == "review":
        score = max(score, config.medium_threshold)
    return min(1.0, max(0.0, score))


def review_priority(record: PublicNarrativeGovernanceRecord, config: PublicNarrativeGovernanceConfig) -> str:
    score = governance_priority_score(record, config)
    if score >= config.high_threshold:
        return "high"
    if score >= config.medium_threshold:
        return "medium"
    return "standard"
