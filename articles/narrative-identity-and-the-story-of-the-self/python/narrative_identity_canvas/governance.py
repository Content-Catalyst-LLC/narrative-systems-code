from hashlib import sha256
from .models import NarrativeIdentityConfig, NarrativeIdentityRecord
from .scoring import governance_priority_score, identity_story_risk, interpretation_readiness, narrative_coherence, review_priority, revision_readiness

def card_id(r,c): return sha256(f"{c.article_slug}|{r.item}|{r.claim_context}".encode()).hexdigest()[:16]
def governance_note(r,c):
    p=review_priority(r,c); notes=["High-priority narrative-identity governance review required." if p=="high" else "Medium-priority review recommended before reuse." if p=="medium" else "Standard editorial review sufficient."]
    if identity_story_risk(r)>=0.55: notes.append("Identity-story risk is elevated; review reduction forced coherence power blindness trauma extraction and algorithmic capture.")
    if interpretation_readiness(r)<0.60: notes.append("Interpretation readiness is limited; strengthen context method limits and review ownership.")
    if r.notes: notes.append(r.notes)
    return " ".join(notes)
def build_identity_card(r,c):
    return {"schema_version":"1.0.0","card_id":card_id(r,c),"card_type":"narrative_identity_story_of_self","article_title":c.article_title,"article_slug":c.article_slug,"item":r.item,"claim_context":r.claim_context,"scores":{"narrative_coherence":round(narrative_coherence(r),4),"revision_readiness":round(revision_readiness(r),4),"identity_story_risk":round(identity_story_risk(r),4),"interpretation_readiness":round(interpretation_readiness(r),4),"governance_priority_score":round(governance_priority_score(r,c),4)},"review":{"priority":review_priority(r,c),"owner":r.owner,"status":r.status,"governance_note":governance_note(r,c)}}
