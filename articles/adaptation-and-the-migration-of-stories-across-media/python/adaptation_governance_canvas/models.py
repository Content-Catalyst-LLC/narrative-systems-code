from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class AdaptationGovernanceConfig:
    article_title: str = "Adaptation and the Migration of Stories Across Media"
    article_slug: str = "adaptation-and-the-migration-of-stories-across-media"
    medium_threshold: float = 0.45
    high_threshold: float = 0.62
    allowed_statuses: tuple[str, ...] = ("active", "archive", "review", "revise")


@dataclass(frozen=True)
class AdaptationGovernanceRecord:
    item: str
    adaptation_context: str
    source_core_preservation: float
    medium_fit: float
    transformation_purpose: float
    context_preservation: float
    reception_value: float
    ethical_governance: float
    voice_loss: float
    interiority_loss: float
    context_loss: float
    provenance_loss: float
    agency_loss: float
    governance_review: float
    repetition_compliance: float
    lore_excess: float
    nostalgia_reliance: float
    continuity_saturation: float
    market_overextension: float
    story_purpose: float
    plot_summary_dependence: float
    voice_style_imitation: float
    synthetic_opacity: float
    uncertainty_erasure: float
    human_review: float
    consent_clarity: float
    source_authority: float
    cultural_context: float
    public_consequence: float
    owner: str = "editorial"
    status: str = "active"
    notes: str = ""
