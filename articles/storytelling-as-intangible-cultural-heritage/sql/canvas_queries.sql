-- canvas_queries.sql

-- Living continuity.
SELECT
    item,
    heritage_context,
    (
        transmission_support +
        performance_context +
        language_vitality +
        apprenticeship_pathways +
        community_recognition +
        variation_management
    ) / 6.0 AS living_continuity
FROM storytelling_heritage_items
ORDER BY living_continuity DESC;

-- Safeguarding readiness.
SELECT
    item,
    heritage_context,
    (
        consent_clarity +
        governance_protocol +
        metadata_quality +
        access_control +
        benefit_sharing +
        review_process
    ) / 6.0 AS safeguarding_readiness
FROM storytelling_heritage_items
ORDER BY safeguarding_readiness DESC;

-- Heritage context preservation.
SELECT
    item,
    heritage_context,
    (
        occasion_context +
        place_linkage +
        ritual_frame +
        embodiment +
        social_transmission +
        knowledge_holder_context
    ) / 6.0 AS heritage_context_preservation
FROM storytelling_heritage_items
ORDER BY heritage_context_preservation DESC;

-- Archive risk.
SELECT
    item,
    heritage_context,
    (
        context_removal * 0.18 +
        sacred_or_restricted_material * 0.22 +
        performance_omission * 0.16 +
        translation_loss * 0.16 +
        extraction_risk * 0.18 +
        (1 - governance_control) * 0.10
    ) AS archive_risk
FROM storytelling_heritage_items
ORDER BY archive_risk DESC;
