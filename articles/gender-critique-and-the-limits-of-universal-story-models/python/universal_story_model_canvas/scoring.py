from __future__ import annotations

from statistics import mean

from .models import UniversalStoryModelConfig, UniversalStoryModelRecord


def universal_model_fit(record: UniversalStoryModelRecord) -> float:
    return mean([
        record.stage_evidence,
        record.agency_match,
        record.transformation_correspondence,
        record.contextual_harmony,
        record.resolution_similarity,
        record.evidence_visibility,
    ])


def universalism_risk(record: UniversalStoryModelRecord) -> float:
    return min(
        1.0,
        record.archive_bias * 0.18
        + record.gender_binary_pressure * 0.20
        + record.cultural_flattening * 0.18
        + record.intersectional_erasure * 0.18
        + record.queer_trans_pressure * 0.16
        + (1 - record.local_context) * 0.10,
    )


def critique_readiness(record: UniversalStoryModelRecord) -> float:
    return mean([
        record.source_context,
        record.local_context,
        record.alternative_lens,
        record.gender_complexity,
        record.intersectional_context,
        record.uncertainty_notes,
        record.review_owner_clarity,
    ])


def alternative_structure_signal(record: UniversalStoryModelRecord) -> float:
    return mean([
        record.relational_motion,
        record.cyclical_form,
        record.witness_structure,
        record.care_labor,
        record.fragmented_form,
        record.open_process,
    ])


def governance_priority_score(record: UniversalStoryModelRecord, config: UniversalStoryModelConfig) -> float:
    score = (
        universalism_risk(record) * 0.38
        + (1 - critique_readiness(record)) * 0.24
        + alternative_structure_signal(record) * 0.18
        + record.public_consequence * 0.20
    )
    if record.status == "revise":
        score = max(score, config.high_threshold)
    elif record.status == "review":
        score = max(score, config.medium_threshold)
    return min(1.0, max(0.0, score))


def review_priority(record: UniversalStoryModelRecord, config: UniversalStoryModelConfig) -> str:
    score = governance_priority_score(record, config)
    if score >= config.high_threshold:
        return "high"
    if score >= config.medium_threshold:
        return "medium"
    return "standard"
