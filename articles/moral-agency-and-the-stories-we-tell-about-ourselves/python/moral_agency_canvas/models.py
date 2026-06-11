from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class MoralAgencyConfig:
    article_title: str = "Moral Agency and the Stories We Tell About Ourselves"
    article_slug: str = "moral-agency-and-the-stories-we-tell-about-ourselves"
    medium_threshold: float = 0.45
    high_threshold: float = 0.62
    allowed_statuses: tuple[str, ...] = ("active", "archive", "review", "revise")


@dataclass(frozen=True)
class MoralAgencyRecord:
    item: str
    claim_context: str
    action_naming: float
    intention_distinction: float
    consequence_clarity: float
    harm_marking: float
    repair_orientation: float
    other_visibility: float
    context_overuse: float
    intention_shielding: float
    victimhood_shielding: float
    blame_shifting: float
    growth_substitution: float
    harm_minimization: float
    harm_acknowledgment: float
    apology_precision: float
    material_response: float
    conduct_change: float
    future_accountability: float
    third_party_oversight: float
    source_context: float
    evidence_visibility: float
    uncertainty_notes: float
    cultural_context: float
    method_limits: float
    review_owner_clarity: float
    public_consequence: float
    owner: str = "editorial"
    status: str = "active"
    notes: str = ""
