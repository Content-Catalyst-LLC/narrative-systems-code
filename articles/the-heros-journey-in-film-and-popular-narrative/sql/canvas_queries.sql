-- Hero journey film governance diagnostic queries.

SELECT
    item,
    film_context,
    (
        call_authenticity +
        threshold_significance +
        ordeal_relevance +
        value_change +
        return_boon +
        ethical_consequence
    ) / 6.0 AS heroic_arc_integrity
FROM hero_journey_film_governance_claims
ORDER BY heroic_arc_integrity DESC;

SELECT
    item,
    film_context,
    (
        beat_compliance +
        (1 - human_review)
    ) / 2.0 AS formula_and_review_risk
FROM hero_journey_film_governance_claims
ORDER BY formula_and_review_risk DESC;
