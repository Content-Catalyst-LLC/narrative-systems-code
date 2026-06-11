from __future__ import annotations

from statistics import mean
from .models import LegalNarrativeResponsibilityConfig, LegalNarrativeResponsibilityRecord


def evidence_support(record: LegalNarrativeResponsibilityRecord) -> float:
    return mean([
        record.relevance,
        record.authentication,
        record.provenance,
        record.corroboration,
        record.cross_checking,
        record.uncertainty_notation,
    ])


def narrative_overreach_risk(record: LegalNarrativeResponsibilityRecord) -> float:
    return min(
        1.0,
        record.overcoherence * 0.18
        + record.evidentiary_gap * 0.18
        + record.stereotype_reliance * 0.16
        + record.causation_flattening * 0.16
        + record.affective_bias * 0.16
        + (1 - record.uncertainty_visibility) * 0.16,
    )


def procedural_voice(record: LegalNarrativeResponsibilityRecord) -> float:
    return mean([
        record.opportunity_to_be_heard,
        record.discovery_access,
        record.testimony_context,
        record.record_access,
        record.correction_pathway,
        record.procedural_posture_clarity,
    ])


def testimony_responsibility(record: LegalNarrativeResponsibilityRecord) -> float:
    return mean([
        record.witness_dignity,
        record.testimony_care,
        record.role_complexity,
        record.testimony_context,
        record.uncertainty_notation,
        record.remedy_connection,
    ])


def ai_legal_narrative_risk(record: LegalNarrativeResponsibilityRecord) -> float:
    return min(
        1.0,
        record.hallucinated_authority * 0.22
        + record.summary_dependence * 0.18
        + record.context_loss * 0.18
        + record.procedural_distortion * 0.18
        + record.bias_reproduction * 0.14
        + (1 - record.human_review) * 0.10,
    )


def governance_priority_score(record: LegalNarrativeResponsibilityRecord, config: LegalNarrativeResponsibilityConfig) -> float:
    score = (
        narrative_overreach_risk(record) * 0.30
        + ai_legal_narrative_risk(record) * 0.22
        + (1 - evidence_support(record)) * 0.18
        + (1 - procedural_voice(record)) * 0.12
        + (1 - testimony_responsibility(record)) * 0.08
        + record.public_consequence * 0.10
    )
    if record.status == "revise":
        score = max(score, config.high_threshold)
    elif record.status == "review":
        score = max(score, config.medium_threshold)
    return min(1.0, max(0.0, score))


def review_priority(record: LegalNarrativeResponsibilityRecord, config: LegalNarrativeResponsibilityConfig) -> str:
    score = governance_priority_score(record, config)
    if score >= config.high_threshold:
        return "high"
    if score >= config.medium_threshold:
        return "medium"
    return "standard"
