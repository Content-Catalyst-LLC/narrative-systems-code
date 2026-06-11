-- Fragmented narrative diagnostic queries.

SELECT
    item,
    claim_context,
    (
        temporal_rupture +
        gap_marking +
        repetition_patterning +
        silence_respect +
        uncertainty_notes +
        contextual_care
    ) / 6.0 AS fragmentation_sensitivity
FROM fragmented_narrative_claims
ORDER BY fragmentation_sensitivity DESC;

SELECT
    item,
    claim_context,
    (
        forced_coherence * 0.20 +
        redemptive_shortcut * 0.18 +
        extraction_risk * 0.20 +
        identity_reduction * 0.18 +
        spectacle_pressure * 0.14
    ) AS trauma_narrative_risk
FROM fragmented_narrative_claims
ORDER BY trauma_narrative_risk DESC;
