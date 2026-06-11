from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class LegalNarrativeResponsibilityConfig:
    article_title: str = "Law, Evidence, and Narrative Responsibility"
    article_slug: str = "law-evidence-and-narrative-responsibility"
    medium_threshold: float = 0.45
    high_threshold: float = 0.62
    allowed_statuses: tuple[str, ...] = ("active", "archive", "review", "revise")


@dataclass(frozen=True)
class LegalNarrativeResponsibilityRecord:
    item: str
    claim_context: str
    relevance: float
    authentication: float
    provenance: float
    corroboration: float
    cross_checking: float
    uncertainty_notation: float
    overcoherence: float
    evidentiary_gap: float
    stereotype_reliance: float
    causation_flattening: float
    affective_bias: float
    uncertainty_visibility: float
    opportunity_to_be_heard: float
    discovery_access: float
    testimony_context: float
    record_access: float
    correction_pathway: float
    procedural_posture_clarity: float
    witness_dignity: float
    testimony_care: float
    role_complexity: float
    remedy_connection: float
    hallucinated_authority: float
    summary_dependence: float
    context_loss: float
    procedural_distortion: float
    bias_reproduction: float
    human_review: float
    public_consequence: float
    owner: str = "editorial"
    status: str = "active"
    notes: str = ""
