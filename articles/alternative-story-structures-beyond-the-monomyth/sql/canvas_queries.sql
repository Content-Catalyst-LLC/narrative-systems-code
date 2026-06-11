-- Alternative story structure diagnostic queries.

SELECT
    item,
    claim_context,
    (
        arc_signal +
        cycle_signal +
        braid_signal +
        mosaic_signal +
        network_signal +
        relational_signal +
        fragment_signal
    ) / 7.0 AS structural_plurality
FROM alternative_structure_claims
ORDER BY structural_plurality DESC;

SELECT
    item,
    claim_context,
    (
        hero_forcing * 0.20 +
        conflict_substitution * 0.18 +
        return_pressure * 0.16 +
        individualization_pressure * 0.18 +
        template_forcing * 0.18 +
        (1 - evidence_visibility) * 0.10
    ) AS monomyth_overfit_risk
FROM alternative_structure_claims
ORDER BY monomyth_overfit_risk DESC;
