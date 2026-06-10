-- canvas_queries.sql

-- Plot unity.
SELECT
    item,
    story_type,
    (
        action_clarity +
        causal_linkage +
        episode_dependency +
        turning_point_relevance +
        resolution_support +
        goal_coherence
    ) / 6.0 AS plot_unity
FROM aristotelian_plot_items
ORDER BY plot_unity DESC;

-- Reversal and recognition strength.
SELECT
    item,
    story_type,
    (
        direction_change +
        knowledge_change +
        preparation_strength +
        consequence_pressure +
        emotional_intellectual_impact
    ) / 5.0 AS reversal_recognition_strength
FROM aristotelian_plot_items
ORDER BY reversal_recognition_strength DESC;

-- Formula risk.
SELECT
    item,
    story_type,
    (
        hero_template_saturation * 0.20 +
        closure_pressure * 0.25 +
        unity_bias * 0.20 +
        genre_bias * 0.20 +
        (1 - medium_fit) * 0.15
    ) AS formula_risk
FROM aristotelian_plot_items
ORDER BY formula_risk DESC;

-- Governance score.
SELECT
    item,
    story_type,
    (
        (
            action_clarity +
            causal_linkage +
            episode_dependency +
            turning_point_relevance +
            resolution_support +
            goal_coherence
        ) / 6.0 +
        character_action_integration +
        genre_fit +
        medium_fit +
        cultural_awareness
    ) / 5.0 AS governance_score
FROM aristotelian_plot_items
ORDER BY governance_score DESC;
