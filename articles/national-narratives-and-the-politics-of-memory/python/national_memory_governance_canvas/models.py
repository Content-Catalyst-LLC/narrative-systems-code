from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class NationalMemoryGovernanceConfig:
    article_title: str = "National Narratives and the Politics of Memory"
    article_slug: str = "national-narratives-and-the-politics-of-memory"
    medium_threshold: float = 0.45
    high_threshold: float = 0.62
    allowed_statuses: tuple[str, ...] = ("active", "archive", "review", "revise")


@dataclass(frozen=True)
class NationalMemoryGovernanceRecord:
    item: str
    claim_context: str
    group_representation: float
    source_diversity: float
    testimony_visibility: float
    archive_coverage: float
    countermemory_inclusion: float
    dissent_space: float
    hero_compression: float
    innocence_story: float
    exclusion_omission: float
    victimhood_monopoly: float
    purity_symbolism: float
    revision_capacity: float
    evidence_visibility: float
    provenance_reliability: float
    record_access: float
    testimony_care: float
    contextual_explanation: float
    repair_linkage: float
    curriculum_balance: float
    monument_context: float
    platform_context: float
    summary_dependence: float
    context_loss: float
    dominant_archive_bias: float
    uncertainty_erasure: float
    omission_of_minority_memory: float
    human_review: float
    public_consequence: float
    owner: str = "editorial"
    status: str = "active"
    notes: str = ""
