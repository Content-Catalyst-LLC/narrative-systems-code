-- Sacred-history diagnostic queries.
SELECT item, claim_context, (sacred_disclosure + event_meaning + authority_clarity) / 3.0 AS revelatory_core FROM sacred_history_claims ORDER BY revelatory_core DESC;
