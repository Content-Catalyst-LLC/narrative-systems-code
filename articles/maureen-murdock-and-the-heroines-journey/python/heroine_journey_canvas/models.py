from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class HeroineJourneyConfig:
    article_title: str = "Maureen Murdock and the Heroine's Journey"
    article_slug: str = "maureen-murdock-and-the-heroines-journey"
    medium_threshold: float = 0.45
    high_threshold: float = 0.62
    allowed_statuses: tuple[str, ...] = ("active", "archive", "review", "revise")


@dataclass(frozen=True)
class HeroineJourneyRecord:
    item: str
    claim_context: str
    separation_from_feminine: float
    masculine_identification: float
    aridity_after_success: float
    descent_crisis: float
    reconnection_feminine: float
    integration_wholeness: float
    template_forcing: float
    gender_essentialism: float
    universal_womanhood: float
    psychological_overreach: float
    healing_pressure: float
    cultural_context: float
    source_context: float
    alternative_lens: float
    gender_complexity: float
    uncertainty_notes: float
    review_owner_clarity: float
    agency: float
    relational_grounding: float
    embodiment: float
    healthy_power: float
    emotional_maturity: float
    open_process: float
    public_consequence: float
    owner: str = "editorial"
    status: str = "active"
    notes: str = ""
