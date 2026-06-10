from __future__ import annotations


def governance_note(row: dict[str, object]) -> str:
    priority = str(row.get("review_priority", "standard"))
    if priority == "high":
        return "Requires review for drift risk, source age, context retention, representation risk, and revision pressure."
    if priority == "medium":
        return "Review temporal coherence, memory durability, and article-map dependency."
    return "Standard temporal narrative governance review."
