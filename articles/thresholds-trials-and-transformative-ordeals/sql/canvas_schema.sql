-- SQLite-compatible schema for threshold, trial, and ordeal analysis.

DROP TABLE IF EXISTS threshold_ordeal_claims;

CREATE TABLE threshold_ordeal_claims (
    claim_id INTEGER PRIMARY KEY,
    item TEXT NOT NULL UNIQUE,
    claim_context TEXT NOT NULL,
    threshold_strength REAL CHECK (threshold_strength >= 0 AND threshold_strength <= 1),
    trial_depth REAL CHECK (trial_depth >= 0 AND trial_depth <= 1),
    ordeal_transformation REAL CHECK (ordeal_transformation >= 0 AND ordeal_transformation <= 1),
    ethical_risk REAL,
    interpretation_readiness REAL,
    governance_priority_score REAL,
    review_priority TEXT,
    owner TEXT,
    status TEXT
);
