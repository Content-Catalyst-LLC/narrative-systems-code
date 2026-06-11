-- Non-heroic narrative diagnostic queries.

SELECT
    item,
    claim_context,
    (
        consequential_action +
        limit_pressure +
        reversal +
        recognition_knowledge +
        irreversibility +
        witness_burden
    ) / 6.0 AS tragic_structure
FROM non_heroic_narrative_claims
ORDER BY tragic_structure DESC;

SELECT
    item,
    claim_context,
    (
        care +
        endurance +
        witness +
        refusal +
        maintenance +
        survival
    ) / 6.0 AS non_heroic_agency
FROM non_heroic_narrative_claims
ORDER BY non_heroic_agency DESC;
