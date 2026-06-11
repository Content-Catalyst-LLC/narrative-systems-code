-- SQLite-compatible schema for Ricoeurian narrative-time analysis.

DROP TABLE IF EXISTS ricoeur_narrative_time_claims;

CREATE TABLE ricoeur_narrative_time_claims (
    claim_id INTEGER PRIMARY KEY,
    item TEXT NOT NULL UNIQUE,
    claim_context TEXT NOT NULL,
    memory_mapping REAL CHECK (memory_mapping >= 0 AND memory_mapping <= 1),
    anticipation REAL CHECK (anticipation >= 0 AND anticipation <= 1),
    plot_logic REAL CHECK (plot_logic >= 0 AND plot_logic <= 1),
    configuration REAL CHECK (configuration >= 0 AND configuration <= 1),
    refiguration REAL CHECK (refiguration >= 0 AND refiguration <= 1),
    ending_function REAL CHECK (ending_function >= 0 AND ending_function <= 1),
    premature_closure REAL CHECK (premature_closure >= 0 AND premature_closure <= 1),
    redemptive_shortcut REAL CHECK (redemptive_shortcut >= 0 AND redemptive_shortcut <= 1),
    erased_continuity REAL CHECK (erased_continuity >= 0 AND erased_continuity <= 1),
    delayed_accountability REAL CHECK (delayed_accountability >= 0 AND delayed_accountability <= 1),
    nostalgic_origin REAL CHECK (nostalgic_origin >= 0 AND nostalgic_origin <= 1),
    owner TEXT,
    status TEXT,
    notes TEXT
);
