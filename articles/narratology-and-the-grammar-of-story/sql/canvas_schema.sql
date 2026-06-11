-- SQLite-compatible schema for narratology and narrative grammar analysis.

DROP TABLE IF EXISTS narratology_claims;

CREATE TABLE narratology_claims (
    claim_id INTEGER PRIMARY KEY,
    item TEXT NOT NULL UNIQUE,
    claim_context TEXT NOT NULL,
    story_discourse_clarity REAL CHECK (story_discourse_clarity >= 0 AND story_discourse_clarity <= 1),
    voice_clarity REAL CHECK (voice_clarity >= 0 AND voice_clarity <= 1),
    focalization_clarity REAL CHECK (focalization_clarity >= 0 AND focalization_clarity <= 1),
    temporal_mapping REAL CHECK (temporal_mapping >= 0 AND temporal_mapping <= 1),
    character_agency_mapping REAL CHECK (character_agency_mapping >= 0 AND character_agency_mapping <= 1),
    information_control_analysis REAL CHECK (information_control_analysis >= 0 AND information_control_analysis <= 1),
    omission_risk REAL CHECK (omission_risk >= 0 AND omission_risk <= 1),
    power_blindness REAL CHECK (power_blindness >= 0 AND power_blindness <= 1),
    voice_imbalance REAL CHECK (voice_imbalance >= 0 AND voice_imbalance <= 1),
    closure_pressure REAL CHECK (closure_pressure >= 0 AND closure_pressure <= 1),
    unreliable_framing_risk REAL CHECK (unreliable_framing_risk >= 0 AND unreliable_framing_risk <= 1),
    owner TEXT,
    status TEXT,
    notes TEXT
);
