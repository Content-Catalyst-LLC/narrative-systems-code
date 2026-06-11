-- SQLite-compatible schema for interactive narrative governance analysis.

DROP TABLE IF EXISTS interactive_narrative_governance_claims;

CREATE TABLE interactive_narrative_governance_claims (
    claim_id INTEGER PRIMARY KEY,
    item TEXT NOT NULL UNIQUE,
    game_context TEXT NOT NULL,
    choice_meaningfulness REAL CHECK (choice_meaningfulness >= 0 AND choice_meaningfulness <= 1),
    system_response REAL CHECK (system_response >= 0 AND system_response <= 1),
    feedback_clarity REAL CHECK (feedback_clarity >= 0 AND feedback_clarity <= 1),
    world_memory REAL CHECK (world_memory >= 0 AND world_memory <= 1),
    branch_count_pressure REAL CHECK (branch_count_pressure >= 0 AND branch_count_pressure <= 1),
    state_dependency REAL CHECK (state_dependency >= 0 AND state_dependency <= 1),
    consequence_tracking REAL CHECK (consequence_tracking >= 0 AND consequence_tracking <= 1),
    human_review REAL CHECK (human_review >= 0 AND human_review <= 1),
    owner TEXT,
    status TEXT,
    notes TEXT
);
