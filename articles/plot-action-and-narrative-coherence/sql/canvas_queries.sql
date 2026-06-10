-- canvas_queries.sql

-- Plot coherence.
SELECT
    item,
    story_type,
    (
        action_clarity +
        causal_linkage +
        motivation_visibility +
        episode_dependency +
        turning_point_strength +
        resolution_consequence
    ) / 6.0 AS plot_coherence
FROM plot_coherence_items
ORDER BY plot_coherence DESC;

-- Action dependency.
SELECT
    item,
    story_type,
    (
        state_change +
        knowledge_change +
        pressure_change +
        relationship_impact +
        future_movement
    ) / 5.0 AS action_dependency
FROM plot_coherence_items
ORDER BY action_dependency DESC;

-- Coherence risk.
SELECT
    item,
    story_type,
    (
        false_causality * 0.25 +
        simplification_bias * 0.20 +
        closure_pressure * 0.20 +
        evidence_omission * 0.20 +
        (1 - uncertainty_clarity) * 0.15
    ) AS coherence_risk
FROM plot_coherence_items
ORDER BY coherence_risk DESC;

-- Governance priority.
SELECT
    item,
    story_type,
    (
        (
            action_clarity +
            causal_linkage +
            motivation_visibility +
            episode_dependency +
            turning_point_strength +
            resolution_consequence
        ) / 6.0 * 0.20 +
        (
            false_causality * 0.25 +
            simplification_bias * 0.20 +
            closure_pressure * 0.20 +
            evidence_omission * 0.20 +
            (1 - uncertainty_clarity) * 0.15
        ) * 0.35 +
        audience_sensitivity * 0.20 +
        public_consequence * 0.25
    ) AS governance_priority_score
FROM plot_coherence_items
ORDER BY governance_priority_score DESC;
