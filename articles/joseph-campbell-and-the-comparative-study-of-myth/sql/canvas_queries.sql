-- canvas_queries.sql

-- Comparative pattern.
SELECT
    item,
    claim_context,
    (
        departure_pattern +
        threshold_crossing +
        ordeal_or_trial +
        helper_presence +
        return_pattern +
        boon_or_renewal
    ) / 6.0 AS comparative_pattern
FROM comparative_myth_claims
ORDER BY comparative_pattern DESC;

-- Cultural specificity.
SELECT
    item,
    claim_context,
    (
        language_notes +
        ritual_context +
        historical_context +
        community_authority +
        source_tradition +
        performance_or_oral_context
    ) / 6.0 AS cultural_specificity
FROM comparative_myth_claims
ORDER BY cultural_specificity DESC;

-- Generalization risk.
SELECT
    item,
    claim_context,
    (
        universal_claim_strength * 0.18 +
        selective_evidence * 0.18 +
        context_loss * 0.18 +
        formula_reduction * 0.16 +
        ethical_risk * 0.16 +
        (1 - counterexample_inclusion) * 0.14
    ) AS generalization_risk
FROM comparative_myth_claims
ORDER BY generalization_risk DESC;

-- Interpretation readiness.
SELECT
    item,
    claim_context,
    (
        (
            language_notes +
            ritual_context +
            historical_context +
            community_authority +
            source_tradition +
            performance_or_oral_context
        ) / 6.0 +
        counterexample_inclusion +
        method_limits +
        ritual_verification +
        ethics_governance +
        uncertainty_marking
    ) / 6.0 AS interpretation_readiness
FROM comparative_myth_claims
ORDER BY interpretation_readiness DESC;
