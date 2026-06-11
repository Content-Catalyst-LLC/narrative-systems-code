-- SQLite-compatible schema for national memory governance analysis.

DROP TABLE IF EXISTS national_memory_governance_claims;

CREATE TABLE national_memory_governance_claims (
    claim_id INTEGER PRIMARY KEY,
    item TEXT NOT NULL UNIQUE,
    claim_context TEXT NOT NULL,
    group_representation REAL CHECK (group_representation >= 0 AND group_representation <= 1),
    source_diversity REAL CHECK (source_diversity >= 0 AND source_diversity <= 1),
    testimony_visibility REAL CHECK (testimony_visibility >= 0 AND testimony_visibility <= 1),
    countermemory_inclusion REAL CHECK (countermemory_inclusion >= 0 AND countermemory_inclusion <= 1),
    hero_compression REAL CHECK (hero_compression >= 0 AND hero_compression <= 1),
    innocence_story REAL CHECK (innocence_story >= 0 AND innocence_story <= 1),
    exclusion_omission REAL CHECK (exclusion_omission >= 0 AND exclusion_omission <= 1),
    revision_capacity REAL CHECK (revision_capacity >= 0 AND revision_capacity <= 1),
    evidence_visibility REAL CHECK (evidence_visibility >= 0 AND evidence_visibility <= 1),
    human_review REAL CHECK (human_review >= 0 AND human_review <= 1),
    owner TEXT,
    status TEXT,
    notes TEXT
);
