from __future__ import annotations


def governance_note(row: dict[str, object]) -> str:
    risk = float(row.get("governance_risk", 0.0))
    priority = str(row.get("review_priority", "standard"))
    if priority == "high":
        return "Requires editorial and ethical review before publication."
    if priority == "medium":
        return "Review evidence, representation, context, and persuasive framing."
    if risk > 0.25:
        return "Monitor for evidence and representation drift."
    return "Standard editorial review."
