-- SQLite-compatible schema for storytelling value governance analysis.

DROP TABLE IF EXISTS storytelling_value_governance_claims;

CREATE TABLE storytelling_value_governance_claims (
    claim_id INTEGER PRIMARY KEY,
    item TEXT NOT NULL UNIQUE,
    story_context TEXT NOT NULL,
    clarity REAL CHECK (clarity >= 0 AND clarity <= 1),
    evidence_grounding REAL CHECK (evidence_grounding >= 0 AND evidence_grounding <= 1),
    memory_continuity REAL CHECK (memory_continuity >= 0 AND memory_continuity <= 1),
    audience_reasoning REAL CHECK (audience_reasoning >= 0 AND audience_reasoning <= 1),
    dignity_protection REAL CHECK (dignity_protection >= 0 AND dignity_protection <= 1),
    truthfulness REAL CHECK (truthfulness >= 0 AND truthfulness <= 1),
    context_adequacy REAL CHECK (context_adequacy >= 0 AND context_adequacy <= 1),
    oversimplification REAL CHECK (oversimplification >= 0 AND oversimplification <= 1),
    human_review REAL CHECK (human_review >= 0 AND human_review <= 1),
    owner TEXT,
    status TEXT,
    notes TEXT
);
