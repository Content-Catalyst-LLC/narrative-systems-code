-- canvas_queries.sql

-- Oral-form context.
SELECT
    item,
    oral_form,
    (
        form_identification +
        speaker_role +
        audience_documentation +
        occasion_notes +
        place_linkage +
        use_context
    ) / 6.0 AS oral_form_context
FROM compact_oral_forms_items
ORDER BY oral_form_context DESC;

-- Sound and repetition.
SELECT
    item,
    oral_form,
    (
        rhythm +
        melody +
        cadence +
        refrain_or_formula +
        participation +
        embodiment
    ) / 6.0 AS sound_and_repetition
FROM compact_oral_forms_items
ORDER BY sound_and_repetition DESC;

-- Ritual authority.
SELECT
    item,
    oral_form,
    (
        role_legitimacy +
        protocol_review +
        consent_status +
        access_control +
        governance_oversight +
        benefit_sharing
    ) / 6.0 AS ritual_authority
FROM compact_oral_forms_items
ORDER BY ritual_authority DESC;

-- Archive risk.
SELECT
    item,
    oral_form,
    (
        quote_extraction_risk * 0.18 +
        context_removal * 0.18 +
        sound_loss * 0.16 +
        translation_loss * 0.16 +
        extraction_risk * 0.18 +
        (1 - governance_control) * 0.14
    ) AS archive_risk
FROM compact_oral_forms_items
ORDER BY archive_risk DESC;
