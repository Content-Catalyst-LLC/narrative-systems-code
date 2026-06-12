-- Narrative risk governance diagnostic queries.

SELECT
    item,
    narrative_context,
    (
        corroboration +
        source_quality +
        revision_openness +
        human_review
    ) / 4.0 AS inquiry_integrity_partial
FROM narrative_risk_governance_claims
ORDER BY inquiry_integrity_partial DESC;

SELECT
    item,
    narrative_context,
    (
        scapegoating +
        evidence_immunity +
        mythic_simplification +
        synthetic_evidence +
        (1 - revision_openness)
    ) / 5.0 AS narrative_risk_partial
FROM narrative_risk_governance_claims
ORDER BY narrative_risk_partial DESC;
