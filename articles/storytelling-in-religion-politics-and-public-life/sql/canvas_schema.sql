-- SQLite-compatible schema for public story governance analysis.

DROP TABLE IF EXISTS public_story_governance_claims;

CREATE TABLE public_story_governance_claims (
    claim_id INTEGER PRIMARY KEY,
    item TEXT NOT NULL UNIQUE,
    claim_context TEXT NOT NULL,
    self_story_evidence REAL CHECK (self_story_evidence >= 0 AND self_story_evidence <= 1),
    shared_value_clarity REAL CHECK (shared_value_clarity >= 0 AND shared_value_clarity <= 1),
    now_challenge_clarity REAL CHECK (now_challenge_clarity >= 0 AND now_challenge_clarity <= 1),
    enemy_simplification REAL CHECK (enemy_simplification >= 0 AND enemy_simplification <= 1),
    boundary_hardening REAL CHECK (boundary_hardening >= 0 AND boundary_hardening <= 1),
    crisis_compression REAL CHECK (crisis_compression >= 0 AND crisis_compression <= 1),
    scapegoat_intensity REAL CHECK (scapegoat_intensity >= 0 AND scapegoat_intensity <= 1),
    evidence_visibility REAL CHECK (evidence_visibility >= 0 AND evidence_visibility <= 1),
    dissent_space REAL CHECK (dissent_space >= 0 AND dissent_space <= 1),
    human_governance REAL CHECK (human_governance >= 0 AND human_governance <= 1),
    owner TEXT,
    status TEXT,
    notes TEXT
);
