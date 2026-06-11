from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class FragmentedNarrativeConfig:
    article_title: str = "Memory, Trauma, and Fragmented Narrative"
    article_slug: str = "memory-trauma-and-fragmented-narrative"
    medium_threshold: float = 0.45
    high_threshold: float = 0.62
    allowed_statuses: tuple[str, ...] = ("active", "archive", "review", "revise")


@dataclass(frozen=True)
class FragmentedNarrativeRecord:
    item: str
    claim_context: str
    temporal_rupture: float
    gap_marking: float
    repetition_patterning: float
    silence_respect: float
    uncertainty_notes: float
    contextual_care: float
    consent: float
    agency: float
    privacy: float
    relational_context: float
    safety_framing: float
    boundary_discipline: float
    forced_coherence: float
    redemptive_shortcut: float
    extraction_risk: float
    identity_reduction: float
    spectacle_pressure: float
    method_limits: float
    source_context: float
    cultural_context: float
    ethics_governance: float
    review_owner_clarity: float
    public_consequence: float
    owner: str = "editorial"
    status: str = "active"
    notes: str = ""
