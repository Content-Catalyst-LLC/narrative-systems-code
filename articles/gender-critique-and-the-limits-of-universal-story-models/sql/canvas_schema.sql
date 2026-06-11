-- SQLite-compatible schema for universal story model critique.

DROP TABLE IF EXISTS universal_story_model_claims;

CREATE TABLE universal_story_model_claims (
    claim_id INTEGER PRIMARY KEY,
    item TEXT NOT NULL UNIQUE,
    claim_context TEXT NOT NULL,
    stage_evidence REAL CHECK (stage_evidence >= 0 AND stage_evidence <= 1),
    agency_match REAL CHECK (agency_match >= 0 AND agency_match <= 1),
    transformation_correspondence REAL CHECK (transformation_correspondence >= 0 AND transformation_correspondence <= 1),
    contextual_harmony REAL CHECK (contextual_harmony >= 0 AND contextual_harmony <= 1),
    resolution_similarity REAL CHECK (resolution_similarity >= 0 AND resolution_similarity <= 1),
    evidence_visibility REAL CHECK (evidence_visibility >= 0 AND evidence_visibility <= 1),
    archive_bias REAL CHECK (archive_bias >= 0 AND archive_bias <= 1),
    gender_binary_pressure REAL CHECK (gender_binary_pressure >= 0 AND gender_binary_pressure <= 1),
    cultural_flattening REAL CHECK (cultural_flattening >= 0 AND cultural_flattening <= 1),
    intersectional_erasure REAL CHECK (intersectional_erasure >= 0 AND intersectional_erasure <= 1),
    queer_trans_pressure REAL CHECK (queer_trans_pressure >= 0 AND queer_trans_pressure <= 1),
    local_context REAL CHECK (local_context >= 0 AND local_context <= 1),
    owner TEXT,
    status TEXT,
    notes TEXT
);
