from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class DigitalStorytellingGovernanceConfig:
    article_title: str = "Digital Storytelling and Platform Culture"
    article_slug: str = "digital-storytelling-and-platform-culture"
    medium_threshold: float = 0.45
    high_threshold: float = 0.62
    allowed_statuses: tuple[str, ...] = ("active", "archive", "review", "revise")


@dataclass(frozen=True)
class DigitalStorytellingGovernanceRecord:
    item: str
    platform_context: str
    context_preservation: float
    source_authority: float
    visibility_provenance_fit: float
    audience_care: float
    medium_format_fit: float
    ethical_governance: float
    audience_spread: float
    compression_severity: float
    hostile_context_exposure: float
    engagement_intensity: float
    sensitive_visibility: float
    governance_review: float
    hook_overdependence: float
    trend_compliance: float
    metric_pressure: float
    retention_framing: float
    outrage_signaling: float
    judgment_stability: float
    archive_metadata: float
    consent_status: float
    preservation_plan: float
    access_context: float
    synthetic_opacity: float
    voice_imitation: float
    provenance_loss: float
    ai_context_loss: float
    manipulation_targeting: float
    human_review: float
    public_consequence: float
    owner: str = "editorial"
    status: str = "active"
    notes: str = ""
