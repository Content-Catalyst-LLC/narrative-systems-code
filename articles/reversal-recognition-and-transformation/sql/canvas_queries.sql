-- canvas_queries.sql

-- Reversal integrity.
SELECT
    item,
    story_type,
    (
        preparation_trace +
        causal_linkage +
        state_change +
        earned_surprise +
        action_fit +
        knowledge_reorientation
    ) / 6.0 AS reversal_integrity
FROM reversal_recognition_items
ORDER BY reversal_integrity DESC;

-- Recognition clarity.
SELECT
    item,
    story_type,
    (
        evidence_visibility +
        interpretive_support +
        meaning_revision +
        relation_linkage +
        uncertainty_clarity
    ) / 5.0 AS recognition_clarity
FROM reversal_recognition_items
ORDER BY recognition_clarity DESC;

-- Transformation depth.
SELECT
    item,
    story_type,
    (
        identity_change +
        action_consequence +
        relationship_change +
        value_change +
        future_possibility +
        governance_accountability
    ) / 6.0 AS transformation_depth
FROM reversal_recognition_items
ORDER BY transformation_depth DESC;

-- Recognition risk.
SELECT
    item,
    story_type,
    (
        false_recognition * 0.25 +
        arbitrary_twist * 0.25 +
        closure_pressure * 0.20 +
        evidence_omission * 0.20 +
        (1 - uncertainty_clarity) * 0.10
    ) AS recognition_risk
FROM reversal_recognition_items
ORDER BY recognition_risk DESC;
