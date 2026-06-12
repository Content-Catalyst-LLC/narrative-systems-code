-- Storytelling value governance diagnostic queries.

SELECT
    item,
    story_context,
    (
        clarity +
        evidence_grounding +
        memory_continuity +
        audience_reasoning +
        dignity_protection
    ) / 5.0 AS storytelling_value_partial
FROM storytelling_value_governance_claims
ORDER BY storytelling_value_partial DESC;

SELECT
    item,
    story_context,
    (
        oversimplification +
        (1 - human_review) +
        (1 - truthfulness) +
        (1 - context_adequacy)
    ) / 4.0 AS misuse_risk_partial
FROM storytelling_value_governance_claims
ORDER BY misuse_risk_partial DESC;
