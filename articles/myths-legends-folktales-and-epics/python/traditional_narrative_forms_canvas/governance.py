from __future__ import annotations


def governance_note(row: dict[str, object]) -> str:
    priority = str(row.get("review_priority", "standard"))
    if priority == "high":
        return "Requires review for sacred or restricted material, context removal, performance omission, translation loss, extraction risk, and weak governance control."
    if priority == "medium":
        return "Review form classification, truth claim, hybrid boundaries, source context, performance trace, and adaptation constraints."
    return "Standard traditional narrative form review."
