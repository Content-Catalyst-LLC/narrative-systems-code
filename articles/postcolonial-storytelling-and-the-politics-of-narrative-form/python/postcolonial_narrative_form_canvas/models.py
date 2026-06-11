from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class PostcolonialNarrativeFormConfig:
    article_title: str = "Postcolonial Storytelling and the Politics of Narrative Form"
    article_slug: str = "postcolonial-storytelling-and-the-politics-of-narrative-form"
    medium_threshold: float = 0.45
    high_threshold: float = 0.62
    allowed_statuses: tuple[str, ...] = ("active", "archive", "review", "revise")


@dataclass(frozen=True)
class PostcolonialNarrativeFormRecord:
    item: str
    claim_context: str
    archive_dominance: float
    language_hierarchy: float
    gaze_centrality: float
    template_forcing: float
    extraction_anxiety: float
    opacity_protection: float
    voice_complexity: float
    language_politics: float
    memory_fragmentation: float
    archive_critique: float
    temporal_multiplicity: float
    spatial_politics: float
    relational_land_context: float
    cultural_specificity: float
    local_authority: float
    opacity_notes: float
    untranslated_terms: float
    reviewer_visibility: float
    harm_review: float
    english_dominance: float
    stereotype_bias: float
    extraction_risk: float
    archive_flattening: float
    visual_orientalism: float
    community_governance: float
    public_consequence: float
    owner: str = "editorial"
    status: str = "active"
    notes: str = ""
