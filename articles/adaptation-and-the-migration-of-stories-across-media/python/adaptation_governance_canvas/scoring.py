from __future__ import annotations

from statistics import mean
from .models import AdaptationGovernanceConfig, AdaptationGovernanceRecord


def adaptation_integrity(record: AdaptationGovernanceRecord) -> float:
    return mean([
        record.source_core_preservation,
        record.medium_fit,
        record.transformation_purpose,
        record.context_preservation,
        record.reception_value,
        record.ethical_governance,
    ])


def transfer_loss(record: AdaptationGovernanceRecord) -> float:
    return min(
        1.0,
        record.voice_loss * 0.18
        + record.interiority_loss * 0.16
        + record.context_loss * 0.20
        + record.provenance_loss * 0.18
        + record.agency_loss * 0.16
        + (1 - record.governance_review) * 0.12,
    )


def franchise_drift(record: AdaptationGovernanceRecord) -> float:
    return min(
        1.0,
        record.repetition_compliance * 0.18
        + record.lore_excess * 0.18
        + record.nostalgia_reliance * 0.16
        + record.continuity_saturation * 0.16
        + record.market_overextension * 0.16
        + (1 - record.story_purpose) * 0.16,
    )


def ai_adaptation_risk(record: AdaptationGovernanceRecord) -> float:
    return min(
        1.0,
        record.plot_summary_dependence * 0.18
        + record.voice_style_imitation * 0.20
        + record.context_loss * 0.18
        + record.synthetic_opacity * 0.16
        + record.uncertainty_erasure * 0.16
        + (1 - record.human_review) * 0.12,
    )


def consent_and_context_strength(record: AdaptationGovernanceRecord) -> float:
    return mean([
        record.consent_clarity,
        record.source_authority,
        record.cultural_context,
        record.context_preservation,
        1 - record.provenance_loss,
        record.governance_review,
    ])


def governance_priority_score(record: AdaptationGovernanceRecord, config: AdaptationGovernanceConfig) -> float:
    score = (
        transfer_loss(record) * 0.22
        + franchise_drift(record) * 0.16
        + ai_adaptation_risk(record) * 0.20
        + (1 - adaptation_integrity(record)) * 0.16
        + (1 - consent_and_context_strength(record)) * 0.12
        + record.public_consequence * 0.14
    )
    if record.status == "revise":
        score = max(score, config.high_threshold)
    elif record.status == "review":
        score = max(score, config.medium_threshold)
    return min(1.0, max(0.0, score))


def review_priority(record: AdaptationGovernanceRecord, config: AdaptationGovernanceConfig) -> str:
    score = governance_priority_score(record, config)
    if score >= config.high_threshold:
        return "high"
    if score >= config.medium_threshold:
        return "medium"
    return "standard"
