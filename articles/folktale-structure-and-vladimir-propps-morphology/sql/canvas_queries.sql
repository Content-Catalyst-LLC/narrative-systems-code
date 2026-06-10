-- canvas_queries.sql

-- Function coverage.
SELECT
    item,
    tale_type,
    (
        function_identification +
        sequence_clarity +
        role_mapping +
        variation_tracking +
        context_notes
    ) / 5.0 AS function_coverage
FROM folktale_morphology_items
ORDER BY function_coverage DESC;

-- Sequence integrity.
SELECT
    item,
    tale_type,
    (
        order_coherence +
        transition_logic +
        gap_management +
        repetition_awareness +
        closure_handling
    ) / 5.0 AS sequence_integrity
FROM folktale_morphology_items
ORDER BY sequence_integrity DESC;

-- Morphology-context balance.
SELECT
    item,
    tale_type,
    (
        performance_context +
        cultural_specificity +
        language_notes +
        tradition_review +
        ethical_governance
    ) / 5.0 AS morphology_context_balance
FROM folktale_morphology_items
ORDER BY morphology_context_balance DESC;

-- Formula reduction risk.
SELECT
    item,
    tale_type,
    (
        universalization_risk * 0.22 +
        cultural_erasure_risk * 0.22 +
        performance_omission * 0.18 +
        variation_omission * 0.18 +
        (1 - (
            performance_context +
            cultural_specificity +
            language_notes +
            tradition_review +
            ethical_governance
        ) / 5.0) * 0.20
    ) AS reduction_risk
FROM folktale_morphology_items
ORDER BY reduction_risk DESC;
