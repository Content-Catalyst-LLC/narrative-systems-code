from __future__ import annotations

from statistics import mean
from .models import HeroJourneyFilmGovernanceConfig, HeroJourneyFilmGovernanceRecord


def heroic_arc_integrity(record: HeroJourneyFilmGovernanceRecord) -> float:
    return mean([
        record.call_authenticity,
        record.threshold_significance,
        record.ordeal_relevance,
        record.value_change,
        record.return_boon,
        record.ethical_consequence,
    ])


def formula_risk(record: HeroJourneyFilmGovernanceRecord) -> float:
    return min(
        1.0,
        record.beat_compliance * 0.18
        + record.generic_mentor * 0.16
        + record.mechanical_call * 0.18
        + record.ordeal_spectacle * 0.16
        + record.forced_return * 0.16
        + (1 - record.story_particularity) * 0.16,
    )


def cinematic_transformation(record: HeroJourneyFilmGovernanceRecord) -> float:
    return mean([
        record.visual_motif,
        record.sound_design,
        record.editing_rhythm,
        record.performance_shift,
        record.blocking_change,
        record.mise_en_scene,
    ])


def culture_gender_integrity(record: HeroJourneyFilmGovernanceRecord) -> float:
    return mean([
        record.collective_agency,
        record.cultural_specificity,
        record.gender_complexity,
        record.nonheroic_alternatives,
        record.story_particularity,
        record.ethical_consequence,
    ])


def ai_hero_template_risk(record: HeroJourneyFilmGovernanceRecord) -> float:
    return min(
        1.0,
        record.stage_compliance * 0.18
        + record.cultural_loss * 0.20
        + record.genre_cliche * 0.18
        + record.universalist_pressure * 0.16
        + record.trope_recycling * 0.16
        + (1 - record.human_review) * 0.12,
    )


def governance_priority_score(record: HeroJourneyFilmGovernanceRecord, config: HeroJourneyFilmGovernanceConfig) -> float:
    score = (
        formula_risk(record) * 0.24
        + ai_hero_template_risk(record) * 0.20
        + (1 - heroic_arc_integrity(record)) * 0.16
        + (1 - cinematic_transformation(record)) * 0.12
        + (1 - culture_gender_integrity(record)) * 0.14
        + record.public_consequence * 0.14
    )
    if record.status == "revise":
        score = max(score, config.high_threshold)
    elif record.status == "review":
        score = max(score, config.medium_threshold)
    return min(1.0, max(0.0, score))


def review_priority(record: HeroJourneyFilmGovernanceRecord, config: HeroJourneyFilmGovernanceConfig) -> str:
    score = governance_priority_score(record, config)
    if score >= config.high_threshold:
        return "high"
    if score >= config.medium_threshold:
        return "medium"
    return "standard"
