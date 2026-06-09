from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class StoryItem:
    item: str
    story_type: str
    description: str
    sequence_clarity: float
    agency_clarity: float
    causal_connection: float
    conflict_definition: float
    transformation_clarity: float
    motif_use: float
    interpretive_relevance: float
    evidence_strength: float
    representation_care: float
    persuasive_intensity: float
    audience_consequence: float
    owner: str
    status: str
