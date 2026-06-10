from __future__ import annotations

from statistics import mean

from .models import ConflictTensionItem


def conflict_clarity(item: ConflictTensionItem) -> float:
    return mean([
        item.desire_clarity,
        item.obstacle_clarity,
        item.pressure_strength,
        item.agency_visibility,
        item.stakes_visibility,
        item.relation_legibility,
    ])


def tension_durability(item: ConflictTensionItem) -> float:
    return mean([
        item.unresolved_pressure,
        item.meaningful_delay,
        item.stakes_heightening,
        item.expectation_pressure,
        item.complication_movement,
    ])


def narrative_movement(item: ConflictTensionItem) -> float:
    return mean([
        item.state_change,
        item.knowledge_change,
        item.relationship_impact,
        item.pressure_change,
        item.future_movement,
        item.value_transformation,
    ])


def conflict_risk(item: ConflictTensionItem) -> float:
    return min(
        1.0,
        item.scapegoating * 0.25
        + item.conflict_inflation * 0.20
        + item.trauma_spectacle * 0.20
        + item.false_balance * 0.20
        + item.closure_pressure * 0.15,
    )


def governance_priority_score(item: ConflictTensionItem) -> float:
    return min(
        1.0,
        conflict_risk(item) * 0.35
        + item.audience_sensitivity * 0.20
        + item.public_consequence * 0.25
        + (1 - conflict_clarity(item)) * 0.20,
    )


def review_priority(item: ConflictTensionItem) -> str:
    risk = conflict_risk(item)
    priority = governance_priority_score(item)
    clarity = conflict_clarity(item)
    movement = narrative_movement(item)

    if item.status == "revise" or risk >= 0.55 or priority >= 0.62 or clarity < 0.55 or movement < 0.50:
        return "high"
    if item.status == "review" or risk >= 0.40 or priority >= 0.48 or clarity < 0.68:
        return "medium"
    return "standard"
