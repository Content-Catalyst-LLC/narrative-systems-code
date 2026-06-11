from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class InteractiveNarrativeGovernanceConfig:
    article_title: str = "Games, Interactivity, and Branching Narrative"
    article_slug: str = "games-interactivity-and-branching-narrative"
    medium_threshold: float = 0.45
    high_threshold: float = 0.62
    allowed_statuses: tuple[str, ...] = ("active", "archive", "review", "revise")


@dataclass(frozen=True)
class InteractiveNarrativeGovernanceRecord:
    item: str
    game_context: str
    choice_meaningfulness: float
    system_response: float
    feedback_clarity: float
    role_variation: float
    world_memory: float
    ethical_governance: float
    branch_count_pressure: float
    state_dependency: float
    consequence_tracking: float
    testing_load: float
    localization_cost: float
    recombination_coherence: float
    mechanic_theme_fit: float
    rule_fiction_fit: float
    goal_value_fit: float
    progression_coherence: float
    interface_legibility: float
    consequence_consistency: float
    failure_meaning: float
    replay_value: float
    player_consent: float
    identity_care: float
    generic_quest_generation: float
    character_memory_failure: float
    opaque_system_response: float
    player_manipulation: float
    harmful_stereotype_risk: float
    human_review: float
    public_consequence: float
    owner: str = "editorial"
    status: str = "active"
    notes: str = ""
