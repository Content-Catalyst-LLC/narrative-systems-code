from __future__ import annotations

from hashlib import sha256
from typing import Any

from .models import CanvasConfig, CanvasRecord
from .scoring import confidence_band, domain_strength, governance_priority_score, interpretation_readiness, review_priority, risk_score


def stable_card_id(record: CanvasRecord, config: CanvasConfig) -> str:
    raw = f"{config.article_slug}|{record.item}|{record.claim_context}"
    return sha256(raw.encode("utf-8")).hexdigest()[:16]


def governance_note(record: CanvasRecord, config: CanvasConfig) -> str:
    notes: list[str] = []
    priority = review_priority(record, config)
    if priority == "high":
        notes.append("High-priority governance review required.")
    elif priority == "medium":
        notes.append("Medium-priority editorial review recommended.")
    else:
        notes.append("Standard review sufficient.")
    if risk_score(record, config) >= 0.60:
        notes.append("Risk signals are elevated; review power, omissions, ethical framing, and potential distortion.")
    if interpretation_readiness(record, config) < 0.60:
        notes.append("Interpretation readiness is limited; strengthen source context, counterexamples, method limits, and uncertainty notes.")
    if domain_strength(record, config) < 0.55:
        notes.append("Domain signal is thin; verify support.")
    if record.status == "revise":
        notes.append("Record status is revise; prioritize correction.")
    if record.notes:
        notes.append(f"Record note: {record.notes}")
    return " ".join(notes)


def build_canvas_card(record: CanvasRecord, config: CanvasConfig) -> dict[str, Any]:
    return {
        "schema_version": "1.0.0",
        "card_id": stable_card_id(record, config),
        "card_type": "catalyst_canvas_article_governance",
        "article_title": config.article_title,
        "article_slug": config.article_slug,
        "module_name": config.module_name,
        "item": record.item,
        "claim_context": record.claim_context,
        "scores": {
            "domain_strength": round(domain_strength(record, config), 4),
            "risk_score": round(risk_score(record, config), 4),
            "interpretation_readiness": round(interpretation_readiness(record, config), 4),
            "governance_priority_score": round(governance_priority_score(record, config), 4),
        },
        "review": {
            "priority": review_priority(record, config),
            "confidence_band": confidence_band(record, config),
            "owner": record.owner,
            "status": record.status,
            "governance_note": governance_note(record, config),
        },
        "signals": {
            "metrics": record.metrics,
            "risk_signals": record.risk_signals,
            "readiness_signals": record.readiness_signals,
        },
    }
