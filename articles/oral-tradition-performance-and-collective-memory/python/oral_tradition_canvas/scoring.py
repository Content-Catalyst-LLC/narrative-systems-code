from __future__ import annotations

from statistics import mean

from .models import OralTraditionItem


def performance_context(item: OralTraditionItem) -> float:
    return mean([
        item.teller_role,
        item.audience_response,
        item.occasion_clarity,
        item.embodiment,
        item.setting_place,
        item.cultural_frame,
    ])


def transmission_integrity(item: OralTraditionItem) -> float:
    return mean([
        item.lineage_clarity,
        item.variation_tracking,
        item.memory_supports,
        item.governance_protocol,
        item.authority_permission,
        item.record_context,
    ])


def memory_function(item: OralTraditionItem) -> float:
    return mean([
        item.origin_memory,
        item.place_memory,
        item.identity_memory,
        item.historical_memory,
        item.ritual_memory,
        item.future_obligation,
    ])


def archive_risk(item: OralTraditionItem) -> float:
    return min(
        1.0,
        item.consent_limits * 0.18
        + item.restricted_knowledge * 0.22
        + item.exposure_risk * 0.18
        + item.ownership_risk * 0.18
        + item.extraction_risk * 0.14
        + (1 - item.governance_control) * 0.10,
    )


def governance_priority_score(item: OralTraditionItem) -> float:
    return min(
        1.0,
        archive_risk(item) * 0.35
        + item.community_sensitivity * 0.25
        + item.public_consequence * 0.20
        + (1 - transmission_integrity(item)) * 0.20,
    )


def review_priority(item: OralTraditionItem) -> str:
    risk = archive_risk(item)
    priority = governance_priority_score(item)
    transmission = transmission_integrity(item)

    if item.status == "revise" or risk >= 0.55 or priority >= 0.62 or transmission < 0.55:
        return "high"
    if item.status == "review" or risk >= 0.40 or priority >= 0.48 or transmission < 0.68:
        return "medium"
    return "standard"
