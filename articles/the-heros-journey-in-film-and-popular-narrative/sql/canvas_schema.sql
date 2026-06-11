-- SQLite-compatible schema for hero journey film governance analysis.

DROP TABLE IF EXISTS hero_journey_film_governance_claims;

CREATE TABLE hero_journey_film_governance_claims (
    claim_id INTEGER PRIMARY KEY,
    item TEXT NOT NULL UNIQUE,
    film_context TEXT NOT NULL,
    call_authenticity REAL CHECK (call_authenticity >= 0 AND call_authenticity <= 1),
    threshold_significance REAL CHECK (threshold_significance >= 0 AND threshold_significance <= 1),
    ordeal_relevance REAL CHECK (ordeal_relevance >= 0 AND ordeal_relevance <= 1),
    value_change REAL CHECK (value_change >= 0 AND value_change <= 1),
    return_boon REAL CHECK (return_boon >= 0 AND return_boon <= 1),
    ethical_consequence REAL CHECK (ethical_consequence >= 0 AND ethical_consequence <= 1),
    beat_compliance REAL CHECK (beat_compliance >= 0 AND beat_compliance <= 1),
    formula_risk_note TEXT,
    human_review REAL CHECK (human_review >= 0 AND human_review <= 1),
    owner TEXT,
    status TEXT,
    notes TEXT
);
