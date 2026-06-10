-- canvas_queries.sql

-- Temporal coherence.
SELECT
    item,
    story_type,
    (
        origin_clarity +
        sequence_clarity +
        continuity_support +
        rupture_recognition +
        future_projection +
        governance_visibility
    ) / 6.0 AS temporal_coherence
FROM meaning_architecture_items
ORDER BY temporal_coherence DESC;

-- Memory durability.
SELECT
    item,
    story_type,
    (
        preservation +
        archive_support +
        repetition_strength +
        context_retention +
        transmission_strength
    ) / 5.0 AS memory_durability
FROM meaning_architecture_items
ORDER BY memory_durability DESC;

-- Narrative drift risk.
SELECT
    item,
    story_type,
    (
        (1 - evidence_strength) * 0.25 +
        source_age * 0.20 +
        link_breakage * 0.20 +
        (1 - context_retention) * 0.20 +
        repetition_strength * 0.15
    ) AS drift_risk
FROM meaning_architecture_items
ORDER BY drift_risk DESC;

-- Revision priority.
SELECT
    item,
    story_type,
    (
        (
            (1 - evidence_strength) * 0.25 +
            source_age * 0.20 +
            link_breakage * 0.20 +
            (1 - context_retention) * 0.20 +
            repetition_strength * 0.15
        ) * 0.40 +
        audience_consequence * 0.20 +
        representation_risk * 0.20 +
        map_dependency * 0.20
    ) AS revision_priority_score
FROM meaning_architecture_items
ORDER BY revision_priority_score DESC;
