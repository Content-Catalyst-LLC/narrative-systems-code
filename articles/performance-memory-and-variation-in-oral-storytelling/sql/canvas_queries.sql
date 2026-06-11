-- canvas_queries.sql

-- Performance context.
SELECT
    item,
    storytelling_context,
    (
        teller_role +
        audience_documentation +
        occasion_context +
        place_linkage +
        embodiment +
        interaction_notes
    ) / 6.0 AS performance_context
FROM oral_storytelling_variation_items
ORDER BY performance_context DESC;

-- Memory support.
SELECT
    item,
    storytelling_context,
    (
        repetition +
        formula_use +
        sequence_clarity +
        audience_recognition +
        community_correction +
        transmission_pathway
    ) / 6.0 AS memory_support
FROM oral_storytelling_variation_items
ORDER BY memory_support DESC;

-- Variation accountability.
SELECT
    item,
    storytelling_context,
    (
        variation_tracking +
        context_explanation +
        language_notes +
        source_review +
        access_protocol +
        governance_oversight
    ) / 6.0 AS variation_accountability
FROM oral_storytelling_variation_items
ORDER BY variation_accountability DESC;

-- Archive risk.
SELECT
    item,
    storytelling_context,
    (
        fixation_risk * 0.18 +
        context_removal * 0.18 +
        performance_omission * 0.18 +
        translation_loss * 0.14 +
        extraction_risk * 0.18 +
        (1 - governance_control) * 0.14
    ) AS archive_risk
FROM oral_storytelling_variation_items
ORDER BY archive_risk DESC;
