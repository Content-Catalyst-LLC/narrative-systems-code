-- SQLite-compatible schema for hero's journey analysis.

DROP TABLE IF EXISTS heros_journey_claims;

CREATE TABLE heros_journey_claims (
    claim_id INTEGER PRIMARY KEY,
    item TEXT NOT NULL UNIQUE,
    claim_context TEXT NOT NULL,
    departure_pattern REAL CHECK (departure_pattern >= 0 AND departure_pattern <= 1),
    threshold_crossing REAL CHECK (threshold_crossing >= 0 AND threshold_crossing <= 1),
    initiation_trial REAL CHECK (initiation_trial >= 0 AND initiation_trial <= 1),
    descent_symbolic_death REAL CHECK (descent_symbolic_death >= 0 AND descent_symbolic_death <= 1),
    boon REAL CHECK (boon >= 0 AND boon <= 1),
    return_pattern REAL CHECK (return_pattern >= 0 AND return_pattern <= 1),
    transformation_depth REAL CHECK (transformation_depth >= 0 AND transformation_depth <= 1),
    return_responsibility REAL CHECK (return_responsibility >= 0 AND return_responsibility <= 1),
    specificity_preservation REAL CHECK (specificity_preservation >= 0 AND specificity_preservation <= 1),
    formula_drift REAL,
    interpretation_readiness REAL,
    governance_priority_score REAL,
    review_priority TEXT,
    owner TEXT,
    status TEXT
);
