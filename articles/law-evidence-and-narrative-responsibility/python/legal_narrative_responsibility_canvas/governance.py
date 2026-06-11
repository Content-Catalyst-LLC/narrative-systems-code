from __future__ import annotations

from hashlib import sha256
from typing import Any

from .models import LegalNarrativeResponsibilityConfig, LegalNarrativeResponsibilityRecord
from .scoring import ai_legal_narrative_risk, evidence_support, governance_priority_score, narrative_overreach_risk, procedural_voice, review_priority, testimony_responsibility


def card_id(record: LegalNarrativeResponsibilityRecord, config: LegalNarrativeResponsibilityConfig) -> str:
    raw = f"{config.article_slug}|{record.item}|{record.claim_context}"
    return sha256(raw.encode("utf-8")).hexdigest()[:16]


def governance_note(record: LegalNarrativeResponsibilityRecord, config: LegalNarrativeResponsibilityConfig) -> str:
    priority = review_priority(record, config)
    notes: list[str] = []
    if priority == "high":
        notes.append("High-priority legal narrative responsibility review required.")
    elif priority == "medium":
        notes.append("Medium-priority review recommended before reuse.")
    else:
        notes.append("Standard editorial review sufficient.")
    if narrative_overreach_risk(record) >= 0.55:
        notes.append("Narrative-overreach risk is elevated. Review overcoherence, evidentiary gaps, stereotype reliance, causation flattening, affective bias, and weak uncertainty visibility.")
    if evidence_support(record) < 0.65:
        notes.append("Evidence support is limited. Strengthen relevance, authentication, provenance, corroboration, cross-checking, and uncertainty notation.")
    if procedural_voice(record) < 0.65:
        notes.append("Procedural voice is limited. Review hearing opportunity, discovery access, testimony context, record access, correction pathways, and procedural posture clarity.")
    if testimony_responsibility(record) < 0.65:
        notes.append("Testimony responsibility is limited. Review witness dignity, testimony care, role complexity, context, uncertainty, and remedy connection.")
    if ai_legal_narrative_risk(record) >= 0.55:
        notes.append("AI-legal narrative risk is elevated. Review hallucinated authority, summary dependence, context loss, procedural distortion, bias reproduction, and human review.")
    if record.notes:
        notes.append(record.notes)
    return " ".join(notes)


def build_legal_narrative_responsibility_card(record: LegalNarrativeResponsibilityRecord, config: LegalNarrativeResponsibilityConfig) -> dict[str, Any]:
    return {
        "schema_version": "1.0.0",
        "card_id": card_id(record, config),
        "card_type": "legal_narrative_responsibility",
        "article_title": config.article_title,
        "article_slug": config.article_slug,
        "item": record.item,
        "claim_context": record.claim_context,
        "scores": {
            "evidence_support": round(evidence_support(record), 4),
            "narrative_overreach_risk": round(narrative_overreach_risk(record), 4),
            "procedural_voice": round(procedural_voice(record), 4),
            "testimony_responsibility": round(testimony_responsibility(record), 4),
            "ai_legal_narrative_risk": round(ai_legal_narrative_risk(record), 4),
            "governance_priority_score": round(governance_priority_score(record, config), 4),
        },
        "review": {
            "priority": review_priority(record, config),
            "owner": record.owner,
            "status": record.status,
            "governance_note": governance_note(record, config),
        },
    }
