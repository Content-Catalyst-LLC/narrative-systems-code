-- Ricoeur narrative-time diagnostic queries.

SELECT
    item,
    claim_context,
    (
        memory_mapping +
        anticipation +
        plot_logic +
        configuration +
        refiguration +
        ending_function
    ) / 6.0 AS narrative_time_configuration
FROM ricoeur_narrative_time_claims
ORDER BY narrative_time_configuration DESC;

SELECT
    item,
    claim_context,
    (
        premature_closure * 0.20 +
        redemptive_shortcut * 0.18 +
        erased_continuity * 0.18 +
        delayed_accountability * 0.18 +
        nostalgic_origin * 0.14
    ) AS temporal_governance_risk
FROM ricoeur_narrative_time_claims
ORDER BY temporal_governance_risk DESC;
