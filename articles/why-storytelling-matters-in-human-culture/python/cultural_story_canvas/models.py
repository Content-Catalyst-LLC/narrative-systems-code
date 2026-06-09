from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class CulturalStoryItem:
    item: str
    story_type: str
    cultural_context: str
    memory_function: float
    teaching_value: float
    identity_function: float
    belonging_function: float
    moral_imagination: float
    social_coordination: float
    transmission_strength: float
    source_transparency: float
    representation_care: float
    persuasive_intensity: float
    audience_consequence: float
    public_impact: float
    owner: str
    status: str
