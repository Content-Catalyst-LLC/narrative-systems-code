from __future__ import annotations
from hashlib import sha256
from typing import Any
from .models import NarrativeFormulaDriftConfig, NarrativeFormulaDriftRecord
from .scoring import ai_template_risk, formula_drift, framework_health, governance_priority_score, narrative_specificity, review_priority

def card_id(record: NarrativeFormulaDriftRecord, config: NarrativeFormulaDriftConfig) -> str:
    return sha256(f"{config.article_slug}|{record.item}|{record.claim_context}".encode("utf-8")).hexdigest()[:16]

def governance_note(record: NarrativeFormulaDriftRecord, config: NarrativeFormulaDriftConfig) -> str:
    notes = []
    if formula_drift(record) >= 0.55:
        notes.append("Formula drift elevated.")
    if ai_template_risk(record) >= 0.55:
        notes.append("AI-template risk elevated.")
    if framework_health(record) < 0.65:
        notes.append("Framework health needs strengthening.")
    if narrative_specificity(record) < 0.65:
        notes.append("Narrative specificity needs restoration.")
    if record.notes:
        notes.append(record.notes)
    return " ".join(notes) or "Standard review."

def build_narrative_formula_drift_card(record: NarrativeFormulaDriftRecord, config: NarrativeFormulaDriftConfig) -> dict[str, Any]:
    return {
        "schema_version": "1.0.0",
        "card_id": card_id(record, config),
        "card_type": "narrative_formula_drift",
        "article_title": config.article_title,
        "article_slug": config.article_slug,
        "item": record.item,
        "claim_context": record.claim_context,
        "scores": {
            "formula_drift": round(formula_drift(record), 4),
            "framework_health": round(framework_health(record), 4),
            "narrative_specificity": round(narrative_specificity(record), 4),
            "ai_template_risk": round(ai_template_risk(record), 4),
            "governance_priority_score": round(governance_priority_score(record, config), 4),
        },
        "review": {
            "priority": review_priority(record, config),
            "owner": record.owner,
            "status": record.status,
            "governance_note": governance_note(record, config),
        },
    }
