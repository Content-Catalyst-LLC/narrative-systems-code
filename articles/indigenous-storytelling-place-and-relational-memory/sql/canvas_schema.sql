-- SQLite-compatible schema for Indigenous story governance analysis.

DROP TABLE IF EXISTS indigenous_story_governance_claims;

CREATE TABLE indigenous_story_governance_claims (
    claim_id INTEGER PRIMARY KEY,
    item TEXT NOT NULL UNIQUE,
    claim_context TEXT NOT NULL,
    place_specificity REAL CHECK (place_specificity >= 0 AND place_specificity <= 1),
    community_authority REAL CHECK (community_authority >= 0 AND community_authority <= 1),
    teller_relationship REAL CHECK (teller_relationship >= 0 AND teller_relationship <= 1),
    listener_context REAL CHECK (listener_context >= 0 AND listener_context <= 1),
    obligation_visibility REAL CHECK (obligation_visibility >= 0 AND obligation_visibility <= 1),
    governance_visibility REAL CHECK (governance_visibility >= 0 AND governance_visibility <= 1),
    access_pressure REAL CHECK (access_pressure >= 0 AND access_pressure <= 1),
    seasonal_restriction REAL CHECK (seasonal_restriction >= 0 AND seasonal_restriction <= 1),
    ceremonial_restriction REAL CHECK (ceremonial_restriction >= 0 AND ceremonial_restriction <= 1),
    template_forcing REAL CHECK (template_forcing >= 0 AND template_forcing <= 1),
    digital_exposure REAL CHECK (digital_exposure >= 0 AND digital_exposure <= 1),
    community_governance REAL CHECK (community_governance >= 0 AND community_governance <= 1),
    owner TEXT,
    status TEXT,
    notes TEXT
);
