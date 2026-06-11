from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class PublicNarrativeGovernanceConfig:
    article_title: str = "Public Narrative and Social Change"
    article_slug: str = "public-narrative-and-social-change"
    medium_threshold: float = 0.45
    high_threshold: float = 0.62
    allowed_statuses: tuple[str, ...] = ("active", "archive", "review", "revise")


@dataclass(frozen=True)
class PublicNarrativeGovernanceRecord:
    item: str
    claim_context: str
    self_clarity: float
    us_clarity: float
    now_clarity: float
    value_articulation: float
    action_clarity: float
    governance_review: float
    diagnostic_frame: float
    proposed_solution: float
    resource_support: float
    coalition_openness: float
    tactical_action: float
    feedback_loop: float
    consent_deficit: float
    emotional_targeting: float
    safety_risk: float
    reuse_uncertainty: float
    visibility_risk: float
    agency: float
    voice_plurality: float
    affected_community_authority: float
    evidence_visibility: float
    digital_context: float
    summary_dependence: float
    omitted_voices: float
    context_loss: float
    bias_reproduction: float
    uncertainty_erasure: float
    human_review: float
    public_consequence: float
    owner: str = "editorial"
    status: str = "active"
    notes: str = ""
