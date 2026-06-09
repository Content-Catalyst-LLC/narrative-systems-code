-- canvas_schema.sql
-- SQLite-compatible schema for narrative-system and storytelling analysis.

PRAGMA foreign_keys = ON;

DROP TABLE IF EXISTS ethical_flags;
DROP TABLE IF EXISTS motifs;
DROP TABLE IF EXISTS relationships;
DROP TABLE IF EXISTS characters;
DROP TABLE IF EXISTS narrative_events;
DROP TABLE IF EXISTS storytelling_items;

CREATE TABLE storytelling_items (
    item_id INTEGER PRIMARY KEY,
    item TEXT NOT NULL UNIQUE,
    story_type TEXT NOT NULL,
    description TEXT,
    sequence_clarity REAL CHECK (sequence_clarity >= 0 AND sequence_clarity <= 1),
    agency_clarity REAL CHECK (agency_clarity >= 0 AND agency_clarity <= 1),
    causal_connection REAL CHECK (causal_connection >= 0 AND causal_connection <= 1),
    conflict_definition REAL CHECK (conflict_definition >= 0 AND conflict_definition <= 1),
    transformation_clarity REAL CHECK (transformation_clarity >= 0 AND transformation_clarity <= 1),
    motif_use REAL CHECK (motif_use >= 0 AND motif_use <= 1),
    interpretive_relevance REAL CHECK (interpretive_relevance >= 0 AND interpretive_relevance <= 1),
    evidence_strength REAL CHECK (evidence_strength >= 0 AND evidence_strength <= 1),
    representation_care REAL CHECK (representation_care >= 0 AND representation_care <= 1),
    persuasive_intensity REAL CHECK (persuasive_intensity >= 0 AND persuasive_intensity <= 1),
    audience_consequence REAL CHECK (audience_consequence >= 0 AND audience_consequence <= 1),
    owner TEXT,
    status TEXT
);

CREATE TABLE narrative_events (
    event_id TEXT PRIMARY KEY,
    item TEXT NOT NULL,
    event_order INTEGER NOT NULL,
    event_label TEXT NOT NULL,
    event_function TEXT,
    turning_point INTEGER DEFAULT 0,
    FOREIGN KEY (item) REFERENCES storytelling_items(item)
);

CREATE TABLE characters (
    character_id TEXT PRIMARY KEY,
    item TEXT NOT NULL,
    character_name TEXT NOT NULL,
    role TEXT,
    agency_score REAL CHECK (agency_score >= 0 AND agency_score <= 1),
    representation_note TEXT,
    FOREIGN KEY (item) REFERENCES storytelling_items(item)
);

CREATE TABLE relationships (
    relationship_id INTEGER PRIMARY KEY,
    source TEXT NOT NULL,
    target TEXT NOT NULL,
    item TEXT NOT NULL,
    relationship_type TEXT,
    weight REAL CHECK (weight >= 0 AND weight <= 1)
);

CREATE TABLE motifs (
    motif_id TEXT PRIMARY KEY,
    item TEXT NOT NULL,
    motif TEXT NOT NULL,
    frequency INTEGER,
    interpretive_weight REAL CHECK (interpretive_weight >= 0 AND interpretive_weight <= 1),
    notes TEXT,
    FOREIGN KEY (item) REFERENCES storytelling_items(item)
);

CREATE TABLE ethical_flags (
    flag_id INTEGER PRIMARY KEY,
    item TEXT NOT NULL,
    flag_type TEXT NOT NULL,
    severity TEXT,
    note TEXT,
    FOREIGN KEY (item) REFERENCES storytelling_items(item)
);
