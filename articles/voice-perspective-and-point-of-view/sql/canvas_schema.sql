-- canvas_schema.sql
-- SQLite-compatible schema for voice, perspective, and point-of-view analysis.

PRAGMA foreign_keys = ON;

DROP TABLE IF EXISTS voice_governance_notes;
DROP TABLE IF EXISTS perspective_gaps;
DROP TABLE IF EXISTS reliability_risks;
DROP TABLE IF EXISTS narrator_access_patterns;
DROP TABLE IF EXISTS focalization_map;
DROP TABLE IF EXISTS voice_perspective_items;

CREATE TABLE voice_perspective_items (
    item_id INTEGER PRIMARY KEY,
    item TEXT NOT NULL UNIQUE,
    story_type TEXT NOT NULL,
    tone_stability REAL CHECK (tone_stability >= 0 AND tone_stability <= 1),
    diction_coherence REAL CHECK (diction_coherence >= 0 AND diction_coherence <= 1),
    rhetorical_habit REAL CHECK (rhetorical_habit >= 0 AND rhetorical_habit <= 1),
    address_stability REAL CHECK (address_stability >= 0 AND address_stability <= 1),
    judgment_coherence REAL CHECK (judgment_coherence >= 0 AND judgment_coherence <= 1),
    knowledge_limits REAL CHECK (knowledge_limits >= 0 AND knowledge_limits <= 1),
    interior_access REAL CHECK (interior_access >= 0 AND interior_access <= 1),
    focalization_clarity REAL CHECK (focalization_clarity >= 0 AND focalization_clarity <= 1),
    level_stability REAL CHECK (level_stability >= 0 AND level_stability <= 1),
    source_boundaries REAL CHECK (source_boundaries >= 0 AND source_boundaries <= 1),
    factual_unreliability REAL CHECK (factual_unreliability >= 0 AND factual_unreliability <= 1),
    interpretive_unreliability REAL CHECK (interpretive_unreliability >= 0 AND interpretive_unreliability <= 1),
    ethical_unreliability REAL CHECK (ethical_unreliability >= 0 AND ethical_unreliability <= 1),
    memory_distortion REAL CHECK (memory_distortion >= 0 AND memory_distortion <= 1),
    agency_gap REAL CHECK (agency_gap >= 0 AND agency_gap <= 1),
    exposure_sensitivity REAL CHECK (exposure_sensitivity >= 0 AND exposure_sensitivity <= 1),
    public_consequence REAL CHECK (public_consequence >= 0 AND public_consequence <= 1),
    representation_gap REAL CHECK (representation_gap >= 0 AND representation_gap <= 1),
    institutional_evasion REAL CHECK (institutional_evasion >= 0 AND institutional_evasion <= 1),
    owner TEXT,
    status TEXT
);

CREATE TABLE focalization_map (
    focalization_id INTEGER PRIMARY KEY,
    item TEXT NOT NULL,
    scene_or_section TEXT,
    narrator_position TEXT,
    focalizer TEXT,
    access_type TEXT,
    concern TEXT,
    FOREIGN KEY (item) REFERENCES voice_perspective_items(item)
);

CREATE TABLE narrator_access_patterns (
    access_id INTEGER PRIMARY KEY,
    item TEXT NOT NULL,
    point_of_view TEXT,
    knowledge_scope TEXT,
    access_strength TEXT,
    access_risk TEXT,
    FOREIGN KEY (item) REFERENCES voice_perspective_items(item)
);

CREATE TABLE reliability_risks (
    risk_id INTEGER PRIMARY KEY,
    item TEXT NOT NULL,
    risk_type TEXT,
    severity TEXT,
    note TEXT,
    FOREIGN KEY (item) REFERENCES voice_perspective_items(item)
);

CREATE TABLE perspective_gaps (
    gap_id INTEGER PRIMARY KEY,
    item TEXT NOT NULL,
    gap_type TEXT,
    affected_voice TEXT,
    revision_note TEXT,
    FOREIGN KEY (item) REFERENCES voice_perspective_items(item)
);

CREATE TABLE voice_governance_notes (
    note_id INTEGER PRIMARY KEY,
    item TEXT NOT NULL,
    governance_focus TEXT,
    review_owner TEXT,
    status TEXT,
    FOREIGN KEY (item) REFERENCES voice_perspective_items(item)
);
