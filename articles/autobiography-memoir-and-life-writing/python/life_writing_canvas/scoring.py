from __future__ import annotations

from statistics import mean

from .models import LifeWritingConfig, LifeWritingRecord


def life_writing_coherence(record: LifeWritingRecord) -> float:
    return mean([
        record.memory_clarity,
        record.temporal_structure,
        record.voice_consistency,
        record.agency,
        record.relational_grounding,
        record.contextual_depth,
    ])


def truth_practice(record: LifeWritingRecord) -> float:
    return mean([
        record.fact_checking,
        record.memory_framing,
        record.evidence_visibility,
        record.interpretation_distinction,
        record.uncertainty_notes,
        record.archive_review,
    ])


def ethical_risk(record: LifeWritingRecord) -> float:
    return min(
        1.0,
        record.privacy_risk * 0.18
        + record.consent_limits * 0.20
        + record.other_person_exposure * 0.20
        + record.trauma_extraction * 0.18
        + record.self_mythology * 0.14
        + (1 - record.method_limits) * 0.10,
    )


def interpretation_readiness(record: LifeWritingRecord) -> float:
    return mean([
        record.source_context,
        record.cultural_context,
        record.evidence_visibility,
        record.uncertainty_notes,
        record.method_limits,
        record.review_owner_clarity,
    ])


def governance_priority_score(record: LifeWritingRecord, config: LifeWritingConfig) -> float:
    score = (
        ethical_risk(record) * 0.40
        + (1 - truth_practice(record)) * 0.22
        + (1 - interpretation_readiness(record)) * 0.22
        + record.public_consequence * 0.16
    )
    if record.status == "revise":
        score = max(score, config.high_threshold)
    elif record.status == "review":
        score = max(score, config.medium_threshold)
    return min(1.0, max(0.0, score))


def review_priority(record: LifeWritingRecord, config: LifeWritingConfig) -> str:
    score = governance_priority_score(record, config)
    if score >= config.high_threshold:
        return "high"
    if score >= config.medium_threshold:
        return "medium"
    return "standard"
