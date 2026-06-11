-- SQLite-compatible schema for comparative story governance analysis.

DROP TABLE IF EXISTS comparative_story_governance_claims;

CREATE TABLE comparative_story_governance_claims (
    claim_id INTEGER PRIMARY KEY,
    item TEXT NOT NULL UNIQUE,
    comparison_context TEXT NOT NULL,
    source_context REAL CHECK (source_context >= 0 AND source_context <= 1),
    difference_preservation REAL CHECK (difference_preservation >= 0 AND difference_preservation <= 1),
    evidence_quality REAL CHECK (evidence_quality >= 0 AND evidence_quality <= 1),
    translation_reliability REAL CHECK (translation_reliability >= 0 AND translation_reliability <= 1),
    universalism_claims REAL CHECK (universalism_claims >= 0 AND universalism_claims <= 1),
    template_capture REAL CHECK (template_capture >= 0 AND template_capture <= 1),
    archive_bias REAL CHECK (archive_bias >= 0 AND archive_bias <= 1),
    expert_review REAL CHECK (expert_review >= 0 AND expert_review <= 1),
    owner TEXT,
    status TEXT,
    notes TEXT
);
