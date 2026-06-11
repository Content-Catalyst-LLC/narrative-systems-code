from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class OrganizationalStoryGovernanceConfig:
    article_title: str = "Organizational Storytelling, Purpose, and Change"
    article_slug: str = "organizational-storytelling-purpose-and-change"
    medium_threshold: float = 0.45
    high_threshold: float = 0.62
    allowed_statuses: tuple[str, ...] = ("active", "archive", "review", "revise")


@dataclass(frozen=True)
class OrganizationalStoryGovernanceRecord:
    item: str
    claim_context: str
    mission_clarity: float
    decision_alignment: float
    budget_fit: float
    stakeholder_impact: float
    employee_experience: float
    governance_transparency: float
    evidence_visibility: float
    participation_integrity: float
    resource_support: float
    loss_acknowledgment: float
    feedback_loops: float
    accountability_measures: float
    consent_deficit: float
    selection_bias: float
    power_asymmetry: float
    emotional_targeting: float
    brand_repurposing: float
    agency: float
    employee_voice_protection: float
    dissent_visibility: float
    memory_preservation: float
    learning_followthrough: float
    summary_dependence: float
    omitted_dissent: float
    context_loss: float
    privacy_risk: float
    uncertainty_erasure: float
    human_review: float
    public_consequence: float
    owner: str = "editorial"
    status: str = "active"
    notes: str = ""
