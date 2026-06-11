from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class InstitutionalMemoryGovernanceConfig:
    article_title: str = "Origin Stories, Legitimacy, and Institutional Memory"
    article_slug: str = "origin-stories-legitimacy-and-institutional-memory"
    medium_threshold: float = 0.45
    high_threshold: float = 0.62
    allowed_statuses: tuple[str, ...] = ("active", "archive", "review", "revise")


@dataclass(frozen=True)
class InstitutionalMemoryGovernanceRecord:
    item: str
    claim_context: str
    purpose_clarity: float
    mission_action_alignment: float
    record_evidence: float
    affected_community_testimony: float
    conduct_visibility: float
    governance_openness: float
    founder_heroization: float
    exclusion_omission: float
    harm_removal: float
    commemoration_saturation: float
    reputational_branding: float
    voice_multiplicity: float
    record_preservation: float
    archive_completeness: float
    metadata_quality: float
    testimony_stewardship: float
    knowledge_retention: float
    public_access: float
    harm_naming: float
    structural_change: float
    evidence_release: float
    material_repair: float
    oversight: float
    transparent_progress: float
    ai_summary_dependence: float
    archive_bias_risk: float
    context_loss: float
    correction_pathway: float
    public_consequence: float
    owner: str = "editorial"
    status: str = "active"
    notes: str = ""
