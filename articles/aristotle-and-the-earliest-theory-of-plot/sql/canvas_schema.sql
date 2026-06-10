-- canvas_schema.sql
-- SQLite-compatible schema for Aristotelian plot analysis.

PRAGMA foreign_keys = ON;

DROP TABLE IF EXISTS plot_governance_notes;
DROP TABLE IF EXISTS formula_risks;
DROP TABLE IF EXISTS reversal_recognition_map;
DROP TABLE IF EXISTS unity_action_checks;
DROP TABLE IF EXISTS plot_parts;
DROP TABLE IF EXISTS aristotelian_plot_items;

CREATE TABLE aristotelian_plot_items (
    item_id INTEGER PRIMARY KEY,
    item TEXT NOT NULL UNIQUE,
    story_type TEXT NOT NULL,
    action_clarity REAL CHECK (action_clarity >= 0 AND action_clarity <= 1),
    causal_linkage REAL CHECK (causal_linkage >= 0 AND causal_linkage <= 1),
    episode_dependency REAL CHECK (episode_dependency >= 0 AND episode_dependency <= 1),
    turning_point_relevance REAL CHECK (turning_point_relevance >= 0 AND turning_point_relevance <= 1),
    resolution_support REAL CHECK (resolution_support >= 0 AND resolution_support <= 1),
    goal_coherence REAL CHECK (goal_coherence >= 0 AND goal_coherence <= 1),
    direction_change REAL CHECK (direction_change >= 0 AND direction_change <= 1),
    knowledge_change REAL CHECK (knowledge_change >= 0 AND knowledge_change <= 1),
    preparation_strength REAL CHECK (preparation_strength >= 0 AND preparation_strength <= 1),
    consequence_pressure REAL CHECK (consequence_pressure >= 0 AND consequence_pressure <= 1),
    emotional_intellectual_impact REAL CHECK (emotional_intellectual_impact >= 0 AND emotional_intellectual_impact <= 1),
    character_action_integration REAL CHECK (character_action_integration >= 0 AND character_action_integration <= 1),
    genre_fit REAL CHECK (genre_fit >= 0 AND genre_fit <= 1),
    medium_fit REAL CHECK (medium_fit >= 0 AND medium_fit <= 1),
    cultural_awareness REAL CHECK (cultural_awareness >= 0 AND cultural_awareness <= 1),
    hero_template_saturation REAL CHECK (hero_template_saturation >= 0 AND hero_template_saturation <= 1),
    closure_pressure REAL CHECK (closure_pressure >= 0 AND closure_pressure <= 1),
    unity_bias REAL CHECK (unity_bias >= 0 AND unity_bias <= 1),
    genre_bias REAL CHECK (genre_bias >= 0 AND genre_bias <= 1),
    owner TEXT,
    status TEXT
);

CREATE TABLE plot_parts (
    part_id INTEGER PRIMARY KEY,
    item TEXT NOT NULL,
    plot_part TEXT,
    structural_role TEXT,
    diagnostic_question TEXT,
    FOREIGN KEY (item) REFERENCES aristotelian_plot_items(item)
);

CREATE TABLE unity_action_checks (
    check_id INTEGER PRIMARY KEY,
    item TEXT NOT NULL,
    unity_question TEXT,
    result TEXT,
    caution TEXT,
    FOREIGN KEY (item) REFERENCES aristotelian_plot_items(item)
);

CREATE TABLE reversal_recognition_map (
    map_id INTEGER PRIMARY KEY,
    item TEXT NOT NULL,
    reversal_type TEXT,
    recognition_type TEXT,
    preparation_strength TEXT,
    consequence_note TEXT,
    FOREIGN KEY (item) REFERENCES aristotelian_plot_items(item)
);

CREATE TABLE formula_risks (
    risk_id INTEGER PRIMARY KEY,
    item TEXT NOT NULL,
    risk_type TEXT,
    severity TEXT,
    note TEXT,
    FOREIGN KEY (item) REFERENCES aristotelian_plot_items(item)
);

CREATE TABLE plot_governance_notes (
    note_id INTEGER PRIMARY KEY,
    item TEXT NOT NULL,
    governance_focus TEXT,
    review_owner TEXT,
    status TEXT,
    FOREIGN KEY (item) REFERENCES aristotelian_plot_items(item)
);
