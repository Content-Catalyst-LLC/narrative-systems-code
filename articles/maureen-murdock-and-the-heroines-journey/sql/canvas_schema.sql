-- SQLite-compatible schema for heroine journey analysis.

DROP TABLE IF EXISTS heroine_journey_claims;

CREATE TABLE heroine_journey_claims (
    claim_id INTEGER PRIMARY KEY,
    item TEXT NOT NULL UNIQUE,
    claim_context TEXT NOT NULL,
    separation_from_feminine REAL CHECK (separation_from_feminine >= 0 AND separation_from_feminine <= 1),
    masculine_identification REAL CHECK (masculine_identification >= 0 AND masculine_identification <= 1),
    aridity_after_success REAL CHECK (aridity_after_success >= 0 AND aridity_after_success <= 1),
    descent_crisis REAL CHECK (descent_crisis >= 0 AND descent_crisis <= 1),
    reconnection_feminine REAL CHECK (reconnection_feminine >= 0 AND reconnection_feminine <= 1),
    integration_wholeness REAL CHECK (integration_wholeness >= 0 AND integration_wholeness <= 1),
    template_forcing REAL CHECK (template_forcing >= 0 AND template_forcing <= 1),
    gender_essentialism REAL CHECK (gender_essentialism >= 0 AND gender_essentialism <= 1),
    universal_womanhood REAL CHECK (universal_womanhood >= 0 AND universal_womanhood <= 1),
    psychological_overreach REAL CHECK (psychological_overreach >= 0 AND psychological_overreach <= 1),
    healing_pressure REAL CHECK (healing_pressure >= 0 AND healing_pressure <= 1),
    cultural_context REAL CHECK (cultural_context >= 0 AND cultural_context <= 1),
    owner TEXT,
    status TEXT,
    notes TEXT
);
