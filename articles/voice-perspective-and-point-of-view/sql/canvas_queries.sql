-- canvas_queries.sql

-- Voice consistency.
SELECT
    item,
    story_type,
    (
        tone_stability +
        diction_coherence +
        rhetorical_habit +
        address_stability +
        judgment_coherence
    ) / 5.0 AS voice_consistency
FROM voice_perspective_items
ORDER BY voice_consistency DESC;

-- Perspective access.
SELECT
    item,
    story_type,
    (
        knowledge_limits +
        interior_access +
        focalization_clarity +
        level_stability +
        source_boundaries
    ) / 5.0 AS perspective_access
FROM voice_perspective_items
ORDER BY perspective_access DESC;

-- Reliability risk.
SELECT
    item,
    story_type,
    (
        factual_unreliability * 0.20 +
        interpretive_unreliability * 0.20 +
        ethical_unreliability * 0.20 +
        memory_distortion * 0.20 +
        agency_gap * 0.20
    ) AS reliability_risk
FROM voice_perspective_items
ORDER BY reliability_risk DESC;

-- Perspective governance priority.
SELECT
    item,
    story_type,
    (
        (1 - (
            knowledge_limits +
            interior_access +
            focalization_clarity +
            level_stability +
            source_boundaries
        ) / 5.0) * 0.20 +
        (
            factual_unreliability * 0.20 +
            interpretive_unreliability * 0.20 +
            ethical_unreliability * 0.20 +
            memory_distortion * 0.20 +
            agency_gap * 0.20
        ) * 0.30 +
        exposure_sensitivity * 0.20 +
        public_consequence * 0.20 +
        representation_gap * 0.10
    ) AS governance_priority_score
FROM voice_perspective_items
ORDER BY governance_priority_score DESC;
