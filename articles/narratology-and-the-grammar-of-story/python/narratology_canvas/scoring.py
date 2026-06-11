from __future__ import annotations

from statistics import mean

from .models import NarratologyConfig, NarratologyRecord


def narrative_grammar_strength(record: NarratologyRecord) -> float:
    return mean([record.story_discourse_clarity, record.voice_clarity, record.focalization_clarity, record.temporal_mapping, record.character_agency_mapping, record.information_control_analysis])


def focalization_complexity(record: NarratologyRecord) -> float:
    return mean([record.perspective_shifts, record.knowledge_restriction, record.interior_access, record.source_hierarchy, record.multiple_focalizers])


def temporal_complexity(record: NarratologyRecord) -> float:
    return mean([record.analepsis, record.prolepsis, record.ellipsis, record.duration_variation, record.repetition_frequency])


def interpretation_readiness(record: NarratologyRecord) -> float:
    return mean([record.source_context, record.counterexamples, record.method_limits, record.uncertainty_notes, record.story_discourse_clarity, record.focalization_clarity])


def governance_risk(record: NarratologyRecord) -> float:
    return min(1.0, record.omission_risk * 0.18 + record.power_blindness * 0.20 + record.voice_imbalance * 0.20 + record.closure_pressure * 0.16 + record.unreliable_framing_risk * 0.16 + (1 - record.method_limits) * 0.10)


def governance_priority_score(record: NarratologyRecord, config: NarratologyConfig) -> float:
    score = governance_risk(record) * 0.40 + (1 - interpretation_readiness(record)) * 0.28 + record.voice_imbalance * 0.16 + record.omission_risk * 0.16
    if record.status == "revise":
        score = max(score, config.high_threshold)
    elif record.status == "review":
        score = max(score, config.medium_threshold)
    return min(1.0, max(0.0, score))


def review_priority(record: NarratologyRecord, config: NarratologyConfig) -> str:
    score = governance_priority_score(record, config)
    if score >= config.high_threshold:
        return "high"
    if score >= config.medium_threshold:
        return "medium"
    return "standard"
