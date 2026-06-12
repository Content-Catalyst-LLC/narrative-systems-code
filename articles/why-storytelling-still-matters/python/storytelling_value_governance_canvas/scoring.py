from __future__ import annotations

from statistics import mean
from .models import StorytellingValueGovernanceConfig, StorytellingValueGovernanceRecord


def storytelling_value(record: StorytellingValueGovernanceRecord) -> float:
    return mean([
        record.clarity,
        record.evidence_grounding,
        record.memory_continuity,
        record.audience_reasoning,
        record.dignity_protection,
        record.public_usefulness,
    ])


def narrative_responsibility(record: StorytellingValueGovernanceRecord) -> float:
    return mean([
        record.truthfulness,
        record.context_adequacy,
        record.consent_discipline,
        record.uncertainty_disclosure,
        record.revision_openness,
        record.accountability,
    ])


def misuse_risk(record: StorytellingValueGovernanceRecord) -> float:
    return min(
        1.0,
        record.oversimplification * 0.18
        + record.emotional_exploitation * 0.18
        + record.scapegoating * 0.18
        + record.context_loss * 0.18
        + record.platform_frictionlessness * 0.14
        + (1 - record.human_review) * 0.14,
    )


def ai_storytelling_governance(record: StorytellingValueGovernanceRecord) -> float:
    return mean([
        record.provenance_visibility,
        record.source_traceability,
        record.ai_human_review,
        record.ai_consent_discipline,
        record.use_limit_clarity,
        record.correction_process,
    ])


def governance_priority_score(record: StorytellingValueGovernanceRecord, config: StorytellingValueGovernanceConfig) -> float:
    score = (
        misuse_risk(record) * 0.28
        + (1 - narrative_responsibility(record)) * 0.22
        + (1 - storytelling_value(record)) * 0.16
        + (1 - ai_storytelling_governance(record)) * 0.14
        + record.ethical_stakes * 0.12
        + (1 - record.cultural_context) * 0.08
    )
    if record.status == "revise":
        score = max(score, config.high_threshold)
    elif record.status == "review":
        score = max(score, config.medium_threshold)
    return min(1.0, max(0.0, score))


def review_priority(record: StorytellingValueGovernanceRecord, config: StorytellingValueGovernanceConfig) -> str:
    score = governance_priority_score(record, config)
    if score >= config.high_threshold:
        return "high"
    if score >= config.medium_threshold:
        return "medium"
    return "standard"
