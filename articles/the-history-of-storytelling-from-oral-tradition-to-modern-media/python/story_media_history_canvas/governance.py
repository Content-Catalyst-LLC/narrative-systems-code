from __future__ import annotations


def governance_note(row: dict[str, object]) -> str:
    priority = str(row.get("review_priority", "standard"))
    if priority == "high":
        return "Requires archival, cultural, and editorial review before publication or reuse."
    if priority == "medium":
        return "Review preservation, context retention, access, and authority assumptions."
    return "Standard historical and editorial review."
