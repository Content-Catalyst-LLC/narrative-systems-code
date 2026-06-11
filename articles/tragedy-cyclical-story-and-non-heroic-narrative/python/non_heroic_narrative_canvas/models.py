from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class NonHeroicNarrativeConfig:
    article_title: str = "Tragedy, Cyclical Story, and Non-Heroic Narrative"
    article_slug: str = "tragedy-cyclical-story-and-non-heroic-narrative"
    medium_threshold: float = 0.45
    high_threshold: float = 0.62
    allowed_statuses: tuple[str, ...] = ("active", "archive", "review", "revise")


@dataclass(frozen=True)
class NonHeroicNarrativeRecord:
    item: str
    claim_context: str
    consequential_action: float
    limit_pressure: float
    reversal: float
    recognition_knowledge: float
    irreversibility: float
    witness_burden: float
    repeated_pattern: float
    seasonal_ritual_signal: float
    generational_transmission: float
    institutional_habit: float
    ecological_feedback: float
    variation_across_return: float
    care: float
    endurance: float
    witness: float
    refusal: float
    maintenance: float
    survival: float
    hero_forcing: float
    victory_pressure: float
    closure_pressure: float
    return_pressure: float
    growth_pressure: float
    evidence_visibility: float
    public_consequence: float
    source_context: float
    method_limits: float
    uncertainty_notes: float
    review_owner_clarity: float
    owner: str = "editorial"
    status: str = "active"
    notes: str = ""
