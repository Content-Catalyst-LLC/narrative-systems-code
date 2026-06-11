-- SQLite-compatible schema for four-function myth analysis.

DROP TABLE IF EXISTS four_function_myth_claims;

CREATE TABLE four_function_myth_claims (
    claim_id INTEGER PRIMARY KEY,
    item TEXT NOT NULL UNIQUE,
    claim_context TEXT NOT NULL,
    mystical_function REAL CHECK (mystical_function >= 0 AND mystical_function <= 1),
    cosmological_function REAL CHECK (cosmological_function >= 0 AND cosmological_function <= 1),
    sociological_function REAL CHECK (sociological_function >= 0 AND sociological_function <= 1),
    pedagogical_function REAL CHECK (pedagogical_function >= 0 AND pedagogical_function <= 1),
    cultural_work REAL,
    function_balance REAL,
    sociological_risk REAL,
    interpretation_readiness REAL,
    governance_priority_score REAL,
    review_priority TEXT,
    owner TEXT,
    status TEXT
);
