from __future__ import annotations

from statistics import mean
from .models import InteractiveNarrativeGovernanceConfig, InteractiveNarrativeGovernanceRecord


def agency_integrity(record: InteractiveNarrativeGovernanceRecord) -> float:
    return mean([
        record.choice_meaningfulness,
        record.system_response,
        record.feedback_clarity,
        record.role_variation,
        record.world_memory,
        record.ethical_governance,
    ])


def branching_burden(record: InteractiveNarrativeGovernanceRecord) -> float:
    return min(
        1.0,
        record.branch_count_pressure * 0.16
        + record.state_dependency * 0.18
        + record.consequence_tracking * 0.20
        + record.testing_load * 0.18
        + record.localization_cost * 0.12
        + (1 - record.recombination_coherence) * 0.16,
    )


def system_story_alignment(record: InteractiveNarrativeGovernanceRecord) -> float:
    return mean([
        record.mechanic_theme_fit,
        record.rule_fiction_fit,
        record.goal_value_fit,
        record.progression_coherence,
        record.interface_legibility,
        record.consequence_consistency,
    ])


def failure_and_identity_strength(record: InteractiveNarrativeGovernanceRecord) -> float:
    return mean([
        record.failure_meaning,
        record.replay_value,
        record.player_consent,
        record.identity_care,
        record.feedback_clarity,
        record.ethical_governance,
    ])


def ai_interactive_narrative_risk(record: InteractiveNarrativeGovernanceRecord) -> float:
    return min(
        1.0,
        record.generic_quest_generation * 0.18
        + record.character_memory_failure * 0.20
        + record.opaque_system_response * 0.18
        + record.player_manipulation * 0.18
        + record.harmful_stereotype_risk * 0.14
        + (1 - record.human_review) * 0.12,
    )


def governance_priority_score(record: InteractiveNarrativeGovernanceRecord, config: InteractiveNarrativeGovernanceConfig) -> float:
    score = (
        branching_burden(record) * 0.18
        + ai_interactive_narrative_risk(record) * 0.22
        + (1 - agency_integrity(record)) * 0.18
        + (1 - system_story_alignment(record)) * 0.18
        + (1 - failure_and_identity_strength(record)) * 0.10
        + record.public_consequence * 0.14
    )
    if record.status == "revise":
        score = max(score, config.high_threshold)
    elif record.status == "review":
        score = max(score, config.medium_threshold)
    return min(1.0, max(0.0, score))


def review_priority(record: InteractiveNarrativeGovernanceRecord, config: InteractiveNarrativeGovernanceConfig) -> str:
    score = governance_priority_score(record, config)
    if score >= config.high_threshold:
        return "high"
    if score >= config.medium_threshold:
        return "medium"
    return "standard"
