-- Organizational story governance diagnostic queries.

SELECT
    item,
    claim_context,
    (
        mission_clarity +
        decision_alignment +
        budget_fit +
        stakeholder_impact +
        employee_experience +
        governance_transparency
    ) / 6.0 AS purpose_alignment
FROM organizational_story_governance_claims
ORDER BY purpose_alignment DESC;

SELECT
    item,
    claim_context,
    (
        participation_integrity +
        dissent_visibility +
        human_review
    ) / 3.0 AS voice_and_review_signal
FROM organizational_story_governance_claims
ORDER BY voice_and_review_signal ASC;
