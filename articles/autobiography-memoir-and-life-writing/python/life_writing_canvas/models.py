from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class LifeWritingConfig:
    article_title: str = "Autobiography, Memoir, and Life-Writing"
    article_slug: str = "autobiography-memoir-and-life-writing"
    medium_threshold: float = 0.45
    high_threshold: float = 0.62
    allowed_statuses: tuple[str, ...] = ("active", "archive", "review", "revise")


@dataclass(frozen=True)
class LifeWritingRecord:
    item: str
    claim_context: str
    memory_clarity: float
    temporal_structure: float
    voice_consistency: float
    agency: float
    relational_grounding: float
    contextual_depth: float
    fact_checking: float
    memory_framing: float
    evidence_visibility: float
    interpretation_distinction: float
    uncertainty_notes: float
    archive_review: float
    privacy_risk: float
    consent_limits: float
    other_person_exposure: float
    trauma_extraction: float
    self_mythology: float
    method_limits: float
    source_context: float
    cultural_context: float
    review_owner_clarity: float
    public_consequence: float
    owner: str = "editorial"
    status: str = "active"
    notes: str = ""
