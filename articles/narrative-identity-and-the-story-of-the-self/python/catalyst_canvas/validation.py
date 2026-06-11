from .models import CanvasConfig, CanvasRecord

def _check_map(name, values):
    if not values:
        raise ValueError(f"{name} must not be empty")
    for k, v in values.items():
        if not isinstance(v, (int, float)) or v < 0 or v > 1:
            raise ValueError(f"{name}.{k} must be numeric between 0 and 1")

def validate_config(config: CanvasConfig) -> None:
    if not config.article_title or not config.article_slug:
        raise ValueError("article title and slug are required")
    for name in ["metric_weights", "risk_weights", "readiness_weights"]:
        weights = getattr(config, name)
        if not weights or sum(weights.values()) <= 0:
            raise ValueError(f"{name} must have positive total weight")

def validate_record(record: CanvasRecord, config: CanvasConfig, strict: bool = False) -> None:
    if record.status not in config.required_statuses:
        raise ValueError(f"Invalid status {record.status}")
    _check_map("metrics", record.metrics)
    _check_map("risk_signals", record.risk_signals)
    _check_map("readiness_signals", record.readiness_signals)
    if strict:
        for label, required, actual in [("metrics", set(config.metric_weights), set(record.metrics)), ("risks", set(config.risk_weights), set(record.risk_signals)), ("readiness", set(config.readiness_weights), set(record.readiness_signals))]:
            missing = required - actual
            if missing:
                raise ValueError(f"Missing {label}: {sorted(missing)}")
