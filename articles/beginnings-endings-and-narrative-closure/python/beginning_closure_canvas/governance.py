from __future__ import annotations


def governance_note(row: dict[str, object]) -> str:
    priority = str(row.get("review_priority", "standard"))
    if priority == "high":
        return "Requires review for premature repair, false resolution, system flattening, aftermath omission, audience comfort, and public consequence."
    if priority == "medium":
        return "Review opening promise, closure integrity, alignment, unresolved consequence, and aftermath clarity."
    return "Standard beginning and closure review."
