-- SQLite-compatible schema for alternative story structure analysis.

DROP TABLE IF EXISTS alternative_structure_claims;

CREATE TABLE alternative_structure_claims (
    claim_id INTEGER PRIMARY KEY,
    item TEXT NOT NULL UNIQUE,
    claim_context TEXT NOT NULL,
    arc_signal REAL CHECK (arc_signal >= 0 AND arc_signal <= 1),
    cycle_signal REAL CHECK (cycle_signal >= 0 AND cycle_signal <= 1),
    braid_signal REAL CHECK (braid_signal >= 0 AND braid_signal <= 1),
    mosaic_signal REAL CHECK (mosaic_signal >= 0 AND mosaic_signal <= 1),
    network_signal REAL CHECK (network_signal >= 0 AND network_signal <= 1),
    relational_signal REAL CHECK (relational_signal >= 0 AND relational_signal <= 1),
    fragment_signal REAL CHECK (fragment_signal >= 0 AND fragment_signal <= 1),
    hero_forcing REAL CHECK (hero_forcing >= 0 AND hero_forcing <= 1),
    conflict_substitution REAL CHECK (conflict_substitution >= 0 AND conflict_substitution <= 1),
    return_pressure REAL CHECK (return_pressure >= 0 AND return_pressure <= 1),
    individualization_pressure REAL CHECK (individualization_pressure >= 0 AND individualization_pressure <= 1),
    template_forcing REAL CHECK (template_forcing >= 0 AND template_forcing <= 1),
    evidence_visibility REAL CHECK (evidence_visibility >= 0 AND evidence_visibility <= 1),
    owner TEXT,
    status TEXT,
    notes TEXT
);
