-- canvas_queries.sql

-- Performance context.
SELECT
    item,
    tradition_type,
    (
        teller_role +
        audience_response +
        occasion_clarity +
        embodiment +
        setting_place +
        cultural_frame
    ) / 6.0 AS performance_context
FROM oral_tradition_items
ORDER BY performance_context DESC;

-- Transmission integrity.
SELECT
    item,
    tradition_type,
    (
        lineage_clarity +
        variation_tracking +
        memory_supports +
        governance_protocol +
        authority_permission +
        record_context
    ) / 6.0 AS transmission_integrity
FROM oral_tradition_items
ORDER BY transmission_integrity DESC;

-- Memory function.
SELECT
    item,
    tradition_type,
    (
        origin_memory +
        place_memory +
        identity_memory +
        historical_memory +
        ritual_memory +
        future_obligation
    ) / 6.0 AS memory_function
FROM oral_tradition_items
ORDER BY memory_function DESC;

-- Archive risk.
SELECT
    item,
    tradition_type,
    (
        consent_limits * 0.18 +
        restricted_knowledge * 0.22 +
        exposure_risk * 0.18 +
        ownership_risk * 0.18 +
        extraction_risk * 0.14 +
        (1 - governance_control) * 0.10
    ) AS archive_risk
FROM oral_tradition_items
ORDER BY archive_risk DESC;
