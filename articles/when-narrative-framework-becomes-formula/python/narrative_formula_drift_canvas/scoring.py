from __future__ import annotations
from statistics import mean
from .models import NarrativeFormulaDriftConfig, NarrativeFormulaDriftRecord

def formula_drift(r: NarrativeFormulaDriftRecord) -> float:
    return min(1.0, r.template_forcing*0.20 + r.beat_rigidity*0.18 + r.closure_pressure*0.18 + r.universality_pressure*0.16 + r.automation_dependence*0.14 + (1-r.story_specificity)*0.14)

def framework_health(r: NarrativeFormulaDriftRecord) -> float:
    return mean([r.scope_clarity, r.context_sensitivity, r.alternative_lenses, r.refusal_monitoring, r.ethical_governance, r.human_judgment])

def narrative_specificity(r: NarrativeFormulaDriftRecord) -> float:
    return mean([r.voice_originality, r.place_logic, r.temporal_method, r.material_detail, r.relational_logic, r.cultural_specificity])

def ai_template_risk(r: NarrativeFormulaDriftRecord) -> float:
    return min(1.0, r.default_arc_use*0.18 + r.generic_phrasing*0.18 + r.heroic_arc_pressure*0.18 + r.market_story_pressure*0.16 + r.resolution_smoothing*0.16 + (1-r.variant_comparison)*0.14)

def governance_priority_score(r: NarrativeFormulaDriftRecord, c: NarrativeFormulaDriftConfig) -> float:
    score = formula_drift(r)*0.32 + ai_template_risk(r)*0.24 + (1-framework_health(r))*0.16 + (1-narrative_specificity(r))*0.12 + r.public_consequence*0.16
    if r.status == "revise":
        score = max(score, c.high_threshold)
    elif r.status == "review":
        score = max(score, c.medium_threshold)
    return min(1.0, max(0.0, score))

def review_priority(r: NarrativeFormulaDriftRecord, c: NarrativeFormulaDriftConfig) -> str:
    score = governance_priority_score(r, c)
    if score >= c.high_threshold:
        return "high"
    if score >= c.medium_threshold:
        return "medium"
    return "standard"
