from __future__ import annotations

from statistics import mean
from .models import SerialNarrativeGovernanceConfig, SerialNarrativeGovernanceRecord


def season_coherence(record: SerialNarrativeGovernanceRecord) -> float:
    return mean([
        record.episode_function,
        record.arc_progression,
        record.thematic_development,
        record.character_memory,
        record.payoff_integrity_signal,
        record.finale_consequence,
    ])


def continuity_burden(record: SerialNarrativeGovernanceRecord) -> float:
    return min(
        1.0,
        record.unresolved_arcs * 0.20
        + record.lore_density * 0.16
        + record.memory_expectation * 0.18
        + record.recap_uncertainty * 0.14
        + record.continuity_saturation * 0.18
        + (1 - record.audience_accessibility) * 0.14,
    )


def payoff_integrity(record: SerialNarrativeGovernanceRecord) -> float:
    return mean([
        record.foreshadowing_support,
        record.character_relevance,
        record.emotional_payoff,
        record.mystery_logic,
        record.retrospective_coherence,
        record.thematic_alignment,
    ])


def ensemble_and_ethics_strength(record: SerialNarrativeGovernanceRecord) -> float:
    return mean([
        record.ensemble_balance,
        record.representation_depth,
        record.trauma_care,
        record.audience_trust,
        record.character_memory,
        record.finale_consequence,
    ])


def ai_serial_risk(record: SerialNarrativeGovernanceRecord) -> float:
    return min(
        1.0,
        record.generic_plotting * 0.18
        + record.continuity_fabrication * 0.20
        + record.memory_erasure * 0.18
        + record.payoff_simplification * 0.16
        + record.franchise_overextension * 0.16
        + (1 - record.human_review) * 0.12,
    )


def governance_priority_score(record: SerialNarrativeGovernanceRecord, config: SerialNarrativeGovernanceConfig) -> float:
    score = (
        continuity_burden(record) * 0.20
        + ai_serial_risk(record) * 0.20
        + (1 - season_coherence(record)) * 0.16
        + (1 - payoff_integrity(record)) * 0.18
        + (1 - ensemble_and_ethics_strength(record)) * 0.12
        + record.public_consequence * 0.14
    )
    if record.status == "revise":
        score = max(score, config.high_threshold)
    elif record.status == "review":
        score = max(score, config.medium_threshold)
    return min(1.0, max(0.0, score))


def review_priority(record: SerialNarrativeGovernanceRecord, config: SerialNarrativeGovernanceConfig) -> str:
    score = governance_priority_score(record, config)
    if score >= config.high_threshold:
        return "high"
    if score >= config.medium_threshold:
        return "medium"
    return "standard"
