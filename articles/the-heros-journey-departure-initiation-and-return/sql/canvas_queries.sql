-- Journey structure.
SELECT
    item,
    claim_context,
    (
        departure_pattern +
        threshold_crossing +
        initiation_trial +
        descent_symbolic_death +
        boon +
        return_pattern
    ) / 6.0 AS journey_structure
FROM heros_journey_claims
ORDER BY journey_structure DESC;
