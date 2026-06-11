DROP TABLE IF EXISTS narrative_identity_claims;
CREATE TABLE narrative_identity_claims (
  claim_id INTEGER PRIMARY KEY,
  item TEXT NOT NULL UNIQUE,
  claim_context TEXT NOT NULL,
  memory_continuity REAL CHECK (memory_continuity >= 0 AND memory_continuity <= 1),
  agency REAL CHECK (agency >= 0 AND agency <= 1),
  reduction_risk REAL CHECK (reduction_risk >= 0 AND reduction_risk <= 1),
  forced_coherence REAL CHECK (forced_coherence >= 0 AND forced_coherence <= 1),
  owner TEXT,
  status TEXT,
  notes TEXT
);
