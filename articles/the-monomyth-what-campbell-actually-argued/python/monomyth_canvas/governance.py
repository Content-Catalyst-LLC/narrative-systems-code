from __future__ import annotations


def governance_note(row: dict[str, object]) -> str:
    priority = str(row.get("review_priority", "standard"))
    if priority == "high":
        return "Requires review for formula drift, stage literalism, context loss, overfitting, source authority, counterexamples, public consequence, and ethical risk."
    if priority == "medium":
        return "Review monomyth pattern claim, source context, method limits, ritual verification, and uncertainty marking."
    return "Standard monomyth claim review."
