from __future__ import annotations

from hashlib import sha256
from typing import Any

from .models import NationalMemoryGovernanceConfig, NationalMemoryGovernanceRecord
from .scoring import ai_memory_risk, governance_priority_score, memory_accountability, memory_plurality, national_myth_risk, public_memory_infrastructure, review_priority


def card_id(record: NationalMemoryGovernanceRecord, config: NationalMemoryGovernanceConfig) -> str:
    raw = f"{config.article_slug}|{record.item}|{record.claim_context}"
    return sha256(raw.encode("utf-8")).hexdigest()[:16]


def governance_note(record: NationalMemoryGovernanceRecord, config: NationalMemoryGovernanceConfig) -> str:
    priority = review_priority(record, config)
    notes: list[str] = []
    if priority == "high":
        notes.append("High-priority national-memory governance review required.")
    elif priority == "medium":
        notes.append("Medium-priority review recommended before reuse.")
    else:
        notes.append("Standard editorial review sufficient.")
    if national_myth_risk(record) >= 0.55:
        notes.append("National-myth risk is elevated. Review hero compression, innocence story, exclusion omission, victimhood monopoly, purity symbolism, and weak revision capacity.")
    if memory_plurality(record) < 0.65:
        notes.append("Memory plurality is limited. Strengthen group representation, source diversity, testimony visibility, archive coverage, countermemory inclusion, and dissent space.")
    if memory_accountability(record) < 0.65:
        notes.append("Memory accountability is limited. Strengthen evidence visibility, provenance, record access, testimony care, context, and repair linkage.")
    if ai_memory_risk(record) >= 0.55:
        notes.append("AI-memory risk is elevated. Review summary dependence, context loss, dominant-archive bias, uncertainty erasure, omitted minority memory, and human review.")
    if record.notes:
        notes.append(record.notes)
    return " ".join(notes)


def build_national_memory_governance_card(record: NationalMemoryGovernanceRecord, config: NationalMemoryGovernanceConfig) -> dict[str, Any]:
    return {
        "schema_version": "1.0.0",
        "card_id": card_id(record, config),
        "card_type": "national_memory_governance",
        "article_title": config.article_title,
        "article_slug": config.article_slug,
        "item": record.item,
        "claim_context": record.claim_context,
        "scores": {
            "memory_plurality": round(memory_plurality(record), 4),
            "national_myth_risk": round(national_myth_risk(record), 4),
            "memory_accountability": round(memory_accountability(record), 4),
            "public_memory_infrastructure": round(public_memory_infrastructure(record), 4),
            "ai_memory_risk": round(ai_memory_risk(record), 4),
            "governance_priority_score": round(governance_priority_score(record, config), 4),
        },
        "review": {
            "priority": review_priority(record, config),
            "owner": record.owner,
            "status": record.status,
            "governance_note": governance_note(record, config),
        },
    }
