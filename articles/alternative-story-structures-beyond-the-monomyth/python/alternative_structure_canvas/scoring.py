from __future__ import annotations

from statistics import mean

from .models import AlternativeStructureConfig, AlternativeStructureRecord


def structural_plurality(record: AlternativeStructureRecord) -> float:
    return mean([
        record.arc_signal,
        record.cycle_signal,
        record.braid_signal,
        record.mosaic_signal,
        record.network_signal,
        record.relational_signal,
        record.fragment_signal,
    ])


def monomyth_overfit_risk(record: AlternativeStructureRecord) -> float:
    return min(
        1.0,
        record.hero_forcing * 0.20
        + record.conflict_substitution * 0.18
        + record.return_pressure * 0.16
        + record.individualization_pressure * 0.18
        + record.template_forcing * 0.18
        + (1 - record.evidence_visibility) * 0.10,
    )


def alternative_readiness(record: AlternativeStructureRecord) -> float:
    return mean([
        record.source_context,
        record.method_limits,
        record.alternative_lens,
        record.cultural_context,
        record.uncertainty_notes,
        record.review_owner_clarity,
    ])


def medium_fit(record: AlternativeStructureRecord) -> float:
    return mean([
        record.temporal_match,
        record.agency_design,
        record.pacing_compatibility,
        record.sequence_logic,
        record.interaction_affordance,
        record.experiential_coherence,
    ])


def governance_priority_score(record: AlternativeStructureRecord, config: AlternativeStructureConfig) -> float:
    score = (
        monomyth_overfit_risk(record) * 0.36
        + (1 - alternative_readiness(record)) * 0.24
        + structural_plurality(record) * 0.18
        + record.public_consequence * 0.22
    )
    if record.status == "revise":
        score = max(score, config.high_threshold)
    elif record.status == "review":
        score = max(score, config.medium_threshold)
    return min(1.0, max(0.0, score))


def review_priority(record: AlternativeStructureRecord, config: AlternativeStructureConfig) -> str:
    score = governance_priority_score(record, config)
    if score >= config.high_threshold:
        return "high"
    if score >= config.medium_threshold:
        return "medium"
    return "standard"
