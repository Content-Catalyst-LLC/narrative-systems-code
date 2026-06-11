-- Moral agency diagnostic queries.

SELECT
    item,
    claim_context,
    (
        action_naming +
        intention_distinction +
        consequence_clarity +
        harm_marking +
        repair_orientation +
        other_visibility
    ) / 6.0 AS moral_clarity
FROM moral_agency_claims
ORDER BY moral_clarity DESC;

SELECT
    item,
    claim_context,
    (
        context_overuse * 0.16 +
        intention_shielding * 0.18 +
        victimhood_shielding * 0.18 +
        blame_shifting * 0.18 +
        growth_substitution * 0.16 +
        harm_minimization * 0.14
    ) AS excuse_risk
FROM moral_agency_claims
ORDER BY excuse_risk DESC;
