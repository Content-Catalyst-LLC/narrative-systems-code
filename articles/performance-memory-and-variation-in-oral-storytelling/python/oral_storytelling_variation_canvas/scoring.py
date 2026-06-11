from __future__ import annotations

from statistics import mean

from .models import OralStorytellingVariationItem


def performance_context(item: OralStorytellingVariationItem) -> float:
    return mean([
        item.teller_role,
        item.audience_documentation,
        item.occasion_context,
        item.place_linkage,
        item.embodiment,
        item.interaction_notes,
    ])


def memory_support(item: OralStorytellingVariationItem) -> float:
    return mean([
        item.repetition,
        item.formula_use,
        item.sequence_clarity,
        item.audience_recognition,
        item.community_correction,
        item.transmission_pathway,
    ])


def variation_accountability(item: OralStorytellingVariationItem) -> float:
    return mean([
        item.variation_tracking,
        item.context_explanation,
        item.language_notes,
        item.source_review,
        item.access_protocol,
        item.governance_oversight,
    ])


def archive_risk(item: OralStorytellingVariationItem) -> float:
    return min(
        1.0,
        item.fixation_risk * 0.18
        + item.context_removal * 0.18
        + item.performance_omission * 0.18
        + item.translation_loss * 0.14
        + item.extraction_risk * 0.18
        + (1 - item.governance_control) * 0.14,
    )


def governance_priority_score(item: OralStorytellingVariationItem) -> float:
    return min(
        1.0,
        archive_risk(item) * 0.35
        + item.community_sensitivity * 0.25
        + item.public_consequence * 0.20
        + (1 - variation_accountability(item)) * 0.20,
    )


def review_priority(item: OralStorytellingVariationItem) -> str:
    risk = archive_risk(item)
    priority = governance_priority_score(item)
    accountability = variation_accountability(item)

    if item.status == "revise" or risk >= 0.55 or priority >= 0.62 or accountability < 0.55:
        return "high"
    if item.status == "review" or risk >= 0.40 or priority >= 0.48 or accountability < 0.68:
        return "medium"
    return "standard"
