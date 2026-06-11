from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class ComparativeStoryGovernanceConfig:
    article_title: str = "Storytelling in Comparative Perspective"
    article_slug: str = "storytelling-in-comparative-perspective"
    medium_threshold: float = 0.45
    high_threshold: float = 0.62
    allowed_statuses: tuple[str, ...] = ("active", "archive", "review", "revise")


@dataclass(frozen=True)
class ComparativeStoryGovernanceRecord:
    item: str
    comparison_context: str
    source_context: float
    difference_preservation: float
    evidence_quality: float
    translation_reliability: float
    protocol_compliance: float
    human_review: float
    universalism_claims: float
    template_capture: float
    context_loss: float
    archive_bias: float
    power_imbalance: float
    language_gap: float
    media_shift: float
    archive_gap: float
    performance_loss: float
    restricted_source_concern: float
    version_documentation: float
    local_interpretation: float
    community_review: float
    attribution_quality: float
    corpus_balance: float
    biased_corpus: float
    hallucinated_source_risk: float
    ai_translation_loss: float
    sacred_material_risk: float
    overgeneralized_claims: float
    expert_review: float
    public_consequence: float
    owner: str = "editorial"
    status: str = "active"
    notes: str = ""
