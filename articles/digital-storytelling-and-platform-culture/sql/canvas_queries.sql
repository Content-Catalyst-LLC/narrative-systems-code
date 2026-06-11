-- Digital storytelling governance diagnostic queries.

SELECT
    item,
    platform_context,
    (
        context_preservation +
        source_authority +
        visibility_provenance_fit +
        ethical_governance
    ) / 4.0 AS platform_integrity_partial
FROM digital_storytelling_governance_claims
ORDER BY platform_integrity_partial DESC;

SELECT
    item,
    platform_context,
    (
        audience_spread +
        compression_severity +
        synthetic_opacity +
        (1 - human_review)
    ) / 4.0 AS circulation_and_synthetic_risk
FROM digital_storytelling_governance_claims
ORDER BY circulation_and_synthetic_risk DESC;
