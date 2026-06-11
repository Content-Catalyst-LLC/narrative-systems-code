SELECT item, claim_context,
  (template_forcing * 0.20 + beat_rigidity * 0.18 + closure_pressure * 0.18 + (1 - story_specificity) * 0.14) AS partial_formula_drift
FROM narrative_formula_drift_claims
ORDER BY partial_formula_drift DESC;
