from __future__ import annotations

from statistics import mean
from .models import NationalMemoryGovernanceConfig, NationalMemoryGovernanceRecord


def memory_plurality(record: NationalMemoryGovernanceRecord) -> float:
    return mean([
        record.group_representation,
        record.source_diversity,
        record.testimony_visibility,
        record.archive_coverage,
        record.countermemory_inclusion,
        record.dissent_space,
    ])


def national_myth_risk(record: NationalMemoryGovernanceRecord) -> float:
    return min(
        1.0,
        record.hero_compression * 0.17
        + record.innocence_story * 0.18
        + record.exclusion_omission * 0.18
        + record.victimhood_monopoly * 0.15
        + record.purity_symbolism * 0.14
        + (1 - record.revision_capacity) * 0.18,
    )


def memory_accountability(record: NationalMemoryGovernanceRecord) -> float:
    return mean([
        record.evidence_visibility,
        record.provenance_reliability,
        record.record_access,
        record.testimony_care,
        record.contextual_explanation,
        record.repair_linkage,
    ])


def public_memory_infrastructure(record: NationalMemoryGovernanceRecord) -> float:
    return mean([
        record.curriculum_balance,
        record.monument_context,
        record.platform_context,
        record.archive_coverage,
        record.record_access,
        record.dissent_space,
    ])


def ai_memory_risk(record: NationalMemoryGovernanceRecord) -> float:
    return min(
        1.0,
        record.summary_dependence * 0.18
        + record.context_loss * 0.18
        + record.dominant_archive_bias * 0.18
        + record.uncertainty_erasure * 0.16
        + record.omission_of_minority_memory * 0.16
        + (1 - record.human_review) * 0.14,
    )


def governance_priority_score(record: NationalMemoryGovernanceRecord, config: NationalMemoryGovernanceConfig) -> float:
    score = (
        national_myth_risk(record) * 0.30
        + ai_memory_risk(record) * 0.20
        + (1 - memory_plurality(record)) * 0.18
        + (1 - memory_accountability(record)) * 0.14
        + (1 - public_memory_infrastructure(record)) * 0.08
        + record.public_consequence * 0.10
    )
    if record.status == "revise":
        score = max(score, config.high_threshold)
    elif record.status == "review":
        score = max(score, config.medium_threshold)
    return min(1.0, max(0.0, score))


def review_priority(record: NationalMemoryGovernanceRecord, config: NationalMemoryGovernanceConfig) -> str:
    score = governance_priority_score(record, config)
    if score >= config.high_threshold:
        return "high"
    if score >= config.medium_threshold:
        return "medium"
    return "standard"
