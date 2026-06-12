from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class NarrativeRiskGovernanceConfig:
    article_title: str = "Narrative Risk and the Misuse of Story"
    article_slug: str = "narrative-risk-and-the-misuse-of-story"
    medium_threshold: float = 0.45
    high_threshold: float = 0.62
    allowed_statuses: tuple[str, ...] = ("active", "archive", "review", "revise")


@dataclass(frozen=True)
class NarrativeRiskGovernanceRecord:
    item: str
    narrative_context: str
    scapegoating: float
    evidence_immunity: float
    mythic_simplification: float
    context_loss: float
    group_blame_intensity: float
    revision_openness: float
    corroboration: float
    source_quality: float
    timeline_clarity: float
    uncertainty_disclosure: float
    accountability_clarity: float
    disconfirmation_openness: float
    institutional_failure: float
    opacity: float
    historical_distrust_reason: float
    public_consequence: float
    correction_difficulty: float
    affected_listener_stakes: float
    platform_speed: float
    repetition_intensity: float
    social_proof_pressure: float
    monetization_pressure: float
    synthetic_evidence: float
    provenance_opacity: float
    fabricated_patterning: float
    automated_consensus: float
    vulnerability_targeting: float
    human_review: float
    owner: str = "editorial"
    status: str = "active"
    notes: str = ""
