-- SQLite-compatible schema for tragic, cyclical, and non-heroic narrative analysis.

DROP TABLE IF EXISTS non_heroic_narrative_claims;

CREATE TABLE non_heroic_narrative_claims (
    claim_id INTEGER PRIMARY KEY,
    item TEXT NOT NULL UNIQUE,
    claim_context TEXT NOT NULL,
    consequential_action REAL CHECK (consequential_action >= 0 AND consequential_action <= 1),
    limit_pressure REAL CHECK (limit_pressure >= 0 AND limit_pressure <= 1),
    reversal REAL CHECK (reversal >= 0 AND reversal <= 1),
    recognition_knowledge REAL CHECK (recognition_knowledge >= 0 AND recognition_knowledge <= 1),
    irreversibility REAL CHECK (irreversibility >= 0 AND irreversibility <= 1),
    witness_burden REAL CHECK (witness_burden >= 0 AND witness_burden <= 1),
    repeated_pattern REAL CHECK (repeated_pattern >= 0 AND repeated_pattern <= 1),
    seasonal_ritual_signal REAL CHECK (seasonal_ritual_signal >= 0 AND seasonal_ritual_signal <= 1),
    generational_transmission REAL CHECK (generational_transmission >= 0 AND generational_transmission <= 1),
    institutional_habit REAL CHECK (institutional_habit >= 0 AND institutional_habit <= 1),
    ecological_feedback REAL CHECK (ecological_feedback >= 0 AND ecological_feedback <= 1),
    variation_across_return REAL CHECK (variation_across_return >= 0 AND variation_across_return <= 1),
    care REAL CHECK (care >= 0 AND care <= 1),
    endurance REAL CHECK (endurance >= 0 AND endurance <= 1),
    witness REAL CHECK (witness >= 0 AND witness <= 1),
    refusal REAL CHECK (refusal >= 0 AND refusal <= 1),
    maintenance REAL CHECK (maintenance >= 0 AND maintenance <= 1),
    survival REAL CHECK (survival >= 0 AND survival <= 1),
    owner TEXT,
    status TEXT,
    notes TEXT
);
