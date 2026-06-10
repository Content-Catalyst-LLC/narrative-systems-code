-- canvas_schema.sql
-- SQLite-compatible schema for reversal, recognition, and transformation analysis.

PRAGMA foreign_keys = ON;

DROP TABLE IF EXISTS recognition_governance_notes;
DROP TABLE IF EXISTS recognition_risks;
DROP TABLE IF EXISTS transformation_paths;
DROP TABLE IF EXISTS recognition_events;
DROP TABLE IF EXISTS reversal_patterns;
DROP TABLE IF EXISTS reversal_recognition_items;

CREATE TABLE reversal_recognition_items (
    item_id INTEGER PRIMARY KEY,
    item TEXT NOT NULL UNIQUE,
    story_type TEXT NOT NULL,
    preparation_trace REAL CHECK (preparation_trace >= 0 AND preparation_trace <= 1),
    causal_linkage REAL CHECK (causal_linkage >= 0 AND causal_linkage <= 1),
    state_change REAL CHECK (state_change >= 0 AND state_change <= 1),
    earned_surprise REAL CHECK (earned_surprise >= 0 AND earned_surprise <= 1),
    action_fit REAL CHECK (action_fit >= 0 AND action_fit <= 1),
    knowledge_reorientation REAL CHECK (knowledge_reorientation >= 0 AND knowledge_reorientation <= 1),
    evidence_visibility REAL CHECK (evidence_visibility >= 0 AND evidence_visibility <= 1),
    interpretive_support REAL CHECK (interpretive_support >= 0 AND interpretive_support <= 1),
    meaning_revision REAL CHECK (meaning_revision >= 0 AND meaning_revision <= 1),
    relation_linkage REAL CHECK (relation_linkage >= 0 AND relation_linkage <= 1),
    uncertainty_clarity REAL CHECK (uncertainty_clarity >= 0 AND uncertainty_clarity <= 1),
    identity_change REAL CHECK (identity_change >= 0 AND identity_change <= 1),
    action_consequence REAL CHECK (action_consequence >= 0 AND action_consequence <= 1),
    relationship_change REAL CHECK (relationship_change >= 0 AND relationship_change <= 1),
    value_change REAL CHECK (value_change >= 0 AND value_change <= 1),
    future_possibility REAL CHECK (future_possibility >= 0 AND future_possibility <= 1),
    governance_accountability REAL CHECK (governance_accountability >= 0 AND governance_accountability <= 1),
    false_recognition REAL CHECK (false_recognition >= 0 AND false_recognition <= 1),
    arbitrary_twist REAL CHECK (arbitrary_twist >= 0 AND arbitrary_twist <= 1),
    closure_pressure REAL CHECK (closure_pressure >= 0 AND closure_pressure <= 1),
    evidence_omission REAL CHECK (evidence_omission >= 0 AND evidence_omission <= 1),
    audience_sensitivity REAL CHECK (audience_sensitivity >= 0 AND audience_sensitivity <= 1),
    public_consequence REAL CHECK (public_consequence >= 0 AND public_consequence <= 1),
    owner TEXT,
    status TEXT
);

CREATE TABLE reversal_patterns (
    pattern_id INTEGER PRIMARY KEY,
    item TEXT NOT NULL,
    reversal_type TEXT,
    what_turns TEXT,
    preparation_note TEXT,
    FOREIGN KEY (item) REFERENCES reversal_recognition_items(item)
);

CREATE TABLE recognition_events (
    recognition_id INTEGER PRIMARY KEY,
    item TEXT NOT NULL,
    recognition_event TEXT,
    recognition_object TEXT,
    evidence_type TEXT,
    uncertainty_note TEXT,
    FOREIGN KEY (item) REFERENCES reversal_recognition_items(item)
);

CREATE TABLE transformation_paths (
    transformation_id INTEGER PRIMARY KEY,
    item TEXT NOT NULL,
    transformation_level TEXT,
    changed_condition TEXT,
    accountability_note TEXT,
    FOREIGN KEY (item) REFERENCES reversal_recognition_items(item)
);

CREATE TABLE recognition_risks (
    risk_id INTEGER PRIMARY KEY,
    item TEXT NOT NULL,
    risk_type TEXT,
    severity TEXT,
    note TEXT,
    FOREIGN KEY (item) REFERENCES reversal_recognition_items(item)
);

CREATE TABLE recognition_governance_notes (
    note_id INTEGER PRIMARY KEY,
    item TEXT NOT NULL,
    governance_focus TEXT,
    review_owner TEXT,
    status TEXT,
    FOREIGN KEY (item) REFERENCES reversal_recognition_items(item)
);
