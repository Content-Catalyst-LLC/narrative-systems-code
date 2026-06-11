from __future__ import annotations

from hashlib import sha256
from typing import Any

from .models import InstitutionalMemoryGovernanceConfig, InstitutionalMemoryGovernanceRecord
from .scoring import ai_memory_distortion_risk, governance_priority_score, institutional_memory_strength, legitimacy_alignment, origin_myth_risk, reform_credibility, review_priority


def card_id(record: InstitutionalMemoryGovernanceRecord, config: InstitutionalMemoryGovernanceConfig) -> str:
    raw = f"{config.article_slug}|{record.item}|{record.claim_context}"
    return sha256(raw.encode("utf-8")).hexdigest()[:16]


def governance_note(record: InstitutionalMemoryGovernanceRecord, config: InstitutionalMemoryGovernanceConfig) -> str:
    priority = review_priority(record, config)
    notes: list[str] = []
    if priority == "high":
        notes.append("High-priority institutional-memory governance review required.")
    elif priority == "medium":
        notes.append("Medium-priority review recommended before reuse.")
    else:
        notes.append("Standard editorial review sufficient.")
    if origin_myth_risk(record) >= 0.55:
        notes.append("Origin-myth risk is elevated. Review founder heroization, exclusion omission, harm removal, commemoration saturation, reputational branding, and voice multiplicity.")
    if institutional_memory_strength(record) < 0.65:
        notes.append("Institutional memory is limited. Strengthen record preservation, archive completeness, metadata quality, testimony stewardship, knowledge retention, and public access.")
    if reform_credibility(record) < 0.60:
        notes.append("Reform credibility is limited. Strengthen harm naming, structural change, evidence release, material repair, oversight, and transparent progress.")
    if ai_memory_distortion_risk(record) >= 0.55:
        notes.append("AI-memory distortion risk is elevated. Review summary dependence, archive bias, context loss, correction pathways, and public access.")
    if record.notes:
        notes.append(record.notes)
    return " ".join(notes)


def build_institutional_memory_governance_card(record: InstitutionalMemoryGovernanceRecord, config: InstitutionalMemoryGovernanceConfig) -> dict[str, Any]:
    return {
        "schema_version": "1.0.0",
        "card_id": card_id(record, config),
        "card_type": "institutional_memory_governance",
        "article_title": config.article_title,
        "article_slug": config.article_slug,
        "item": record.item,
        "claim_context": record.claim_context,
        "scores": {
            "legitimacy_alignment": round(legitimacy_alignment(record), 4),
            "origin_myth_risk": round(origin_myth_risk(record), 4),
            "institutional_memory_strength": round(institutional_memory_strength(record), 4),
            "reform_credibility": round(reform_credibility(record), 4),
            "ai_memory_distortion_risk": round(ai_memory_distortion_risk(record), 4),
            "governance_priority_score": round(governance_priority_score(record, config), 4),
        },
        "review": {
            "priority": review_priority(record, config),
            "owner": record.owner,
            "status": record.status,
            "governance_note": governance_note(record, config),
        },
    }
