-- Public story governance diagnostic queries.

SELECT
    item,
    claim_context,
    (
        self_story_evidence +
        shared_value_clarity +
        now_challenge_clarity
    ) / 3.0 AS public_narrative_strength_partial
FROM public_story_governance_claims
ORDER BY public_narrative_strength_partial DESC;

SELECT
    item,
    claim_context,
    (
        enemy_simplification * 0.18 +
        boundary_hardening * 0.18 +
        crisis_compression * 0.17 +
        scapegoat_intensity * 0.17 +
        (1 - evidence_visibility) * 0.14
    ) AS mythic_simplification_risk_partial
FROM public_story_governance_claims
ORDER BY mythic_simplification_risk_partial DESC;
