-- Narratology diagnostic queries.

SELECT
    item,
    claim_context,
    (
        story_discourse_clarity +
        voice_clarity +
        focalization_clarity +
        temporal_mapping +
        character_agency_mapping +
        information_control_analysis
    ) / 6.0 AS narrative_grammar_strength
FROM narratology_claims
ORDER BY narrative_grammar_strength DESC;

SELECT
    item,
    claim_context,
    (
        omission_risk * 0.18 +
        power_blindness * 0.20 +
        voice_imbalance * 0.20 +
        closure_pressure * 0.16 +
        unreliable_framing_risk * 0.16
    ) AS governance_risk
FROM narratology_claims
ORDER BY governance_risk DESC;
