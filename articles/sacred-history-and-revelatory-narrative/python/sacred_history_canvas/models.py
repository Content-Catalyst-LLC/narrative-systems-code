from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class SacredHistoryConfig:
    article_title: str = "Sacred History and Revelatory Narrative"
    article_slug: str = "sacred-history-and-revelatory-narrative"
    medium_threshold: float = 0.45
    high_threshold: float = 0.62
    allowed_statuses: tuple[str, ...] = ("active", "archive", "review", "revise")


@dataclass(frozen=True)
class SacredHistoryRecord:
    item: str
    claim_context: str
    sacred_disclosure: float
    event_meaning: float
    authority_clarity: float
    obligation: float
    transformation: float
    communal_memory: float
    historical_context: float
    memory_depth: float
    ritual_transmission: float
    interpretive_authority: float
    ethical_governance: float
    public_responsibility: float
    sacred_certainty: float
    omission_risk: float
    political_sanctification: float
    exclusion_risk: float
    historical_flattening: float
    uncertainty_marking: float
    source_context: float
    authority_notes: float
    counterexamples: float
    method_limits: float
    owner: str = "editorial"
    status: str = "active"
    notes: str = ""
