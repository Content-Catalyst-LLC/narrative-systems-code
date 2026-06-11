from __future__ import annotations
from dataclasses import fields
from .models import NarrativeFormulaDriftConfig, NarrativeFormulaDriftRecord

def validate_record(record: NarrativeFormulaDriftRecord, config: NarrativeFormulaDriftConfig) -> None:
    if not record.item.strip():
        raise ValueError("item is required.")
    if not record.claim_context.strip():
        raise ValueError("claim_context is required.")
    if record.status not in config.allowed_statuses:
        raise ValueError(f"Invalid status: {record.status!r}")
    for field in fields(record):
        value = getattr(record, field.name)
        if isinstance(value, float) and not (0 <= value <= 1):
            raise ValueError(f"{field.name} must be between 0 and 1.")
