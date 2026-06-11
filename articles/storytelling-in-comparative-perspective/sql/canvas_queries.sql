-- Comparative story governance diagnostic queries.

SELECT
    item,
    comparison_context,
    (
        source_context +
        difference_preservation +
        evidence_quality +
        translation_reliability
    ) / 4.0 AS comparative_integrity_partial
FROM comparative_story_governance_claims
ORDER BY comparative_integrity_partial DESC;

SELECT
    item,
    comparison_context,
    (
        universalism_claims +
        template_capture +
        archive_bias +
        (1 - expert_review)
    ) / 4.0 AS flattening_and_ai_review_risk
FROM comparative_story_governance_claims
ORDER BY flattening_and_ai_review_risk DESC;
