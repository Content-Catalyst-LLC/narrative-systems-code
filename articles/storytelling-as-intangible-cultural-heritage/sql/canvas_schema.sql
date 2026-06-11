-- canvas_schema.sql
-- SQLite-compatible schema for storytelling as intangible cultural heritage.

PRAGMA foreign_keys = ON;

DROP TABLE IF EXISTS storytelling_heritage_governance_notes;
DROP TABLE IF EXISTS archive_risks;
DROP TABLE IF EXISTS consent_access_controls;
DROP TABLE IF EXISTS transmission_pathways;
DROP TABLE IF EXISTS safeguarding_contexts;
DROP TABLE IF EXISTS storytelling_heritage_items;

CREATE TABLE storytelling_heritage_items (
    item_id INTEGER PRIMARY KEY,
    item TEXT NOT NULL UNIQUE,
    heritage_context TEXT NOT NULL,
    transmission_support REAL CHECK (transmission_support >= 0 AND transmission_support <= 1),
    performance_context REAL CHECK (performance_context >= 0 AND performance_context <= 1),
    language_vitality REAL CHECK (language_vitality >= 0 AND language_vitality <= 1),
    apprenticeship_pathways REAL CHECK (apprenticeship_pathways >= 0 AND apprenticeship_pathways <= 1),
    community_recognition REAL CHECK (community_recognition >= 0 AND community_recognition <= 1),
    variation_management REAL CHECK (variation_management >= 0 AND variation_management <= 1),
    consent_clarity REAL CHECK (consent_clarity >= 0 AND consent_clarity <= 1),
    governance_protocol REAL CHECK (governance_protocol >= 0 AND governance_protocol <= 1),
    metadata_quality REAL CHECK (metadata_quality >= 0 AND metadata_quality <= 1),
    access_control REAL CHECK (access_control >= 0 AND access_control <= 1),
    benefit_sharing REAL CHECK (benefit_sharing >= 0 AND benefit_sharing <= 1),
    review_process REAL CHECK (review_process >= 0 AND review_process <= 1),
    occasion_context REAL CHECK (occasion_context >= 0 AND occasion_context <= 1),
    place_linkage REAL CHECK (place_linkage >= 0 AND place_linkage <= 1),
    ritual_frame REAL CHECK (ritual_frame >= 0 AND ritual_frame <= 1),
    embodiment REAL CHECK (embodiment >= 0 AND embodiment <= 1),
    social_transmission REAL CHECK (social_transmission >= 0 AND social_transmission <= 1),
    knowledge_holder_context REAL CHECK (knowledge_holder_context >= 0 AND knowledge_holder_context <= 1),
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

CREATE TABLE safeguarding_contexts (
    context_id INTEGER PRIMARY KEY,
    item TEXT NOT NULL,
    safeguarding_context TEXT,
    primary_need TEXT,
    review_note TEXT,
    FOREIGN KEY (item) REFERENCES storytelling_heritage_items(item)
);

CREATE TABLE transmission_pathways (
    pathway_id INTEGER PRIMARY KEY,
    item TEXT NOT NULL,
    transmission_pathway TEXT,
    language_status TEXT,
    apprenticeship_note TEXT,
    FOREIGN KEY (item) REFERENCES storytelling_heritage_items(item)
);

CREATE TABLE consent_access_controls (
    consent_id INTEGER PRIMARY KEY,
    item TEXT NOT NULL,
    consent_layer TEXT,
    access_level TEXT,
    control_note TEXT,
    FOREIGN KEY (item) REFERENCES storytelling_heritage_items(item)
);

CREATE TABLE archive_risks (
    risk_id INTEGER PRIMARY KEY,
    item TEXT NOT NULL,
    risk_type TEXT,
    severity TEXT,
    note TEXT,
    FOREIGN KEY (item) REFERENCES storytelling_heritage_items(item)
);

CREATE TABLE storytelling_heritage_governance_notes (
    note_id INTEGER PRIMARY KEY,
    item TEXT NOT NULL,
    governance_focus TEXT,
    review_owner TEXT,
    status TEXT,
    FOREIGN KEY (item) REFERENCES storytelling_heritage_items(item)
);
