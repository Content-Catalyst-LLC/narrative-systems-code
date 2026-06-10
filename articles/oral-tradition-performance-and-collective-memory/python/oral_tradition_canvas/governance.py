from __future__ import annotations


def governance_note(row: dict[str, object]) -> str:
    priority = str(row.get("review_priority", "standard"))
    if priority == "high":
        return "Requires review for consent limits, restricted knowledge, ownership risk, extraction risk, exposure risk, community sensitivity, and governance control."
    if priority == "medium":
        return "Review performance context, transmission integrity, access protocol, record context, and community authority."
    return "Standard oral tradition review."
