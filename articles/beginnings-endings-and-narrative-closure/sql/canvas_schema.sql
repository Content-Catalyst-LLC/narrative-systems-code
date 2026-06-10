-- canvas_schema.sql
-- SQLite-compatible schema for beginnings, endings, and narrative closure analysis.

PRAGMA foreign_keys = ON;

DROP TABLE IF EXISTS closure_governance_notes;
DROP TABLE IF EXISTS unresolved_consequences;
DROP TABLE IF EXISTS closure_risks;
DROP TABLE IF EXISTS ending_patterns;
DROP TABLE IF EXISTS opening_promises;
DROP TABLE IF EXISTS beginning_closure_items;

CREATE TABLE beginning_closure_items (
    item_id INTEGER PRIMARY KEY,
    item TEXT NOT NULL UNIQUE,
    story_type TEXT NOT NULL,
    voice_signal REAL CHECK (voice_signal >= 0 AND voice_signal <= 1),
    world_orientation REAL CHECK (world_orientation >= 0 AND world_orientation <= 1),
    pressure_introduction REAL CHECK (pressure_introduction >= 0 AND pressure_introduction <= 1),
    stakes_visibility REAL CHECK (stakes_visibility >= 0 AND stakes_visibility <= 1),
    question_framing REAL CHECK (question_framing >= 0 AND question_framing <= 1),
    contract_transparency REAL CHECK (contract_transparency >= 0 AND contract_transparency <= 1),
    promise_fulfillment REAL CHECK (promise_fulfillment >= 0 AND promise_fulfillment <= 1),
    resolution_suitability REAL CHECK (resolution_suitability >= 0 AND resolution_suitability <= 1),
    transformation_depth REAL CHECK (transformation_depth >= 0 AND transformation_depth <= 1),
    aftermath_clarity REAL CHECK (aftermath_clarity >= 0 AND aftermath_clarity <= 1),
    emotional_honesty REAL CHECK (emotional_honesty >= 0 AND emotional_honesty <= 1),
    unresolved_harm_honesty REAL CHECK (unresolved_harm_honesty >= 0 AND unresolved_harm_honesty <= 1),
    motif_return REAL CHECK (motif_return >= 0 AND motif_return <= 1),
    question_answer REAL CHECK (question_answer >= 0 AND question_answer <= 1),
    interpretive_echo REAL CHECK (interpretive_echo >= 0 AND interpretive_echo <= 1),
    thematic_continuity REAL CHECK (thematic_continuity >= 0 AND thematic_continuity <= 1),
    frame_revision REAL CHECK (frame_revision >= 0 AND frame_revision <= 1),
    premature_repair REAL CHECK (premature_repair >= 0 AND premature_repair <= 1),
    false_resolution REAL CHECK (false_resolution >= 0 AND false_resolution <= 1),
    system_flattening REAL CHECK (system_flattening >= 0 AND system_flattening <= 1),
    aftermath_omission REAL CHECK (aftermath_omission >= 0 AND aftermath_omission <= 1),
    excessive_audience_comfort REAL CHECK (excessive_audience_comfort >= 0 AND excessive_audience_comfort <= 1),
    audience_sensitivity REAL CHECK (audience_sensitivity >= 0 AND audience_sensitivity <= 1),
    public_consequence REAL CHECK (public_consequence >= 0 AND public_consequence <= 1),
    owner TEXT,
    status TEXT
);

CREATE TABLE opening_promises (
    promise_id INTEGER PRIMARY KEY,
    item TEXT NOT NULL,
    opening_type TEXT,
    opening_promise TEXT,
    orientation_note TEXT,
    risk_note TEXT,
    FOREIGN KEY (item) REFERENCES beginning_closure_items(item)
);

CREATE TABLE ending_patterns (
    ending_id INTEGER PRIMARY KEY,
    item TEXT NOT NULL,
    ending_type TEXT,
    closure_form TEXT,
    alignment_note TEXT,
    FOREIGN KEY (item) REFERENCES beginning_closure_items(item)
);

CREATE TABLE closure_risks (
    risk_id INTEGER PRIMARY KEY,
    item TEXT NOT NULL,
    risk_type TEXT,
    severity TEXT,
    note TEXT,
    FOREIGN KEY (item) REFERENCES beginning_closure_items(item)
);

CREATE TABLE unresolved_consequences (
    consequence_id INTEGER PRIMARY KEY,
    item TEXT NOT NULL,
    unresolved_consequence TEXT,
    afterward_note TEXT,
    governance_need TEXT,
    FOREIGN KEY (item) REFERENCES beginning_closure_items(item)
);

CREATE TABLE closure_governance_notes (
    note_id INTEGER PRIMARY KEY,
    item TEXT NOT NULL,
    governance_focus TEXT,
    review_owner TEXT,
    status TEXT,
    FOREIGN KEY (item) REFERENCES beginning_closure_items(item)
);
