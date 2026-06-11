-- canvas_schema.sql
-- SQLite-compatible schema for Joseph Campbell and comparative myth analysis.

PRAGMA foreign_keys = ON;

DROP TABLE IF EXISTS comparative_myth_governance_notes;
DROP TABLE IF EXISTS generalization_risks;
DROP TABLE IF EXISTS cultural_specificity_notes;
DROP TABLE IF EXISTS pattern_features;
DROP TABLE IF EXISTS source_contexts;
DROP TABLE IF EXISTS comparative_myth_claims;

CREATE TABLE comparative_myth_claims (
    claim_id INTEGER PRIMARY KEY,
    item TEXT NOT NULL UNIQUE,
    claim_context TEXT NOT NULL,
    departure_pattern REAL CHECK (departure_pattern >= 0 AND departure_pattern <= 1),
    threshold_crossing REAL CHECK (threshold_crossing >= 0 AND threshold_crossing <= 1),
    ordeal_or_trial REAL CHECK (ordeal_or_trial >= 0 AND ordeal_or_trial <= 1),
    helper_presence REAL CHECK (helper_presence >= 0 AND helper_presence <= 1),
    return_pattern REAL CHECK (return_pattern >= 0 AND return_pattern <= 1),
    boon_or_renewal REAL CHECK (boon_or_renewal >= 0 AND boon_or_renewal <= 1),
    language_notes REAL CHECK (language_notes >= 0 AND language_notes <= 1),
    ritual_context REAL CHECK (ritual_context >= 0 AND ritual_context <= 1),
    historical_context REAL CHECK (historical_context >= 0 AND historical_context <= 1),
    community_authority REAL CHECK (community_authority >= 0 AND community_authority <= 1),
    source_tradition REAL CHECK (source_tradition >= 0 AND source_tradition <= 1),
    performance_or_oral_context REAL CHECK (performance_or_oral_context >= 0 AND performance_or_oral_context <= 1),
    universal_claim_strength REAL CHECK (universal_claim_strength >= 0 AND universal_claim_strength <= 1),
    selective_evidence REAL CHECK (selective_evidence >= 0 AND selective_evidence <= 1),
    context_loss REAL CHECK (context_loss >= 0 AND context_loss <= 1),
    formula_reduction REAL CHECK (formula_reduction >= 0 AND formula_reduction <= 1),
    ethical_risk REAL CHECK (ethical_risk >= 0 AND ethical_risk <= 1),
    counterexample_inclusion REAL CHECK (counterexample_inclusion >= 0 AND counterexample_inclusion <= 1),
    method_limits REAL CHECK (method_limits >= 0 AND method_limits <= 1),
    ritual_verification REAL CHECK (ritual_verification >= 0 AND ritual_verification <= 1),
    ethics_governance REAL CHECK (ethics_governance >= 0 AND ethics_governance <= 1),
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
    FOREIGN KEY (item) REFERENCES comparative_myth_claims(item)
);

CREATE TABLE pattern_features (
    pattern_id INTEGER PRIMARY KEY,
    item TEXT NOT NULL,
    pattern_feature TEXT,
    fit_note TEXT,
    FOREIGN KEY (item) REFERENCES comparative_myth_claims(item)
);

CREATE TABLE cultural_specificity_notes (
    specificity_id INTEGER PRIMARY KEY,
    item TEXT NOT NULL,
    specificity_focus TEXT,
    review_note TEXT,
    FOREIGN KEY (item) REFERENCES comparative_myth_claims(item)
);

CREATE TABLE generalization_risks (
    risk_id INTEGER PRIMARY KEY,
    item TEXT NOT NULL,
    risk_type TEXT,
    severity TEXT,
    note TEXT,
    FOREIGN KEY (item) REFERENCES comparative_myth_claims(item)
);

CREATE TABLE comparative_myth_governance_notes (
    note_id INTEGER PRIMARY KEY,
    item TEXT NOT NULL,
    governance_focus TEXT,
    review_owner TEXT,
    status TEXT,
    FOREIGN KEY (item) REFERENCES comparative_myth_claims(item)
);
