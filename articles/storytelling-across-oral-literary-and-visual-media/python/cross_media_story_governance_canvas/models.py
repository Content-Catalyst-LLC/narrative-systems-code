from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class CrossMediaStoryGovernanceConfig:
    article_title: str = "Storytelling Across Oral, Literary, and Visual Media"
    article_slug: str = "storytelling-across-oral-literary-and-visual-media"
    medium_threshold: float = 0.45
    high_threshold: float = 0.62
    allowed_statuses: tuple[str, ...] = ("active", "archive", "review", "revise")


@dataclass(frozen=True)
class CrossMediaStoryGovernanceRecord:
    item: str
    transfer_context: str
    embodiment: float
    interior_depth: float
    spatial_quality: float
    temporal_control: float
    audience_relation: float
    contextual_fit: float
    voice_loss: float
    context_loss: float
    provenance_loss: float
    audience_shift: float
    representational_distortion: float
    governance_review: float
    text_image_integration: float
    image_sequence_logic: float
    sound_design_alignment: float
    rhythm_harmony: float
    provenance_visibility: float
    uncertainty_notation: float
    consent_clarity: float
    source_authority: float
    cultural_context: float
    reuse_boundaries: float
    synthetic_documentary_ambiguity: float
    provenance_opacity: float
    voice_likeness_imitation: float
    bias_reproduction: float
    human_review: float
    public_consequence: float
    owner: str = "editorial"
    status: str = "active"
    notes: str = ""
