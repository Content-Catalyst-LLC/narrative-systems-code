from __future__ import annotations

from hashlib import sha256
from typing import Any

from .models import RepresentationEthicsGovernanceConfig, RepresentationEthicsGovernanceRecord
from .scoring import ai_representation_risk, consent_adequacy, cultural_and_visual_strength, governance_priority_score, representation_integrity, representation_risk, review_priority


def card_id(record: RepresentationEthicsGovernanceRecord, config: RepresentationEthicsGovernanceConfig) -> str:
    raw = f"{config.article_slug}|{record.item}|{record.representation_context}"
    return sha256(raw.encode("utf-8")).hexdigest()[:16]


def governance_note(record: RepresentationEthicsGovernanceRecord, config: RepresentationEthicsGovernanceConfig) -> str:
    priority = review_priority(record, config)
    notes: list[str] = []
    if priority == "high":
        notes.append("High-priority representation ethics review required.")
    elif priority == "medium":
        notes.append("Medium-priority representation review recommended.")
    else:
        notes.append("Standard editorial review sufficient.")
    if representation_integrity(record) < 0.65:
        notes.append("Representation integrity is limited. Strengthen voice agency, context, dignity, source accuracy, provenance, and accountability.")
    if representation_risk(record) >= 0.55:
        notes.append("Representation risk is elevated. Review stereotype tendency, exposure risk, context loss, voice replacement, power asymmetry, and governance.")
    if consent_adequacy(record) < 0.65:
        notes.append("Consent adequacy is limited. Review informed consent, ongoing consent, use clarity, platform circulation, withdrawal, and reuse/AI clarity.")
    if cultural_and_visual_strength(record) < 0.65:
        notes.append("Cultural/visual strength is limited. Review cultural protocols, community review, attribution, image context, visual dignity, and captions.")
    if ai_representation_risk(record) >= 0.55:
        notes.append("AI representation risk is elevated. Review synthetic opacity, likeness imitation, cultural fabrication, provenance loss, evidence confusion, and human review.")
    if record.notes:
        notes.append(record.notes)
    return " ".join(notes)


def build_representation_ethics_governance_card(record: RepresentationEthicsGovernanceRecord, config: RepresentationEthicsGovernanceConfig) -> dict[str, Any]:
    return {
        "schema_version": "1.0.0",
        "card_id": card_id(record, config),
        "card_type": "representation_ethics_governance",
        "article_title": config.article_title,
        "article_slug": config.article_slug,
        "item": record.item,
        "representation_context": record.representation_context,
        "scores": {
            "representation_integrity": round(representation_integrity(record), 4),
            "representation_risk": round(representation_risk(record), 4),
            "consent_adequacy": round(consent_adequacy(record), 4),
            "cultural_and_visual_strength": round(cultural_and_visual_strength(record), 4),
            "ai_representation_risk": round(ai_representation_risk(record), 4),
            "governance_priority_score": round(governance_priority_score(record, config), 4),
        },
        "review": {
            "priority": review_priority(record, config),
            "owner": record.owner,
            "status": record.status,
            "governance_note": governance_note(record, config),
        },
    }
