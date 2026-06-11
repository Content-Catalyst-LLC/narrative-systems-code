from __future__ import annotations

from statistics import mean

from .models import IndigenousStoryGovernanceConfig, IndigenousStoryGovernanceRecord


def relational_accountability(record: IndigenousStoryGovernanceRecord) -> float:
    return mean([
        record.place_specificity,
        record.community_authority,
        record.teller_relationship,
        record.listener_context,
        record.obligation_visibility,
        record.governance_visibility,
    ])


def protocol_risk(record: IndigenousStoryGovernanceRecord) -> float:
    return min(
        1.0,
        record.access_pressure * 0.18
        + record.seasonal_restriction * 0.16
        + record.ceremonial_restriction * 0.18
        + record.template_forcing * 0.16
        + record.digital_exposure * 0.16
        + (1 - record.governance_visibility) * 0.16,
    )


def place_memory_strength(record: IndigenousStoryGovernanceRecord) -> float:
    return mean([
        record.land_naming,
        record.ecological_knowledge,
        record.ancestral_memory,
        record.route_teaching,
        record.seasonal_context,
        record.future_generation_responsibility,
    ])


def translation_governance(record: IndigenousStoryGovernanceRecord) -> float:
    return mean([
        record.cultural_specificity,
        record.language_context,
        record.opacity_notes,
        record.untranslated_terms,
        record.reviewer_visibility,
        record.harm_review,
    ])


def digital_sovereignty_risk(record: IndigenousStoryGovernanceRecord) -> float:
    return min(
        1.0,
        record.extraction_risk * 0.18
        + record.open_access_assumption * 0.18
        + record.ai_training_risk * 0.20
        + record.stereotype_bias * 0.16
        + record.metadata_flattening * 0.14
        + (1 - record.community_governance) * 0.14,
    )


def governance_priority_score(record: IndigenousStoryGovernanceRecord, config: IndigenousStoryGovernanceConfig) -> float:
    score = (
        protocol_risk(record) * 0.28
        + digital_sovereignty_risk(record) * 0.28
        + (1 - relational_accountability(record)) * 0.16
        + (1 - translation_governance(record)) * 0.12
        + record.public_consequence * 0.16
    )
    if record.status == "revise":
        score = max(score, config.high_threshold)
    elif record.status == "review":
        score = max(score, config.medium_threshold)
    return min(1.0, max(0.0, score))


def review_priority(record: IndigenousStoryGovernanceRecord, config: IndigenousStoryGovernanceConfig) -> str:
    score = governance_priority_score(record, config)
    if score >= config.high_threshold:
        return "high"
    if score >= config.medium_threshold:
        return "medium"
    return "standard"
