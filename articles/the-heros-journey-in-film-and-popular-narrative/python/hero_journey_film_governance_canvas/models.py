from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class HeroJourneyFilmGovernanceConfig:
    article_title: str = "The Hero’s Journey in Film and Popular Narrative"
    article_slug: str = "the-heros-journey-in-film-and-popular-narrative"
    medium_threshold: float = 0.45
    high_threshold: float = 0.62
    allowed_statuses: tuple[str, ...] = ("active", "archive", "review", "revise")


@dataclass(frozen=True)
class HeroJourneyFilmGovernanceRecord:
    item: str
    film_context: str
    call_authenticity: float
    threshold_significance: float
    ordeal_relevance: float
    value_change: float
    return_boon: float
    ethical_consequence: float
    beat_compliance: float
    generic_mentor: float
    mechanical_call: float
    ordeal_spectacle: float
    forced_return: float
    story_particularity: float
    visual_motif: float
    sound_design: float
    editing_rhythm: float
    performance_shift: float
    blocking_change: float
    mise_en_scene: float
    collective_agency: float
    cultural_specificity: float
    gender_complexity: float
    nonheroic_alternatives: float
    stage_compliance: float
    cultural_loss: float
    genre_cliche: float
    universalist_pressure: float
    trope_recycling: float
    human_review: float
    public_consequence: float
    owner: str = "editorial"
    status: str = "active"
    notes: str = ""
