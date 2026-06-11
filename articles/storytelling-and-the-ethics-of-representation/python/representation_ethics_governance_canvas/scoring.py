from __future__ import annotations

from statistics import mean
from .models import RepresentationEthicsGovernanceConfig, RepresentationEthicsGovernanceRecord


def representation_integrity(record: RepresentationEthicsGovernanceRecord) -> float:
    return mean([
        record.voice_agency,
        record.context_preservation,
        record.dignity_protection,
        record.source_accuracy,
        record.provenance_visibility,
        record.accountability_capacity,
    ])


def representation_risk(record: RepresentationEthicsGovernanceRecord) -> float:
    return min(
        1.0,
        record.stereotype_tendency * 0.18
        + record.exposure_risk * 0.18
        + record.context_loss * 0.18
        + record.voice_replacement * 0.16
        + record.power_asymmetry * 0.16
        + (1 - record.governance_review) * 0.14,
    )


def consent_adequacy(record: RepresentationEthicsGovernanceRecord) -> float:
    return mean([
        record.informed_consent,
        record.ongoing_consent,
        record.use_clarity,
        record.platform_circulation_clarity,
        record.withdrawal_clarity,
        record.reuse_ai_clarity,
    ])


def cultural_and_visual_strength(record: RepresentationEthicsGovernanceRecord) -> float:
    return mean([
        record.cultural_protocols,
        record.community_review,
        record.attribution_quality,
        record.image_context,
        record.visual_dignity,
        record.caption_accuracy,
    ])


def ai_representation_risk(record: RepresentationEthicsGovernanceRecord) -> float:
    return min(
        1.0,
        record.synthetic_opacity * 0.18
        + record.likeness_imitation * 0.18
        + record.cultural_fabrication * 0.20
        + record.provenance_loss * 0.18
        + record.evidence_confusion * 0.14
        + (1 - record.human_review) * 0.12,
    )


def governance_priority_score(record: RepresentationEthicsGovernanceRecord, config: RepresentationEthicsGovernanceConfig) -> float:
    score = (
        representation_risk(record) * 0.22
        + ai_representation_risk(record) * 0.20
        + (1 - representation_integrity(record)) * 0.18
        + (1 - consent_adequacy(record)) * 0.16
        + (1 - cultural_and_visual_strength(record)) * 0.10
        + record.public_consequence * 0.14
    )
    if record.status == "revise":
        score = max(score, config.high_threshold)
    elif record.status == "review":
        score = max(score, config.medium_threshold)
    return min(1.0, max(0.0, score))


def review_priority(record: RepresentationEthicsGovernanceRecord, config: RepresentationEthicsGovernanceConfig) -> str:
    score = governance_priority_score(record, config)
    if score >= config.high_threshold:
        return "high"
    if score >= config.medium_threshold:
        return "medium"
    return "standard"
