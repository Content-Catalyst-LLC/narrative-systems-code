-- canvas_schema.sql
-- SQLite-compatible schema for narrative understanding analysis.

PRAGMA foreign_keys = ON;

DROP TABLE IF EXISTS overreach_risks;
DROP TABLE IF EXISTS moral_understanding;
DROP TABLE IF EXISTS agency_maps;
DROP TABLE IF EXISTS causal_frames;
DROP TABLE IF EXISTS event_sequences;
DROP TABLE IF EXISTS narrative_understanding_items;

CREATE TABLE narrative_understanding_items (
    item_id INTEGER PRIMARY KEY,
    item TEXT NOT NULL UNIQUE,
    story_type TEXT NOT NULL,
    sequence_clarity REAL CHECK (sequence_clarity >= 0 AND sequence_clarity <= 1),
    causal_framing REAL CHECK (causal_framing >= 0 AND causal_framing <= 1),
    agency_mapping REAL CHECK (agency_mapping >= 0 AND agency_mapping <= 1),
    memory_integration REAL CHECK (memory_integration >= 0 AND memory_integration <= 1),
    evidence_support REAL CHECK (evidence_support >= 0 AND evidence_support <= 1),
    openness_to_revision REAL CHECK (openness_to_revision >= 0 AND openness_to_revision <= 1),
    consequence_visibility REAL CHECK (consequence_visibility >= 0 AND consequence_visibility <= 1),
    harm_recognition REAL CHECK (harm_recognition >= 0 AND harm_recognition <= 1),
    responsibility_mapping REAL CHECK (responsibility_mapping >= 0 AND responsibility_mapping <= 1),
    repair_awareness REAL CHECK (repair_awareness >= 0 AND repair_awareness <= 1),
    alternative_logic REAL CHECK (alternative_logic >= 0 AND alternative_logic <= 1),
    uncertainty_signaling REAL CHECK (uncertainty_signaling >= 0 AND uncertainty_signaling <= 1),
    interpretive_diversity REAL CHECK (interpretive_diversity >= 0 AND interpretive_diversity <= 1),
    hindsight_bias REAL CHECK (hindsight_bias >= 0 AND hindsight_bias <= 1),
    false_coherence REAL CHECK (false_coherence >= 0 AND false_coherence <= 1),
    selection_bias REAL CHECK (selection_bias >= 0 AND selection_bias <= 1),
    closure_pressure REAL CHECK (closure_pressure >= 0 AND closure_pressure <= 1),
    owner TEXT,
    status TEXT
);

CREATE TABLE event_sequences (
    sequence_id INTEGER PRIMARY KEY,
    item TEXT NOT NULL,
    event_order INTEGER,
    event_label TEXT,
    event_role TEXT,
    sequence_caution TEXT,
    FOREIGN KEY (item) REFERENCES narrative_understanding_items(item)
);

CREATE TABLE causal_frames (
    causal_id INTEGER PRIMARY KEY,
    item TEXT NOT NULL,
    causal_claim TEXT,
    evidence_strength TEXT,
    causal_risk TEXT,
    FOREIGN KEY (item) REFERENCES narrative_understanding_items(item)
);

CREATE TABLE agency_maps (
    agency_id INTEGER PRIMARY KEY,
    item TEXT NOT NULL,
    actor TEXT,
    agency_role TEXT,
    constraint_note TEXT,
    omission_risk TEXT,
    FOREIGN KEY (item) REFERENCES narrative_understanding_items(item)
);

CREATE TABLE moral_understanding (
    moral_id INTEGER PRIMARY KEY,
    item TEXT NOT NULL,
    harm_visible TEXT,
    responsibility_clear TEXT,
    repair_named TEXT,
    moral_caution TEXT,
    FOREIGN KEY (item) REFERENCES narrative_understanding_items(item)
);

CREATE TABLE overreach_risks (
    risk_id INTEGER PRIMARY KEY,
    item TEXT NOT NULL,
    risk_type TEXT,
    severity TEXT,
    note TEXT,
    FOREIGN KEY (item) REFERENCES narrative_understanding_items(item)
);
