from __future__ import annotations


def governance_note(row: dict[str, object]) -> str:
    priority = str(row.get("review_priority", "standard"))
    if priority == "high":
        return "Requires review for false recognition, arbitrary twist, closure pressure, evidence omission, uncertainty clarity, transformation depth, and public consequence."
    if priority == "medium":
        return "Review reversal preparation, recognition clarity, transformation consequence, and accountability follow-through."
    return "Standard reversal and recognition review."
