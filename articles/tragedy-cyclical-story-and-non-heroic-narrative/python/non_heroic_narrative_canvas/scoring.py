from __future__ import annotations

from statistics import mean

from .models import NonHeroicNarrativeConfig, NonHeroicNarrativeRecord


def tragic_structure(record: NonHeroicNarrativeRecord) -> float:
    return mean([
        record.consequential_action,
        record.limit_pressure,
        record.reversal,
        record.recognition_knowledge,
        record.irreversibility,
        record.witness_burden,
    ])


def cyclical_structure(record: NonHeroicNarrativeRecord) -> float:
    return mean([
        record.repeated_pattern,
        record.seasonal_ritual_signal,
        record.generational_transmission,
        record.institutional_habit,
        record.ecological_feedback,
        record.variation_across_return,
    ])


def non_heroic_agency(record: NonHeroicNarrativeRecord) -> float:
    return mean([
        record.care,
        record.endurance,
        record.witness,
        record.refusal,
        record.maintenance,
        record.survival,
    ])


def heroic_overfit_risk(record: NonHeroicNarrativeRecord) -> float:
    return min(
        1.0,
        record.hero_forcing * 0.18
        + record.victory_pressure * 0.18
        + record.closure_pressure * 0.18
        + record.return_pressure * 0.16
        + record.growth_pressure * 0.16
        + (1 - record.evidence_visibility) * 0.14,
    )


def review_readiness(record: NonHeroicNarrativeRecord) -> float:
    return mean([
        record.source_context,
        record.method_limits,
        record.uncertainty_notes,
        record.review_owner_clarity,
        record.evidence_visibility,
    ])


def governance_priority_score(record: NonHeroicNarrativeRecord, config: NonHeroicNarrativeConfig) -> float:
    score = (
        heroic_overfit_risk(record) * 0.34
        + (1 - review_readiness(record)) * 0.24
        + max(tragic_structure(record), cyclical_structure(record), non_heroic_agency(record)) * 0.18
        + record.public_consequence * 0.24
    )
    if record.status == "revise":
        score = max(score, config.high_threshold)
    elif record.status == "review":
        score = max(score, config.medium_threshold)
    return min(1.0, max(0.0, score))


def review_priority(record: NonHeroicNarrativeRecord, config: NonHeroicNarrativeConfig) -> str:
    score = governance_priority_score(record, config)
    if score >= config.high_threshold:
        return "high"
    if score >= config.medium_threshold:
        return "medium"
    return "standard"
