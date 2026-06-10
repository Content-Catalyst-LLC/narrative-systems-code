from __future__ import annotations


def governance_note(row: dict[str, object]) -> str:
    priority = str(row.get("review_priority", "standard"))
    if priority == "high":
        return "Requires review for evidence support, causality, agency, omitted perspectives, and closure pressure."
    if priority == "medium":
        return "Review causal assumptions, overreach risk, and interpretive openness."
    return "Standard narrative understanding review."
