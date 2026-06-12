-- SQLite-compatible schema for narrative risk governance analysis.

DROP TABLE IF EXISTS narrative_risk_governance_claims;

CREATE TABLE narrative_risk_governance_claims (
    claim_id INTEGER PRIMARY KEY,
    item TEXT NOT NULL UNIQUE,
    narrative_context TEXT NOT NULL,
    scapegoating REAL CHECK (scapegoating >= 0 AND scapegoating <= 1),
    evidence_immunity REAL CHECK (evidence_immunity >= 0 AND evidence_immunity <= 1),
    mythic_simplification REAL CHECK (mythic_simplification >= 0 AND mythic_simplification <= 1),
    context_loss REAL CHECK (context_loss >= 0 AND context_loss <= 1),
    revision_openness REAL CHECK (revision_openness >= 0 AND revision_openness <= 1),
    corroboration REAL CHECK (corroboration >= 0 AND corroboration <= 1),
    source_quality REAL CHECK (source_quality >= 0 AND source_quality <= 1),
    synthetic_evidence REAL CHECK (synthetic_evidence >= 0 AND synthetic_evidence <= 1),
    human_review REAL CHECK (human_review >= 0 AND human_review <= 1),
    owner TEXT,
    status TEXT,
    notes TEXT
);
