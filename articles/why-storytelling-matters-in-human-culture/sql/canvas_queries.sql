-- canvas_queries.sql

-- Cultural story value score.
SELECT
    item,
    story_type,
    (
        memory_function +
        teaching_value +
        identity_function +
        belonging_function +
        moral_imagination +
        social_coordination
    ) / 6.0 AS cultural_value_score
FROM cultural_story_items
ORDER BY cultural_value_score DESC;

-- Narrative risk score.
SELECT
    item,
    story_type,
    (
        persuasive_intensity * 0.25 +
        (1 - source_transparency) * 0.25 +
        (1 - representation_care) * 0.30 +
        audience_consequence * 0.20
    ) AS narrative_risk
FROM cultural_story_items
ORDER BY narrative_risk DESC;

-- Transmission score.
SELECT
    item,
    story_type,
    (
        transmission_strength +
        source_transparency +
        memory_function
    ) / 3.0 AS transmission_score
FROM cultural_story_items
ORDER BY transmission_score DESC;

-- Ethical risk inventory.
SELECT
    item,
    risk_type,
    severity,
    note
FROM ethical_story_risks
ORDER BY item, severity DESC;
