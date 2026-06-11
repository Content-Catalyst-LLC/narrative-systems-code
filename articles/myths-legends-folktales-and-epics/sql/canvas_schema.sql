-- canvas_schema.sql
-- SQLite-compatible schema for myths, legends, folktales, and epics analysis.

PRAGMA foreign_keys = ON;

DROP TABLE IF EXISTS traditional_narrative_governance_notes;
DROP TABLE IF EXISTS adaptation_risks;
DROP TABLE IF EXISTS memory_functions;
DROP TABLE IF EXISTS truth_claims;
DROP TABLE IF EXISTS form_distinctions;
DROP TABLE IF EXISTS traditional_narrative_forms_items;

CREATE TABLE traditional_narrative_forms_items (
    item_id INTEGER PRIMARY KEY,
    item TEXT NOT NULL UNIQUE,
    proposed_form TEXT NOT NULL,
    truth_claim_clarity REAL CHECK (truth_claim_clarity >= 0 AND truth_claim_clarity <= 1),
    social_function REAL CHECK (social_function >= 0 AND social_function <= 1),
    memory_orientation REAL CHECK (memory_orientation >= 0 AND memory_orientation <= 1),
    performance_trace REAL CHECK (performance_trace >= 0 AND performance_trace <= 1),
    authority_context REAL CHECK (authority_context >= 0 AND authority_context <= 1),
    genre_notes REAL CHECK (genre_notes >= 0 AND genre_notes <= 1),
    boundary_clarity REAL CHECK (boundary_clarity >= 0 AND boundary_clarity <= 1),
    category_specificity REAL CHECK (category_specificity >= 0 AND category_specificity <= 1),
    hybrid_tracking REAL CHECK (hybrid_tracking >= 0 AND hybrid_tracking <= 1),
    responsible_analogy REAL CHECK (responsible_analogy >= 0 AND responsible_analogy <= 1),
    variation_management REAL CHECK (variation_management >= 0 AND variation_management <= 1),
    origin_memory REAL CHECK (origin_memory >= 0 AND origin_memory <= 1),
    place_memory REAL CHECK (place_memory >= 0 AND place_memory <= 1),
    ritual_memory REAL CHECK (ritual_memory >= 0 AND ritual_memory <= 1),
    heroic_memory REAL CHECK (heroic_memory >= 0 AND heroic_memory <= 1),
    identity_memory REAL CHECK (identity_memory >= 0 AND identity_memory <= 1),
    future_obligation REAL CHECK (future_obligation >= 0 AND future_obligation <= 1),
    context_removal REAL CHECK (context_removal >= 0 AND context_removal <= 1),
    sacred_or_restricted_material REAL CHECK (sacred_or_restricted_material >= 0 AND sacred_or_restricted_material <= 1),
    performance_omission REAL CHECK (performance_omission >= 0 AND performance_omission <= 1),
    translation_loss REAL CHECK (translation_loss >= 0 AND translation_loss <= 1),
    extraction_risk REAL CHECK (extraction_risk >= 0 AND extraction_risk <= 1),
    governance_control REAL CHECK (governance_control >= 0 AND governance_control <= 1),
    community_sensitivity REAL CHECK (community_sensitivity >= 0 AND community_sensitivity <= 1),
    public_consequence REAL CHECK (public_consequence >= 0 AND public_consequence <= 1),
    owner TEXT,
    status TEXT
);

CREATE TABLE form_distinctions (
    form_id INTEGER PRIMARY KEY,
    form TEXT NOT NULL UNIQUE,
    primary_orientation TEXT,
    typical_time TEXT,
    typical_authority TEXT,
    typical_movement TEXT
);

CREATE TABLE truth_claims (
    truth_claim_id INTEGER PRIMARY KEY,
    item TEXT NOT NULL,
    truth_claim_type TEXT,
    belief_context TEXT,
    interpretive_note TEXT,
    FOREIGN KEY (item) REFERENCES traditional_narrative_forms_items(item)
);

CREATE TABLE memory_functions (
    memory_id INTEGER PRIMARY KEY,
    item TEXT NOT NULL,
    primary_memory_function TEXT,
    secondary_memory_function TEXT,
    continuity_note TEXT,
    FOREIGN KEY (item) REFERENCES traditional_narrative_forms_items(item)
);

CREATE TABLE adaptation_risks (
    risk_id INTEGER PRIMARY KEY,
    item TEXT NOT NULL,
    risk_type TEXT,
    severity TEXT,
    note TEXT,
    FOREIGN KEY (item) REFERENCES traditional_narrative_forms_items(item)
);

CREATE TABLE traditional_narrative_governance_notes (
    note_id INTEGER PRIMARY KEY,
    item TEXT NOT NULL,
    governance_focus TEXT,
    review_owner TEXT,
    status TEXT,
    FOREIGN KEY (item) REFERENCES traditional_narrative_forms_items(item)
);
