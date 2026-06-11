from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class IndigenousStoryGovernanceConfig:
    article_title: str = "Indigenous Storytelling, Place, and Relational Memory"
    article_slug: str = "indigenous-storytelling-place-and-relational-memory"
    medium_threshold: float = 0.45
    high_threshold: float = 0.62
    allowed_statuses: tuple[str, ...] = ("active", "archive", "review", "revise")


@dataclass(frozen=True)
class IndigenousStoryGovernanceRecord:
    item: str
    claim_context: str
    place_specificity: float
    community_authority: float
    teller_relationship: float
    listener_context: float
    obligation_visibility: float
    governance_visibility: float
    access_pressure: float
    seasonal_restriction: float
    ceremonial_restriction: float
    template_forcing: float
    digital_exposure: float
    land_naming: float
    ecological_knowledge: float
    ancestral_memory: float
    route_teaching: float
    seasonal_context: float
    future_generation_responsibility: float
    cultural_specificity: float
    language_context: float
    opacity_notes: float
    untranslated_terms: float
    reviewer_visibility: float
    harm_review: float
    extraction_risk: float
    open_access_assumption: float
    ai_training_risk: float
    stereotype_bias: float
    metadata_flattening: float
    community_governance: float
    public_consequence: float
    owner: str = "editorial"
    status: str = "active"
    notes: str = ""
