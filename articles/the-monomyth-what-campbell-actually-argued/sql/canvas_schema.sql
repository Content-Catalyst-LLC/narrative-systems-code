-- canvas_schema.sql
-- SQLite-compatible schema for monomyth claim analysis.

PRAGMA foreign_keys = ON;

DROP TABLE IF EXISTS monomyth_governance_notes;
DROP TABLE IF EXISTS formula_drift_risks;
DROP TABLE IF EXISTS specificity_notes;
DROP TABLE IF EXISTS pattern_features;
DROP TABLE IF EXISTS source_contexts;
DROP TABLE IF EXISTS monomyth_claims;

CREATE TABLE monomyth_claims (
    claim_id INTEGER PRIMARY KEY,
    item TEXT NOT NULL UNIQUE,
    claim_context TEXT NOT NULL,
    departure_pattern REAL CHECK (departure_pattern >= 0 AND departure_pattern <= 1),
    threshold_crossing REAL CHECK (threshold_crossing >= 0 AND threshold_crossing <= 1),
    initiation_trial REAL CHECK (initiation_trial >= 0 AND initiation_trial <= 1),
    descent_symbolic_death REAL CHECK (descent_symbolic_death >= 0 AND descent_symbolic_death <= 1),
    boon REAL CHECK (boon >= 0 AND boon <= 1),
    return_pattern REAL CHECK (return_pattern >= 0 AND return_pattern <= 1),
    language_notes REAL CHECK (language_notes >= 0 AND language_notes <= 1),
    cultural_tradition REAL CHECK (cultural_tradition >= 0 AND cultural_tradition <= 1),
    ritual_context REAL CHECK (ritual_context >= 0 AND ritual_context <= 1),
    historical_context REAL CHECK (historical_context >= 0 AND historical_context <= 1),
    oral_performance_context REAL CHECK (oral_performance_context >= 0 AND oral_performance_context <= 1),
    authority_notes REAL CHECK (authority_notes >= 0 AND authority_notes <= 1),
    stage_literalism REAL CHECK (stage_literalism >= 0 AND stage_literalism <= 1),
    beat_matching REAL CHECK (beat_matching >= 0 AND beat_matching <= 1),
    context_loss REAL CHECK (context_loss >= 0 AND context_loss <= 1),
    overfitting REAL CHECK (overfitting >= 0 AND overfitting <= 1),
    universal_claim_strength REAL CHECK (universal_claim_strength >= 0 AND universal_claim_strength <= 1),
    counterexample_inclusion REAL CHECK (counterexample_inclusion >= 0 AND counterexample_inclusion <= 1),
    method_limits REAL CHECK (method_limits >= 0 AND method_limits <= 1),
    ethics_governance REAL CHECK (ethics_governance >= 0 AND ethics_governance <= 1),
    ritual_verification REAL CHECK (ritual_verification >= 0 AND ritual_verification <= 1),
    uncertainty_marking REAL CHECK (uncertainty_marking >= 0 AND uncertainty_marking <= 1),
    community_sensitivity REAL CHECK (community_sensitivity >= 0 AND community_sensitivity <= 1),
    public_consequence REAL CHECK (public_consequence >= 0 AND public_consequence <= 1),
    owner TEXT,
    status TEXT
);

CREATE TABLE source_contexts (
    source_id INTEGER PRIMARY KEY,
    item TEXT NOT NULL,
    source_type TEXT,
    source_context TEXT,
    documentation_note TEXT,
    FOREIGN KEY (item) REFERENCES monomyth_claims(item)
);

CREATE TABLE pattern_features (
    pattern_id INTEGER PRIMARY KEY,
    item TEXT NOT NULL,
    pattern_feature TEXT,
    fit_note TEXT,
    FOREIGN KEY (item) REFERENCES monomyth_claims(item)
);

CREATE TABLE specificity_notes (
    specificity_id INTEGER PRIMARY KEY,
    item TEXT NOT NULL,
    specificity_focus TEXT,
    review_note TEXT,
    FOREIGN KEY (item) REFERENCES monomyth_claims(item)
);

CREATE TABLE formula_drift_risks (
    risk_id INTEGER PRIMARY KEY,
    item TEXT NOT NULL,
    risk_type TEXT,
    severity TEXT,
    note TEXT,
    FOREIGN KEY (item) REFERENCES monomyth_claims(item)
);

CREATE TABLE monomyth_governance_notes (
    note_id INTEGER PRIMARY KEY,
    item TEXT NOT NULL,
    governance_focus TEXT,
    review_owner TEXT,
    status TEXT,
    FOREIGN KEY (item) REFERENCES monomyth_claims(item)
);
