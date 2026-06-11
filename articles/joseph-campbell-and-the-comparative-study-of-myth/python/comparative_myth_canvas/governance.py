from __future__ import annotations


def governance_note(row: dict[str, object]) -> str:
    priority = str(row.get("review_priority", "standard"))
    if priority == "high":
        return "Requires review for formula reduction, context loss, source authority, cultural specificity, counterexamples, public consequence, and ethical risk."
    if priority == "medium":
        return "Review Campbell pattern claim, source context, method limits, ritual verification, and uncertainty marking."
    return "Standard comparative mythology review."
