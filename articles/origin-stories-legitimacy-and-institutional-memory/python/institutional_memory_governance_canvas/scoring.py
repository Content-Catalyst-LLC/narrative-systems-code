from __future__ import annotations

from statistics import mean
from .models import InstitutionalMemoryGovernanceConfig, InstitutionalMemoryGovernanceRecord


def legitimacy_alignment(record: InstitutionalMemoryGovernanceRecord) -> float:
    return mean([
        record.purpose_clarity,
        record.mission_action_alignment,
        record.record_evidence,
        record.affected_community_testimony,
        record.conduct_visibility,
        record.governance_openness,
    ])


def origin_myth_risk(record: InstitutionalMemoryGovernanceRecord) -> float:
    return min(
        1.0,
        record.founder_heroization * 0.18
        + record.exclusion_omission * 0.18
        + record.harm_removal * 0.18
        + record.commemoration_saturation * 0.14
        + record.reputational_branding * 0.16
        + (1 - record.voice_multiplicity) * 0.16,
    )


def institutional_memory_strength(record: InstitutionalMemoryGovernanceRecord) -> float:
    return mean([
        record.record_preservation,
        record.archive_completeness,
        record.metadata_quality,
        record.testimony_stewardship,
        record.knowledge_retention,
        record.public_access,
    ])


def reform_credibility(record: InstitutionalMemoryGovernanceRecord) -> float:
    return mean([
        record.harm_naming,
        record.structural_change,
        record.evidence_release,
        record.material_repair,
        record.oversight,
        record.transparent_progress,
    ])


def ai_memory_distortion_risk(record: InstitutionalMemoryGovernanceRecord) -> float:
    return min(
        1.0,
        record.ai_summary_dependence * 0.24
        + record.archive_bias_risk * 0.24
        + record.context_loss * 0.22
        + (1 - record.correction_pathway) * 0.16
        + (1 - record.public_access) * 0.14,
    )


def governance_priority_score(record: InstitutionalMemoryGovernanceRecord, config: InstitutionalMemoryGovernanceConfig) -> float:
    score = (
        origin_myth_risk(record) * 0.30
        + ai_memory_distortion_risk(record) * 0.18
        + (1 - legitimacy_alignment(record)) * 0.18
        + (1 - institutional_memory_strength(record)) * 0.14
        + (1 - reform_credibility(record)) * 0.10
        + record.public_consequence * 0.10
    )
    if record.status == "revise":
        score = max(score, config.high_threshold)
    elif record.status == "review":
        score = max(score, config.medium_threshold)
    return min(1.0, max(0.0, score))


def review_priority(record: InstitutionalMemoryGovernanceRecord, config: InstitutionalMemoryGovernanceConfig) -> str:
    score = governance_priority_score(record, config)
    if score >= config.high_threshold:
        return "high"
    if score >= config.medium_threshold:
        return "medium"
    return "standard"
