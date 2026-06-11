-- canvas_schema.sql
-- SQLite-compatible schema for myth, ritual, and symbolic story analysis.

PRAGMA foreign_keys = ON;

DROP TABLE IF EXISTS myth_ritual_governance_notes;
DROP TABLE IF EXISTS ethical_risks;
DROP TABLE IF EXISTS power_and_authority_notes;
DROP TABLE IF EXISTS ritual_contexts;
DROP TABLE IF EXISTS symbolic_functions;
DROP TABLE IF EXISTS myth_ritual_symbolic_items;

CREATE TABLE myth_ritual_symbolic_items (
    item_id INTEGER PRIMARY KEY,
    item TEXT NOT NULL UNIQUE,
    symbolic_context TEXT NOT NULL,
    origin_function REAL CHECK (origin_function >= 0 AND origin_function <= 1),
    cosmological_order REAL CHECK (cosmological_order >= 0 AND cosmological_order <= 1),
    memory_function REAL CHECK (memory_function >= 0 AND memory_function <= 1),
    identity_function REAL CHECK (identity_function >= 0 AND identity_function <= 1),
    transition_function REAL CHECK (transition_function >= 0 AND transition_function <= 1),
    authority_function REAL CHECK (authority_function >= 0 AND authority_function <= 1),
    sequence_clarity REAL CHECK (sequence_clarity >= 0 AND sequence_clarity <= 1),
    place_linkage REAL CHECK (place_linkage >= 0 AND place_linkage <= 1),
    gesture_documentation REAL CHECK (gesture_documentation >= 0 AND gesture_documentation <= 1),
    object_symbolism REAL CHECK (object_symbolism >= 0 AND object_symbolism <= 1),
    participant_role REAL CHECK (participant_role >= 0 AND participant_role <= 1),
    protocol_transparency REAL CHECK (protocol_transparency >= 0 AND protocol_transparency <= 1),
    totalizing_order REAL CHECK (totalizing_order >= 0 AND totalizing_order <= 1),
    scapegoating_risk REAL CHECK (scapegoating_risk >= 0 AND scapegoating_risk <= 1),
    exclusion_risk REAL CHECK (exclusion_risk >= 0 AND exclusion_risk <= 1),
    appropriation_risk REAL CHECK (appropriation_risk >= 0 AND appropriation_risk <= 1),
    harm_exposure REAL CHECK (harm_exposure >= 0 AND harm_exposure <= 1),
    governance_control REAL CHECK (governance_control >= 0 AND governance_control <= 1),
    context_explanation REAL CHECK (context_explanation >= 0 AND context_explanation <= 1),
    ritual_verification REAL CHECK (ritual_verification >= 0 AND ritual_verification <= 1),
    language_notes REAL CHECK (language_notes >= 0 AND language_notes <= 1),
    access_control REAL CHECK (access_control >= 0 AND access_control <= 1),
    governance_oversight REAL CHECK (governance_oversight >= 0 AND governance_oversight <= 1),
    uncertainty_marking REAL CHECK (uncertainty_marking >= 0 AND uncertainty_marking <= 1),
    community_sensitivity REAL CHECK (community_sensitivity >= 0 AND community_sensitivity <= 1),
    public_consequence REAL CHECK (public_consequence >= 0 AND public_consequence <= 1),
    owner TEXT,
    status TEXT
);

CREATE TABLE symbolic_functions (
    function_id INTEGER PRIMARY KEY,
    item TEXT NOT NULL,
    primary_symbolic_function TEXT,
    secondary_function TEXT,
    interpretive_note TEXT,
    FOREIGN KEY (item) REFERENCES myth_ritual_symbolic_items(item)
);

CREATE TABLE ritual_contexts (
    ritual_id INTEGER PRIMARY KEY,
    item TEXT NOT NULL,
    ritual_context TEXT,
    ritual_elements TEXT,
    context_note TEXT,
    FOREIGN KEY (item) REFERENCES myth_ritual_symbolic_items(item)
);

CREATE TABLE power_and_authority_notes (
    power_id INTEGER PRIMARY KEY,
    item TEXT NOT NULL,
    power_issue TEXT,
    authority_note TEXT,
    review_note TEXT,
    FOREIGN KEY (item) REFERENCES myth_ritual_symbolic_items(item)
);

CREATE TABLE ethical_risks (
    risk_id INTEGER PRIMARY KEY,
    item TEXT NOT NULL,
    risk_type TEXT,
    severity TEXT,
    note TEXT,
    FOREIGN KEY (item) REFERENCES myth_ritual_symbolic_items(item)
);

CREATE TABLE myth_ritual_governance_notes (
    note_id INTEGER PRIMARY KEY,
    item TEXT NOT NULL,
    governance_focus TEXT,
    review_owner TEXT,
    status TEXT,
    FOREIGN KEY (item) REFERENCES myth_ritual_symbolic_items(item)
);
