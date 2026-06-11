-- SQLite-compatible schema for life-writing analysis.

DROP TABLE IF EXISTS life_writing_claims;

CREATE TABLE life_writing_claims (
    claim_id INTEGER PRIMARY KEY,
    item TEXT NOT NULL UNIQUE,
    claim_context TEXT NOT NULL,
    memory_clarity REAL CHECK (memory_clarity >= 0 AND memory_clarity <= 1),
    temporal_structure REAL CHECK (temporal_structure >= 0 AND temporal_structure <= 1),
    voice_consistency REAL CHECK (voice_consistency >= 0 AND voice_consistency <= 1),
    agency REAL CHECK (agency >= 0 AND agency <= 1),
    relational_grounding REAL CHECK (relational_grounding >= 0 AND relational_grounding <= 1),
    contextual_depth REAL CHECK (contextual_depth >= 0 AND contextual_depth <= 1),
    fact_checking REAL CHECK (fact_checking >= 0 AND fact_checking <= 1),
    evidence_visibility REAL CHECK (evidence_visibility >= 0 AND evidence_visibility <= 1),
    privacy_risk REAL CHECK (privacy_risk >= 0 AND privacy_risk <= 1),
    consent_limits REAL CHECK (consent_limits >= 0 AND consent_limits <= 1),
    other_person_exposure REAL CHECK (other_person_exposure >= 0 AND other_person_exposure <= 1),
    trauma_extraction REAL CHECK (trauma_extraction >= 0 AND trauma_extraction <= 1),
    self_mythology REAL CHECK (self_mythology >= 0 AND self_mythology <= 1),
    owner TEXT,
    status TEXT,
    notes TEXT
);
