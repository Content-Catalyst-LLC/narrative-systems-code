from __future__ import annotations

from hashlib import sha256
from typing import Any
from .models import SacredHistoryConfig, SacredHistoryRecord
from .scoring import governance_priority_score, interpretation_readiness, revelatory_claim_strength, review_priority, sacred_authority_risk, sacred_history_integration


def card_id(record: SacredHistoryRecord, config: SacredHistoryConfig) -> str:
    return sha256(f"{config.article_slug}|{record.item}|{record.claim_context}".encode("utf-8")).hexdigest()[:16]


def governance_note(record: SacredHistoryRecord, config: SacredHistoryConfig) -> str:
    priority = review_priority(record, config)
    notes: list[str] = []
    if priority == "high":
        notes.append("High-priority sacred-history governance review required.")
    elif priority == "medium":
        notes.append("Medium-priority review recommended before reuse.")
    else:
        notes.append("Standard editorial review sufficient.")
    if sacred_authority_risk(record) >= 0.55:
        notes.append("Authority risk is elevated; review certainty, omission, exclusion, political sanctification, and historical flattening.")
    if interpretation_readiness(record) < 0.60:
        notes.append("Interpretation readiness is limited; strengthen source context, authority notes, counterexamples, method limits, and uncertainty marking.")
    if record.notes:
        notes.append(record.notes)
    return " ".join(notes)


def build_sacred_history_card(record: SacredHistoryRecord, config: SacredHistoryConfig) -> dict[str, Any]:
    return {
        "schema_version": "1.0.0",
        "card_id": card_id(record, config),
        "card_type": "sacred_history_revelatory_narrative",
        "article_title": config.article_title,
        "article_slug": config.article_slug,
        "item": record.item,
        "claim_context": record.claim_context,
        "scores": {
            "revelatory_claim_strength": round(revelatory_claim_strength(record), 4),
            "sacred_history_integration": round(sacred_history_integration(record), 4),
            "sacred_authority_risk": round(sacred_authority_risk(record), 4),
            "interpretation_readiness": round(interpretation_readiness(record), 4),
            "governance_priority_score": round(governance_priority_score(record, config), 4),
        },
        "review": {"priority": review_priority(record, config), "owner": record.owner, "status": record.status, "governance_note": governance_note(record, config)},
    }
