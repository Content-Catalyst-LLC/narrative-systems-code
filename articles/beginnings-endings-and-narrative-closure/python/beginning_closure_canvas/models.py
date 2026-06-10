from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class BeginningClosureItem:
    item: str
    story_type: str
    voice_signal: float
    world_orientation: float
    pressure_introduction: float
    stakes_visibility: float
    question_framing: float
    contract_transparency: float
    promise_fulfillment: float
    resolution_suitability: float
    transformation_depth: float
    aftermath_clarity: float
    emotional_honesty: float
    unresolved_harm_honesty: float
    motif_return: float
    question_answer: float
    interpretive_echo: float
    thematic_continuity: float
    frame_revision: float
    premature_repair: float
    false_resolution: float
    system_flattening: float
    aftermath_omission: float
    excessive_audience_comfort: float
    audience_sensitivity: float
    public_consequence: float
    owner: str
    status: str
