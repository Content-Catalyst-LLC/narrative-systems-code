-- Life-writing diagnostic queries.

SELECT
    item,
    claim_context,
    (
        memory_clarity +
        temporal_structure +
        voice_consistency +
        agency +
        relational_grounding +
        contextual_depth
    ) / 6.0 AS life_writing_coherence
FROM life_writing_claims
ORDER BY life_writing_coherence DESC;

SELECT
    item,
    claim_context,
    (
        privacy_risk * 0.18 +
        consent_limits * 0.20 +
        other_person_exposure * 0.20 +
        trauma_extraction * 0.18 +
        self_mythology * 0.14
    ) AS ethical_risk
FROM life_writing_claims
ORDER BY ethical_risk DESC;
