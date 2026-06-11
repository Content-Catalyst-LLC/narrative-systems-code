from __future__ import annotations

from hashlib import sha256
from typing import Any

from .models import HeroineJourneyConfig, HeroineJourneyRecord
from .scoring import critique_readiness, framework_risk, governance_priority_score, heroine_alignment, integration_quality, review_priority


def card_id(record: HeroineJourneyRecord, config: HeroineJourneyConfig) -> str:
    raw = f"{config.article_slug}|{record.item}|{record.claim_context}"
    return sha256(raw.encode("utf-8")).hexdigest()[:16]


def governance_note(record: HeroineJourneyRecord, config: HeroineJourneyConfig) -> str:
    priority = review_priority(record, config)
    notes: list[str] = []
    if priority == "high":
        notes.append("High-priority heroine-journey governance review required.")
    elif priority == "medium":
        notes.append("Medium-priority review recommended before reuse.")
    else:
        notes.append("Standard editorial review sufficient.")
    if framework_risk(record) >= 0.55:
        notes.append("Framework risk is elevated; review template forcing, gender essentialism, universal womanhood assumptions, psychological overreach, healing pressure, and cultural context.")
    if critique_readiness(record) < 0.65:
        notes.append("Critique readiness is limited; strengthen source context, cultural context, alternative lenses, gender-complexity notes, uncertainty notes, and review ownership.")
    if integration_quality(record) < 0.60:
        notes.append("Integration quality is limited; review whether wholeness is claimed too quickly or agency, relationship, embodiment, healthy power, emotional maturity, and open process remain underdeveloped.")
    if record.notes:
        notes.append(record.notes)
    return " ".join(notes)


def build_heroine_journey_card(record: HeroineJourneyRecord, config: HeroineJourneyConfig) -> dict[str, Any]:
    return {
        "schema_version": "1.0.0",
        "card_id": card_id(record, config),
        "card_type": "maureen_murdock_heroine_journey",
        "article_title": config.article_title,
        "article_slug": config.article_slug,
        "item": record.item,
        "claim_context": record.claim_context,
        "scores": {
            "heroine_alignment": round(heroine_alignment(record), 4),
            "framework_risk": round(framework_risk(record), 4),
            "critique_readiness": round(critique_readiness(record), 4),
            "integration_quality": round(integration_quality(record), 4),
            "governance_priority_score": round(governance_priority_score(record, config), 4),
        },
        "review": {
            "priority": review_priority(record, config),
            "owner": record.owner,
            "status": record.status,
            "governance_note": governance_note(record, config),
        },
    }
