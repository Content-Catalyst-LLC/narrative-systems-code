-- canvas_queries.sql

-- Symbolic function.
SELECT
    item,
    symbolic_context,
    (
        origin_function +
        cosmological_order +
        memory_function +
        identity_function +
        transition_function +
        authority_function
    ) / 6.0 AS symbolic_function
FROM myth_ritual_symbolic_items
ORDER BY symbolic_function DESC;

-- Ritual context.
SELECT
    item,
    symbolic_context,
    (
        sequence_clarity +
        place_linkage +
        gesture_documentation +
        object_symbolism +
        participant_role +
        protocol_transparency
    ) / 6.0 AS ritual_context
FROM myth_ritual_symbolic_items
ORDER BY ritual_context DESC;

-- Ethical risk.
SELECT
    item,
    symbolic_context,
    (
        totalizing_order * 0.18 +
        scapegoating_risk * 0.20 +
        exclusion_risk * 0.18 +
        appropriation_risk * 0.18 +
        harm_exposure * 0.16 +
        (1 - governance_control) * 0.10
    ) AS ethical_risk
FROM myth_ritual_symbolic_items
ORDER BY ethical_risk DESC;

-- Interpretation readiness.
SELECT
    item,
    symbolic_context,
    (
        context_explanation +
        ritual_verification +
        language_notes +
        access_control +
        governance_oversight +
        uncertainty_marking
    ) / 6.0 AS interpretation_readiness
FROM myth_ritual_symbolic_items
ORDER BY interpretation_readiness DESC;
