from __future__ import annotations


def governance_note(row: dict[str, object]) -> str:
    priority = str(row.get("review_priority", "standard"))
    if priority == "high":
        return "Requires review for universalization, cultural erasure, performance omission, variation omission, archive bias, and weak source context."
    if priority == "medium":
        return "Review function mapping, variant comparison, language notes, performance context, and tradition-specific framing."
    return "Standard folktale morphology review."
