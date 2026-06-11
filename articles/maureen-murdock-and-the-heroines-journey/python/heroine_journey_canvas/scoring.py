from __future__ import annotations

from statistics import mean

from .models import HeroineJourneyConfig, HeroineJourneyRecord


def heroine_alignment(record: HeroineJourneyRecord) -> float:
    return mean([
        record.separation_from_feminine,
        record.masculine_identification,
        record.aridity_after_success,
        record.descent_crisis,
        record.reconnection_feminine,
        record.integration_wholeness,
    ])


def framework_risk(record: HeroineJourneyRecord) -> float:
    return min(
        1.0,
        record.template_forcing * 0.20
        + record.gender_essentialism * 0.20
        + record.universal_womanhood * 0.18
        + record.psychological_overreach * 0.18
        + record.healing_pressure * 0.14
        + (1 - record.cultural_context) * 0.10,
    )


def critique_readiness(record: HeroineJourneyRecord) -> float:
    return mean([
        record.source_context,
        record.cultural_context,
        record.alternative_lens,
        record.gender_complexity,
        record.uncertainty_notes,
        record.review_owner_clarity,
    ])


def integration_quality(record: HeroineJourneyRecord) -> float:
    return mean([
        record.agency,
        record.relational_grounding,
        record.embodiment,
        record.healthy_power,
        record.emotional_maturity,
        record.open_process,
    ])


def governance_priority_score(record: HeroineJourneyRecord, config: HeroineJourneyConfig) -> float:
    score = (
        framework_risk(record) * 0.38
        + (1 - critique_readiness(record)) * 0.24
        + (1 - integration_quality(record)) * 0.18
        + record.public_consequence * 0.20
    )
    if record.status == "revise":
        score = max(score, config.high_threshold)
    elif record.status == "review":
        score = max(score, config.medium_threshold)
    return min(1.0, max(0.0, score))


def review_priority(record: HeroineJourneyRecord, config: HeroineJourneyConfig) -> str:
    score = governance_priority_score(record, config)
    if score >= config.high_threshold:
        return "high"
    if score >= config.medium_threshold:
        return "medium"
    return "standard"
