-- Representation ethics governance diagnostic queries.

SELECT
    item,
    representation_context,
    (
        voice_agency +
        context_preservation +
        dignity_protection +
        source_accuracy
    ) / 4.0 AS representation_integrity_partial
FROM representation_ethics_governance_claims
ORDER BY representation_integrity_partial DESC;

SELECT
    item,
    representation_context,
    (
        stereotype_tendency +
        exposure_risk +
        synthetic_opacity +
        (1 - human_review)
    ) / 4.0 AS representation_and_synthetic_risk
FROM representation_ethics_governance_claims
ORDER BY representation_and_synthetic_risk DESC;
