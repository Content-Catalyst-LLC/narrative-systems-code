from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class PublicStoryItem:
    item: str
    story_type: str
    ethos_strength: float
    logos_support: float
    pathos_proportionality: float
    audience_fit: float
    context_clarity: float
    identification_strength: float
    emotional_intensity: float
    causal_clarity: float
    urgency: float
    action_clarity: float
    verification_strength: float
    emotional_coercion: float
    scapegoating_risk: float
    identity_manipulation: float
    closure_pressure: float
    audience_consequence: float
    representation_sensitivity: float
    owner: str
    status: str
