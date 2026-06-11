-- canvas_schema.sql
-- SQLite-compatible schema for proverb, song, chant, and ritual speech analysis.

PRAGMA foreign_keys = ON;

DROP TABLE IF EXISTS compact_oral_forms_governance_notes;
DROP TABLE IF EXISTS archive_risks;
DROP TABLE IF EXISTS ritual_authority_notes;
DROP TABLE IF EXISTS sound_repetition_features;
DROP TABLE IF EXISTS oral_form_contexts;
DROP TABLE IF EXISTS compact_oral_forms_items;

CREATE TABLE compact_oral_forms_items (
    item_id INTEGER PRIMARY KEY,
    item TEXT NOT NULL UNIQUE,
    oral_form TEXT NOT NULL,
    form_identification REAL CHECK (form_identification >= 0 AND form_identification <= 1),
    speaker_role REAL CHECK (speaker_role >= 0 AND speaker_role <= 1),
    audience_documentation REAL CHECK (audience_documentation >= 0 AND audience_documentation <= 1),
    occasion_notes REAL CHECK (occasion_notes >= 0 AND occasion_notes <= 1),
    place_linkage REAL CHECK (place_linkage >= 0 AND place_linkage <= 1),
    use_context REAL CHECK (use_context >= 0 AND use_context <= 1),
    rhythm REAL CHECK (rhythm >= 0 AND rhythm <= 1),
    melody REAL CHECK (melody >= 0 AND melody <= 1),
    cadence REAL CHECK (cadence >= 0 AND cadence <= 1),
    refrain_or_formula REAL CHECK (refrain_or_formula >= 0 AND refrain_or_formula <= 1),
    participation REAL CHECK (participation >= 0 AND participation <= 1),
    embodiment REAL CHECK (embodiment >= 0 AND embodiment <= 1),
    role_legitimacy REAL CHECK (role_legitimacy >= 0 AND role_legitimacy <= 1),
    protocol_review REAL CHECK (protocol_review >= 0 AND protocol_review <= 1),
    consent_status REAL CHECK (consent_status >= 0 AND consent_status <= 1),
    access_control REAL CHECK (access_control >= 0 AND access_control <= 1),
    governance_oversight REAL CHECK (governance_oversight >= 0 AND governance_oversight <= 1),
    benefit_sharing REAL CHECK (benefit_sharing >= 0 AND benefit_sharing <= 1),
    quote_extraction_risk REAL CHECK (quote_extraction_risk >= 0 AND quote_extraction_risk <= 1),
    context_removal REAL CHECK (context_removal >= 0 AND context_removal <= 1),
    sound_loss REAL CHECK (sound_loss >= 0 AND sound_loss <= 1),
    translation_loss REAL CHECK (translation_loss >= 0 AND translation_loss <= 1),
    extraction_risk REAL CHECK (extraction_risk >= 0 AND extraction_risk <= 1),
    governance_control REAL CHECK (governance_control >= 0 AND governance_control <= 1),
    community_sensitivity REAL CHECK (community_sensitivity >= 0 AND community_sensitivity <= 1),
    public_consequence REAL CHECK (public_consequence >= 0 AND public_consequence <= 1),
    owner TEXT,
    status TEXT
);

CREATE TABLE oral_form_contexts (
    context_id INTEGER PRIMARY KEY,
    item TEXT NOT NULL,
    context_type TEXT,
    performance_setting TEXT,
    documentation_note TEXT,
    FOREIGN KEY (item) REFERENCES compact_oral_forms_items(item)
);

CREATE TABLE sound_repetition_features (
    feature_id INTEGER PRIMARY KEY,
    item TEXT NOT NULL,
    sound_feature TEXT,
    repetition_feature TEXT,
    interpretive_note TEXT,
    FOREIGN KEY (item) REFERENCES compact_oral_forms_items(item)
);

CREATE TABLE ritual_authority_notes (
    authority_id INTEGER PRIMARY KEY,
    item TEXT NOT NULL,
    authority_issue TEXT,
    access_level TEXT,
    governance_note TEXT,
    FOREIGN KEY (item) REFERENCES compact_oral_forms_items(item)
);

CREATE TABLE archive_risks (
    risk_id INTEGER PRIMARY KEY,
    item TEXT NOT NULL,
    risk_type TEXT,
    severity TEXT,
    note TEXT,
    FOREIGN KEY (item) REFERENCES compact_oral_forms_items(item)
);

CREATE TABLE compact_oral_forms_governance_notes (
    note_id INTEGER PRIMARY KEY,
    item TEXT NOT NULL,
    governance_focus TEXT,
    review_owner TEXT,
    status TEXT,
    FOREIGN KEY (item) REFERENCES compact_oral_forms_items(item)
);
