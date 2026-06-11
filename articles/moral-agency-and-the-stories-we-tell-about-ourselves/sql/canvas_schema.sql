-- SQLite-compatible schema for moral agency self-narrative analysis.

DROP TABLE IF EXISTS moral_agency_claims;

CREATE TABLE moral_agency_claims (
    claim_id INTEGER PRIMARY KEY,
    item TEXT NOT NULL UNIQUE,
    claim_context TEXT NOT NULL,
    action_naming REAL CHECK (action_naming >= 0 AND action_naming <= 1),
    intention_distinction REAL CHECK (intention_distinction >= 0 AND intention_distinction <= 1),
    consequence_clarity REAL CHECK (consequence_clarity >= 0 AND consequence_clarity <= 1),
    harm_marking REAL CHECK (harm_marking >= 0 AND harm_marking <= 1),
    repair_orientation REAL CHECK (repair_orientation >= 0 AND repair_orientation <= 1),
    other_visibility REAL CHECK (other_visibility >= 0 AND other_visibility <= 1),
    context_overuse REAL CHECK (context_overuse >= 0 AND context_overuse <= 1),
    intention_shielding REAL CHECK (intention_shielding >= 0 AND intention_shielding <= 1),
    victimhood_shielding REAL CHECK (victimhood_shielding >= 0 AND victimhood_shielding <= 1),
    blame_shifting REAL CHECK (blame_shifting >= 0 AND blame_shifting <= 1),
    growth_substitution REAL CHECK (growth_substitution >= 0 AND growth_substitution <= 1),
    harm_minimization REAL CHECK (harm_minimization >= 0 AND harm_minimization <= 1),
    owner TEXT,
    status TEXT,
    notes TEXT
);
