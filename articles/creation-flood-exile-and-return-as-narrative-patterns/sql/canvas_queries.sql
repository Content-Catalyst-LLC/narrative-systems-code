-- Creation/flood/exile/return diagnostic queries.

SELECT
    item,
    claim_context,
    (
        creation_signal +
        flood_signal +
        exile_signal +
        return_signal
    ) / 4.0 AS pattern_strength
FROM narrative_pattern_claims
ORDER BY pattern_strength DESC;

SELECT
    item,
    claim_context,
    (
        origin_nostalgia * 0.18 +
        cleansing_fantasy * 0.20 +
        exile_romanticization * 0.18 +
        false_return * 0.18 +
        power_blindness * 0.16
    ) AS ethical_risk
FROM narrative_pattern_claims
ORDER BY ethical_risk DESC;
