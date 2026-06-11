-- Threshold and ordeal review queries.

SELECT
    item,
    claim_context,
    threshold_strength,
    trial_depth,
    ordeal_transformation
FROM threshold_ordeal_claims
ORDER BY ordeal_transformation DESC;
