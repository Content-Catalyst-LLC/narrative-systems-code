from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class MeaningArchitectureItem:
    item: str
    story_type: str
    origin_clarity: float
    sequence_clarity: float
    continuity_support: float
    rupture_recognition: float
    future_projection: float
    governance_visibility: float
    preservation: float
    archive_support: float
    repetition_strength: float
    context_retention: float
    transmission_strength: float
    evidence_strength: float
    source_age: float
    link_breakage: float
    audience_consequence: float
    representation_risk: float
    map_dependency: float
    owner: str
    status: str
