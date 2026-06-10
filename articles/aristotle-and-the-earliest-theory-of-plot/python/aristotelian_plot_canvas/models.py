from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class PlotItem:
    item: str
    story_type: str
    action_clarity: float
    causal_linkage: float
    episode_dependency: float
    turning_point_relevance: float
    resolution_support: float
    goal_coherence: float
    direction_change: float
    knowledge_change: float
    preparation_strength: float
    consequence_pressure: float
    emotional_intellectual_impact: float
    character_action_integration: float
    genre_fit: float
    medium_fit: float
    cultural_awareness: float
    hero_template_saturation: float
    closure_pressure: float
    unity_bias: float
    genre_bias: float
    owner: str
    status: str
