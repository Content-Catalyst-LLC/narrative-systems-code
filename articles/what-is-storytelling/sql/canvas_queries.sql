-- canvas_queries.sql

-- Narrative coherence score.
SELECT
    item,
    story_type,
    (
        sequence_clarity +
        agency_clarity +
        causal_connection +
        transformation_clarity +
        interpretive_relevance
    ) / 5.0 AS coherence_score
FROM storytelling_items
ORDER BY coherence_score DESC;

-- Governance risk score.
SELECT
    item,
    story_type,
    (
        (1 - evidence_strength) * 0.30 +
        (1 - representation_care) * 0.30 +
        persuasive_intensity * 0.20 +
        audience_consequence * 0.20
    ) AS governance_risk
FROM storytelling_items
ORDER BY governance_risk DESC;

-- Motif recurrence score.
SELECT
    item,
    motif,
    frequency,
    interpretive_weight,
    frequency * interpretive_weight AS motif_score
FROM motifs
ORDER BY motif_score DESC;

-- Turning point inventory.
SELECT
    item,
    event_order,
    event_label,
    event_function
FROM narrative_events
WHERE turning_point = 1
ORDER BY item, event_order;
