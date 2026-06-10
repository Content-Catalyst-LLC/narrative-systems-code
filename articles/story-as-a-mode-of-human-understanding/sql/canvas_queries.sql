-- canvas_queries.sql

-- Narrative understanding score.
SELECT
    item,
    story_type,
    (
        sequence_clarity +
        causal_framing +
        agency_mapping +
        memory_integration +
        evidence_support +
        openness_to_revision
    ) / 6.0 AS understanding_score
FROM narrative_understanding_items
ORDER BY understanding_score DESC;

-- Moral understanding score.
SELECT
    item,
    story_type,
    (
        consequence_visibility +
        agency_mapping +
        harm_recognition +
        responsibility_mapping +
        repair_awareness
    ) / 5.0 AS moral_understanding_score
FROM narrative_understanding_items
ORDER BY moral_understanding_score DESC;

-- Possible-world score.
SELECT
    item,
    story_type,
    (
        alternative_logic +
        causal_framing +
        uncertainty_signaling +
        interpretive_diversity +
        openness_to_revision
    ) / 5.0 AS possible_world_score
FROM narrative_understanding_items
ORDER BY possible_world_score DESC;

-- Narrative overreach risk.
SELECT
    item,
    story_type,
    (
        (1 - evidence_support) * 0.25 +
        hindsight_bias * 0.20 +
        false_coherence * 0.25 +
        selection_bias * 0.15 +
        closure_pressure * 0.15
    ) AS overreach_risk
FROM narrative_understanding_items
ORDER BY overreach_risk DESC;
