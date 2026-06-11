from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class UniversalStoryModelConfig:
    article_title: str = "Gender, Critique, and the Limits of Universal Story Models"
    article_slug: str = "gender-critique-and-the-limits-of-universal-story-models"
    medium_threshold: float = 0.45
    high_threshold: float = 0.62
    allowed_statuses: tuple[str, ...] = ("active", "archive", "review", "revise")


@dataclass(frozen=True)
class UniversalStoryModelRecord:
    item: str
    claim_context: str
    stage_evidence: float
    agency_match: float
    transformation_correspondence: float
    contextual_harmony: float
    resolution_similarity: float
    evidence_visibility: float
    archive_bias: float
    gender_binary_pressure: float
    cultural_flattening: float
    intersectional_erasure: float
    queer_trans_pressure: float
    local_context: float
    source_context: float
    alternative_lens: float
    gender_complexity: float
    intersectional_context: float
    uncertainty_notes: float
    review_owner_clarity: float
    relational_motion: float
    cyclical_form: float
    witness_structure: float
    care_labor: float
    fragmented_form: float
    open_process: float
    public_consequence: float
    owner: str = "editorial"
    status: str = "active"
    notes: str = ""
