from __future__ import annotations

from .models import CanvasConfig, CanvasRecord


def _validate_numeric_map(name: str, values: dict[str, float]) -> None:
    if not values:
        raise ValueError(f"{name} must not be empty.")
    for key, value in values.items():
        if not isinstance(key, str) or not key.strip():
            raise ValueError(f"{name} contains an invalid key: {key!r}")
        if not isinstance(value, (int, float)):
            raise ValueError(f"{name}.{key} must be numeric.")
        if value < 0 or value > 1:
            raise ValueError(f"{name}.{key} must be between 0 and 1.")


def _validate_weights(name: str, weights: dict[str, float]) -> None:
    if not weights:
        raise ValueError(f"{name} must not be empty.")
    for key, value in weights.items():
        if not isinstance(value, (int, float)):
            raise ValueError(f"{name}.{key} must be numeric.")
        if value < 0:
            raise ValueError(f"{name}.{key} must be non-negative.")
    if sum(weights.values()) <= 0:
        raise ValueError(f"{name} must have a positive total weight.")


def validate_config(config: CanvasConfig) -> None:
    if not config.article_title.strip():
        raise ValueError("article_title is required.")
    if not config.article_slug.strip():
        raise ValueError("article_slug is required.")
    if not config.module_name.strip():
        raise ValueError("module_name is required.")
    _validate_weights("metric_weights", config.metric_weights)
    _validate_weights("risk_weights", config.risk_weights)
    _validate_weights("readiness_weights", config.readiness_weights)
    if "medium" not in config.thresholds or "high" not in config.thresholds:
        raise ValueError("thresholds must include medium and high.")
    if config.thresholds["medium"] >= config.thresholds["high"]:
        raise ValueError("medium threshold must be lower than high threshold.")


def validate_record(record: CanvasRecord, config: CanvasConfig, strict: bool = False) -> None:
    if not record.item.strip():
        raise ValueError("item is required.")
    if not record.claim_context.strip():
        raise ValueError("claim_context is required.")
    if record.status not in config.required_statuses:
        raise ValueError(f"status must be one of {config.required_statuses}; got {record.status!r}.")

    _validate_numeric_map("metrics", record.metrics)
    _validate_numeric_map("risk_signals", record.risk_signals)
    _validate_numeric_map("readiness_signals", record.readiness_signals)

    if strict:
        missing_metrics = set(config.metric_weights) - set(record.metrics)
        missing_risks = set(config.risk_weights) - set(record.risk_signals)
        missing_readiness = set(config.readiness_weights) - set(record.readiness_signals)
        if missing_metrics:
            raise ValueError(f"Missing metric fields: {sorted(missing_metrics)}")
        if missing_risks:
            raise ValueError(f"Missing risk fields: {sorted(missing_risks)}")
        if missing_readiness:
            raise ValueError(f"Missing readiness fields: {sorted(missing_readiness)}")
