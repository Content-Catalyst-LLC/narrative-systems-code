from __future__ import annotations


def governance_note(row: dict[str, object]) -> str:
    priority = str(row.get("review_priority", "standard"))
    if priority == "high":
        return "Requires review for causal logic, closure pressure, evidence omission, uncertainty clarity, audience sensitivity, and public consequence."
    if priority == "medium":
        return "Review plot coherence, action dependency, motivation visibility, and episode dependency."
    return "Standard plot coherence review."
