-- canvas_schema.sql
-- SQLite-compatible schema for folktale structure and Proppian morphology analysis.

PRAGMA foreign_keys = ON;

DROP TABLE IF EXISTS folktale_governance_notes;
DROP TABLE IF EXISTS morphology_risks;
DROP TABLE IF EXISTS tale_variants;
DROP TABLE IF EXISTS spheres_of_action;
DROP TABLE IF EXISTS propp_function_map;
DROP TABLE IF EXISTS folktale_morphology_items;

CREATE TABLE folktale_morphology_items (
    item_id INTEGER PRIMARY KEY,
    item TEXT NOT NULL UNIQUE,
    tale_type TEXT NOT NULL,
    function_identification REAL CHECK (function_identification >= 0 AND function_identification <= 1),
    sequence_clarity REAL CHECK (sequence_clarity >= 0 AND sequence_clarity <= 1),
    role_mapping REAL CHECK (role_mapping >= 0 AND role_mapping <= 1),
    variation_tracking REAL CHECK (variation_tracking >= 0 AND variation_tracking <= 1),
    context_notes REAL CHECK (context_notes >= 0 AND context_notes <= 1),
    order_coherence REAL CHECK (order_coherence >= 0 AND order_coherence <= 1),
    transition_logic REAL CHECK (transition_logic >= 0 AND transition_logic <= 1),
    gap_management REAL CHECK (gap_management >= 0 AND gap_management <= 1),
    repetition_awareness REAL CHECK (repetition_awareness >= 0 AND repetition_awareness <= 1),
    closure_handling REAL CHECK (closure_handling >= 0 AND closure_handling <= 1),
    performance_context REAL CHECK (performance_context >= 0 AND performance_context <= 1),
    cultural_specificity REAL CHECK (cultural_specificity >= 0 AND cultural_specificity <= 1),
    language_notes REAL CHECK (language_notes >= 0 AND language_notes <= 1),
    tradition_review REAL CHECK (tradition_review >= 0 AND tradition_review <= 1),
    ethical_governance REAL CHECK (ethical_governance >= 0 AND ethical_governance <= 1),
    universalization_risk REAL CHECK (universalization_risk >= 0 AND universalization_risk <= 1),
    cultural_erasure_risk REAL CHECK (cultural_erasure_risk >= 0 AND cultural_erasure_risk <= 1),
    performance_omission REAL CHECK (performance_omission >= 0 AND performance_omission <= 1),
    variation_omission REAL CHECK (variation_omission >= 0 AND variation_omission <= 1),
    archive_bias REAL CHECK (archive_bias >= 0 AND archive_bias <= 1),
    community_sensitivity REAL CHECK (community_sensitivity >= 0 AND community_sensitivity <= 1),
    public_consequence REAL CHECK (public_consequence >= 0 AND public_consequence <= 1),
    owner TEXT,
    status TEXT
);

CREATE TABLE propp_function_map (
    function_id INTEGER PRIMARY KEY,
    item TEXT NOT NULL,
    function_family TEXT,
    propp_functions_present TEXT,
    sequence_note TEXT,
    FOREIGN KEY (item) REFERENCES folktale_morphology_items(item)
);

CREATE TABLE spheres_of_action (
    sphere_id INTEGER PRIMARY KEY,
    item TEXT NOT NULL,
    villain TEXT,
    donor TEXT,
    helper TEXT,
    dispatcher TEXT,
    hero TEXT,
    false_hero TEXT,
    sought_for_person_or_value TEXT,
    FOREIGN KEY (item) REFERENCES folktale_morphology_items(item)
);

CREATE TABLE tale_variants (
    variant_id INTEGER PRIMARY KEY,
    item TEXT NOT NULL,
    variant_status TEXT,
    variation_pattern TEXT,
    context_note TEXT,
    FOREIGN KEY (item) REFERENCES folktale_morphology_items(item)
);

CREATE TABLE morphology_risks (
    risk_id INTEGER PRIMARY KEY,
    item TEXT NOT NULL,
    risk_type TEXT,
    severity TEXT,
    note TEXT,
    FOREIGN KEY (item) REFERENCES folktale_morphology_items(item)
);

CREATE TABLE folktale_governance_notes (
    note_id INTEGER PRIMARY KEY,
    item TEXT NOT NULL,
    governance_focus TEXT,
    review_owner TEXT,
    status TEXT,
    FOREIGN KEY (item) REFERENCES folktale_morphology_items(item)
);
