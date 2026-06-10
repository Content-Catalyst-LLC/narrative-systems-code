from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class ConflictTensionItem:
    item: str
    story_type: str
    desire_clarity: float
    obstacle_clarity: float
    pressure_strength: float
    agency_visibility: float
    stakes_visibility: float
    relation_legibility: float
    unresolved_pressure: float
    meaningful_delay: float
    stakes_heightening: float
    expectation_pressure: float
    complication_movement: float
    state_change: float
    knowledge_change: float
    relationship_impact: float
    pressure_change: float
    future_movement: float
    value_transformation: float
    scapegoating: float
    conflict_inflation: float
    trauma_spectacle: float
    false_balance: float
    closure_pressure: float
    audience_sensitivity: float
    public_consequence: float
    owner: str
    status: str
