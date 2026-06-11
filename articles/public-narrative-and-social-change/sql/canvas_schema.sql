-- SQLite-compatible schema for public narrative governance analysis.

DROP TABLE IF EXISTS public_narrative_governance_claims;

CREATE TABLE public_narrative_governance_claims (
    claim_id INTEGER PRIMARY KEY,
    item TEXT NOT NULL UNIQUE,
    claim_context TEXT NOT NULL,
    self_clarity REAL CHECK (self_clarity >= 0 AND self_clarity <= 1),
    us_clarity REAL CHECK (us_clarity >= 0 AND us_clarity <= 1),
    now_clarity REAL CHECK (now_clarity >= 0 AND now_clarity <= 1),
    value_articulation REAL CHECK (value_articulation >= 0 AND value_articulation <= 1),
    action_clarity REAL CHECK (action_clarity >= 0 AND action_clarity <= 1),
    governance_review REAL CHECK (governance_review >= 0 AND governance_review <= 1),
    consent_deficit REAL CHECK (consent_deficit >= 0 AND consent_deficit <= 1),
    omitted_voices REAL CHECK (omitted_voices >= 0 AND omitted_voices <= 1),
    human_review REAL CHECK (human_review >= 0 AND human_review <= 1),
    owner TEXT,
    status TEXT,
    notes TEXT
);
