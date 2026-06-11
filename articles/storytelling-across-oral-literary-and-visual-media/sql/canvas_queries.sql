-- Cross-media story governance diagnostic queries.

SELECT
    item,
    transfer_context,
    (
        embodiment +
        interior_depth +
        spatial_quality +
        temporal_control +
        audience_relation +
        contextual_fit
    ) / 6.0 AS medium_affordance_fit
FROM cross_media_story_governance_claims
ORDER BY medium_affordance_fit DESC;

SELECT
    item,
    transfer_context,
    (
        voice_loss +
        context_loss +
        provenance_loss +
        (1 - governance_review)
    ) / 4.0 AS transfer_risk_partial
FROM cross_media_story_governance_claims
ORDER BY transfer_risk_partial DESC;
