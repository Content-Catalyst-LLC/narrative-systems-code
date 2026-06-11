from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class SerialNarrativeGovernanceConfig:
    article_title: str = "Serial Storytelling, Television, and Long-Form Narrative"
    article_slug: str = "serial-storytelling-television-and-long-form-narrative"
    medium_threshold: float = 0.45
    high_threshold: float = 0.62
    allowed_statuses: tuple[str, ...] = ("active", "archive", "review", "revise")


@dataclass(frozen=True)
class SerialNarrativeGovernanceRecord:
    item: str
    serial_context: str
    episode_function: float
    arc_progression: float
    thematic_development: float
    character_memory: float
    payoff_integrity_signal: float
    finale_consequence: float
    unresolved_arcs: float
    lore_density: float
    memory_expectation: float
    recap_uncertainty: float
    continuity_saturation: float
    audience_accessibility: float
    foreshadowing_support: float
    character_relevance: float
    emotional_payoff: float
    mystery_logic: float
    retrospective_coherence: float
    thematic_alignment: float
    ensemble_balance: float
    representation_depth: float
    trauma_care: float
    audience_trust: float
    generic_plotting: float
    continuity_fabrication: float
    memory_erasure: float
    payoff_simplification: float
    franchise_overextension: float
    human_review: float
    public_consequence: float
    owner: str = "editorial"
    status: str = "active"
    notes: str = ""
