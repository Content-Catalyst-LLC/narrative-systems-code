-- SQLite-compatible schema for representation ethics governance analysis.

DROP TABLE IF EXISTS representation_ethics_governance_claims;

CREATE TABLE representation_ethics_governance_claims (
    claim_id INTEGER PRIMARY KEY,
    item TEXT NOT NULL UNIQUE,
    representation_context TEXT NOT NULL,
    voice_agency REAL CHECK (voice_agency >= 0 AND voice_agency <= 1),
    context_preservation REAL CHECK (context_preservation >= 0 AND context_preservation <= 1),
    dignity_protection REAL CHECK (dignity_protection >= 0 AND dignity_protection <= 1),
    source_accuracy REAL CHECK (source_accuracy >= 0 AND source_accuracy <= 1),
    stereotype_tendency REAL CHECK (stereotype_tendency >= 0 AND stereotype_tendency <= 1),
    exposure_risk REAL CHECK (exposure_risk >= 0 AND exposure_risk <= 1),
    informed_consent REAL CHECK (informed_consent >= 0 AND informed_consent <= 1),
    synthetic_opacity REAL CHECK (synthetic_opacity >= 0 AND synthetic_opacity <= 1),
    human_review REAL CHECK (human_review >= 0 AND human_review <= 1),
    owner TEXT,
    status TEXT,
    notes TEXT
);
