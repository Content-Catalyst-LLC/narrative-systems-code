from __future__ import annotations

from hashlib import sha256
from typing import Any

from .models import AlternativeStructureConfig, AlternativeStructureRecord
from .scoring import alternative_readiness, governance_priority_score, medium_fit, monomyth_overfit_risk, review_priority, structural_plurality


def card_id(record: AlternativeStructureRecord, config: AlternativeStructureConfig) -> str:
    raw = f"{config.article_slug}|{record.item}|{record.claim_context}"
    return sha256(raw.encode("utf-8")).hexdigest()[:16]


def governance_note(record: AlternativeStructureRecord, config: AlternativeStructureConfig) -> str:
    priority = review_priority(record, config)
    notes: list[str] = []
    if priority == "high":
        notes.append("High-priority alternative-structure governance review required.")
    elif priority == "medium":
        notes.append("Medium-priority review recommended before reuse.")
    else:
        notes.append("Standard editorial review sufficient.")
    if monomyth_overfit_risk(record) >= 0.55:
        notes.append("Monomyth-overfit risk is elevated. Review hero forcing, conflict substitution, return pressure, individualization pressure, template forcing, and evidence visibility.")
    if structural_plurality(record) >= 0.65:
        notes.append("Structural plurality is strong. Compare arc, cycle, braid, mosaic, network, relational, and fragmented forms before selecting a framework.")
    if alternative_readiness(record) < 0.65:
        notes.append("Alternative-structure readiness is limited. Strengthen source context, method limits, alternative lenses, cultural context, uncertainty notes, and review ownership.")
    if medium_fit(record) < 0.60:
        notes.append("Medium fit is limited. Review temporal match, agency design, pacing, sequence, interaction affordance, and experiential coherence.")
    if record.notes:
        notes.append(record.notes)
    return " ".join(notes)


def build_alternative_structure_card(record: AlternativeStructureRecord, config: AlternativeStructureConfig) -> dict[str, Any]:
    return {
        "schema_version": "1.0.0",
        "card_id": card_id(record, config),
        "card_type": "alternative_story_structure_beyond_monomyth",
        "article_title": config.article_title,
        "article_slug": config.article_slug,
        "item": record.item,
        "claim_context": record.claim_context,
        "scores": {
            "structural_plurality": round(structural_plurality(record), 4),
            "monomyth_overfit_risk": round(monomyth_overfit_risk(record), 4),
            "alternative_readiness": round(alternative_readiness(record), 4),
            "medium_fit": round(medium_fit(record), 4),
            "governance_priority_score": round(governance_priority_score(record, config), 4),
        },
        "review": {
            "priority": review_priority(record, config),
            "owner": record.owner,
            "status": record.status,
            "governance_note": governance_note(record, config),
        },
    }
