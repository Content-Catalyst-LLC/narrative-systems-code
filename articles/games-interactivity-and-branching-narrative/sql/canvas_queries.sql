-- Interactive narrative governance diagnostic queries.

SELECT
    item,
    game_context,
    (
        choice_meaningfulness +
        system_response +
        feedback_clarity +
        world_memory
    ) / 4.0 AS agency_integrity_partial
FROM interactive_narrative_governance_claims
ORDER BY agency_integrity_partial DESC;

SELECT
    item,
    game_context,
    (
        branch_count_pressure +
        state_dependency +
        consequence_tracking +
        (1 - human_review)
    ) / 4.0 AS branch_and_review_risk
FROM interactive_narrative_governance_claims
ORDER BY branch_and_review_risk DESC;
