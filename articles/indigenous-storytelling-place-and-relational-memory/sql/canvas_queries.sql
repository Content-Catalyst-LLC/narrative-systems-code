-- Indigenous story governance diagnostic queries.

SELECT
    item,
    claim_context,
    (
        place_specificity +
        community_authority +
        teller_relationship +
        listener_context +
        obligation_visibility +
        governance_visibility
    ) / 6.0 AS relational_accountability
FROM indigenous_story_governance_claims
ORDER BY relational_accountability DESC;

SELECT
    item,
    claim_context,
    (
        access_pressure * 0.18 +
        seasonal_restriction * 0.16 +
        ceremonial_restriction * 0.18 +
        template_forcing * 0.16 +
        digital_exposure * 0.16 +
        (1 - governance_visibility) * 0.16
    ) AS protocol_risk
FROM indigenous_story_governance_claims
ORDER BY protocol_risk DESC;
