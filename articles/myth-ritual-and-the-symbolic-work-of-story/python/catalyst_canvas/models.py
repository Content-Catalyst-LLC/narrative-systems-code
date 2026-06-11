from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass(frozen=True)
class CanvasConfig:
    article_title: str
    article_slug: str
    module_name: str
    metric_weights: dict[str, float]
    risk_weights: dict[str, float]
    readiness_weights: dict[str, float]
    thresholds: dict[str, float]
    required_statuses: tuple[str, ...] = ('active', 'archive', 'review', 'revise')


@dataclass(frozen=True)
class CanvasRecord:
    item: str
    claim_context: str
    article_title: str
    article_slug: str
    metrics: dict[str, float] = field(default_factory=dict)
    risk_signals: dict[str, float] = field(default_factory=dict)
    readiness_signals: dict[str, float] = field(default_factory=dict)
    owner: str = 'editorial'
    status: str = 'active'
    notes: str = ''

    def as_flat_dict(self) -> dict[str, Any]:
        output: dict[str, Any] = {
            'item': self.item,
            'claim_context': self.claim_context,
            'article_title': self.article_title,
            'article_slug': self.article_slug,
            'owner': self.owner,
            'status': self.status,
            'notes': self.notes,
        }
        for key, value in self.metrics.items():
            output[f'metric_{key}'] = value
        for key, value in self.risk_signals.items():
            output[f'risk_{key}'] = value
        for key, value in self.readiness_signals.items():
            output[f'readiness_{key}'] = value
        return output
