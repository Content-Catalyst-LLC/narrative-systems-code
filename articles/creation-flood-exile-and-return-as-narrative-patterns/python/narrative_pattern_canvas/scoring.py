from __future__ import annotations

from statistics import mean

from .models import NarrativePatternRecord, PatternConfig


def pattern_strength(record: NarrativePatternRecord) -> float:
    return mean([
        record.creation_signal,
        record.flood_signal,
        record.exile_signal,
        record.return_signal,
    ])


def rupture_renewal_strength(record: NarrativePatternRecord) -> float:
    return mean([
        record.flood_signal,
        record.exile_signal,
        record.memory_maintenance,
        record.repair_responsibility,
    ])


def interpretation_readiness(record: NarrativePatternRecord) -> float:
    return mean([
        record.source_context,
        record.historical_context,
        record.counterexamples,
        record.method_limits,
        record.ethics_governance,
        record.uncertainty_notes,
    ])


def ethical_risk(record: NarrativePatternRecord) -> float:
    return min(
        1.0,
        record.origin_nostalgia * 0.18
        + record.cleansing_fantasy * 0.20
        + record.exile_romanticization * 0.18
        + record.false_return * 0.18
        + record.power_blindness * 0.16
        + (1 - record.uncertainty_notes) * 0.10,
    )


def governance_priority_score(record: NarrativePatternRecord, config: PatternConfig) -> float:
    score = (
        ethical_risk(record) * 0.40
        + (1 - interpretation_readiness(record)) * 0.28
        + record.public_consequence * 0.17
        + (1 - record.repair_responsibility) * 0.15
    )

    if record.status == "revise":
        score = max(score, config.high_threshold)
    elif record.status == "review":
        score = max(score, config.medium_threshold)

    return min(1.0, max(0.0, score))


def review_priority(record: NarrativePatternRecord, config: PatternConfig) -> str:
    score = governance_priority_score(record, config)
    if score >= config.high_threshold:
        return "high"
    if score >= config.medium_threshold:
        return "medium"
    return "standard"
