from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class PlotCoherenceItem:
    item: str
    story_type: str
    action_clarity: float
    causal_linkage: float
    motivation_visibility: float
    episode_dependency: float
    turning_point_strength: float
    resolution_consequence: float
    state_change: float
    knowledge_change: float
    pressure_change: float
    relationship_impact: float
    future_movement: float
    false_causality: float
    simplification_bias: float
    closure_pressure: float
    evidence_omission: float
    uncertainty_clarity: float
    audience_sensitivity: float
    public_consequence: float
    owner: str
    status: str
