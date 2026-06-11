-- National memory governance diagnostic queries.

SELECT
    item,
    claim_context,
    (
        group_representation +
        source_diversity +
        testimony_visibility +
        countermemory_inclusion
    ) / 4.0 AS memory_plurality_partial
FROM national_memory_governance_claims
ORDER BY memory_plurality_partial DESC;

SELECT
    item,
    claim_context,
    (
        hero_compression * 0.17 +
        innocence_story * 0.18 +
        exclusion_omission * 0.18 +
        (1 - revision_capacity) * 0.18
    ) AS national_myth_risk_partial
FROM national_memory_governance_claims
ORDER BY national_myth_risk_partial DESC;
