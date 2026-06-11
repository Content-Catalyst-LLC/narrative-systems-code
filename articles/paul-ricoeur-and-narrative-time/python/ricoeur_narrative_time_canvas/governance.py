from __future__ import annotations

from hashlib import sha256
from typing import Any

from .models import NarrativeTimeConfig, NarrativeTimeRecord
from .scoring import emplotment_strength, governance_priority_score, interpretation_readiness, narrative_identity_readiness, narrative_time_configuration, review_priority, temporal_governance_risk


def card_id(record: NarrativeTimeRecord, config: NarrativeTimeConfig) -> str:
    raw = f"{config.article_slug}|{record.item}|{record.claim_context}"
    return sha256(raw.encode("utf-8")).hexdigest()[:16]


def governance_note(record: NarrativeTimeRecord, config: NarrativeTimeConfig) -> str:
    priority = review_priority(record, config)
    notes: list[str] = []
    if priority == "high":
        notes.append("High-priority narrative-time governance review required.")
    elif priority == "medium":
        notes.append("Medium-priority review recommended before reuse.")
    else:
        notes.append("Standard editorial review sufficient.")
    if temporal_governance_risk(record) >= 0.55:
        notes.append("Temporal governance risk is elevated; review premature closure, redemptive shortcut, erased continuity, delayed accountability, and nostalgic origin.")
    if interpretation_readiness(record) < 0.60:
        notes.append("Interpretation readiness is limited; strengthen source context, counterexamples, method limits, and uncertainty notes.")
    if record.notes:
        notes.append(record.notes)
    return " ".join(notes)


def build_ricoeur_card(record: NarrativeTimeRecord, config: NarrativeTimeConfig) -> dict[str, Any]:
    return {
        "schema_version": "1.0.0",
        "card_id": card_id(record, config),
        "card_type": "ricoeur_narrative_time",
        "article_title": config.article_title,
        "article_slug": config.article_slug,
        "item": record.item,
        "claim_context": record.claim_context,
        "scores": {
            "narrative_time_configuration": round(narrative_time_configuration(record), 4),
            "emplotment_strength": round(emplotment_strength(record), 4),
            "narrative_identity_readiness": round(narrative_identity_readiness(record), 4),
            "temporal_governance_risk": round(temporal_governance_risk(record), 4),
            "interpretation_readiness": round(interpretation_readiness(record), 4),
            "governance_priority_score": round(governance_priority_score(record, config), 4),
        },
        "review": {"priority": review_priority(record, config), "owner": record.owner, "status": record.status, "governance_note": governance_note(record, config)},
    }
