-- canvas_schema.sql
-- SQLite-compatible schema for cultural storytelling analysis.

PRAGMA foreign_keys = ON;

DROP TABLE IF EXISTS ethical_story_risks;
DROP TABLE IF EXISTS identity_belonging_functions;
DROP TABLE IF EXISTS teaching_functions;
DROP TABLE IF EXISTS cultural_memory_functions;
DROP TABLE IF EXISTS cultural_story_items;

CREATE TABLE cultural_story_items (
    item_id INTEGER PRIMARY KEY,
    item TEXT NOT NULL UNIQUE,
    story_type TEXT NOT NULL,
    cultural_context TEXT,
    memory_function REAL CHECK (memory_function >= 0 AND memory_function <= 1),
    teaching_value REAL CHECK (teaching_value >= 0 AND teaching_value <= 1),
    identity_function REAL CHECK (identity_function >= 0 AND identity_function <= 1),
    belonging_function REAL CHECK (belonging_function >= 0 AND belonging_function <= 1),
    moral_imagination REAL CHECK (moral_imagination >= 0 AND moral_imagination <= 1),
    social_coordination REAL CHECK (social_coordination >= 0 AND social_coordination <= 1),
    transmission_strength REAL CHECK (transmission_strength >= 0 AND transmission_strength <= 1),
    source_transparency REAL CHECK (source_transparency >= 0 AND source_transparency <= 1),
    representation_care REAL CHECK (representation_care >= 0 AND representation_care <= 1),
    persuasive_intensity REAL CHECK (persuasive_intensity >= 0 AND persuasive_intensity <= 1),
    audience_consequence REAL CHECK (audience_consequence >= 0 AND audience_consequence <= 1),
    public_impact REAL CHECK (public_impact >= 0 AND public_impact <= 1),
    owner TEXT,
    status TEXT
);

CREATE TABLE cultural_memory_functions (
    memory_id INTEGER PRIMARY KEY,
    item TEXT NOT NULL,
    memory_role TEXT,
    selected_memory TEXT,
    omission_risk TEXT,
    repair_potential TEXT,
    FOREIGN KEY (item) REFERENCES cultural_story_items(item)
);

CREATE TABLE teaching_functions (
    teaching_id INTEGER PRIMARY KEY,
    item TEXT NOT NULL,
    teaching_type TEXT,
    lesson_or_warning TEXT,
    teaching_strength REAL,
    ethical_caution TEXT,
    FOREIGN KEY (item) REFERENCES cultural_story_items(item)
);

CREATE TABLE identity_belonging_functions (
    identity_id INTEGER PRIMARY KEY,
    item TEXT NOT NULL,
    identity_layer TEXT,
    belonging_mechanism TEXT,
    exclusion_risk TEXT,
    FOREIGN KEY (item) REFERENCES cultural_story_items(item)
);

CREATE TABLE ethical_story_risks (
    risk_id INTEGER PRIMARY KEY,
    item TEXT NOT NULL,
    risk_type TEXT,
    severity TEXT,
    note TEXT,
    FOREIGN KEY (item) REFERENCES cultural_story_items(item)
);
