-- SQLite-compatible schema for serial narrative governance analysis.

DROP TABLE IF EXISTS serial_narrative_governance_claims;

CREATE TABLE serial_narrative_governance_claims (
    claim_id INTEGER PRIMARY KEY,
    item TEXT NOT NULL UNIQUE,
    serial_context TEXT NOT NULL,
    episode_function REAL CHECK (episode_function >= 0 AND episode_function <= 1),
    arc_progression REAL CHECK (arc_progression >= 0 AND arc_progression <= 1),
    thematic_development REAL CHECK (thematic_development >= 0 AND thematic_development <= 1),
    character_memory REAL CHECK (character_memory >= 0 AND character_memory <= 1),
    payoff_integrity_signal REAL CHECK (payoff_integrity_signal >= 0 AND payoff_integrity_signal <= 1),
    finale_consequence REAL CHECK (finale_consequence >= 0 AND finale_consequence <= 1),
    unresolved_arcs REAL CHECK (unresolved_arcs >= 0 AND unresolved_arcs <= 1),
    lore_density REAL CHECK (lore_density >= 0 AND lore_density <= 1),
    human_review REAL CHECK (human_review >= 0 AND human_review <= 1),
    owner TEXT,
    status TEXT,
    notes TEXT
);
