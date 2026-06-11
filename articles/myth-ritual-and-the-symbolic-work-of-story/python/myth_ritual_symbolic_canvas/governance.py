from __future__ import annotations


def governance_note(row: dict[str, object]) -> str:
    priority = str(row.get("review_priority", "standard"))
    if priority == "high":
        return "Requires review for appropriation, totalizing myth, scapegoating, exclusion, harm exposure, weak ritual context, and weak interpretation readiness."
    if priority == "medium":
        return "Review symbolic function, ritual context, language notes, access controls, public consequence, and interpretive uncertainty."
    return "Standard myth and ritual symbolic review."
