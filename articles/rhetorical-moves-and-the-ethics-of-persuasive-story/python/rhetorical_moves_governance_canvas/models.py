from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class RhetoricalMovesGovernanceConfig:
    article_title: str = "Rhetorical Moves and the Ethics of Persuasive Story"
    article_slug: str = "rhetorical-moves-and-the-ethics-of-persuasive-story"
    medium_threshold: float = 0.45
    high_threshold: float = 0.62
    allowed_statuses: tuple[str, ...] = ("active", "archive", "review", "revise")


@dataclass(frozen=True)
class RhetoricalMovesGovernanceRecord:
    item: str
    persuasion_context: str
    evidence_truthfulness: float
    proportionality: float
    context_adequacy: float
    dignity_protection: float
    audience_agency: float
    transparency: float
    fear_amplification: float
    emotional_exploitation: float
    omission_of_context: float
    social_proof_pressure: float
    urgency_coercion: float
    judgment_review: float
    claim_clarity: float
    uncertainty_disclosure: float
    tradeoff_openness: float
    evidence_visibility: float
    response_optionality: float
    question_space: float
    platform_amplification: float
    microtargeting_intensity: float
    context_collapse_risk: float
    sponsorship_clarity: float
    personalization_targeting: float
    vulnerability_exploitation: float
    synthetic_evidence_risk: float
    opaque_testing: float
    data_opacity: float
    human_review: float
    public_consequence: float
    owner: str = "editorial"
    status: str = "active"
    notes: str = ""
