from dataclasses import dataclass, field
@dataclass(frozen=True)
class CanvasConfig:
    article_title: str
    article_slug: str
    module_name: str
    metric_weights: dict[str, float]
    risk_weights: dict[str, float]
    readiness_weights: dict[str, float]
    thresholds: dict[str, float]
    required_statuses: tuple[str, ...] = ("active", "archive", "review", "revise")
@dataclass(frozen=True)
class CanvasRecord:
    item: str
    claim_context: str
    article_title: str
    article_slug: str
    metrics: dict[str, float] = field(default_factory=dict)
    risk_signals: dict[str, float] = field(default_factory=dict)
    readiness_signals: dict[str, float] = field(default_factory=dict)
    owner: str = "editorial"
    status: str = "active"
    notes: str = ""
