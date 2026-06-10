-- canvas_queries.sql

-- Rhetorical balance.
SELECT
    item,
    story_type,
    (
        ethos_strength +
        logos_support +
        pathos_proportionality +
        audience_fit +
        context_clarity
    ) / 5.0 AS rhetorical_balance
FROM public_story_rhetoric_items
ORDER BY rhetorical_balance DESC;

-- Persuasion force.
SELECT
    item,
    story_type,
    (
        identification_strength * 0.25 +
        emotional_intensity * 0.20 +
        causal_clarity * 0.20 +
        urgency * 0.15 +
        action_clarity * 0.20
    ) AS persuasion_force
FROM public_story_rhetoric_items
ORDER BY persuasion_force DESC;

-- Public story risk.
SELECT
    item,
    story_type,
    (
        (1 - verification_strength) * 0.25 +
        emotional_coercion * 0.20 +
        scapegoating_risk * 0.25 +
        identity_manipulation * 0.15 +
        closure_pressure * 0.15
    ) AS public_story_risk
FROM public_story_rhetoric_items
ORDER BY public_story_risk DESC;

-- Governance priority.
SELECT
    item,
    story_type,
    (
        (
            identification_strength * 0.25 +
            emotional_intensity * 0.20 +
            causal_clarity * 0.20 +
            urgency * 0.15 +
            action_clarity * 0.20
        ) * 0.25 +
        (
            (1 - verification_strength) * 0.25 +
            emotional_coercion * 0.20 +
            scapegoating_risk * 0.25 +
            identity_manipulation * 0.15 +
            closure_pressure * 0.15
        ) * 0.35 +
        audience_consequence * 0.20 +
        representation_sensitivity * 0.20
    ) AS governance_priority_score
FROM public_story_rhetoric_items
ORDER BY governance_priority_score DESC;
