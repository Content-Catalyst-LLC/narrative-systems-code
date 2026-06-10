-- canvas_schema.sql
-- SQLite-compatible schema for oral tradition, performance, and collective memory analysis.

PRAGMA foreign_keys = ON;

DROP TABLE IF EXISTS oral_tradition_governance_notes;
DROP TABLE IF EXISTS archive_risks;
DROP TABLE IF EXISTS collective_memory_functions;
DROP TABLE IF EXISTS transmission_patterns;
DROP TABLE IF EXISTS performance_contexts;
DROP TABLE IF EXISTS oral_tradition_items;

CREATE TABLE oral_tradition_items (
    item_id INTEGER PRIMARY KEY,
    item TEXT NOT NULL UNIQUE,
    tradition_type TEXT NOT NULL,
    teller_role REAL CHECK (teller_role >= 0 AND teller_role <= 1),
    audience_response REAL CHECK (audience_response >= 0 AND audience_response <= 1),
    occasion_clarity REAL CHECK (occasion_clarity >= 0 AND occasion_clarity <= 1),
    embodiment REAL CHECK (embodiment >= 0 AND embodiment <= 1),
    setting_place REAL CHECK (setting_place >= 0 AND setting_place <= 1),
    cultural_frame REAL CHECK (cultural_frame >= 0 AND cultural_frame <= 1),
    lineage_clarity REAL CHECK (lineage_clarity >= 0 AND lineage_clarity <= 1),
    variation_tracking REAL CHECK (variation_tracking >= 0 AND variation_tracking <= 1),
    memory_supports REAL CHECK (memory_supports >= 0 AND memory_supports <= 1),
    governance_protocol REAL CHECK (governance_protocol >= 0 AND governance_protocol <= 1),
    authority_permission REAL CHECK (authority_permission >= 0 AND authority_permission <= 1),
    record_context REAL CHECK (record_context >= 0 AND record_context <= 1),
    origin_memory REAL CHECK (origin_memory >= 0 AND origin_memory <= 1),
    place_memory REAL CHECK (place_memory >= 0 AND place_memory <= 1),
    identity_memory REAL CHECK (identity_memory >= 0 AND identity_memory <= 1),
    historical_memory REAL CHECK (historical_memory >= 0 AND historical_memory <= 1),
    ritual_memory REAL CHECK (ritual_memory >= 0 AND ritual_memory <= 1),
    future_obligation REAL CHECK (future_obligation >= 0 AND future_obligation <= 1),
    consent_limits REAL CHECK (consent_limits >= 0 AND consent_limits <= 1),
    restricted_knowledge REAL CHECK (restricted_knowledge >= 0 AND restricted_knowledge <= 1),
    exposure_risk REAL CHECK (exposure_risk >= 0 AND exposure_risk <= 1),
    ownership_risk REAL CHECK (ownership_risk >= 0 AND ownership_risk <= 1),
    extraction_risk REAL CHECK (extraction_risk >= 0 AND extraction_risk <= 1),
    governance_control REAL CHECK (governance_control >= 0 AND governance_control <= 1),
    community_sensitivity REAL CHECK (community_sensitivity >= 0 AND community_sensitivity <= 1),
    public_consequence REAL CHECK (public_consequence >= 0 AND public_consequence <= 1),
    owner TEXT,
    status TEXT
);

CREATE TABLE performance_contexts (
    context_id INTEGER PRIMARY KEY,
    item TEXT NOT NULL,
    performance_context TEXT,
    teller TEXT,
    audience TEXT,
    occasion TEXT,
    setting_note TEXT,
    FOREIGN KEY (item) REFERENCES oral_tradition_items(item)
);

CREATE TABLE transmission_patterns (
    transmission_id INTEGER PRIMARY KEY,
    item TEXT NOT NULL,
    transmission_mode TEXT,
    variation_pattern TEXT,
    authority_note TEXT,
    review_need TEXT,
    FOREIGN KEY (item) REFERENCES oral_tradition_items(item)
);

CREATE TABLE collective_memory_functions (
    memory_id INTEGER PRIMARY KEY,
    item TEXT NOT NULL,
    primary_memory_function TEXT,
    secondary_memory_function TEXT,
    continuity_note TEXT,
    FOREIGN KEY (item) REFERENCES oral_tradition_items(item)
);

CREATE TABLE archive_risks (
    risk_id INTEGER PRIMARY KEY,
    item TEXT NOT NULL,
    risk_type TEXT,
    severity TEXT,
    note TEXT,
    FOREIGN KEY (item) REFERENCES oral_tradition_items(item)
);

CREATE TABLE oral_tradition_governance_notes (
    note_id INTEGER PRIMARY KEY,
    item TEXT NOT NULL,
    governance_focus TEXT,
    review_owner TEXT,
    status TEXT,
    FOREIGN KEY (item) REFERENCES oral_tradition_items(item)
);
