-- Postcolonial narrative-form diagnostic queries.

SELECT
    item,
    claim_context,
    (
        archive_dominance * 0.18 +
        language_hierarchy * 0.18 +
        gaze_centrality * 0.18 +
        template_forcing * 0.18 +
        extraction_anxiety * 0.16 +
        (1 - opacity_protection) * 0.12
    ) AS colonial_form_risk
FROM postcolonial_narrative_form_claims
ORDER BY colonial_form_risk DESC;

SELECT
    item,
    claim_context,
    (
        english_dominance * 0.18 +
        stereotype_bias * 0.18 +
        (1 - community_governance) * 0.14
    ) AS digital_coloniality_partial
FROM postcolonial_narrative_form_claims
ORDER BY digital_coloniality_partial DESC;
