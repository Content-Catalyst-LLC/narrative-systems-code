from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class PatternConfig:
    article_title: str = "Creation, Flood, Exile, and Return as Narrative Patterns"
    article_slug: str = "creation-flood-exile-and-return-as-narrative-patterns"
    medium_threshold: float = 0.45
    high_threshold: float = 0.62
    allowed_statuses: tuple[str, ...] = ("active", "archive", "review", "revise")


@dataclass(frozen=True)
class NarrativePatternRecord:
    item: str
    claim_context: str
    creation_signal: float
    flood_signal: float
    exile_signal: float
    return_signal: float
    memory_maintenance: float
    repair_responsibility: float
    source_context: float
    historical_context: float
    counterexamples: float
    method_limits: float
    ethics_governance: float
    uncertainty_notes: float
    origin_nostalgia: float
    cleansing_fantasy: float
    exile_romanticization: float
    false_return: float
    power_blindness: float
    public_consequence: float
    owner: str = "editorial"
    status: str = "active"
    notes: str = ""
