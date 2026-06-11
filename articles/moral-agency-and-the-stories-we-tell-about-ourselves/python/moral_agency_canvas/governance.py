from __future__ import annotations

from hashlib import sha256
from typing import Any

from .models import MoralAgencyConfig, MoralAgencyRecord
from .scoring import excuse_risk, governance_priority_score, interpretation_readiness, moral_clarity, repair_readiness, review_priority


def card_id(record: MoralAgencyRecord, config: MoralAgencyConfig) -> str:
    raw = f"{config.article_slug}|{record.item}|{record.claim_context}"
    return sha256(raw.encode("utf-8")).hexdigest()[:16]


def governance_note(record: MoralAgencyRecord, config: MoralAgencyConfig) -> str:
    priority = review_priority(record, config)
    notes: list[str] = []
    if priority == "high":
        notes.append("High-priority moral-agency governance review required.")
    elif priority == "medium":
        notes.append("Medium-priority review recommended before reuse.")
    else:
        notes.append("Standard editorial review sufficient.")
    if excuse_risk(record) >= 0.55:
        notes.append("Excuse risk is elevated; review context overuse, intention shielding, victimhood shielding, blame shifting, growth substitution, and harm minimization.")
    if repair_readiness(record) < 0.60:
        notes.append("Repair readiness is limited; strengthen harm acknowledgment, apology precision, material response, conduct change, future accountability, and oversight.")
    if interpretation_readiness(record) < 0.60:
        notes.append("Interpretation readiness is limited; strengthen source context, evidence visibility, uncertainty notes, cultural context, method limits, and review owner clarity.")
    if record.notes:
        notes.append(record.notes)
    return " ".join(notes)


def build_moral_agency_card(record: MoralAgencyRecord, config: MoralAgencyConfig) -> dict[str, Any]:
    return {
        "schema_version": "1.0.0",
        "card_id": card_id(record, config),
        "card_type": "moral_agency_self_narrative",
        "article_title": config.article_title,
        "article_slug": config.article_slug,
        "item": record.item,
        "claim_context": record.claim_context,
        "scores": {
            "moral_clarity": round(moral_clarity(record), 4),
            "excuse_risk": round(excuse_risk(record), 4),
            "repair_readiness": round(repair_readiness(record), 4),
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
