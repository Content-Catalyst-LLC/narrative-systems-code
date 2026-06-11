from __future__ import annotations
from dataclasses import dataclass

@dataclass(frozen=True)
class NarrativeFormulaDriftConfig:
    article_title: str = "When Narrative Framework Becomes Formula"
    article_slug: str = "when-narrative-framework-becomes-formula"
    medium_threshold: float = 0.45
    high_threshold: float = 0.62
    allowed_statuses: tuple[str, ...] = ("active", "archive", "review", "revise")

@dataclass(frozen=True)
class NarrativeFormulaDriftRecord:
    item: str
    claim_context: str
    template_forcing: float
    beat_rigidity: float
    closure_pressure: float
    universality_pressure: float
    automation_dependence: float
    story_specificity: float
    scope_clarity: float
    context_sensitivity: float
    alternative_lenses: float
    refusal_monitoring: float
    ethical_governance: float
    human_judgment: float
    voice_originality: float
    place_logic: float
    temporal_method: float
    material_detail: float
    relational_logic: float
    cultural_specificity: float
    default_arc_use: float
    generic_phrasing: float
    heroic_arc_pressure: float
    market_story_pressure: float
    resolution_smoothing: float
    variant_comparison: float
    public_consequence: float
    owner: str = "editorial"
    status: str = "active"
    notes: str = ""
