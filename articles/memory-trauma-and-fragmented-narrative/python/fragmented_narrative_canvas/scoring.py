from __future__ import annotations

from statistics import mean

from .models import FragmentedNarrativeConfig, FragmentedNarrativeRecord


def fragmentation_sensitivity(record: FragmentedNarrativeRecord) -> float:
    return mean([
        record.temporal_rupture,
        record.gap_marking,
        record.repetition_patterning,
        record.silence_respect,
        record.uncertainty_notes,
        record.contextual_care,
    ])


def witness_care(record: FragmentedNarrativeRecord) -> float:
    return mean([
        record.consent,
        record.agency,
        record.privacy,
        record.relational_context,
        record.safety_framing,
        record.boundary_discipline,
    ])


def trauma_narrative_risk(record: FragmentedNarrativeRecord) -> float:
    return min(
        1.0,
        record.forced_coherence * 0.20
        + record.redemptive_shortcut * 0.18
        + record.extraction_risk * 0.20
        + record.identity_reduction * 0.18
        + record.spectacle_pressure * 0.14
        + (1 - record.method_limits) * 0.10,
    )


def interpretation_readiness(record: FragmentedNarrativeRecord) -> float:
    return mean([
        record.source_context,
        record.cultural_context,
        record.uncertainty_notes,
        record.method_limits,
        record.ethics_governance,
        record.review_owner_clarity,
    ])


def governance_priority_score(record: FragmentedNarrativeRecord, config: FragmentedNarrativeConfig) -> float:
    score = (
        trauma_narrative_risk(record) * 0.40
        + (1 - witness_care(record)) * 0.22
        + (1 - interpretation_readiness(record)) * 0.22
        + record.public_consequence * 0.16
    )
    if record.status == "revise":
        score = max(score, config.high_threshold)
    elif record.status == "review":
        score = max(score, config.medium_threshold)
    return min(1.0, max(0.0, score))


def review_priority(record: FragmentedNarrativeRecord, config: FragmentedNarrativeConfig) -> str:
    score = governance_priority_score(record, config)
    if score >= config.high_threshold:
        return "high"
    if score >= config.medium_threshold:
        return "medium"
    return "standard"
