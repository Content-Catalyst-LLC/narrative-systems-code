from __future__ import annotations

from statistics import mean
from .models import SacredHistoryConfig, SacredHistoryRecord


def revelatory_claim_strength(record: SacredHistoryRecord) -> float:
    return mean([record.sacred_disclosure, record.event_meaning, record.authority_clarity, record.obligation, record.transformation, record.communal_memory])


def sacred_history_integration(record: SacredHistoryRecord) -> float:
    return mean([record.historical_context, record.memory_depth, record.ritual_transmission, record.interpretive_authority, record.ethical_governance, record.public_responsibility])


def sacred_authority_risk(record: SacredHistoryRecord) -> float:
    return min(1.0, record.sacred_certainty * 0.20 + record.omission_risk * 0.18 + record.political_sanctification * 0.18 + record.exclusion_risk * 0.16 + record.historical_flattening * 0.16 + (1 - record.uncertainty_marking) * 0.12)


def interpretation_readiness(record: SacredHistoryRecord) -> float:
    return mean([record.source_context, record.authority_notes, record.counterexamples, record.method_limits, record.ethical_governance, record.uncertainty_marking])


def governance_priority_score(record: SacredHistoryRecord, config: SacredHistoryConfig) -> float:
    score = sacred_authority_risk(record) * 0.42 + (1 - interpretation_readiness(record)) * 0.28 + record.public_responsibility * 0.16 + (1 - sacred_history_integration(record)) * 0.14
    if record.status == "revise":
        score = max(score, config.high_threshold)
    elif record.status == "review":
        score = max(score, config.medium_threshold)
    return min(1.0, max(0.0, score))


def review_priority(record: SacredHistoryRecord, config: SacredHistoryConfig) -> str:
    score = governance_priority_score(record, config)
    if score >= config.high_threshold:
        return "high"
    if score >= config.medium_threshold:
        return "medium"
    return "standard"
