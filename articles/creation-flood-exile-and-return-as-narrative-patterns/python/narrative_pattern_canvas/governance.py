from __future__ import annotations

from hashlib import sha256
from typing import Any

from .models import NarrativePatternRecord, PatternConfig
from .scoring import (
    ethical_risk,
    governance_priority_score,
    interpretation_readiness,
    pattern_strength,
    review_priority,
    rupture_renewal_strength,
)


def card_id(record: NarrativePatternRecord, config: PatternConfig) -> str:
    raw = f"{config.article_slug}|{record.item}|{record.claim_context}"
    return sha256(raw.encode("utf-8")).hexdigest()[:16]


def governance_note(record: NarrativePatternRecord, config: PatternConfig) -> str:
    priority = review_priority(record, config)
    risk = ethical_risk(record)
    readiness = interpretation_readiness(record)

    notes: list[str] = []

    if priority == "high":
        notes.append("High-priority narrative-pattern governance review required.")
    elif priority == "medium":
        notes.append("Medium-priority review recommended before reuse.")
    else:
        notes.append("Standard editorial review sufficient.")

    if risk >= 0.55:
        notes.append("Ethical risk is elevated; review origin nostalgia, cleansing fantasy, exile romanticization, false return, and power blindness.")
    if readiness < 0.60:
        notes.append("Interpretation readiness is limited; strengthen source context, historical context, counterexamples, method limits, and uncertainty notes.")
    if record.notes:
        notes.append(record.notes)

    return " ".join(notes)


def build_pattern_card(record: NarrativePatternRecord, config: PatternConfig) -> dict[str, Any]:
    return {
        "schema_version": "1.0.0",
        "card_id": card_id(record, config),
        "card_type": "creation_flood_exile_return_pattern",
        "article_title": config.article_title,
        "article_slug": config.article_slug,
        "item": record.item,
        "claim_context": record.claim_context,
        "scores": {
            "pattern_strength": round(pattern_strength(record), 4),
            "rupture_renewal_strength": round(rupture_renewal_strength(record), 4),
            "ethical_risk": round(ethical_risk(record), 4),
            "interpretation_readiness": round(interpretation_readiness(record), 4),
            "governance_priority_score": round(governance_priority_score(record, config), 4),
        },
        "review": {
            "priority": review_priority(record, config),
            "owner": record.owner,
            "status": record.status,
            "governance_note": governance_note(record, config),
        },
    }
