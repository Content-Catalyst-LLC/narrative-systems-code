-- Public narrative governance diagnostic queries.

SELECT
    item,
    claim_context,
    (
        self_clarity +
        us_clarity +
        now_clarity +
        value_articulation +
        action_clarity +
        governance_review
    ) / 6.0 AS public_narrative_coherence
FROM public_narrative_governance_claims
ORDER BY public_narrative_coherence DESC;

SELECT
    item,
    claim_context,
    (
        consent_deficit +
        omitted_voices +
        (1 - human_review)
    ) / 3.0 AS voice_and_consent_risk
FROM public_narrative_governance_claims
ORDER BY voice_and_consent_risk DESC;
