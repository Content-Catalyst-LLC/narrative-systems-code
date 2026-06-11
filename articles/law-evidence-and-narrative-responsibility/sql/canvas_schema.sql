-- SQLite-compatible schema for legal narrative responsibility analysis.

DROP TABLE IF EXISTS legal_narrative_responsibility_claims;

CREATE TABLE legal_narrative_responsibility_claims (
    claim_id INTEGER PRIMARY KEY,
    item TEXT NOT NULL UNIQUE,
    claim_context TEXT NOT NULL,
    relevance REAL CHECK (relevance >= 0 AND relevance <= 1),
    authentication REAL CHECK (authentication >= 0 AND authentication <= 1),
    provenance REAL CHECK (provenance >= 0 AND provenance <= 1),
    corroboration REAL CHECK (corroboration >= 0 AND corroboration <= 1),
    uncertainty_notation REAL CHECK (uncertainty_notation >= 0 AND uncertainty_notation <= 1),
    overcoherence REAL CHECK (overcoherence >= 0 AND overcoherence <= 1),
    evidentiary_gap REAL CHECK (evidentiary_gap >= 0 AND evidentiary_gap <= 1),
    procedural_posture_clarity REAL CHECK (procedural_posture_clarity >= 0 AND procedural_posture_clarity <= 1),
    hallucinated_authority REAL CHECK (hallucinated_authority >= 0 AND hallucinated_authority <= 1),
    human_review REAL CHECK (human_review >= 0 AND human_review <= 1),
    owner TEXT,
    status TEXT,
    notes TEXT
);
