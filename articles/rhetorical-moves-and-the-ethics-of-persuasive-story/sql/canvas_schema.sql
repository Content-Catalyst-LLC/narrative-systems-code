-- SQLite-compatible schema for rhetorical moves governance analysis.

DROP TABLE IF EXISTS rhetorical_moves_governance_claims;

CREATE TABLE rhetorical_moves_governance_claims (
    claim_id INTEGER PRIMARY KEY,
    item TEXT NOT NULL UNIQUE,
    persuasion_context TEXT NOT NULL,
    evidence_truthfulness REAL CHECK (evidence_truthfulness >= 0 AND evidence_truthfulness <= 1),
    proportionality REAL CHECK (proportionality >= 0 AND proportionality <= 1),
    context_adequacy REAL CHECK (context_adequacy >= 0 AND context_adequacy <= 1),
    audience_agency REAL CHECK (audience_agency >= 0 AND audience_agency <= 1),
    fear_amplification REAL CHECK (fear_amplification >= 0 AND fear_amplification <= 1),
    emotional_exploitation REAL CHECK (emotional_exploitation >= 0 AND emotional_exploitation <= 1),
    urgency_coercion REAL CHECK (urgency_coercion >= 0 AND urgency_coercion <= 1),
    human_review REAL CHECK (human_review >= 0 AND human_review <= 1),
    owner TEXT,
    status TEXT,
    notes TEXT
);
