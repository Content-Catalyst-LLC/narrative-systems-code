-- canvas_queries.sql

-- Transmission strength by medium.
SELECT
    medium,
    period_label,
    (
        preservation +
        repeatability +
        circulation +
        archive_durability
    ) / 4.0 AS transmission_strength
FROM story_media_history
ORDER BY transmission_strength DESC;

-- Preservation risk by medium.
SELECT
    medium,
    period_label,
    (
        (1 - archive_durability) * 0.25 +
        governance_complexity * 0.20 +
        (1 - context_retention) * 0.25 +
        (1 - access_openness) * 0.15 +
        (1 - platform_stability) * 0.15
    ) AS preservation_risk
FROM story_media_history
ORDER BY preservation_risk DESC;

-- Audience participation by medium.
SELECT
    medium,
    participation,
    circulation,
    governance_complexity
FROM story_media_history
ORDER BY participation DESC;

-- Preservation risk inventory.
SELECT
    medium,
    risk_type,
    severity,
    note
FROM preservation_risks
ORDER BY medium, severity DESC;
