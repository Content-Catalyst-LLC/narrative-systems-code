-- Serial narrative governance diagnostic queries.

SELECT
    item,
    serial_context,
    (
        episode_function +
        arc_progression +
        thematic_development +
        character_memory +
        payoff_integrity_signal +
        finale_consequence
    ) / 6.0 AS season_coherence
FROM serial_narrative_governance_claims
ORDER BY season_coherence DESC;

SELECT
    item,
    serial_context,
    (
        unresolved_arcs +
        lore_density +
        (1 - human_review)
    ) / 3.0 AS continuity_and_review_risk
FROM serial_narrative_governance_claims
ORDER BY continuity_and_review_risk DESC;
