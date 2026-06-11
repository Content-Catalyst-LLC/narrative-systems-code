from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class NarratologyConfig:
    article_title: str = "Narratology and the Grammar of Story"
    article_slug: str = "narratology-and-the-grammar-of-story"
    medium_threshold: float = 0.45
    high_threshold: float = 0.62
    allowed_statuses: tuple[str, ...] = ("active", "archive", "review", "revise")


@dataclass(frozen=True)
class NarratologyRecord:
    item: str
    claim_context: str
    story_discourse_clarity: float
    voice_clarity: float
    focalization_clarity: float
    temporal_mapping: float
    character_agency_mapping: float
    information_control_analysis: float
    perspective_shifts: float
    knowledge_restriction: float
    interior_access: float
    source_hierarchy: float
    multiple_focalizers: float
    analepsis: float
    prolepsis: float
    ellipsis: float
    duration_variation: float
    repetition_frequency: float
    omission_risk: float
    power_blindness: float
    voice_imbalance: float
    closure_pressure: float
    unreliable_framing_risk: float
    method_limits: float
    source_context: float
    counterexamples: float
    uncertainty_notes: float
    owner: str = "editorial"
    status: str = "active"
    notes: str = ""
