-- canvas_schema.sql
-- SQLite-compatible schema for public story rhetoric analysis.

PRAGMA foreign_keys = ON;

DROP TABLE IF EXISTS rhetorical_governance_notes;
DROP TABLE IF EXISTS public_story_risks;
DROP TABLE IF EXISTS evidence_support;
DROP TABLE IF EXISTS identification_patterns;
DROP TABLE IF EXISTS rhetorical_appeals;
DROP TABLE IF EXISTS public_story_rhetoric_items;

CREATE TABLE public_story_rhetoric_items (
    item_id INTEGER PRIMARY KEY,
    item TEXT NOT NULL UNIQUE,
    story_type TEXT NOT NULL,
    ethos_strength REAL CHECK (ethos_strength >= 0 AND ethos_strength <= 1),
    logos_support REAL CHECK (logos_support >= 0 AND logos_support <= 1),
    pathos_proportionality REAL CHECK (pathos_proportionality >= 0 AND pathos_proportionality <= 1),
    audience_fit REAL CHECK (audience_fit >= 0 AND audience_fit <= 1),
    context_clarity REAL CHECK (context_clarity >= 0 AND context_clarity <= 1),
    identification_strength REAL CHECK (identification_strength >= 0 AND identification_strength <= 1),
    emotional_intensity REAL CHECK (emotional_intensity >= 0 AND emotional_intensity <= 1),
    causal_clarity REAL CHECK (causal_clarity >= 0 AND causal_clarity <= 1),
    urgency REAL CHECK (urgency >= 0 AND urgency <= 1),
    action_clarity REAL CHECK (action_clarity >= 0 AND action_clarity <= 1),
    verification_strength REAL CHECK (verification_strength >= 0 AND verification_strength <= 1),
    emotional_coercion REAL CHECK (emotional_coercion >= 0 AND emotional_coercion <= 1),
    scapegoating_risk REAL CHECK (scapegoating_risk >= 0 AND scapegoating_risk <= 1),
    identity_manipulation REAL CHECK (identity_manipulation >= 0 AND identity_manipulation <= 1),
    closure_pressure REAL CHECK (closure_pressure >= 0 AND closure_pressure <= 1),
    audience_consequence REAL CHECK (audience_consequence >= 0 AND audience_consequence <= 1),
    representation_sensitivity REAL CHECK (representation_sensitivity >= 0 AND representation_sensitivity <= 1),
    owner TEXT,
    status TEXT
);

CREATE TABLE rhetorical_appeals (
    appeal_id INTEGER PRIMARY KEY,
    item TEXT NOT NULL,
    appeal TEXT,
    signal TEXT,
    review_note TEXT,
    FOREIGN KEY (item) REFERENCES public_story_rhetoric_items(item)
);

CREATE TABLE identification_patterns (
    identification_id INTEGER PRIMARY KEY,
    item TEXT NOT NULL,
    identification_pattern TEXT,
    invited_role TEXT,
    exclusion_risk TEXT,
    FOREIGN KEY (item) REFERENCES public_story_rhetoric_items(item)
);

CREATE TABLE evidence_support (
    evidence_id INTEGER PRIMARY KEY,
    item TEXT NOT NULL,
    evidence_type TEXT,
    evidence_strength TEXT,
    evidence_caution TEXT,
    FOREIGN KEY (item) REFERENCES public_story_rhetoric_items(item)
);

CREATE TABLE public_story_risks (
    risk_id INTEGER PRIMARY KEY,
    item TEXT NOT NULL,
    risk_type TEXT,
    severity TEXT,
    note TEXT,
    FOREIGN KEY (item) REFERENCES public_story_rhetoric_items(item)
);

CREATE TABLE rhetorical_governance_notes (
    note_id INTEGER PRIMARY KEY,
    item TEXT NOT NULL,
    governance_focus TEXT,
    review_owner TEXT,
    status TEXT,
    FOREIGN KEY (item) REFERENCES public_story_rhetoric_items(item)
);
