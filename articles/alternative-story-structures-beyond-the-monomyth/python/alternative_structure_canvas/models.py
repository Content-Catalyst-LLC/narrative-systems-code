from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class AlternativeStructureConfig:
    article_title: str = "Alternative Story Structures Beyond the Monomyth"
    article_slug: str = "alternative-story-structures-beyond-the-monomyth"
    medium_threshold: float = 0.45
    high_threshold: float = 0.62
    allowed_statuses: tuple[str, ...] = ("active", "archive", "review", "revise")


@dataclass(frozen=True)
class AlternativeStructureRecord:
    item: str
    claim_context: str
    arc_signal: float
    cycle_signal: float
    braid_signal: float
    mosaic_signal: float
    network_signal: float
    relational_signal: float
    fragment_signal: float
    hero_forcing: float
    conflict_substitution: float
    return_pressure: float
    individualization_pressure: float
    template_forcing: float
    evidence_visibility: float
    source_context: float
    method_limits: float
    alternative_lens: float
    cultural_context: float
    uncertainty_notes: float
    review_owner_clarity: float
    temporal_match: float
    agency_design: float
    pacing_compatibility: float
    sequence_logic: float
    interaction_affordance: float
    experiential_coherence: float
    public_consequence: float
    owner: str = "editorial"
    status: str = "active"
    notes: str = ""
