-- Narrative systems governance diagnostic queries.

SELECT
    item,
    modeling_context,
    (
        causal_alignment +
        state_transition_clarity +
        agent_goal_fit +
        world_rule_consistency
    ) / 4.0 AS narrative_coherence_partial
FROM narrative_systems_governance_claims
ORDER BY narrative_coherence_partial DESC;

SELECT
    item,
    modeling_context,
    (
        beat_template_dependence +
        universal_model_claims +
        plot_hallucination +
        (1 - human_review)
    ) / 4.0 AS formula_and_ai_risk
FROM narrative_systems_governance_claims
ORDER BY formula_and_ai_risk DESC;
