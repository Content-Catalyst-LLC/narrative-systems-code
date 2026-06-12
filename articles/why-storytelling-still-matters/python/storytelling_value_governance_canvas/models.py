from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class StorytellingValueGovernanceConfig:
    article_title: str = "Why Storytelling Still Matters"
    article_slug: str = "why-storytelling-still-matters"
    medium_threshold: float = 0.45
    high_threshold: float = 0.62
    allowed_statuses: tuple[str, ...] = ("active", "archive", "review", "revise")


@dataclass(frozen=True)
class StorytellingValueGovernanceRecord:
    item: str
    story_context: str
    clarity: float
    evidence_grounding: float
    memory_continuity: float
    audience_reasoning: float
    dignity_protection: float
    public_usefulness: float
    truthfulness: float
    context_adequacy: float
    consent_discipline: float
    uncertainty_disclosure: float
    revision_openness: float
    accountability: float
    oversimplification: float
    emotional_exploitation: float
    scapegoating: float
    context_loss: float
    platform_frictionlessness: float
    human_review: float
    provenance_visibility: float
    source_traceability: float
    ai_human_review: float
    ai_consent_discipline: float
    use_limit_clarity: float
    correction_process: float
    cultural_context: float
    ethical_stakes: float
    owner: str = "editorial"
    status: str = "active"
    notes: str = ""
