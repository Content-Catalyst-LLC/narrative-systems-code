from dataclasses import fields
from .models import NarrativeIdentityConfig, NarrativeIdentityRecord

def validate_record(record: NarrativeIdentityRecord, config: NarrativeIdentityConfig):
    if not record.item.strip() or not record.claim_context.strip(): raise ValueError("item and claim_context are required")
    if record.status not in config.allowed_statuses: raise ValueError(f"Invalid status {record.status}")
    for f in fields(record):
        v=getattr(record,f.name)
        if isinstance(v,float) and (v < 0 or v > 1): raise ValueError(f"{f.name} must be between 0 and 1")
