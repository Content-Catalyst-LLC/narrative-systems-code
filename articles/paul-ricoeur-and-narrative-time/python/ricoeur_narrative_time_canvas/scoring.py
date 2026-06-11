from __future__ import annotations

from statistics import mean

from .models import NarrativeTimeConfig, NarrativeTimeRecord


def narrative_time_configuration(record: NarrativeTimeRecord) -> float:
    return mean([record.memory_mapping, record.anticipation, record.plot_logic, record.configuration, record.refiguration, record.ending_function])


def emplotment_strength(record: NarrativeTimeRecord) -> float:
    return mean([record.event_selection, record.causal_articulation, record.reversal_recognition, record.concordance, record.discordance, record.whole_plot_coherence])


def narrative_identity_readiness(record: NarrativeTimeRecord) -> float:
    return mean([record.continuity, record.change, record.promise_responsibility, record.memory_revision, record.agency, record.relational_recognition])


def interpretation_readiness(record: NarrativeTimeRecord) -> float:
    return mean([record.source_context, record.counterexamples, record.method_limits, record.uncertainty_notes, record.configuration, record.refiguration])


def temporal_governance_risk(record: NarrativeTimeRecord) -> float:
    return min(1.0, record.premature_closure * 0.20 + record.redemptive_shortcut * 0.18 + record.erased_continuity * 0.18 + record.delayed_accountability * 0.18 + record.nostalgic_origin * 0.14 + (1 - record.uncertainty_notes) * 0.12)


def governance_priority_score(record: NarrativeTimeRecord, config: NarrativeTimeConfig) -> float:
    score = temporal_governance_risk(record) * 0.40 + (1 - interpretation_readiness(record)) * 0.28 + record.delayed_accountability * 0.16 + record.premature_closure * 0.16
    if record.status == "revise":
        score = max(score, config.high_threshold)
    elif record.status == "review":
        score = max(score, config.medium_threshold)
    return min(1.0, max(0.0, score))


def review_priority(record: NarrativeTimeRecord, config: NarrativeTimeConfig) -> str:
    score = governance_priority_score(record, config)
    if score >= config.high_threshold:
        return "high"
    if score >= config.medium_threshold:
        return "medium"
    return "standard"
