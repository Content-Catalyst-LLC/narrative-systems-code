-- Institutional memory governance diagnostic queries.

SELECT
    item,
    claim_context,
    (
        purpose_clarity +
        mission_action_alignment +
        record_evidence +
        affected_community_testimony
    ) / 4.0 AS legitimacy_alignment_partial
FROM institutional_memory_governance_claims
ORDER BY legitimacy_alignment_partial DESC;

SELECT
    item,
    claim_context,
    (
        founder_heroization * 0.18 +
        exclusion_omission * 0.18 +
        (1 - voice_multiplicity) * 0.16
    ) AS origin_myth_risk_partial
FROM institutional_memory_governance_claims
ORDER BY origin_myth_risk_partial DESC;
