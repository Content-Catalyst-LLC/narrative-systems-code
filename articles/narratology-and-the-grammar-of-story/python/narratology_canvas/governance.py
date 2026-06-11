from __future__ import annotations

from hashlib import sha256
from typing import Any

from .models import NarratologyConfig, NarratologyRecord
from .scoring import focalization_complexity, governance_priority_score, governance_risk, interpretation_readiness, narrative_grammar_strength, review_priority, temporal_complexity


def card_id(record: NarratologyRecord, config: NarratologyConfig) -> str:
    raw = f"{config.article_slug}|{record.item}|{record.claim_context}"
    return sha256(raw.encode("utf-8")).hexdigest()[:16]


def governance_note(record: NarratologyRecord, config: NarratologyConfig) -> str:
    priority = review_priority(record, config)
    notes: list[str] = []
    if priority == "high":
        notes.append("High-priority narratology governance review required.")
    elif priority == "medium":
        notes.append("Medium-priority review recommended before reuse.")
    else:
        notes.append("Standard editorial review sufficient.")
    if governance_risk(record) >= 0.55:
        notes.append("Governance risk is elevated; review omission, power blindness, voice imbalance, closure pressure, and unreliable framing.")
    if interpretation_readiness(record) < 0.60:
        notes.append("Interpretation readiness is limited; strengthen source context, counterexamples, method limits, and uncertainty notes.")
    if record.notes:
        notes.append(record.notes)
    return " ".join(notes)


def build_narratology_card(record: NarratologyRecord, config: NarratologyConfig) -> dict[str, Any]:
    return {
        "schema_version": "1.0.0",
        "card_id": card_id(record, config),
        "card_type": "narratology_grammar_of_story",
        "article_title": config.article_title,
        "article_slug": config.article_slug,
        "item": record.item,
        "claim_context": record.claim_context,
        "scores": {
            "narrative_grammar_strength": round(narrative_grammar_strength(record), 4),
            "focalization_complexity": round(focalization_complexity(record), 4),
            "temporal_complexity": round(temporal_complexity(record), 4),
            "governance_risk": round(governance_risk(record), 4),
            "interpretation_readiness": round(interpretation_readiness(record), 4),
            "governance_priority_score": round(governance_priority_score(record, config), 4),
        },
        "review": {"priority": review_priority(record, config), "owner": record.owner, "status": record.status, "governance_note": governance_note(record, config)},
    }
