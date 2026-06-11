-- SQLite-compatible schema for fragmented narrative analysis.

DROP TABLE IF EXISTS fragmented_narrative_claims;

CREATE TABLE fragmented_narrative_claims (
    claim_id INTEGER PRIMARY KEY,
    item TEXT NOT NULL UNIQUE,
    claim_context TEXT NOT NULL,
    temporal_rupture REAL CHECK (temporal_rupture >= 0 AND temporal_rupture <= 1),
    gap_marking REAL CHECK (gap_marking >= 0 AND gap_marking <= 1),
    repetition_patterning REAL CHECK (repetition_patterning >= 0 AND repetition_patterning <= 1),
    silence_respect REAL CHECK (silence_respect >= 0 AND silence_respect <= 1),
    uncertainty_notes REAL CHECK (uncertainty_notes >= 0 AND uncertainty_notes <= 1),
    contextual_care REAL CHECK (contextual_care >= 0 AND contextual_care <= 1),
    consent REAL CHECK (consent >= 0 AND consent <= 1),
    agency REAL CHECK (agency >= 0 AND agency <= 1),
    privacy REAL CHECK (privacy >= 0 AND privacy <= 1),
    forced_coherence REAL CHECK (forced_coherence >= 0 AND forced_coherence <= 1),
    redemptive_shortcut REAL CHECK (redemptive_shortcut >= 0 AND redemptive_shortcut <= 1),
    extraction_risk REAL CHECK (extraction_risk >= 0 AND extraction_risk <= 1),
    identity_reduction REAL CHECK (identity_reduction >= 0 AND identity_reduction <= 1),
    spectacle_pressure REAL CHECK (spectacle_pressure >= 0 AND spectacle_pressure <= 1),
    owner TEXT,
    status TEXT,
    notes TEXT
);
