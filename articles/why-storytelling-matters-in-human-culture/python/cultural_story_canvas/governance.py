from __future__ import annotations


def governance_note(row: dict[str, object]) -> str:
    priority = str(row.get("review_priority", "standard"))
    if priority == "high":
        return "Requires cultural, editorial, and ethical review before publication or reuse."
    if priority == "medium":
        return "Review cultural context, source transparency, representation care, and public impact."
    return "Standard editorial review."
