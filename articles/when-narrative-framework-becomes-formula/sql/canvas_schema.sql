DROP TABLE IF EXISTS narrative_formula_drift_claims;
CREATE TABLE narrative_formula_drift_claims (
  claim_id INTEGER PRIMARY KEY,
  item TEXT NOT NULL UNIQUE,
  claim_context TEXT NOT NULL,
  template_forcing REAL CHECK (template_forcing >= 0 AND template_forcing <= 1),
  beat_rigidity REAL CHECK (beat_rigidity >= 0 AND beat_rigidity <= 1),
  closure_pressure REAL CHECK (closure_pressure >= 0 AND closure_pressure <= 1),
  story_specificity REAL CHECK (story_specificity >= 0 AND story_specificity <= 1),
  owner TEXT,
  status TEXT,
  notes TEXT
);
