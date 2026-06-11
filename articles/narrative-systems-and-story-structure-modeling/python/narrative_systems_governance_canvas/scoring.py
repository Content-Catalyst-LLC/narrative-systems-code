from __future__ import annotations

from statistics import mean
from .models import NarrativeSystemsGovernanceConfig, NarrativeSystemsGovernanceRecord


def narrative_coherence(record: NarrativeSystemsGovernanceRecord) -> float:
    return mean([
        record.causal_alignment,
        record.state_transition_clarity,
        record.agent_goal_fit,
        record.world_rule_consistency,
        record.temporal_mapping,
        record.evidence_quality,
    ])


def formula_drift_risk(record: NarrativeSystemsGovernanceRecord) -> float:
    return min(
        1.0,
        record.beat_template_dependence * 0.18
        + record.universal_model_claims * 0.18
        + record.context_loss * 0.18
        + record.genre_flattening * 0.16
        + record.model_overconfidence * 0.16
        + (1 - record.judgment_review) * 0.14,
    )


def responsibility_balance(record: NarrativeSystemsGovernanceRecord) -> float:
    return max(0.0, 1 - abs(record.individual_agency_visibility - record.systemic_agency_visibility))


def network_system_strength(record: NarrativeSystemsGovernanceRecord) -> float:
    return mean([
        record.network_mapping,
        record.relationship_specificity,
        record.constraint_visibility,
        record.feedback_loop_clarity,
        record.agent_goal_fit,
        record.world_rule_consistency,
    ])


def ai_story_structure_risk(record: NarrativeSystemsGovernanceRecord) -> float:
    return min(
        1.0,
        record.plot_hallucination * 0.18
        + record.causal_invention * 0.18
        + record.stereotype_tendency * 0.18
        + record.formula_generation * 0.18
        + record.biased_corpus * 0.16
        + (1 - record.human_review) * 0.12,
    )


def governance_priority_score(record: NarrativeSystemsGovernanceRecord, config: NarrativeSystemsGovernanceConfig) -> float:
    score = (
        formula_drift_risk(record) * 0.22
        + ai_story_structure_risk(record) * 0.22
        + (1 - narrative_coherence(record)) * 0.18
        + (1 - responsibility_balance(record)) * 0.12
        + (1 - network_system_strength(record)) * 0.12
        + record.public_consequence * 0.14
    )
    if record.status == "revise":
        score = max(score, config.high_threshold)
    elif record.status == "review":
        score = max(score, config.medium_threshold)
    return min(1.0, max(0.0, score))


def review_priority(record: NarrativeSystemsGovernanceRecord, config: NarrativeSystemsGovernanceConfig) -> str:
    score = governance_priority_score(record, config)
    if score >= config.high_threshold:
        return "high"
    if score >= config.medium_threshold:
        return "medium"
    return "standard"
