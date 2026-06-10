-- canvas_schema.sql
-- SQLite-compatible schema for plot coherence analysis.

PRAGMA foreign_keys = ON;

DROP TABLE IF EXISTS plot_governance_notes;
DROP TABLE IF EXISTS coherence_risks;
DROP TABLE IF EXISTS causal_links;
DROP TABLE IF EXISTS action_dependencies;
DROP TABLE IF EXISTS plot_events;
DROP TABLE IF EXISTS plot_coherence_items;

CREATE TABLE plot_coherence_items (
    item_id INTEGER PRIMARY KEY,
    item TEXT NOT NULL UNIQUE,
    story_type TEXT NOT NULL,
    action_clarity REAL CHECK (action_clarity >= 0 AND action_clarity <= 1),
    causal_linkage REAL CHECK (causal_linkage >= 0 AND causal_linkage <= 1),
    motivation_visibility REAL CHECK (motivation_visibility >= 0 AND motivation_visibility <= 1),
    episode_dependency REAL CHECK (episode_dependency >= 0 AND episode_dependency <= 1),
    turning_point_strength REAL CHECK (turning_point_strength >= 0 AND turning_point_strength <= 1),
    resolution_consequence REAL CHECK (resolution_consequence >= 0 AND resolution_consequence <= 1),
    state_change REAL CHECK (state_change >= 0 AND state_change <= 1),
    knowledge_change REAL CHECK (knowledge_change >= 0 AND knowledge_change <= 1),
    pressure_change REAL CHECK (pressure_change >= 0 AND pressure_change <= 1),
    relationship_impact REAL CHECK (relationship_impact >= 0 AND relationship_impact <= 1),
    future_movement REAL CHECK (future_movement >= 0 AND future_movement <= 1),
    false_causality REAL CHECK (false_causality >= 0 AND false_causality <= 1),
    simplification_bias REAL CHECK (simplification_bias >= 0 AND simplification_bias <= 1),
    closure_pressure REAL CHECK (closure_pressure >= 0 AND closure_pressure <= 1),
    evidence_omission REAL CHECK (evidence_omission >= 0 AND evidence_omission <= 1),
    uncertainty_clarity REAL CHECK (uncertainty_clarity >= 0 AND uncertainty_clarity <= 1),
    audience_sensitivity REAL CHECK (audience_sensitivity >= 0 AND audience_sensitivity <= 1),
    public_consequence REAL CHECK (public_consequence >= 0 AND public_consequence <= 1),
    owner TEXT,
    status TEXT
);

CREATE TABLE plot_events (
    event_id INTEGER PRIMARY KEY,
    item TEXT NOT NULL,
    event TEXT,
    sequence_position INTEGER,
    structural_role TEXT,
    FOREIGN KEY (item) REFERENCES plot_coherence_items(item)
);

CREATE TABLE action_dependencies (
    dependency_id INTEGER PRIMARY KEY,
    item TEXT NOT NULL,
    scene_or_event TEXT,
    state_change REAL,
    knowledge_change REAL,
    pressure_change REAL,
    relationship_impact REAL,
    future_movement REAL,
    note TEXT,
    FOREIGN KEY (item) REFERENCES plot_coherence_items(item)
);

CREATE TABLE causal_links (
    link_id INTEGER PRIMARY KEY,
    item TEXT NOT NULL,
    source_event TEXT,
    target_event TEXT,
    causal_type TEXT,
    confidence REAL,
    caution TEXT,
    FOREIGN KEY (item) REFERENCES plot_coherence_items(item)
);

CREATE TABLE coherence_risks (
    risk_id INTEGER PRIMARY KEY,
    item TEXT NOT NULL,
    risk_type TEXT,
    severity TEXT,
    note TEXT,
    FOREIGN KEY (item) REFERENCES plot_coherence_items(item)
);

CREATE TABLE plot_governance_notes (
    note_id INTEGER PRIMARY KEY,
    item TEXT NOT NULL,
    governance_focus TEXT,
    review_owner TEXT,
    status TEXT,
    FOREIGN KEY (item) REFERENCES plot_coherence_items(item)
);
