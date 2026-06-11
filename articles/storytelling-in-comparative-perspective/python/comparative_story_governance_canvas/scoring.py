from __future__ import annotations

from statistics import mean
from .models import ComparativeStoryGovernanceConfig, ComparativeStoryGovernanceRecord


def comparative_integrity(record: ComparativeStoryGovernanceRecord) -> float:
    return mean([
        record.source_context,
        record.difference_preservation,
        record.evidence_quality,
        record.translation_reliability,
        record.protocol_compliance,
        record.human_review,
    ])


def flattening_risk(record: ComparativeStoryGovernanceRecord) -> float:
    return min(
        1.0,
        record.universalism_claims * 0.18
        + record.template_capture * 0.18
        + record.context_loss * 0.18
        + record.archive_bias * 0.16
        + record.power_imbalance * 0.16
        + (1 - record.difference_preservation) * 0.14,
    )


def transmission_uncertainty(record: ComparativeStoryGovernanceRecord) -> float:
    return min(
        1.0,
        record.language_gap * 0.18
        + record.media_shift * 0.16
        + record.archive_gap * 0.18
        + record.performance_loss * 0.18
        + record.restricted_source_concern * 0.14
        + (1 - record.version_documentation) * 0.16,
    )


def contextual_grounding(record: ComparativeStoryGovernanceRecord) -> float:
    return mean([
        record.local_interpretation,
        record.community_review,
        record.attribution_quality,
        record.corpus_balance,
        record.source_context,
        record.protocol_compliance,
    ])


def ai_comparative_risk(record: ComparativeStoryGovernanceRecord) -> float:
    return min(
        1.0,
        record.biased_corpus * 0.18
        + record.hallucinated_source_risk * 0.18
        + record.ai_translation_loss * 0.18
        + record.sacred_material_risk * 0.18
        + record.overgeneralized_claims * 0.16
        + (1 - record.expert_review) * 0.12,
    )


def governance_priority_score(record: ComparativeStoryGovernanceRecord, config: ComparativeStoryGovernanceConfig) -> float:
    score = (
        flattening_risk(record) * 0.22
        + transmission_uncertainty(record) * 0.16
        + ai_comparative_risk(record) * 0.20
        + (1 - comparative_integrity(record)) * 0.16
        + (1 - contextual_grounding(record)) * 0.12
        + record.public_consequence * 0.14
    )
    if record.status == "revise":
        score = max(score, config.high_threshold)
    elif record.status == "review":
        score = max(score, config.medium_threshold)
    return min(1.0, max(0.0, score))


def review_priority(record: ComparativeStoryGovernanceRecord, config: ComparativeStoryGovernanceConfig) -> str:
    score = governance_priority_score(record, config)
    if score >= config.high_threshold:
        return "high"
    if score >= config.medium_threshold:
        return "medium"
    return "standard"
