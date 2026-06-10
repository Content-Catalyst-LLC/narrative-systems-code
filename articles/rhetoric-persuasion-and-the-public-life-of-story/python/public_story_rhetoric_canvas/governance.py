from __future__ import annotations


def governance_note(row: dict[str, object]) -> str:
    priority = str(row.get("review_priority", "standard"))
    if priority == "high":
        return "Requires review for verification, emotional coercion, scapegoating, identity manipulation, closure pressure, and representation sensitivity."
    if priority == "medium":
        return "Review rhetorical balance, evidence support, identification pattern, and public consequence."
    return "Standard public story rhetoric review."
