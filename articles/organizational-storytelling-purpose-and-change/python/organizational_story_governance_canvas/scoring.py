from __future__ import annotations

from statistics import mean
from .models import OrganizationalStoryGovernanceConfig, OrganizationalStoryGovernanceRecord


def purpose_alignment(record: OrganizationalStoryGovernanceRecord) -> float:
    return mean([
        record.mission_clarity,
        record.decision_alignment,
        record.budget_fit,
        record.stakeholder_impact,
        record.employee_experience,
        record.governance_transparency,
    ])


def change_credibility(record: OrganizationalStoryGovernanceRecord) -> float:
    return mean([
        record.evidence_visibility,
        record.participation_integrity,
        record.resource_support,
        record.loss_acknowledgment,
        record.feedback_loops,
        record.accountability_measures,
    ])


def narrative_extraction_risk(record: OrganizationalStoryGovernanceRecord) -> float:
    return min(
        1.0,
        record.consent_deficit * 0.18
        + record.selection_bias * 0.16
        + record.power_asymmetry * 0.18
        + record.emotional_targeting * 0.16
        + record.brand_repurposing * 0.16
        + (1 - record.agency) * 0.16,
    )


def employee_voice_integrity(record: OrganizationalStoryGovernanceRecord) -> float:
    return mean([
        record.employee_experience,
        record.employee_voice_protection,
        record.dissent_visibility,
        record.feedback_loops,
        record.learning_followthrough,
        record.governance_transparency,
    ])


def organizational_memory_strength(record: OrganizationalStoryGovernanceRecord) -> float:
    return mean([
        record.memory_preservation,
        record.learning_followthrough,
        record.evidence_visibility,
        record.feedback_loops,
        record.dissent_visibility,
        record.accountability_measures,
    ])


def ai_organizational_story_risk(record: OrganizationalStoryGovernanceRecord) -> float:
    return min(
        1.0,
        record.summary_dependence * 0.18
        + record.omitted_dissent * 0.20
        + record.context_loss * 0.18
        + record.privacy_risk * 0.16
        + record.uncertainty_erasure * 0.16
        + (1 - record.human_review) * 0.12,
    )


def governance_priority_score(record: OrganizationalStoryGovernanceRecord, config: OrganizationalStoryGovernanceConfig) -> float:
    score = (
        narrative_extraction_risk(record) * 0.22
        + ai_organizational_story_risk(record) * 0.20
        + (1 - purpose_alignment(record)) * 0.16
        + (1 - change_credibility(record)) * 0.14
        + (1 - employee_voice_integrity(record)) * 0.12
        + (1 - organizational_memory_strength(record)) * 0.06
        + record.public_consequence * 0.10
    )
    if record.status == "revise":
        score = max(score, config.high_threshold)
    elif record.status == "review":
        score = max(score, config.medium_threshold)
    return min(1.0, max(0.0, score))


def review_priority(record: OrganizationalStoryGovernanceRecord, config: OrganizationalStoryGovernanceConfig) -> str:
    score = governance_priority_score(record, config)
    if score >= config.high_threshold:
        return "high"
    if score >= config.medium_threshold:
        return "medium"
    return "standard"
