from __future__ import annotations


def governance_note(row: dict[str, object]) -> str:
    priority = str(row.get("review_priority", "standard"))
    if priority == "high":
        return "Requires review for restricted material, weak consent, access control, context removal, platform/data risk, extraction risk, and community governance."
    if priority == "medium":
        return "Review safeguarding readiness, performance context, language vitality, transmission pathways, metadata quality, and access level."
    return "Standard storytelling heritage review."
