from __future__ import annotations


def governance_note(row: dict[str, object]) -> str:
    priority = str(row.get("review_priority", "standard"))
    if priority == "high":
        return "Requires review for ritual authority, consent, access control, quote extraction, sound loss, translation loss, commercial reuse, and governance control."
    if priority == "medium":
        return "Review oral-form context, sound documentation, protocol, source context, and archive risk."
    return "Standard compact oral forms review."
