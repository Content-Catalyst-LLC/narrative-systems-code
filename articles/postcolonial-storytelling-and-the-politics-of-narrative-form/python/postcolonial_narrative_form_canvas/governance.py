from __future__ import annotations

from hashlib import sha256
from typing import Any

from .models import PostcolonialNarrativeFormConfig, PostcolonialNarrativeFormRecord
from .scoring import colonial_form_risk, digital_coloniality, governance_priority_score, postcolonial_form_strength, review_priority, translation_governance


def card_id(record: PostcolonialNarrativeFormRecord, config: PostcolonialNarrativeFormConfig) -> str:
    raw = f"{config.article_slug}|{record.item}|{record.claim_context}"
    return sha256(raw.encode("utf-8")).hexdigest()[:16]


def governance_note(record: PostcolonialNarrativeFormRecord, config: PostcolonialNarrativeFormConfig) -> str:
    priority = review_priority(record, config)
    notes: list[str] = []
    if priority == "high":
        notes.append("High-priority postcolonial narrative-form governance review required.")
    elif priority == "medium":
        notes.append("Medium-priority review recommended before reuse.")
    else:
        notes.append("Standard editorial review sufficient.")
    if colonial_form_risk(record) >= 0.55:
        notes.append("Colonial-form risk is elevated. Review archive dominance, language hierarchy, gaze centrality, template forcing, extraction anxiety, and opacity protection.")
    if digital_coloniality(record) >= 0.55:
        notes.append("Digital coloniality risk is elevated. Review English dominance, stereotype bias, extraction risk, archive flattening, visual orientalism, and community governance.")
    if translation_governance(record) < 0.65:
        notes.append("Translation governance is limited. Strengthen cultural specificity, local authority, opacity notes, untranslated term handling, reviewer visibility, and harm review.")
    if postcolonial_form_strength(record) >= 0.70:
        notes.append("Postcolonial-form strength is high. Preserve voice complexity, language politics, memory fragmentation, archive critique, temporal multiplicity, spatial politics, and land/context relation.")
    if record.notes:
        notes.append(record.notes)
    return " ".join(notes)


def build_postcolonial_narrative_form_card(record: PostcolonialNarrativeFormRecord, config: PostcolonialNarrativeFormConfig) -> dict[str, Any]:
    return {
        "schema_version": "1.0.0",
        "card_id": card_id(record, config),
        "card_type": "postcolonial_narrative_form",
        "article_title": config.article_title,
        "article_slug": config.article_slug,
        "item": record.item,
        "claim_context": record.claim_context,
        "scores": {
            "colonial_form_risk": round(colonial_form_risk(record), 4),
            "postcolonial_form_strength": round(postcolonial_form_strength(record), 4),
            "translation_governance": round(translation_governance(record), 4),
            "digital_coloniality": round(digital_coloniality(record), 4),
            "governance_priority_score": round(governance_priority_score(record, config), 4),
        },
        "review": {
            "priority": review_priority(record, config),
            "owner": record.owner,
            "status": record.status,
            "governance_note": governance_note(record, config),
        },
    }
