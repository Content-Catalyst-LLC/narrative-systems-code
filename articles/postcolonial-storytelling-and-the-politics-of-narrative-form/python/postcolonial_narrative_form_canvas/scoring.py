from __future__ import annotations

from statistics import mean

from .models import PostcolonialNarrativeFormConfig, PostcolonialNarrativeFormRecord


def colonial_form_risk(record: PostcolonialNarrativeFormRecord) -> float:
    return min(
        1.0,
        record.archive_dominance * 0.18
        + record.language_hierarchy * 0.18
        + record.gaze_centrality * 0.18
        + record.template_forcing * 0.18
        + record.extraction_anxiety * 0.16
        + (1 - record.opacity_protection) * 0.12,
    )


def postcolonial_form_strength(record: PostcolonialNarrativeFormRecord) -> float:
    return mean([
        record.voice_complexity,
        record.language_politics,
        record.memory_fragmentation,
        record.archive_critique,
        record.temporal_multiplicity,
        record.spatial_politics,
        record.relational_land_context,
    ])


def translation_governance(record: PostcolonialNarrativeFormRecord) -> float:
    return mean([
        record.cultural_specificity,
        record.local_authority,
        record.opacity_notes,
        record.untranslated_terms,
        record.reviewer_visibility,
        record.harm_review,
    ])


def digital_coloniality(record: PostcolonialNarrativeFormRecord) -> float:
    return min(
        1.0,
        record.english_dominance * 0.18
        + record.stereotype_bias * 0.18
        + record.extraction_risk * 0.18
        + record.archive_flattening * 0.16
        + record.visual_orientalism * 0.16
        + (1 - record.community_governance) * 0.14,
    )


def governance_priority_score(record: PostcolonialNarrativeFormRecord, config: PostcolonialNarrativeFormConfig) -> float:
    score = (
        colonial_form_risk(record) * 0.30
        + digital_coloniality(record) * 0.24
        + (1 - translation_governance(record)) * 0.18
        + record.public_consequence * 0.18
        + (1 - postcolonial_form_strength(record)) * 0.10
    )
    if record.status == "revise":
        score = max(score, config.high_threshold)
    elif record.status == "review":
        score = max(score, config.medium_threshold)
    return min(1.0, max(0.0, score))


def review_priority(record: PostcolonialNarrativeFormRecord, config: PostcolonialNarrativeFormConfig) -> str:
    score = governance_priority_score(record, config)
    if score >= config.high_threshold:
        return "high"
    if score >= config.medium_threshold:
        return "medium"
    return "standard"
