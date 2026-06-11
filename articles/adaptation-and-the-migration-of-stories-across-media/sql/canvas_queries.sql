-- Adaptation governance diagnostic queries.

SELECT
    item,
    adaptation_context,
    (
        source_core_preservation +
        medium_fit +
        transformation_purpose +
        context_preservation +
        ethical_governance
    ) / 5.0 AS adaptation_integrity_partial
FROM adaptation_governance_claims
ORDER BY adaptation_integrity_partial DESC;

SELECT
    item,
    adaptation_context,
    (
        voice_loss +
        context_loss +
        provenance_loss +
        (1 - human_review)
    ) / 4.0 AS transfer_and_review_risk
FROM adaptation_governance_claims
ORDER BY transfer_and_review_risk DESC;
