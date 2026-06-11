-- SQLite-compatible schema for institutional memory governance analysis.

DROP TABLE IF EXISTS institutional_memory_governance_claims;

CREATE TABLE institutional_memory_governance_claims (
    claim_id INTEGER PRIMARY KEY,
    item TEXT NOT NULL UNIQUE,
    claim_context TEXT NOT NULL,
    purpose_clarity REAL CHECK (purpose_clarity >= 0 AND purpose_clarity <= 1),
    mission_action_alignment REAL CHECK (mission_action_alignment >= 0 AND mission_action_alignment <= 1),
    record_evidence REAL CHECK (record_evidence >= 0 AND record_evidence <= 1),
    affected_community_testimony REAL CHECK (affected_community_testimony >= 0 AND affected_community_testimony <= 1),
    founder_heroization REAL CHECK (founder_heroization >= 0 AND founder_heroization <= 1),
    exclusion_omission REAL CHECK (exclusion_omission >= 0 AND exclusion_omission <= 1),
    voice_multiplicity REAL CHECK (voice_multiplicity >= 0 AND voice_multiplicity <= 1),
    public_access REAL CHECK (public_access >= 0 AND public_access <= 1),
    owner TEXT,
    status TEXT,
    notes TEXT
);
