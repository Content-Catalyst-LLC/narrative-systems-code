from __future__ import annotations

from statistics import mean
from .models import NarrativeRiskGovernanceConfig, NarrativeRiskGovernanceRecord


def narrative_risk(record: NarrativeRiskGovernanceRecord) -> float:
    return min(
        1.0,
        record.scapegoating * 0.18
        + record.evidence_immunity * 0.20
        + record.mythic_simplification * 0.18
        + record.context_loss * 0.16
        + record.group_blame_intensity * 0.16
        + (1 - record.revision_openness) * 0.12,
    )


def evidence_integrity(record: NarrativeRiskGovernanceRecord) -> float:
    return mean([
        record.corroboration,
        record.source_quality,
        record.timeline_clarity,
        record.uncertainty_disclosure,
        record.accountability_clarity,
        record.disconfirmation_openness,
    ])


def trust_repair_priority(record: NarrativeRiskGovernanceRecord) -> float:
    return min(
        1.0,
        record.institutional_failure * 0.18
        + record.opacity * 0.18
        + record.historical_distrust_reason * 0.18
        + record.public_consequence * 0.18
        + record.correction_difficulty * 0.14
        + record.affected_listener_stakes * 0.14,
    )


def platform_amplification_risk(record: NarrativeRiskGovernanceRecord) -> float:
    return min(
        1.0,
        record.platform_speed * 0.24
        + record.repetition_intensity * 0.24
        + record.social_proof_pressure * 0.24
        + record.monetization_pressure * 0.16
        + record.context_loss * 0.12,
    )


def ai_narrative_risk(record: NarrativeRiskGovernanceRecord) -> float:
    return min(
        1.0,
        record.synthetic_evidence * 0.20
        + record.provenance_opacity * 0.20
        + record.fabricated_patterning * 0.18
        + record.automated_consensus * 0.16
        + record.vulnerability_targeting * 0.14
        + (1 - record.human_review) * 0.12,
    )


def governance_priority_score(record: NarrativeRiskGovernanceRecord, config: NarrativeRiskGovernanceConfig) -> float:
    score = (
        narrative_risk(record) * 0.24
        + ai_narrative_risk(record) * 0.18
        + platform_amplification_risk(record) * 0.16
        + (1 - evidence_integrity(record)) * 0.16
        + trust_repair_priority(record) * 0.14
        + record.public_consequence * 0.12
    )
    if record.status == "revise":
        score = max(score, config.high_threshold)
    elif record.status == "review":
        score = max(score, config.medium_threshold)
    return min(1.0, max(0.0, score))


def review_priority(record: NarrativeRiskGovernanceRecord, config: NarrativeRiskGovernanceConfig) -> str:
    score = governance_priority_score(record, config)
    if score >= config.high_threshold:
        return "high"
    if score >= config.medium_threshold:
        return "medium"
    return "standard"
