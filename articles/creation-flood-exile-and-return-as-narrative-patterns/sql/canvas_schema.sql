-- SQLite-compatible schema for creation, flood, exile, and return pattern analysis.

DROP TABLE IF EXISTS narrative_pattern_claims;

CREATE TABLE narrative_pattern_claims (
    claim_id INTEGER PRIMARY KEY,
    item TEXT NOT NULL UNIQUE,
    claim_context TEXT NOT NULL,
    creation_signal REAL CHECK (creation_signal >= 0 AND creation_signal <= 1),
    flood_signal REAL CHECK (flood_signal >= 0 AND flood_signal <= 1),
    exile_signal REAL CHECK (exile_signal >= 0 AND exile_signal <= 1),
    return_signal REAL CHECK (return_signal >= 0 AND return_signal <= 1),
    memory_maintenance REAL CHECK (memory_maintenance >= 0 AND memory_maintenance <= 1),
    repair_responsibility REAL CHECK (repair_responsibility >= 0 AND repair_responsibility <= 1),
    origin_nostalgia REAL CHECK (origin_nostalgia >= 0 AND origin_nostalgia <= 1),
    cleansing_fantasy REAL CHECK (cleansing_fantasy >= 0 AND cleansing_fantasy <= 1),
    exile_romanticization REAL CHECK (exile_romanticization >= 0 AND exile_romanticization <= 1),
    false_return REAL CHECK (false_return >= 0 AND false_return <= 1),
    power_blindness REAL CHECK (power_blindness >= 0 AND power_blindness <= 1),
    owner TEXT,
    status TEXT,
    notes TEXT
);
