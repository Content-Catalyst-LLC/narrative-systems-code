from __future__ import annotations


def governance_note(row: dict[str, object]) -> str:
    priority = str(row.get("review_priority", "standard"))
    if priority == "high":
        return "Requires review for reliability risk, perspective access, exposure sensitivity, representation gaps, institutional evasion, and public consequence."
    if priority == "medium":
        return "Review voice consistency, focalization clarity, source boundaries, and access distribution."
    return "Standard voice and perspective review."
