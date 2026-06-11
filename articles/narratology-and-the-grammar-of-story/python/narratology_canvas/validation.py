from __future__ import annotations

from dataclasses import fields

from .models import NarratologyConfig, NarratologyRecord


def validate_score(value: float, field_name: str) -> None:
    if value < 0 or value > 1:
        raise ValueError(f"{field_name} must be between 0 and 1.")


def validate_record(record: NarratologyRecord, config: NarratologyConfig) -> None:
    if not record.item.strip():
        raise ValueError("item is required.")
    if not record.claim_context.strip():
        raise ValueError("claim_context is required.")
    if record.status not in config.allowed_statuses:
        raise ValueError(f"Invalid status: {record.status!r}")
    for field in fields(record):
        value = getattr(record, field.name)
        if isinstance(value, float):
            validate_score(value, field.name)
