-- Heroine journey diagnostic queries.

SELECT
    item,
    claim_context,
    (
        separation_from_feminine +
        masculine_identification +
        aridity_after_success +
        descent_crisis +
        reconnection_feminine +
        integration_wholeness
    ) / 6.0 AS heroine_alignment
FROM heroine_journey_claims
ORDER BY heroine_alignment DESC;

SELECT
    item,
    claim_context,
    (
        template_forcing * 0.20 +
        gender_essentialism * 0.20 +
        universal_womanhood * 0.18 +
        psychological_overreach * 0.18 +
        healing_pressure * 0.14 +
        (1 - cultural_context) * 0.10
    ) AS framework_risk
FROM heroine_journey_claims
ORDER BY framework_risk DESC;
