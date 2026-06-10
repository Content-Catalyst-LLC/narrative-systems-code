-- canvas_schema.sql
-- SQLite-compatible schema for meaning architecture analysis.

PRAGMA foreign_keys = ON;

DROP TABLE IF EXISTS temporal_governance_notes;
DROP TABLE IF EXISTS revision_priorities;
DROP TABLE IF EXISTS narrative_drift_flags;
DROP TABLE IF EXISTS continuity_rupture_map;
DROP TABLE IF EXISTS memory_layers;
DROP TABLE IF EXISTS meaning_architecture_items;

CREATE TABLE meaning_architecture_items (
    item_id INTEGER PRIMARY KEY,
    item TEXT NOT NULL UNIQUE,
    story_type TEXT NOT NULL,
    origin_clarity REAL CHECK (origin_clarity >= 0 AND origin_clarity <= 1),
    sequence_clarity REAL CHECK (sequence_clarity >= 0 AND sequence_clarity <= 1),
    continuity_support REAL CHECK (continuity_support >= 0 AND continuity_support <= 1),
    rupture_recognition REAL CHECK (rupture_recognition >= 0 AND rupture_recognition <= 1),
    future_projection REAL CHECK (future_projection >= 0 AND future_projection <= 1),
    governance_visibility REAL CHECK (governance_visibility >= 0 AND governance_visibility <= 1),
    preservation REAL CHECK (preservation >= 0 AND preservation <= 1),
    archive_support REAL CHECK (archive_support >= 0 AND archive_support <= 1),
    repetition_strength REAL CHECK (repetition_strength >= 0 AND repetition_strength <= 1),
    context_retention REAL CHECK (context_retention >= 0 AND context_retention <= 1),
    transmission_strength REAL CHECK (transmission_strength >= 0 AND transmission_strength <= 1),
    evidence_strength REAL CHECK (evidence_strength >= 0 AND evidence_strength <= 1),
    source_age REAL CHECK (source_age >= 0 AND source_age <= 1),
    link_breakage REAL CHECK (link_breakage >= 0 AND link_breakage <= 1),
    audience_consequence REAL CHECK (audience_consequence >= 0 AND audience_consequence <= 1),
    representation_risk REAL CHECK (representation_risk >= 0 AND representation_risk <= 1),
    map_dependency REAL CHECK (map_dependency >= 0 AND map_dependency <= 1),
    owner TEXT,
    status TEXT
);

CREATE TABLE memory_layers (
    memory_id INTEGER PRIMARY KEY,
    item TEXT NOT NULL,
    memory_layer TEXT,
    preservation_method TEXT,
    context_retention TEXT,
    revision_need TEXT,
    FOREIGN KEY (item) REFERENCES meaning_architecture_items(item)
);

CREATE TABLE continuity_rupture_map (
    map_id INTEGER PRIMARY KEY,
    item TEXT NOT NULL,
    continuity_claim TEXT,
    rupture_claim TEXT,
    continuity_risk TEXT,
    rupture_risk TEXT,
    FOREIGN KEY (item) REFERENCES meaning_architecture_items(item)
);

CREATE TABLE narrative_drift_flags (
    flag_id INTEGER PRIMARY KEY,
    item TEXT NOT NULL,
    drift_type TEXT,
    severity TEXT,
    note TEXT,
    FOREIGN KEY (item) REFERENCES meaning_architecture_items(item)
);

CREATE TABLE revision_priorities (
    revision_id INTEGER PRIMARY KEY,
    item TEXT NOT NULL,
    revision_trigger TEXT,
    priority TEXT,
    note TEXT,
    FOREIGN KEY (item) REFERENCES meaning_architecture_items(item)
);

CREATE TABLE temporal_governance_notes (
    note_id INTEGER PRIMARY KEY,
    item TEXT NOT NULL,
    governance_focus TEXT,
    review_owner TEXT,
    status TEXT,
    FOREIGN KEY (item) REFERENCES meaning_architecture_items(item)
);
