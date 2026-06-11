from __future__ import annotations

from .models import CanvasConfig, CanvasRecord


def weighted_average(values: dict[str, float], weights: dict[str, float]) -> float:
    numerator = 0.0
    denominator = 0.0
    for key, weight in weights.items():
        if key in values:
            numerator += values[key] * weight
            denominator += weight
    if denominator <= 0:
        return 0.0
    return max(0.0, min(1.0, numerator / denominator))


def domain_strength(record: CanvasRecord, config: CanvasConfig) -> float:
    return weighted_average(record.metrics, config.metric_weights)


def risk_score(record: CanvasRecord, config: CanvasConfig) -> float:
    return weighted_average(record.risk_signals, config.risk_weights)


def interpretation_readiness(record: CanvasRecord, config: CanvasConfig) -> float:
    return weighted_average(record.readiness_signals, config.readiness_weights)


def governance_priority_score(record: CanvasRecord, config: CanvasConfig) -> float:
    risk = risk_score(record, config)
    readiness = interpretation_readiness(record, config)
    strength = domain_strength(record, config)
    score = risk * 0.45 + (1 - readiness) * 0.35 + (1 - strength) * 0.20

    if record.status == 'revise':
        score = max(score, config.thresholds['high'])
    elif record.status == 'review':
        score = max(score, config.thresholds['medium'])

    return max(0.0, min(1.0, score))


def review_priority(record: CanvasRecord, config: CanvasConfig) -> str:
    score = governance_priority_score(record, config)
    if score >= config.thresholds['high']:
        return 'high'
    if score >= config.thresholds['medium']:
        return 'medium'
    return 'standard'


def confidence_band(record: CanvasRecord, config: CanvasConfig) -> str:
    readiness = interpretation_readiness(record, config)
    if readiness >= 0.78:
        return 'high'
    if readiness >= 0.58:
        return 'medium'
    return 'low'
