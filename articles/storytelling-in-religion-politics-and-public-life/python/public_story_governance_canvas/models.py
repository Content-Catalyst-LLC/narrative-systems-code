from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class PublicStoryGovernanceConfig:
    article_title: str = "Storytelling in Religion, Politics, and Public Life"
    article_slug: str = "storytelling-in-religion-politics-and-public-life"
    medium_threshold: float = 0.45
    high_threshold: float = 0.62
    allowed_statuses: tuple[str, ...] = ("active", "archive", "review", "revise")


@dataclass(frozen=True)
class PublicStoryGovernanceRecord:
    item: str
    claim_context: str
    self_story_evidence: float
    shared_value_clarity: float
    now_challenge_clarity: float
    agency: float
    hope: float
    responsibility: float
    enemy_simplification: float
    boundary_hardening: float
    crisis_compression: float
    urgency_pressure: float
    scapegoat_intensity: float
    evidence_visibility: float
    memory_plurality: float
    historical_truthfulness: float
    public_limit_clarity: float
    dissent_space: float
    repair_justice: float
    anti_idolatry_critique: float
    witness_care: float
    testimony_context: float
    harm_visibility: float
    extraction_resistance: float
    formulaic_default: float
    outrage_intensity: float
    resolution_smoothing: float
    identity_boundary_pressure: float
    context_missingness: float
    human_governance: float
    public_consequence: float
    owner: str = "editorial"
    status: str = "active"
    notes: str = ""
