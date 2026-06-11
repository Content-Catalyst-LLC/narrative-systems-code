-- canvas_schema.sql
-- SQLite-compatible schema for performance, memory, and variation in oral storytelling.

PRAGMA foreign_keys = ON;

DROP TABLE IF EXISTS oral_storytelling_governance_notes;
DROP TABLE IF EXISTS archive_risks;
DROP TABLE IF EXISTS variation_patterns;
DROP TABLE IF EXISTS memory_supports;
DROP TABLE IF EXISTS performance_contexts;
DROP TABLE IF EXISTS oral_storytelling_variation_items;

CREATE TABLE oral_storytelling_variation_items (
    item_id INTEGER PRIMARY KEY,
    item TEXT NOT NULL UNIQUE,
    storytelling_context TEXT NOT NULL,
    teller_role REAL CHECK (teller_role >= 0 AND teller_role <= 1),
    audience_documentation REAL CHECK (audience_documentation >= 0 AND audience_documentation <= 1),
    occasion_context REAL CHECK (occasion_context >= 0 AND occasion_context <= 1),
    place_linkage REAL CHECK (place_linkage >= 0 AND place_linkage <= 1),
    embodiment REAL CHECK (embodiment >= 0 AND embodiment <= 1),
    interaction_notes REAL CHECK (interaction_notes >= 0 AND interaction_notes <= 1),
    repetition REAL CHECK (repetition >= 0 AND repetition <= 1),
    formula_use REAL CHECK (formula_use >= 0 AND formula_use <= 1),
    sequence_clarity REAL CHECK (sequence_clarity >= 0 AND sequence_clarity <= 1),
    audience_recognition REAL CHECK (audience_recognition >= 0 AND audience_recognition <= 1),
    community_correction REAL CHECK (community_correction >= 0 AND community_correction <= 1),
    transmission_pathway REAL CHECK (transmission_pathway >= 0 AND transmission_pathway <= 1),
    variation_tracking REAL CHECK (variation_tracking >= 0 AND variation_tracking <= 1),
    context_explanation REAL CHECK (context_explanation >= 0 AND context_explanation <= 1),
    language_notes REAL CHECK (language_notes >= 0 AND language_notes <= 1),
    source_review REAL CHECK (source_review >= 0 AND source_review <= 1),
    access_protocol REAL CHECK (access_protocol >= 0 AND access_protocol <= 1),
    governance_oversight REAL CHECK (governance_oversight >= 0 AND governance_oversight <= 1),
    fixation_risk REAL CHECK (fixation_risk >= 0 AND fixation_risk <= 1),
    context_removal REAL CHECK (context_removal >= 0 AND context_removal <= 1),
    performance_omission REAL CHECK (performance_omission >= 0 AND performance_omission <= 1),
    translation_loss REAL CHECK (translation_loss >= 0 AND translation_loss <= 1),
    extraction_risk REAL CHECK (extraction_risk >= 0 AND extraction_risk <= 1),
    governance_control REAL CHECK (governance_control >= 0 AND governance_control <= 1),
    community_sensitivity REAL CHECK (community_sensitivity >= 0 AND community_sensitivity <= 1),
    public_consequence REAL CHECK (public_consequence >= 0 AND public_consequence <= 1),
    owner TEXT,
    status TEXT
);

CREATE TABLE performance_contexts (
    context_id INTEGER PRIMARY KEY,
    item TEXT NOT NULL,
    performance_setting TEXT,
    audience_type TEXT,
    documentation_note TEXT,
    FOREIGN KEY (item) REFERENCES oral_storytelling_variation_items(item)
);

CREATE TABLE memory_supports (
    memory_id INTEGER PRIMARY KEY,
    item TEXT NOT NULL,
    memory_support_type TEXT,
    formula_or_repetition TEXT,
    transmission_note TEXT,
    FOREIGN KEY (item) REFERENCES oral_storytelling_variation_items(item)
);

CREATE TABLE variation_patterns (
    variation_id INTEGER PRIMARY KEY,
    item TEXT NOT NULL,
    variation_type TEXT,
    interpretive_note TEXT,
    FOREIGN KEY (item) REFERENCES oral_storytelling_variation_items(item)
);

CREATE TABLE archive_risks (
    risk_id INTEGER PRIMARY KEY,
    item TEXT NOT NULL,
    risk_type TEXT,
    severity TEXT,
    note TEXT,
    FOREIGN KEY (item) REFERENCES oral_storytelling_variation_items(item)
);

CREATE TABLE oral_storytelling_governance_notes (
    note_id INTEGER PRIMARY KEY,
    item TEXT NOT NULL,
    governance_focus TEXT,
    review_owner TEXT,
    status TEXT,
    FOREIGN KEY (item) REFERENCES oral_storytelling_variation_items(item)
);
