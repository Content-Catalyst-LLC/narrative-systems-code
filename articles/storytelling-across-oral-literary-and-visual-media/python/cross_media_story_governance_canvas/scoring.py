from __future__ import annotations

from statistics import mean
from .models import CrossMediaStoryGovernanceConfig, CrossMediaStoryGovernanceRecord


def medium_affordance_fit(record: CrossMediaStoryGovernanceRecord) -> float:
    return mean([
        record.embodiment,
        record.interior_depth,
        record.spatial_quality,
        record.temporal_control,
        record.audience_relation,
        record.contextual_fit,
    ])


def media_transfer_risk(record: CrossMediaStoryGovernanceRecord) -> float:
    return min(
        1.0,
        record.voice_loss * 0.18
        + record.context_loss * 0.20
        + record.provenance_loss * 0.18
        + record.audience_shift * 0.14
        + record.representational_distortion * 0.18
        + (1 - record.governance_review) * 0.12,
    )


def multimodal_coherence(record: CrossMediaStoryGovernanceRecord) -> float:
    return mean([
        record.text_image_integration,
        record.image_sequence_logic,
        record.sound_design_alignment,
        record.rhythm_harmony,
        record.provenance_visibility,
        record.uncertainty_notation,
    ])


def consent_and_context_strength(record: CrossMediaStoryGovernanceRecord) -> float:
    return mean([
        record.consent_clarity,
        record.source_authority,
        record.cultural_context,
        record.reuse_boundaries,
        record.provenance_visibility,
        record.governance_review,
    ])


def ai_cross_media_risk(record: CrossMediaStoryGovernanceRecord) -> float:
    return min(
        1.0,
        record.synthetic_documentary_ambiguity * 0.20
        + record.context_loss * 0.18
        + record.provenance_opacity * 0.18
        + record.voice_likeness_imitation * 0.16
        + record.bias_reproduction * 0.16
        + (1 - record.human_review) * 0.12,
    )


def governance_priority_score(record: CrossMediaStoryGovernanceRecord, config: CrossMediaStoryGovernanceConfig) -> float:
    score = (
        media_transfer_risk(record) * 0.24
        + ai_cross_media_risk(record) * 0.22
        + (1 - medium_affordance_fit(record)) * 0.14
        + (1 - multimodal_coherence(record)) * 0.14
        + (1 - consent_and_context_strength(record)) * 0.12
        + record.public_consequence * 0.14
    )
    if record.status == "revise":
        score = max(score, config.high_threshold)
    elif record.status == "review":
        score = max(score, config.medium_threshold)
    return min(1.0, max(0.0, score))


def review_priority(record: CrossMediaStoryGovernanceRecord, config: CrossMediaStoryGovernanceConfig) -> str:
    score = governance_priority_score(record, config)
    if score >= config.high_threshold:
        return "high"
    if score >= config.medium_threshold:
        return "medium"
    return "standard"
