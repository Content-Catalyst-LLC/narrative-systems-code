-- SQLite-compatible schema for cross-media story governance analysis.

DROP TABLE IF EXISTS cross_media_story_governance_claims;

CREATE TABLE cross_media_story_governance_claims (
    claim_id INTEGER PRIMARY KEY,
    item TEXT NOT NULL UNIQUE,
    transfer_context TEXT NOT NULL,
    embodiment REAL CHECK (embodiment >= 0 AND embodiment <= 1),
    interior_depth REAL CHECK (interior_depth >= 0 AND interior_depth <= 1),
    spatial_quality REAL CHECK (spatial_quality >= 0 AND spatial_quality <= 1),
    temporal_control REAL CHECK (temporal_control >= 0 AND temporal_control <= 1),
    audience_relation REAL CHECK (audience_relation >= 0 AND audience_relation <= 1),
    contextual_fit REAL CHECK (contextual_fit >= 0 AND contextual_fit <= 1),
    voice_loss REAL CHECK (voice_loss >= 0 AND voice_loss <= 1),
    context_loss REAL CHECK (context_loss >= 0 AND context_loss <= 1),
    provenance_loss REAL CHECK (provenance_loss >= 0 AND provenance_loss <= 1),
    governance_review REAL CHECK (governance_review >= 0 AND governance_review <= 1),
    human_review REAL CHECK (human_review >= 0 AND human_review <= 1),
    owner TEXT,
    status TEXT,
    notes TEXT
);
