-- canvas_schema.sql
-- SQLite-compatible schema for conflict, tension, and narrative movement analysis.

PRAGMA foreign_keys = ON;

DROP TABLE IF EXISTS conflict_governance_notes;
DROP TABLE IF EXISTS conflict_risks;
DROP TABLE IF EXISTS movement_events;
DROP TABLE IF EXISTS tension_progressions;
DROP TABLE IF EXISTS conflict_patterns;
DROP TABLE IF EXISTS conflict_tension_items;

CREATE TABLE conflict_tension_items (
    item_id INTEGER PRIMARY KEY,
    item TEXT NOT NULL UNIQUE,
    story_type TEXT NOT NULL,
    desire_clarity REAL CHECK (desire_clarity >= 0 AND desire_clarity <= 1),
    obstacle_clarity REAL CHECK (obstacle_clarity >= 0 AND obstacle_clarity <= 1),
    pressure_strength REAL CHECK (pressure_strength >= 0 AND pressure_strength <= 1),
    agency_visibility REAL CHECK (agency_visibility >= 0 AND agency_visibility <= 1),
    stakes_visibility REAL CHECK (stakes_visibility >= 0 AND stakes_visibility <= 1),
    relation_legibility REAL CHECK (relation_legibility >= 0 AND relation_legibility <= 1),
    unresolved_pressure REAL CHECK (unresolved_pressure >= 0 AND unresolved_pressure <= 1),
    meaningful_delay REAL CHECK (meaningful_delay >= 0 AND meaningful_delay <= 1),
    stakes_heightening REAL CHECK (stakes_heightening >= 0 AND stakes_heightening <= 1),
    expectation_pressure REAL CHECK (expectation_pressure >= 0 AND expectation_pressure <= 1),
    complication_movement REAL CHECK (complication_movement >= 0 AND complication_movement <= 1),
    state_change REAL CHECK (state_change >= 0 AND state_change <= 1),
    knowledge_change REAL CHECK (knowledge_change >= 0 AND knowledge_change <= 1),
    relationship_impact REAL CHECK (relationship_impact >= 0 AND relationship_impact <= 1),
    pressure_change REAL CHECK (pressure_change >= 0 AND pressure_change <= 1),
    future_movement REAL CHECK (future_movement >= 0 AND future_movement <= 1),
    value_transformation REAL CHECK (value_transformation >= 0 AND value_transformation <= 1),
    scapegoating REAL CHECK (scapegoating >= 0 AND scapegoating <= 1),
    conflict_inflation REAL CHECK (conflict_inflation >= 0 AND conflict_inflation <= 1),
    trauma_spectacle REAL CHECK (trauma_spectacle >= 0 AND trauma_spectacle <= 1),
    false_balance REAL CHECK (false_balance >= 0 AND false_balance <= 1),
    closure_pressure REAL CHECK (closure_pressure >= 0 AND closure_pressure <= 1),
    audience_sensitivity REAL CHECK (audience_sensitivity >= 0 AND audience_sensitivity <= 1),
    public_consequence REAL CHECK (public_consequence >= 0 AND public_consequence <= 1),
    owner TEXT,
    status TEXT
);

CREATE TABLE conflict_patterns (
    pattern_id INTEGER PRIMARY KEY,
    item TEXT NOT NULL,
    conflict_type TEXT,
    pressure_relation TEXT,
    primary_stake TEXT,
    FOREIGN KEY (item) REFERENCES conflict_tension_items(item)
);

CREATE TABLE tension_progressions (
    progression_id INTEGER PRIMARY KEY,
    item TEXT NOT NULL,
    tension_pattern TEXT,
    development_note TEXT,
    risk_note TEXT,
    FOREIGN KEY (item) REFERENCES conflict_tension_items(item)
);

CREATE TABLE movement_events (
    event_id INTEGER PRIMARY KEY,
    item TEXT NOT NULL,
    movement_event TEXT,
    state_change REAL,
    knowledge_change REAL,
    relationship_impact REAL,
    pressure_change REAL,
    future_movement REAL,
    value_transformation REAL,
    note TEXT,
    FOREIGN KEY (item) REFERENCES conflict_tension_items(item)
);

CREATE TABLE conflict_risks (
    risk_id INTEGER PRIMARY KEY,
    item TEXT NOT NULL,
    risk_type TEXT,
    severity TEXT,
    note TEXT,
    FOREIGN KEY (item) REFERENCES conflict_tension_items(item)
);

CREATE TABLE conflict_governance_notes (
    note_id INTEGER PRIMARY KEY,
    item TEXT NOT NULL,
    governance_focus TEXT,
    review_owner TEXT,
    status TEXT,
    FOREIGN KEY (item) REFERENCES conflict_tension_items(item)
);
