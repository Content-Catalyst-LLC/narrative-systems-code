-- Rhetorical moves governance diagnostic queries.

SELECT
    item,
    persuasion_context,
    (
        evidence_truthfulness +
        proportionality +
        context_adequacy +
        audience_agency
    ) / 4.0 AS rhetorical_integrity_partial
FROM rhetorical_moves_governance_claims
ORDER BY rhetorical_integrity_partial DESC;

SELECT
    item,
    persuasion_context,
    (
        fear_amplification +
        emotional_exploitation +
        urgency_coercion +
        (1 - human_review)
    ) / 4.0 AS persuasion_risk_partial
FROM rhetorical_moves_governance_claims
ORDER BY persuasion_risk_partial DESC;
