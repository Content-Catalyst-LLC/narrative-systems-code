from __future__ import annotations


def governance_note(row: dict[str, object]) -> str:
    priority = str(row.get("review_priority", "standard"))
    if priority == "high":
        return "Requires review for performance omission, fixation risk, context removal, translation loss, extraction risk, access protocol, and platform circulation."
    if priority == "medium":
        return "Review teller role, audience documentation, occasion context, language notes, source review, and variation accountability."
    return "Standard oral storytelling variation review."
