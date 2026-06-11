-- SQLite-compatible schema for organizational story governance analysis.

DROP TABLE IF EXISTS organizational_story_governance_claims;

CREATE TABLE organizational_story_governance_claims (
    claim_id INTEGER PRIMARY KEY,
    item TEXT NOT NULL UNIQUE,
    claim_context TEXT NOT NULL,
    mission_clarity REAL CHECK (mission_clarity >= 0 AND mission_clarity <= 1),
    decision_alignment REAL CHECK (decision_alignment >= 0 AND decision_alignment <= 1),
    budget_fit REAL CHECK (budget_fit >= 0 AND budget_fit <= 1),
    stakeholder_impact REAL CHECK (stakeholder_impact >= 0 AND stakeholder_impact <= 1),
    employee_experience REAL CHECK (employee_experience >= 0 AND employee_experience <= 1),
    governance_transparency REAL CHECK (governance_transparency >= 0 AND governance_transparency <= 1),
    participation_integrity REAL CHECK (participation_integrity >= 0 AND participation_integrity <= 1),
    dissent_visibility REAL CHECK (dissent_visibility >= 0 AND dissent_visibility <= 1),
    human_review REAL CHECK (human_review >= 0 AND human_review <= 1),
    owner TEXT,
    status TEXT,
    notes TEXT
);
