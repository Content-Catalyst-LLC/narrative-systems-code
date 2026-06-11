-- SQLite-compatible schema for narrative systems governance analysis.

DROP TABLE IF EXISTS narrative_systems_governance_claims;

CREATE TABLE narrative_systems_governance_claims (
    claim_id INTEGER PRIMARY KEY,
    item TEXT NOT NULL UNIQUE,
    modeling_context TEXT NOT NULL,
    causal_alignment REAL CHECK (causal_alignment >= 0 AND causal_alignment <= 1),
    state_transition_clarity REAL CHECK (state_transition_clarity >= 0 AND state_transition_clarity <= 1),
    agent_goal_fit REAL CHECK (agent_goal_fit >= 0 AND agent_goal_fit <= 1),
    world_rule_consistency REAL CHECK (world_rule_consistency >= 0 AND world_rule_consistency <= 1),
    beat_template_dependence REAL CHECK (beat_template_dependence >= 0 AND beat_template_dependence <= 1),
    universal_model_claims REAL CHECK (universal_model_claims >= 0 AND universal_model_claims <= 1),
    plot_hallucination REAL CHECK (plot_hallucination >= 0 AND plot_hallucination <= 1),
    human_review REAL CHECK (human_review >= 0 AND human_review <= 1),
    owner TEXT,
    status TEXT,
    notes TEXT
);
