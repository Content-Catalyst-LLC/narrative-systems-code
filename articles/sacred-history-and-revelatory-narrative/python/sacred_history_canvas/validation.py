from __future__ import annotations

from dataclasses import fields
from .models import SacredHistoryConfig, SacredHistoryRecord


def validate_record(record: SacredHistoryRecord, config: SacredHistoryConfig) -> None:
    if not record.item.strip() or not record.claim_context.strip():
        raise ValueError("item and claim_context are required.")
    if record.status not in config.allowed_statuses:
        raise ValueError(f"Invalid status: {record.status!r}")
    for field in fields(record):
        value = getattr(record, field.name)
        if isinstance(value, float) and (value < 0 or value > 1):
            raise ValueError(f"{field.name} must be between 0 and 1.")
