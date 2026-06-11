from __future__ import annotations

from statistics import mean
from .models import DigitalStorytellingGovernanceConfig, DigitalStorytellingGovernanceRecord


def platform_narrative_integrity(record: DigitalStorytellingGovernanceRecord) -> float:
    return mean([
        record.context_preservation,
        record.source_authority,
        record.visibility_provenance_fit,
        record.audience_care,
        record.medium_format_fit,
        record.ethical_governance,
    ])


def context_collapse_risk(record: DigitalStorytellingGovernanceRecord) -> float:
    return min(
        1.0,
        record.audience_spread * 0.18
        + record.compression_severity * 0.16
        + record.hostile_context_exposure * 0.18
        + record.engagement_intensity * 0.14
        + record.sensitive_visibility * 0.18
        + (1 - record.governance_review) * 0.16,
    )


def platform_formula_drift(record: DigitalStorytellingGovernanceRecord) -> float:
    return min(
        1.0,
        record.hook_overdependence * 0.16
        + record.trend_compliance * 0.16
        + record.metric_pressure * 0.20
        + record.retention_framing * 0.16
        + record.outrage_signaling * 0.16
        + (1 - record.judgment_stability) * 0.16,
    )


def archive_memory_strength(record: DigitalStorytellingGovernanceRecord) -> float:
    return mean([
        record.archive_metadata,
        record.consent_status,
        record.preservation_plan,
        record.access_context,
        record.context_preservation,
        record.source_authority,
    ])


def ai_synthetic_story_risk(record: DigitalStorytellingGovernanceRecord) -> float:
    return min(
        1.0,
        record.synthetic_opacity * 0.18
        + record.voice_imitation * 0.18
        + record.provenance_loss * 0.18
        + record.ai_context_loss * 0.18
        + record.manipulation_targeting * 0.16
        + (1 - record.human_review) * 0.12,
    )


def governance_priority_score(record: DigitalStorytellingGovernanceRecord, config: DigitalStorytellingGovernanceConfig) -> float:
    score = (
        context_collapse_risk(record) * 0.20
        + platform_formula_drift(record) * 0.18
        + ai_synthetic_story_risk(record) * 0.22
        + (1 - platform_narrative_integrity(record)) * 0.16
        + (1 - archive_memory_strength(record)) * 0.10
        + record.public_consequence * 0.14
    )
    if record.status == "revise":
        score = max(score, config.high_threshold)
    elif record.status == "review":
        score = max(score, config.medium_threshold)
    return min(1.0, max(0.0, score))


def review_priority(record: DigitalStorytellingGovernanceRecord, config: DigitalStorytellingGovernanceConfig) -> str:
    score = governance_priority_score(record, config)
    if score >= config.high_threshold:
        return "high"
    if score >= config.medium_threshold:
        return "medium"
    return "standard"
