-- canvas_queries.sql

-- Monomyth pattern.
SELECT
    item,
    claim_context,
    (
        departure_pattern +
        threshold_crossing +
        initiation_trial +
        descent_symbolic_death +
        boon +
        return_pattern
    ) / 6.0 AS monomyth_pattern
FROM monomyth_claims
ORDER BY monomyth_pattern DESC;

-- Specificity preservation.
SELECT
    item,
    claim_context,
    (
        language_notes +
        cultural_tradition +
        ritual_context +
        historical_context +
        oral_performance_context +
        authority_notes
    ) / 6.0 AS specificity_preservation
FROM monomyth_claims
ORDER BY specificity_preservation DESC;

-- Formula drift.
SELECT
    item,
    claim_context,
    (
        stage_literalism * 0.18 +
        beat_matching * 0.18 +
        context_loss * 0.18 +
        overfitting * 0.16 +
        universal_claim_strength * 0.16 +
        (1 - counterexample_inclusion) * 0.14
    ) AS formula_drift
FROM monomyth_claims
ORDER BY formula_drift DESC;

-- Interpretation readiness.
SELECT
    item,
    claim_context,
    (
        (
            language_notes +
            cultural_tradition +
            ritual_context +
            historical_context +
            oral_performance_context +
            authority_notes
        ) / 6.0 +
        counterexample_inclusion +
        method_limits +
        ethics_governance +
        ritual_verification +
        uncertainty_marking
    ) / 6.0 AS interpretation_readiness
FROM monomyth_claims
ORDER BY interpretation_readiness DESC;
