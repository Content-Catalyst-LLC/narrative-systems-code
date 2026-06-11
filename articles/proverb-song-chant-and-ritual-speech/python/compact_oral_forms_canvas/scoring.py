from __future__ import annotations

from statistics import mean

from .models import CompactOralFormItem


def oral_form_context(item: CompactOralFormItem) -> float:
    return mean([
        item.form_identification,
        item.speaker_role,
        item.audience_documentation,
        item.occasion_notes,
        item.place_linkage,
        item.use_context,
    ])


def sound_and_repetition(item: CompactOralFormItem) -> float:
    return mean([
        item.rhythm,
        item.melody,
        item.cadence,
        item.refrain_or_formula,
        item.participation,
        item.embodiment,
    ])


def ritual_authority(item: CompactOralFormItem) -> float:
    return mean([
        item.role_legitimacy,
        item.protocol_review,
        item.consent_status,
        item.access_control,
        item.governance_oversight,
        item.benefit_sharing,
    ])


def archive_risk(item: CompactOralFormItem) -> float:
    return min(
        1.0,
        item.quote_extraction_risk * 0.18
        + item.context_removal * 0.18
        + item.sound_loss * 0.16
        + item.translation_loss * 0.16
        + item.extraction_risk * 0.18
        + (1 - item.governance_control) * 0.14,
    )


def governance_priority_score(item: CompactOralFormItem) -> float:
    return min(
        1.0,
        archive_risk(item) * 0.35
        + item.community_sensitivity * 0.25
        + item.public_consequence * 0.20
        + (1 - ritual_authority(item)) * 0.20,
    )


def review_priority(item: CompactOralFormItem) -> str:
    risk = archive_risk(item)
    priority = governance_priority_score(item)
    authority = ritual_authority(item)

    if item.status == "revise" or risk >= 0.55 or priority >= 0.62 or authority < 0.55:
        return "high"
    if item.status == "review" or risk >= 0.40 or priority >= 0.48 or authority < 0.68:
        return "medium"
    return "standard"
