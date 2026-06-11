from .models import CanvasConfig, CanvasRecord

def weighted_average(values, weights):
    denom = sum(w for k, w in weights.items() if k in values)
    if denom <= 0:
        return 0.0
    return max(0.0, min(1.0, sum(values[k] * w for k, w in weights.items() if k in values) / denom))

def domain_strength(record: CanvasRecord, config: CanvasConfig): return weighted_average(record.metrics, config.metric_weights)
def risk_score(record: CanvasRecord, config: CanvasConfig): return weighted_average(record.risk_signals, config.risk_weights)
def interpretation_readiness(record: CanvasRecord, config: CanvasConfig): return weighted_average(record.readiness_signals, config.readiness_weights)
def governance_priority_score(record: CanvasRecord, config: CanvasConfig):
    score = risk_score(record, config) * 0.45 + (1 - interpretation_readiness(record, config)) * 0.35 + (1 - domain_strength(record, config)) * 0.20
    if record.status == "revise": score = max(score, config.thresholds["high"])
    if record.status == "review": score = max(score, config.thresholds["medium"])
    return max(0.0, min(1.0, score))
def review_priority(record: CanvasRecord, config: CanvasConfig):
    score = governance_priority_score(record, config)
    return "high" if score >= config.thresholds["high"] else "medium" if score >= config.thresholds["medium"] else "standard"
def confidence_band(record: CanvasRecord, config: CanvasConfig):
    r = interpretation_readiness(record, config)
    return "high" if r >= 0.78 else "medium" if r >= 0.58 else "low"
