from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class NarrativeSystemsGovernanceConfig:
    article_title: str = "Narrative Systems and Story Structure Modeling"
    article_slug: str = "narrative-systems-and-story-structure-modeling"
    medium_threshold: float = 0.45
    high_threshold: float = 0.62
    allowed_statuses: tuple[str, ...] = ("active", "archive", "review", "revise")


@dataclass(frozen=True)
class NarrativeSystemsGovernanceRecord:
    item: str
    modeling_context: str
    causal_alignment: float
    state_transition_clarity: float
    agent_goal_fit: float
    world_rule_consistency: float
    temporal_mapping: float
    evidence_quality: float
    beat_template_dependence: float
    universal_model_claims: float
    context_loss: float
    genre_flattening: float
    model_overconfidence: float
    judgment_review: float
    individual_agency_visibility: float
    systemic_agency_visibility: float
    network_mapping: float
    relationship_specificity: float
    constraint_visibility: float
    feedback_loop_clarity: float
    plot_hallucination: float
    causal_invention: float
    stereotype_tendency: float
    formula_generation: float
    biased_corpus: float
    human_review: float
    public_consequence: float
    owner: str = "editorial"
    status: str = "active"
    notes: str = ""
