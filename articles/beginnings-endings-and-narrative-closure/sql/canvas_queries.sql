-- canvas_queries.sql

-- Opening clarity.
SELECT
    item,
    story_type,
    (
        voice_signal +
        world_orientation +
        pressure_introduction +
        stakes_visibility +
        question_framing +
        contract_transparency
    ) / 6.0 AS opening_clarity
FROM beginning_closure_items
ORDER BY opening_clarity DESC;

-- Closure integrity.
SELECT
    item,
    story_type,
    (
        promise_fulfillment +
        resolution_suitability +
        transformation_depth +
        aftermath_clarity +
        emotional_honesty +
        unresolved_harm_honesty
    ) / 6.0 AS closure_integrity
FROM beginning_closure_items
ORDER BY closure_integrity DESC;

-- Beginning-ending alignment.
SELECT
    item,
    story_type,
    (
        motif_return +
        question_answer +
        interpretive_echo +
        thematic_continuity +
        frame_revision
    ) / 5.0 AS beginning_ending_alignment
FROM beginning_closure_items
ORDER BY beginning_ending_alignment DESC;

-- Closure risk.
SELECT
    item,
    story_type,
    (
        premature_repair * 0.24 +
        false_resolution * 0.24 +
        system_flattening * 0.20 +
        aftermath_omission * 0.18 +
        excessive_audience_comfort * 0.14
    ) AS closure_risk
FROM beginning_closure_items
ORDER BY closure_risk DESC;
