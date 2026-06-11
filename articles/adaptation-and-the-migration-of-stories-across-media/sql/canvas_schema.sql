-- SQLite-compatible schema for adaptation governance analysis.

DROP TABLE IF EXISTS adaptation_governance_claims;

CREATE TABLE adaptation_governance_claims (
    claim_id INTEGER PRIMARY KEY,
    item TEXT NOT NULL UNIQUE,
    adaptation_context TEXT NOT NULL,
    source_core_preservation REAL CHECK (source_core_preservation >= 0 AND source_core_preservation <= 1),
    medium_fit REAL CHECK (medium_fit >= 0 AND medium_fit <= 1),
    transformation_purpose REAL CHECK (transformation_purpose >= 0 AND transformation_purpose <= 1),
    context_preservation REAL CHECK (context_preservation >= 0 AND context_preservation <= 1),
    ethical_governance REAL CHECK (ethical_governance >= 0 AND ethical_governance <= 1),
    voice_loss REAL CHECK (voice_loss >= 0 AND voice_loss <= 1),
    context_loss REAL CHECK (context_loss >= 0 AND context_loss <= 1),
    provenance_loss REAL CHECK (provenance_loss >= 0 AND provenance_loss <= 1),
    human_review REAL CHECK (human_review >= 0 AND human_review <= 1),
    owner TEXT,
    status TEXT,
    notes TEXT
);
