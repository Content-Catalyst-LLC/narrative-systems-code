from hashlib import sha256
from .models import CanvasConfig, CanvasRecord
from .scoring import confidence_band, domain_strength, governance_priority_score, interpretation_readiness, review_priority, risk_score

def _id(record, config): return sha256(f"{config.article_slug}|{record.item}|{record.claim_context}".encode()).hexdigest()[:16]
def governance_note(record: CanvasRecord, config: CanvasConfig):
    p = review_priority(record, config)
    notes = ["High-priority governance review required." if p == "high" else "Medium-priority editorial review recommended." if p == "medium" else "Standard review sufficient."]
    if risk_score(record, config) >= 0.60: notes.append("Risk signals are elevated.")
    if interpretation_readiness(record, config) < 0.60: notes.append("Interpretation readiness is limited.")
    if record.notes: notes.append(record.notes)
    return " ".join(notes)
def build_canvas_card(record: CanvasRecord, config: CanvasConfig):
    return {"schema_version":"1.0.0","card_id":_id(record, config),"card_type":"catalyst_canvas_article_governance","article_title":config.article_title,"article_slug":config.article_slug,"item":record.item,"claim_context":record.claim_context,"scores":{"domain_strength":round(domain_strength(record, config),4),"risk_score":round(risk_score(record, config),4),"interpretation_readiness":round(interpretation_readiness(record, config),4),"governance_priority_score":round(governance_priority_score(record, config),4)},"review":{"priority":review_priority(record, config),"confidence_band":confidence_band(record, config),"owner":record.owner,"status":record.status,"governance_note":governance_note(record, config)}}
