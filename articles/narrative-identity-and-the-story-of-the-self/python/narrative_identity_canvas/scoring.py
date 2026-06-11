from statistics import mean
from .models import NarrativeIdentityConfig, NarrativeIdentityRecord

def narrative_coherence(r): return mean([r.memory_continuity,r.temporal_progression,r.agency,r.relational_grounding,r.promise_responsibility,r.future_openness])
def revision_readiness(r): return mean([r.change_handling,r.memory_revision,r.uncertainty_notes,r.counter_memory,r.silence_respect,r.openness_to_retelling])
def identity_story_risk(r): return min(1.0, r.reduction_risk*0.18+r.forced_coherence*0.20+r.power_blindness*0.18+r.trauma_extraction*0.18+r.algorithmic_capture*0.16+(1-r.cultural_context)*0.10)
def interpretation_readiness(r): return mean([r.source_context,r.cultural_context,r.method_limits,r.uncertainty_notes,r.ethics_governance,r.review_owner_clarity])
def governance_priority_score(r, c):
    score=identity_story_risk(r)*0.40+(1-interpretation_readiness(r))*0.28+r.public_consequence*0.16+(1-revision_readiness(r))*0.16
    if r.status=="revise": score=max(score,c.high_threshold)
    if r.status=="review": score=max(score,c.medium_threshold)
    return min(1.0,max(0.0,score))
def review_priority(r,c):
    score=governance_priority_score(r,c)
    return "high" if score>=c.high_threshold else "medium" if score>=c.medium_threshold else "standard"
