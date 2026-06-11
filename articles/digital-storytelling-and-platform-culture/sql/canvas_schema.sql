-- SQLite-compatible schema for digital storytelling governance analysis.

DROP TABLE IF EXISTS digital_storytelling_governance_claims;

CREATE TABLE digital_storytelling_governance_claims (
    claim_id INTEGER PRIMARY KEY,
    item TEXT NOT NULL UNIQUE,
    platform_context TEXT NOT NULL,
    context_preservation REAL CHECK (context_preservation >= 0 AND context_preservation <= 1),
    source_authority REAL CHECK (source_authority >= 0 AND source_authority <= 1),
    visibility_provenance_fit REAL CHECK (visibility_provenance_fit >= 0 AND visibility_provenance_fit <= 1),
    ethical_governance REAL CHECK (ethical_governance >= 0 AND ethical_governance <= 1),
    audience_spread REAL CHECK (audience_spread >= 0 AND audience_spread <= 1),
    compression_severity REAL CHECK (compression_severity >= 0 AND compression_severity <= 1),
    synthetic_opacity REAL CHECK (synthetic_opacity >= 0 AND synthetic_opacity <= 1),
    human_review REAL CHECK (human_review >= 0 AND human_review <= 1),
    owner TEXT,
    status TEXT,
    notes TEXT
);
