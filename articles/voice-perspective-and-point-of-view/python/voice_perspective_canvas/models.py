from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class VoicePerspectiveItem:
    item: str
    story_type: str
    tone_stability: float
    diction_coherence: float
    rhetorical_habit: float
    address_stability: float
    judgment_coherence: float
    knowledge_limits: float
    interior_access: float
    focalization_clarity: float
    level_stability: float
    source_boundaries: float
    factual_unreliability: float
    interpretive_unreliability: float
    ethical_unreliability: float
    memory_distortion: float
    agency_gap: float
    exposure_sensitivity: float
    public_consequence: float
    representation_gap: float
    institutional_evasion: float
    owner: str
    status: str
