-- Legal narrative responsibility diagnostic queries.

SELECT
    item,
    claim_context,
    (
        relevance +
        authentication +
        provenance +
        corroboration +
        uncertainty_notation
    ) / 5.0 AS evidence_support_partial
FROM legal_narrative_responsibility_claims
ORDER BY evidence_support_partial DESC;

SELECT
    item,
    claim_context,
    (
        overcoherence * 0.18 +
        evidentiary_gap * 0.18 +
        hallucinated_authority * 0.22 +
        (1 - human_review) * 0.10
    ) AS legal_narrative_risk_partial
FROM legal_narrative_responsibility_claims
ORDER BY legal_narrative_risk_partial DESC;
