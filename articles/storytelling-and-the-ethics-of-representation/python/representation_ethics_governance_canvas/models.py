from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class RepresentationEthicsGovernanceConfig:
    article_title: str = "Storytelling and the Ethics of Representation"
    article_slug: str = "storytelling-and-the-ethics-of-representation"
    medium_threshold: float = 0.45
    high_threshold: float = 0.62
    allowed_statuses: tuple[str, ...] = ("active", "archive", "review", "revise")


@dataclass(frozen=True)
class RepresentationEthicsGovernanceRecord:
    item: str
    representation_context: str
    voice_agency: float
    context_preservation: float
    dignity_protection: float
    source_accuracy: float
    provenance_visibility: float
    accountability_capacity: float
    stereotype_tendency: float
    exposure_risk: float
    context_loss: float
    voice_replacement: float
    power_asymmetry: float
    governance_review: float
    informed_consent: float
    ongoing_consent: float
    use_clarity: float
    platform_circulation_clarity: float
    withdrawal_clarity: float
    reuse_ai_clarity: float
    cultural_protocols: float
    community_review: float
    attribution_quality: float
    image_context: float
    visual_dignity: float
    caption_accuracy: float
    synthetic_opacity: float
    likeness_imitation: float
    cultural_fabrication: float
    provenance_loss: float
    evidence_confusion: float
    human_review: float
    public_consequence: float
    owner: str = "editorial"
    status: str = "active"
    notes: str = ""
