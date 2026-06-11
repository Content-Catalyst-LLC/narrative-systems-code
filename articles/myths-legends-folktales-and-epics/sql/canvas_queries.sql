-- canvas_queries.sql

SELECT
    item,
    proposed_form,
    (
        truth_claim_clarity +
        social_function +
        memory_orientation +
        performance_trace +
        authority_context +
        genre_notes
    ) / 6.0 AS form_classification
FROM traditional_narrative_forms_items
ORDER BY form_classification DESC;

SELECT
    item,
    proposed_form,
    (
        boundary_clarity +
        category_specificity +
        hybrid_tracking +
        responsible_analogy +
        variation_management
    ) / 5.0 AS narrative_distinction
FROM traditional_narrative_forms_items
ORDER BY narrative_distinction DESC;

SELECT
    item,
    proposed_form,
    (
        origin_memory +
        place_memory +
        ritual_memory +
        heroic_memory +
        identity_memory +
        future_obligation
    ) / 6.0 AS cultural_memory_function
FROM traditional_narrative_forms_items
ORDER BY cultural_memory_function DESC;

SELECT
    item,
    proposed_form,
    (
        context_removal * 0.18 +
        sacred_or_restricted_material * 0.22 +
        performance_omission * 0.16 +
        translation_loss * 0.16 +
        extraction_risk * 0.18 +
        (1 - governance_control) * 0.10
    ) AS adaptation_risk
FROM traditional_narrative_forms_items
ORDER BY adaptation_risk DESC;
