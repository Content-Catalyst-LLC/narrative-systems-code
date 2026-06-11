from __future__ import annotations

from hashlib import sha256
from typing import Any

from .models import FragmentedNarrativeConfig, FragmentedNarrativeRecord
from .scoring import fragmentation_sensitivity, governance_priority_score, interpretation_readiness, review_priority, trauma_narrative_risk, witness_care


def card_id(record: FragmentedNarrativeRecord, config: FragmentedNarrativeConfig) -> str:
    raw = f"{config.article_slug}|{record.item}|{record.claim_context}"
    return sha256(raw.encode("utf-8")).hexdigest()[:16]


def governance_note(record: FragmentedNarrativeRecord, config: FragmentedNarrativeConfig) -> str:
    priority = review_priority(record, config)
    notes: list[str] = []
    if priority == "high":
        notes.append("High-priority fragmented-narrative governance review required.")
    elif priority == "medium":
        notes.append("Medium-priority review recommended before reuse.")
    else:
        notes.append("Standard editorial review sufficient.")
    if trauma_narrative_risk(record) >= 0.55:
        notes.append("Trauma-narrative risk is elevated; review forced coherence, redemptive shortcut, extraction risk, identity reduction, and spectacle pressure.")
    if witness_care(record) < 0.65:
        notes.append("Witness-care signals are limited; strengthen consent, agency, privacy, relational context, safety framing, and boundary discipline.")
    if interpretation_readiness(record) < 0.60:
        notes.append("Interpretation readiness is limited; strengthen source context, cultural context, uncertainty notes, method limits, and review owner clarity.")
    if record.notes:
        notes.append(record.notes)
    return " ".join(notes)


def build_fragmented_narrative_card(record: FragmentedNarrativeRecord, config: FragmentedNarrativeConfig) -> dict[str, Any]:
    return {
        "schema_version": "1.0.0",
        "card_id": card_id(record, config),
        "card_type": "memory_trauma_fragmented_narrative",
        "article_title": config.article_title,
        "article_slug": config.article_slug,
        "item": record.item,
        "claim_context": record.claim_context,
        "scores": {
            "fragmentation_sensitivity": round(fragmentation_sensitivity(record), 4),
            "witness_care": round(witness_care(record), 4),
            "trauma_narrative_risk": round(trauma_narrative_risk(record), 4),
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
