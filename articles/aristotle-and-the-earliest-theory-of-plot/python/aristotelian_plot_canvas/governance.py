from __future__ import annotations


def governance_note(row: dict[str, object]) -> str:
    priority = str(row.get("review_priority", "standard"))
    if priority == "high":
        return "Requires review for unity, causal linkage, formula risk, genre fit, medium fit, and cultural awareness."
    if priority == "medium":
        return "Review episode dependency, reversal-recognition strength, and character-action integration."
    return "Standard Aristotelian plot review."
