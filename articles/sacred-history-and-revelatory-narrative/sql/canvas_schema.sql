-- SQLite-compatible schema for sacred-history and revelatory-narrative analysis.
DROP TABLE IF EXISTS sacred_history_claims;
CREATE TABLE sacred_history_claims (
    claim_id INTEGER PRIMARY KEY,
    item TEXT NOT NULL UNIQUE,
    claim_context TEXT NOT NULL,
    sacred_disclosure REAL CHECK (sacred_disclosure >= 0 AND sacred_disclosure <= 1),
    event_meaning REAL CHECK (event_meaning >= 0 AND event_meaning <= 1),
    authority_clarity REAL CHECK (authority_clarity >= 0 AND authority_clarity <= 1),
    owner TEXT,
    status TEXT,
    notes TEXT
);
