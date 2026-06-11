-- Universal story model diagnostic queries.

SELECT
    item,
    claim_context,
    (
        stage_evidence +
        agency_match +
        transformation_correspondence +
        contextual_harmony +
        resolution_similarity +
        evidence_visibility
    ) / 6.0 AS universal_model_fit
FROM universal_story_model_claims
ORDER BY universal_model_fit DESC;

SELECT
    item,
    claim_context,
    (
        archive_bias * 0.18 +
        gender_binary_pressure * 0.20 +
        cultural_flattening * 0.18 +
        intersectional_erasure * 0.18 +
        queer_trans_pressure * 0.16 +
        (1 - local_context) * 0.10
    ) AS universalism_risk
FROM universal_story_model_claims
ORDER BY universalism_risk DESC;
