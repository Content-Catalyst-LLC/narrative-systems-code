-- canvas_queries.sql

-- Conflict clarity.
SELECT
    item,
    story_type,
    (
        desire_clarity +
        obstacle_clarity +
        pressure_strength +
        agency_visibility +
        stakes_visibility +
        relation_legibility
    ) / 6.0 AS conflict_clarity
FROM conflict_tension_items
ORDER BY conflict_clarity DESC;

-- Tension durability.
SELECT
    item,
    story_type,
    (
        unresolved_pressure +
        meaningful_delay +
        stakes_heightening +
        expectation_pressure +
        complication_movement
    ) / 5.0 AS tension_durability
FROM conflict_tension_items
ORDER BY tension_durability DESC;

-- Narrative movement.
SELECT
    item,
    story_type,
    (
        state_change +
        knowledge_change +
        relationship_impact +
        pressure_change +
        future_movement +
        value_transformation
    ) / 6.0 AS narrative_movement
FROM conflict_tension_items
ORDER BY narrative_movement DESC;

-- Conflict risk.
SELECT
    item,
    story_type,
    (
        scapegoating * 0.25 +
        conflict_inflation * 0.20 +
        trauma_spectacle * 0.20 +
        false_balance * 0.20 +
        closure_pressure * 0.15
    ) AS conflict_risk
FROM conflict_tension_items
ORDER BY conflict_risk DESC;
