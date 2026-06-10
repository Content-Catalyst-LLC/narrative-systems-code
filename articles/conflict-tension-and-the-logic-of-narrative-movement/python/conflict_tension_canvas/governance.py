from __future__ import annotations


def governance_note(row: dict[str, object]) -> str:
    priority = str(row.get("review_priority", "standard"))
    if priority == "high":
        return "Requires review for conflict risk, scapegoating, conflict inflation, trauma spectacle, false balance, closure pressure, and public consequence."
    if priority == "medium":
        return "Review conflict clarity, tension durability, narrative movement, stakes visibility, and agency pressure."
    return "Standard conflict and tension review."
