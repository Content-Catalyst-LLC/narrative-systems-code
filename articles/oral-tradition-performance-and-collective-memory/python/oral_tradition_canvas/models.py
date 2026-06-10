from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class OralTraditionItem:
    item: str
    tradition_type: str
    teller_role: float
    audience_response: float
    occasion_clarity: float
    embodiment: float
    setting_place: float
    cultural_frame: float
    lineage_clarity: float
    variation_tracking: float
    memory_supports: float
    governance_protocol: float
    authority_permission: float
    record_context: float
    origin_memory: float
    place_memory: float
    identity_memory: float
    historical_memory: float
    ritual_memory: float
    future_obligation: float
    consent_limits: float
    restricted_knowledge: float
    exposure_risk: float
    ownership_risk: float
    extraction_risk: float
    governance_control: float
    community_sensitivity: float
    public_consequence: float
    owner: str
    status: str
