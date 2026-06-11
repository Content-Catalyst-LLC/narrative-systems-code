-- SQLite-compatible schema for postcolonial narrative-form analysis.

DROP TABLE IF EXISTS postcolonial_narrative_form_claims;

CREATE TABLE postcolonial_narrative_form_claims (
    claim_id INTEGER PRIMARY KEY,
    item TEXT NOT NULL UNIQUE,
    claim_context TEXT NOT NULL,
    archive_dominance REAL CHECK (archive_dominance >= 0 AND archive_dominance <= 1),
    language_hierarchy REAL CHECK (language_hierarchy >= 0 AND language_hierarchy <= 1),
    gaze_centrality REAL CHECK (gaze_centrality >= 0 AND gaze_centrality <= 1),
    template_forcing REAL CHECK (template_forcing >= 0 AND template_forcing <= 1),
    extraction_anxiety REAL CHECK (extraction_anxiety >= 0 AND extraction_anxiety <= 1),
    opacity_protection REAL CHECK (opacity_protection >= 0 AND opacity_protection <= 1),
    voice_complexity REAL CHECK (voice_complexity >= 0 AND voice_complexity <= 1),
    language_politics REAL CHECK (language_politics >= 0 AND language_politics <= 1),
    archive_critique REAL CHECK (archive_critique >= 0 AND archive_critique <= 1),
    english_dominance REAL CHECK (english_dominance >= 0 AND english_dominance <= 1),
    stereotype_bias REAL CHECK (stereotype_bias >= 0 AND stereotype_bias <= 1),
    community_governance REAL CHECK (community_governance >= 0 AND community_governance <= 1),
    owner TEXT,
    status TEXT,
    notes TEXT
);
