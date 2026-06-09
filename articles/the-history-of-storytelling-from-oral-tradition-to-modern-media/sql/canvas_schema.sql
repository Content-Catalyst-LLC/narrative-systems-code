-- canvas_schema.sql
-- SQLite-compatible schema for historical storytelling media analysis.

PRAGMA foreign_keys = ON;

DROP TABLE IF EXISTS preservation_risks;
DROP TABLE IF EXISTS digital_interactive_media;
DROP TABLE IF EXISTS visual_broadcast_media;
DROP TABLE IF EXISTS manuscript_print_transitions;
DROP TABLE IF EXISTS oral_tradition_features;
DROP TABLE IF EXISTS story_media_history;

CREATE TABLE story_media_history (
    medium_id INTEGER PRIMARY KEY,
    medium TEXT NOT NULL UNIQUE,
    period_label TEXT,
    preservation REAL CHECK (preservation >= 0 AND preservation <= 1),
    participation REAL CHECK (participation >= 0 AND participation <= 1),
    circulation REAL CHECK (circulation >= 0 AND circulation <= 1),
    repeatability REAL CHECK (repeatability >= 0 AND repeatability <= 1),
    governance_complexity REAL CHECK (governance_complexity >= 0 AND governance_complexity <= 1),
    archive_durability REAL CHECK (archive_durability >= 0 AND archive_durability <= 1),
    context_retention REAL CHECK (context_retention >= 0 AND context_retention <= 1),
    access_openness REAL CHECK (access_openness >= 0 AND access_openness <= 1),
    platform_stability REAL CHECK (platform_stability >= 0 AND platform_stability <= 1),
    owner TEXT,
    status TEXT
);

CREATE TABLE oral_tradition_features (
    feature_id INTEGER PRIMARY KEY,
    feature TEXT NOT NULL,
    cultural_function TEXT,
    preservation_strength REAL,
    context_need TEXT,
    notes TEXT
);

CREATE TABLE manuscript_print_transitions (
    transition_id INTEGER PRIMARY KEY,
    transition_name TEXT,
    from_medium TEXT,
    to_medium TEXT,
    preservation_change REAL,
    circulation_change REAL,
    authority_change REAL,
    notes TEXT
);

CREATE TABLE visual_broadcast_media (
    visual_id INTEGER PRIMARY KEY,
    medium TEXT,
    visuality REAL,
    sound REAL,
    seriality REAL,
    mass_audience REAL,
    ethical_risk TEXT
);

CREATE TABLE digital_interactive_media (
    digital_id INTEGER PRIMARY KEY,
    medium TEXT,
    networking REAL,
    remix REAL,
    choice REAL,
    metrics REAL,
    algorithmic_visibility REAL,
    governance_risk TEXT
);

CREATE TABLE preservation_risks (
    risk_id INTEGER PRIMARY KEY,
    medium TEXT,
    risk_type TEXT,
    severity TEXT,
    note TEXT
);
